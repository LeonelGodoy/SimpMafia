let clinetId = "onwbl5f7e4izyjd7h5x4yv8d4o6gat";
let clinetSecret = "0vx9sscucig7b24gyyrxjkjwj16azq";

function getTwitchAuthorization() {
    let url = `https://id.twitch.tv/oauth2/token?client_id=${clinetId}&client_secret=${clinetSecret}&grant_type=client_credentials`;

    return fetch(url, {
    method: "POST",
    })
    .then((res) => res.json())
    .then((data) => {
        return data;
    });
}

async function getStreams(username) {
//    const endpoint = "https://api.twitch.tv/helix/streams";


//    const endpoint = "https://api.twitch.tv/helix/streams?user_login=billydiamondexists";

    const endpoint = "https://api.twitch.tv/helix/streams?user_login=" + username;

    let authorizationObject = await getTwitchAuthorization();
    let { access_token, expires_in, token_type } = authorizationObject;

    token_type =
    token_type.substring(0, 1).toUpperCase() +
    token_type.substring(1, token_type.length);

    let authorization = `${token_type} ${access_token}`;

    let headers = {
    authorization,
    "Client-Id": clinetId,
    };

    fetch(endpoint, {
    headers,
    })
    .then((res) => res.json())
    .then((data) => checkLIVE(data, username));

}


function checkLIVE(data, username) {
     var { data: streams } = data;


    console.log(username);
//    console.log(streams[0].type);
    console.log(streams.length);
    if (streams.length == 1)
         {
//         document.getElementById(username).style.display = "block";
         document.getElementById(username).classList.remove("hidden");
         }


    console.log("------------------------");
//    document.getElementById(username).style.display = "none";
//    console.log(document.getElementById(username));

}


function showhide(){
    var array = document.getElementsByClassName("btn_live");
    document.write(array)
    console.log(array);

    // regular for loop
        for (let i = 0; i < array.length; i++) {
            console.log(array[i].name);
            getStreams(array[i].name)

         }
    }
showhide()

