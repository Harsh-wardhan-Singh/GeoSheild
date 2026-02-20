document.addEventListener("DOMContentLoaded", function () {

    /* =========================
       THEME TOGGLE (PERSISTENT)
    ========================= */

    const themeToggle = document.getElementById("theme-toggle");

    // Load saved theme
    if (localStorage.getItem("theme") === "light") {
        document.body.classList.add("light-mode");
        themeToggle.innerText = "Toggle Dark Mode";
    }

    themeToggle.addEventListener("click", function () {
        document.body.classList.toggle("light-mode");

        if (document.body.classList.contains("light-mode")) {
            localStorage.setItem("theme", "light");
            themeToggle.innerText = "Toggle Dark Mode";
        } else {
            localStorage.setItem("theme", "dark");
            themeToggle.innerText = "Toggle Light Mode";
        }
    });


    /* =========================
       SECTION REFERENCES
    ========================= */

    const homeSection = document.getElementById("home-section");
    const riskSection = document.getElementById("risk-section");
    const simulationSection = document.getElementById("simulation-section");
    const riskReport = document.getElementById("risk-report");

    const goRisk = document.getElementById("go-risk");
    const goSimulation = document.getElementById("go-simulation");
    const backHome1 = document.getElementById("back-home-1");
    const backHome2 = document.getElementById("back-home-2");

    const analyzeBtn = document.getElementById("analyze-btn");

    const tariffSlider = document.getElementById("tariff-slider");
    const tariffValue = document.getElementById("tariff-value");

    const currencySlider = document.getElementById("currency-slider");
    const currencyValue = document.getElementById("currency-value");

    const exportBanCheckbox = document.getElementById("export-ban");
    const disruptionLevelSelect = document.getElementById("disruption-level");

    const scenarioButtons = document.querySelectorAll(".scenario-btn");

    let businessProfile = {};
    let vulnerabilityScore = 0;


    /* =========================
       FLAG HELPER
    ========================= */

    function getFlag(countryName) {
        const flags = {
            "China": "🇨🇳",
            "Germany": "🇩🇪",
            "Vietnam": "🇻🇳",
            "Japan": "🇯🇵",
            "Malaysia": "🇲🇾",
            "US": "🇺🇸",
            "India": "🇮🇳",
            "South Korea": "🇰🇷"
        };
        return flags[countryName] || "🌍";
    }


    /* =========================
       NAVIGATION
    ========================= */

    goRisk.addEventListener("click", () => {
        homeSection.style.display = "none";
        riskSection.style.display = "block";
    });

    goSimulation.addEventListener("click", () => {
        homeSection.style.display = "none";
        simulationSection.style.display = "block";
    });

    backHome1.addEventListener("click", () => {
        riskSection.style.display = "none";
        riskReport.style.display = "none";
        homeSection.style.display = "block";
    });

    backHome2.addEventListener("click", () => {
        simulationSection.style.display = "none";
        homeSection.style.display = "block";
    });


    /* =========================
       RISK ANALYSIS FLOW
    ========================= */

    analyzeBtn.addEventListener("click", function () {

        const country1 = document.getElementById("country1").value;
        const dep1 = parseFloat(document.getElementById("dep1").value) / 100;

        const country2 = document.getElementById("country2").value;
        const dep2 = parseFloat(document.getElementById("dep2").value) / 100;

        const country3 = document.getElementById("country3").value;
        const dep3 = parseFloat(document.getElementById("dep3").value) / 100;

        const baseMargin = parseFloat(document.getElementById("base-margin").value);
        const importShare = parseFloat(document.getElementById("import-share").value) / 100;

        businessProfile = {
            countries: [
                { name: country1, dependency: dep1 },
                { name: country2, dependency: dep2 },
                { name: country3, dependency: dep3 }
            ],
            baseMargin: baseMargin,
            importShare: importShare
        };

        calculateVulnerability();
        generateExecutiveReport();
        generateRiskAdvisory();

        riskReport.style.display = "block";
    });


    function calculateVulnerability() {

        const mockRiskScores = {
            "China": 72,
            "Vietnam": 35,
            "Germany": 20
        };

        vulnerabilityScore = 0;

        businessProfile.countries.forEach(country => {
            const risk = mockRiskScores[country.name] || 40;
            vulnerabilityScore += country.dependency * risk;
        });

        vulnerabilityScore = parseFloat(vulnerabilityScore.toFixed(1));
    }


    function generateExecutiveReport() {

        let exposureLevel, sensitivity, profitStability;
        let exposureClass, sensitivityClass, profitClass;

        if (vulnerabilityScore > 60) {
            exposureLevel = "HIGH";
            sensitivity = "SEVERE";
            profitStability = "FRAGILE";
            exposureClass = sensitivityClass = profitClass = "status-high";
        } else if (vulnerabilityScore > 40) {
            exposureLevel = "MODERATE";
            sensitivity = "ELEVATED";
            profitStability = "UNSTABLE";
            exposureClass = sensitivityClass = profitClass = "status-medium";
        } else {
            exposureLevel = "LOW";
            sensitivity = "MANAGEABLE";
            profitStability = "STABLE";
            exposureClass = sensitivityClass = profitClass = "status-low";
        }

        const dominant = businessProfile.countries.reduce((prev, current) =>
            (prev.dependency > current.dependency) ? prev : current
        );

        const flag = getFlag(dominant.name);

        document.getElementById("metric-exposure").innerHTML =
            `<span class="${exposureClass}">${exposureLevel}</span>`;

        document.getElementById("metric-region").innerHTML =
            `${flag} ${dominant.name}`;

        document.getElementById("metric-sensitivity").innerHTML =
            `<span class="${sensitivityClass}">${sensitivity}</span>`;

        document.getElementById("metric-profit").innerHTML =
            `<span class="${profitClass}">${profitStability}</span>`;

        document.getElementById("summary-content").innerHTML = `
            Concentration of ${(dominant.dependency * 100).toFixed(0)}% sourcing in ${flag} ${dominant.name}
            materially amplifies exposure to tariff escalation and export controls.
            <br><br>
            Structural diversification would reduce systemic vulnerability.
        `;

        document.getElementById("risk-drivers").innerHTML = `
            • ${flag} ${dominant.name} accounts for ${(dominant.dependency * 100).toFixed(0)}% of sourcing<br>
            • Elevated tariff pass-through sensitivity<br>
            • Currency volatility exposure<br>
            • Limited supplier diversification buffer
        `;
    }


    function generateRiskAdvisory() {

        let advisory;

        if (vulnerabilityScore > 60) {
            advisory = "Immediate diversification recommended. Reduce regional concentration and implement hedging strategies.";
        } else if (vulnerabilityScore > 40) {
            advisory = "Moderate exposure detected. Gradual supplier diversification advised.";
        } else {
            advisory = "Exposure within manageable range. Continue monitoring geopolitical developments.";
        }

        document.getElementById("recommendation-content").innerHTML = advisory;
    }


    /* =========================
       SIMULATION ENGINE
    ========================= */

    scenarioButtons.forEach(button => {
        button.addEventListener("click", function () {

            const scenario = button.getAttribute("data-scenario");

            if (scenario === "stable") {
                tariffSlider.value = 5;
                currencySlider.value = 2;
                exportBanCheckbox.checked = false;
                disruptionLevelSelect.value = "low";
            }

            if (scenario === "conflict") {
                tariffSlider.value = 20;
                currencySlider.value = 8;
                exportBanCheckbox.checked = true;
                disruptionLevelSelect.value = "medium";
            }

            if (scenario === "severe") {
                tariffSlider.value = 35;
                currencySlider.value = 15;
                exportBanCheckbox.checked = true;
                disruptionLevelSelect.value = "high";
            }

            updateShockSimulation();
        });
    });

    tariffSlider.addEventListener("input", updateShockSimulation);
    currencySlider.addEventListener("input", updateShockSimulation);
    exportBanCheckbox.addEventListener("change", updateShockSimulation);
    disruptionLevelSelect.addEventListener("change", updateShockSimulation);


    function updateShockSimulation() {

        tariffValue.textContent = tariffSlider.value;
        currencyValue.textContent = currencySlider.value;

        const tariff = parseFloat(tariffSlider.value) / 100;
        const currency = parseFloat(currencySlider.value) / 100;
        const exportBan = exportBanCheckbox.checked;
        const disruptionLevel = disruptionLevelSelect.value;

        let disruptionImpact = 0;
        if (disruptionLevel === "low") disruptionImpact = 0.03;
        if (disruptionLevel === "medium") disruptionImpact = 0.07;
        if (disruptionLevel === "high") disruptionImpact = 0.12;

        let shockImpact =
            (tariff * 0.4) +
            (currency * 0.5) +
            disruptionImpact +
            (exportBan ? 0.10 : 0);

        const baseMargin = 20;
        const marginDrop = baseMargin * shockImpact;
        const percentDrop = ((marginDrop / baseMargin) * 100).toFixed(1);

        let shockLevel, riskClass, colorClass, meterColor;

        if (shockImpact > 0.25) {
            shockLevel = "SEVERE";
            riskClass = "CRITICAL";
            colorClass = "status-high";
            meterColor = "#ef4444";
        } else if (shockImpact > 0.15) {
            shockLevel = "ELEVATED";
            riskClass = "HIGH";
            colorClass = "status-medium";
            meterColor = "#f59e0b";
        } else {
            shockLevel = "LOW";
            riskClass = "MANAGEABLE";
            colorClass = "status-low";
            meterColor = "#22c55e";
        }

        document.getElementById("sim-shock-level").innerHTML =
            `<span class="${colorClass}">${shockLevel}</span>`;

        document.getElementById("sim-margin-impact").innerHTML =
            `<span class="${colorClass}">-${percentDrop}%</span>`;

        document.getElementById("sim-cost-pressure").innerText =
            (shockImpact * 100).toFixed(1) + "%";

        document.getElementById("sim-risk-class").innerHTML =
            `<span class="${colorClass}">${riskClass}</span>`;

        const meterFill = document.getElementById("shock-fill");
        meterFill.style.width = Math.min(shockImpact * 200, 100) + "%";
        meterFill.style.background = meterColor;

        document.getElementById("simulation-result").innerHTML = `
            This scenario introduces a ${shockLevel.toLowerCase()} trade shock.
            Profit margins compress by ${percentDrop}% under combined tariff,
            export restriction, currency volatility, and supply disruption stress.
        `;
    }

});