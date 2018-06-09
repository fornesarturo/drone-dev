$('input[type="radio"]').checkboxradio();

//Append text to textarea
function appendText(text) {
    let textarea = $("#script_output");
    let currentText = textarea.val();
    textarea.val(currentText + text + "\n");
    textarea.scrollTop(textarea[0].scrollHeight);
}

// Send request and open socket connection
$("#fly").click(() => { 
    let scriptName = $("[name='script_radioset']:checked")[0].value;
    console.log("Selected: ", scriptName);

    startScript(scriptName)
    .then((success) => {
        var socket = io.connect("http://localhost:1337");
        socket.on("output", (data) => {
            appendText(data.data);
        });
        socket.on("exit", (data) => {
            appendText(data.data);
            socket.disconnect();
        });
    });
});