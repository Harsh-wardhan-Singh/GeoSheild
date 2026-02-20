document.addEventListener("DOMContentLoaded", function () {

    fetch("/risk")
        .then(response => response.json())
        .then(data => {

            const container = document.getElementById("risk-container");

            container.innerHTML = "";

            for (const country in data) {
                const line = document.createElement("p");
                line.textContent = country + ": " + data[country];
                container.appendChild(line);
            }
        });

});