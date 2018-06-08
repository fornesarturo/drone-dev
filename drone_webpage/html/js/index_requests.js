async function startScript(scriptName) {
    let response = await fetch("http://localhost:1337/scripts/" + scriptName, {
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