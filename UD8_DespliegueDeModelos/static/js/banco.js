window.onload = () => {
    const mensaje = document.querySelector(".mensaje");
    if (mensaje && mensaje.textContent.trim() !== "") {
        mensaje.style.display = "block";
    }

    const selects = document.querySelectorAll("select");

    selects.forEach((select) => {
        // Ocultar el select original pero mantenerlo funcional
        select.style.display = "none";

        // Crear contenedor wrapper
        const wrapper = document.createElement("div");
        wrapper.className = "custom-select";

        // Crear contenedor para la opción seleccionada
        const selected = document.createElement("div");
        selected.className = "selected-option";
        selected.textContent = select.options[select.selectedIndex]?.text || "Selecciona una opción";

        // Crear lista de opciones
        const optionsBox = document.createElement("div");
        optionsBox.className = "custom-options";

        Array.from(select.options).forEach(option => {
            const opt = document.createElement("div");
            opt.className = "custom-option";
            opt.textContent = option.textContent;

            opt.addEventListener("mouseover", () => {
                opt.style.backgroundColor = "#1882A8";
                opt.style.color = "#fff";
            });

            opt.addEventListener("mouseout", () => {
                opt.style.backgroundColor = "";
                opt.style.color = "";
            });

            opt.addEventListener("click", () => {
                selected.textContent = option.textContent;
                select.value = option.value;
                optionsBox.style.display = "none";
            });

            optionsBox.appendChild(opt);
        });

        // Toggle de apertura/cierre
        selected.addEventListener("click", () => {
            optionsBox.style.display = optionsBox.style.display === "block" ? "none" : "block";
        });

        // Insertar componentes
        wrapper.appendChild(selected);
        wrapper.appendChild(optionsBox);

        // Insertar después del select original
        select.parentElement.insertBefore(wrapper, select.nextSibling);
    });
};