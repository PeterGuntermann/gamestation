
function setUsername() {
    axios.post(
        "/set-username",
        {
            username: usernameInput.value
        })
        .then(res => {
            console.log(res);
            window.location.replace("/lobby")
        })
        .catch(err => console.error(err));
}

const setUsernameButton = document.getElementById("set-username-button");
setUsernameButton.addEventListener("click", setUsername);
const usernameInput = document.getElementById("username-input");
// const username = usernameInput.value;