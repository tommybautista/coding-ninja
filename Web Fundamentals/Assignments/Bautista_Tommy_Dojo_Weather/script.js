function hideMessage(element) {
    document.querySelector(element).remove();
}


function convertTemp(selection) {
	if (document.querySelector(selection).value == "C°") {
        document.querySelector("#highToday").innerText = "24°";
        document.querySelector("#lowToday").innerText = "18°";
        document.querySelector("#highTomorrow").innerText = "27°";
        document.querySelector("#lowTomorrow").innerText = "19°";
        document.querySelector("#highFriday").innerText = "21°";
        document.querySelector("#lowFriday").innerText = "16°";
        document.querySelector("#highSaturday").innerText = "26°";
        document.querySelector("#lowSaturday").innerText = "21°";
    } else {
        document.querySelector("#highToday").innerText = "75°";
        document.querySelector("#lowToday").innerText = "65°";
        document.querySelector("#highTomorrow").innerText = "80°";
        document.querySelector("#lowTomorrow").innerText = "66°";
        document.querySelector("#highFriday").innerText = "69°";
        document.querySelector("#lowFriday").innerText = "61°";
        document.querySelector("#highSaturday").innerText = "78°";
        document.querySelector("#lowSaturday").innerText = "70°";
    }
}

