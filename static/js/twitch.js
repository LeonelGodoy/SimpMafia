
function getTwitchAuthorization() {
    let url = `https://id.twitch.tv/oauth2/token?client_id=${MY_SECRET_SAUCE}&client_secret=${MY_SECRET_ID}&grant_type=client_credentials`;

    return fetch(url, {
    method: "POST",
    })
    .then((res) => res.json())
    .then((data) => {
        return data;
    });
}

async function getStreams(username) {
    const endpoint = "https://api.twitch.tv/helix/streams?user_login=" + username;

    let authorizationObject = await getTwitchAuthorization();
    let { access_token, expires_in, token_type } = authorizationObject;

    token_type =
    token_type.substring(0, 1).toUpperCase() +
    token_type.substring(1, token_type.length);

    let authorization = `${token_type} ${access_token}`;

    let headers = {
    authorization,
    "Client-Id": MY_SECRET_SAUCE,
    };

    fetch(endpoint, {
    headers,
    })
    .then((res) => res.json())
    .then((data) => checkLIVE(data, username));

}


function checkLIVE(data, username) {
    var { data: streams } = data;
    if (streams.length == 1)
         {
         document.getElementById(username).classList.remove("hidden");
         }


}


function init(){
    var array = document.getElementsByClassName("btn_live");
    // regular for loop
        for (let i = 0; i < array.length; i++) {
            getStreams(array[i].name)

         }
    }

init()
