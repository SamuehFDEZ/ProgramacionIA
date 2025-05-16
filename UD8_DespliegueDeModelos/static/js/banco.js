window.onload = () => {
    let options = document.getElementsByTagName("option");
    for (const option of options) {
        option.style.backgroundColor = "#072146";
        option.style.color = "#eaf6ff";
        option.addEventListener("mouseover", ()=>{
            option.style.backgroundColor = "#007bff";
        });
    }
}