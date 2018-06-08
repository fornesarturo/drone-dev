// Main requirements ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const sys   = require("util");
const spawn = require("child_process").spawn;
const express = require("express");
const http = require("http");
const app = express();
const server = http.createServer(app);
const io = require("socket.io").listen(server);
const bodyParser = require("body-parser");

// Express Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const PORT = process.env.PORT || 1337;
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("html"));
function mySubstr(str) {
    if(str.substr(0, 8) == "/scripts" || str == "/") return str;
    else return "";
}
function logger(req, res, next) {
    let url = (req.originalUrl || req.url)
    if(mySubstr(url) != "") console.log(req.method, " ", url);
    next();
}
app.use(logger);

// Router Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
let flyScriptsRouter = express.Router();
app.use("/scripts", flyScriptsRouter);

// App routes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.get(("/"), (req, res) => {
    res.status(200).sendFile(__dirname + "/html/index.html");
});

// Socket configuration ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io.on("connection", (socket) => {

    // Fly script routes (/scripts) ~~~~~~~~~~~~~~~~~~~~~~~
    flyScriptsRouter.get("/simple_takeoff", (req, res) => {
        
        socket.emit("success", {data: "Successfully connected to script's output"});

        // Python test script
        let thermostat = spawn("python2", ["./python/test.py"]);
        thermostat.stdout.on("data", (output) => { 
            let string = String(output);
            console.log("SIMPLE_TAKEOFF OUTPUT: ", string);
            socket.emit("output", {data: string});
        });
        

        res.status(200).json({
            status: "200"
        });
    });
});

// Start server ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
server.listen(PORT, () => {
    console.log("Listening on port ", PORT, " . . .");
});