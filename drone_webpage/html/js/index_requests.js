var remoteHost = location.host;

async function startScript(scriptName, targetAltitude) {
    if(targetAltitude) {
        var url = "http://" + remoteHost + "/scripts/" + scriptName + "?targetAltitude=" + targetAltitude;
    }
    else {
        var url = "http://" + remoteHost + "/scripts/" + scriptName;
    }
    let response = await fetch(url, {
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'content-type': 'application/json'
        },
        method: 'GET',
        redirect: 'follow',
    })
    .then(res => res.json())
    .then((resJSON) => {
        if(resJSON.status == "200") {
            return true;
        }
        else {
            console.error("Status code ", res.status, "\nError: ", resJSON.error);
            return false;
        }
    });
    return response;
}