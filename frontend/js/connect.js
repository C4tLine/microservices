let username = "";
let password = "";

let refresh_token = "";
let connected = false;

const headers = new Headers();
headers.append("Content-Type", "application/x-www-form-urlencoded");

function createSub(channel_name) {
    const sub = client.newSubscription(channel_name);
    let channel = document.createElement("li");
    sub.on("publication", (msg) => {
        let line = `<p><strong>${msg.data.from}:</strong> ${msg.data.message}</p>`;
        messages.innerHTML += line;
    });
    sub.on("subscribed", (context) => {
        console.log(context);
    });
    // let disconnect_button = document.createElement("button");
    let watch_button = document.createElement("button");
    // disconnect_button.addEventListener("click", () => {
    //     client.removeSubscription(sub);
    //     channel.remove();
    // });
    // disconnect_button.innerHTML = "Disconnect";
    watch_button.style.marginLeft = "5px";
    watch_button.addEventListener("click", () => {
        if (current_sub != sub) {
            if (current_sub !== undefined) {
                current_sub.unsubscribe();
            }
            sub.subscribe();
            current_sub = sub;
            messages.innerHTML = "";
            document.getElementById("chat").style.display = "flex";
            if (current_channel !== undefined) {
                current_channel.style.fontWeight = "normal";
                current_channel.style.fontSize = "initial";
            }
            channel.style.fontWeight = "bold";
            channel.style.fontSize = "18px";
            current_channel = channel;
        }
    });
    watch_button.innerHTML = "Watch";
    channel.innerHTML = channel_name + " ";
    // channel.appendChild(disconnect_button);
    channel.appendChild(watch_button);
    document.getElementById("subscriptions").appendChild(channel);
}

const getToken = async () => {
    console.log("get token called");
    const params = new URLSearchParams();
    params.append("client_id", "myclient");
    const requestOptions = {
        method: "POST",
        headers: headers,
        body: params,
    };
    if (refresh_token == "") {
        params.append("username", username);
        params.append("password", password);
        params.append("grant_type", "password");
    } else {
        params.append("refresh_token", refresh_token);
        params.append("grant_type", "refresh_token");
    }
    return fetch(
        "http://127.0.0.1:7070/realms/newrealm/protocol/openid-connect/token",
        requestOptions
    )
        .then((response) => response.json())
        .then((result) => {
            console.log("token accepted");
            refresh_token = result.refresh_token;
            console.log(result);
            return result.access_token
        })
        .catch((error) => {
            console.error(error);
        });
};

let client = undefined;

document.getElementById("btnLogin").addEventListener("click", () => {
    if (connected) {
        return;
    }
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    if (username != "" && password != "") {
        getToken().then((token) => {
            if (token !== undefined) {
                client = new Centrifuge(
                    "ws://127.0.0.1:8080/centrifugo/connection/websocket",
                    {
                        data: { token: token }
                    }
                );
                client.on("connected", () => {
                    password = null;
                    document.getElementById("password").value = "";
                    connected = true;
                    document.getElementById("loginForm").style.display = "none";
                    document.getElementById("userInfo").style.display = "flex";
                    document.getElementById("userHello").textContent = "Hello, " + username;
                    client.rpc("get_user_channels").then(function(res) {
                        res.data.channels.forEach((channel) => {
                            createSub(channel);
                        });
                    }, function(err) {
                        console.log('rpc error', err);
                    });
                });
                client.on("disconnected", () => {
                    refresh_token = "";
                    client.setToken("");
                    connected = false;
                    document.getElementById("loginForm").style.display = "block";
                    document.getElementById("userInfo").style.display = "none";
                });
                client.connect();
            }
        });
    } else {
        console.error("empty username or password");
    }
});

document.getElementById("btnLogout").addEventListener("click", () => {
    if (!connected) {
        return;
    }
    console.log("disconnecting");
    const params = new URLSearchParams();
    params.append("client_id", "myclient");
    const requestOptions = {
        method: "POST",
        headers: headers,
        body: params,
    };
    if (refresh_token != "") {
        params.append("refresh_token", refresh_token);
        params.append("grant_type", "refresh_token");
        fetch(
            "http://127.0.0.1:7070/realms/newrealm/protocol/openid-connect/logout",
            requestOptions
        )
            .then((response) => {
                console.log("session closed");
            })
            .catch((error) => console.error(error))
            .finally(() => {
                client.disconnect();
            });
    } else {
        console.error("no refresh token");
    }
});

const channelInput = document.getElementById("channel");
const messageInput = document.getElementById("message");
const messages = document.getElementById("messages");
let current_sub = undefined;
let current_channel = undefined;

document.getElementById("btnConnect").addEventListener("click", () => {
    const channel_name = channelInput.value;
    createSub(channel_name);
});


document.getElementById("btnPublish").addEventListener("click", () => {
    if (messageInput.value != "") {
        current_sub.publish({
            from: username,
            message: messageInput.value
        });
        messageInput.value = "";
    }
});