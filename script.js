document.querySelector("form").addEventListener("submit", async function(event) {

    event.preventDefault();

    let gender = document.querySelectorAll("select")[0].value;
    let occasion = document.querySelectorAll("select")[1].value;
    let color = document.querySelector("input").value;

    try {
        let response = await fetch("http://127.0.0.1:8000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                gender: gender,
                occasion: occasion,
                color: color
            })
        });

        let data = await response.json();

        alert(data.suggestion);

    } catch (error) {
        console.log("Error:", error);
        alert("Something went wrong. Check backend.");
    }

});