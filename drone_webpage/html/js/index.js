$("input").checkboxradio();

let socket = io.connect("http://localhost:1337");
socket.on("success", (data) => {
    console.log(data.data);
});
socket.on("output", (data) => {
    console.log(data.data);
});

$("#fly").click(() => { 
    let scriptName = $("[name='script_radioset']:checked")[0].value;
    console.log("Selected: ", scriptName);

    startScript(scriptName)
    .then((success) => {
        return;
    });
});