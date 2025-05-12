window.onload = () =>{
    //login();
}

function login(){
    const form = document.querySelector("form");
    const responseDiv = document.getElementById("response");

    form.addEventListener("submit", function(e) {
        e.preventDefault(); // Evita que se recargue la página

        const formData = new FormData(form);

        fetch("/login", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            responseDiv.innerHTML = `<p style="color:${data.success ? 'green' : 'red'};">${data.message}</p>`;
        })
        .catch(err => {
            responseDiv.innerHTML = "<p style='color:red;'>Error en el servidor</p>";
            console.error(err);
        });
    });
}