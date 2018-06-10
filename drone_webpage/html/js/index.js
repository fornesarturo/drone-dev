$('input[type="radio"]').checkboxradio();

$("#target_altitude").spinner({
    step: 0.10,
    numberFormat: "n"
});

$(".script_option").click(() => {
    let radio = $(".script_option:checked");
    console.log(radio);
    if(radio[0].value == "simple_takeoff") {
        $("#ta_container").show();
    }
    else {
        $("#ta_container").hide();
    }
})


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

    if(scriptName == "simple_takeoff") {
        let targetAltitude = $("#target_altitude").val();
        startScript(scriptName, targetAltitude)
        .then((success) => {
            var socket = io.connect("http://10.0.1.128:1337");
            socket.on("output", (data) => {
                appendText(data.data);
            });
            socket.on("exit", (data) => {
                appendText(data.data);
                socket.disconnect();
            });
        });
    }
    else {
        startScript(scriptName)
        .then((success) => {
            var socket = io.connect("http://10.0.1.128:1337");
            socket.on("output", (data) => {
                appendText(data.data);
            });
            socket.on("exit", (data) => {
                appendText(data.data);
                socket.disconnect();
            });
        });
    }
});