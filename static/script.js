document.addEventListener("DOMContentLoaded", function () {

    // =====================================
    // LOAD COUNTRY RISK DATA
    // =====================================

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


    // =====================================
    // LOAD VULNERABILITY SCORE
    // =====================================

    fetch("/vulnerability")
        .then(response => response.json())
        .then(data => {

            document.getElementById("vulnerability-score").innerHTML =
                `<span style="font-size:28px; font-weight:bold;">${data.vulnerability_score}</span>`;
        });


    // =====================================
    // SHOCK SIMULATOR LOGIC
    // =====================================

    const slider = document.getElementById("tariff-slider");
    const tariffText = document.getElementById("tariff-value");

    slider.addEventListener("input", function () {

        tariffText.textContent = slider.value;

        fetch("/simulate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                tariff: parseInt(slider.value)
            })
        })
        .then(response => response.json())
        .then(data => {

            document.getElementById("simulation-result").innerHTML = `
                <p>Base Margin: 20%</p>
                <p style="color: red; font-weight: bold;">
                    New Margin: ${data.new_margin}%
                </p>
            `;
        });

    });

});