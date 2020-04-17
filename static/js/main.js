
function getSomething() {
    console.log("Get something.");
    axios.get("/foobar")
    .then(res => console.log(res))
    .catch(err => console.error(err));
}

function postSomething() {
    console.log("Post something.");
    axios.post("/foobar", { foo: "bar" })
    .then(res => console.log(res))
    .catch(err => console.error(err));
}

document.getElementById("get-button").addEventListener("click", getSomething)
document.getElementById("post-button").addEventListener("click", postSomething)