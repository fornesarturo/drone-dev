// Main requirements ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const sys   = require("util");
const spawn = require("child_process").spawn;
const express = require("express");
const http = require("http");
const app = express();
const server = http.createServer(app);
const io = require("socket.io").listen(server);
const bodyParser = require("body-parser");
// const cors = require('cors');

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
// app.use(cors({
//     credentials: true,
//     origin: (origin, callback) => {
//         // check if origin is valid here. If valid, return null.
//         callback(null, true);
//     }
// }));
app.options("/*", function(req, res, next){
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');
    res.send(200);
});

// Router Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
let flyScriptsRouter = express.Router();
app.use("/scripts", flyScriptsRouter);

// App routes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.get(("/"), (req, res) => {
    res.status(200).sendFile(__dirname + "/html/index.html");
});

// Fly script routes (/scripts) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
flyScriptsRouter.get("/simple_takeoff", (req, res) => {
    if(req.query["targetAltitude"]) {
        startScript("simple_takeoff", req.query["targetAltitude"]);
        res.status(200).json({
            status: "200"
        });
    }
    else {
        res.status(400).json({
            status: "400"
        });
    }
});

flyScriptsRouter.get("/script_test", (req, res) => {
    startScript("script_test");
    res.status(200).json({
        status: "200"
    });
});

flyScriptsRouter.get("/params_check", (req, res) => {
    startScript("params_check");
    res.status(200).json({
        status: "200"
    });
});


// General function for script start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
function startScript(scriptName, targetAltitude) {
    setTimeout(() => {

        io.emit("output", {data: "Successfully connected to script's output\nRunning '" + scriptName + "'."});
        
        if(targetAltitude && targetAltitude >= 0) {
            var script = spawn("python2", ["./python/" + scriptName + ".py", targetAltitude]);
        }
        else {
            var script = spawn("python2", ["./python/" + scriptName + ".py"]);
        }

        // Python test script ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        script.stdout.on("data", (output) => { 
            let string = String(output);
            if(string == "SCRIPT ENDED") {
                console.log(scriptName.toUpperCase()," OUTPUT: ", string);
                io.emit("exit", {data: string});
                script.kill();
            }
            else {
                console.log(scriptName.toUpperCase(), " OUTPUT: ", string);
                io.emit("output", {data: string});
            }
        });
        script.stderr.on("data", (output) => { 
            let string = String(output);
            console.log(scriptName.toUpperCase(), " OUTPUT: ", string);
            io.emit("output", {data: string});
        });
    }, 500);
    
}

// Start server ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
server.listen(PORT, () => {
    console.log("Listening on port ", PORT, " . . .");
});