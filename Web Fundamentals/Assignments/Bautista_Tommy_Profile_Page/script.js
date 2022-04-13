function changeName(jane) {
    document.querySelector(jane).innerText = "Doris J.";
}

function removeUser(userOne) {
    document.querySelector(userOne).remove();
}

function increaseConnections(userOne) {
    document.querySelector(userOne).innerText++;
}

function decreaseConnections(userOne) {
    document.querySelector(userOne).innerText--;
}