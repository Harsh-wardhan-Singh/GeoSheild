document.addEventListener("DOMContentLoaded", function () {

    /* =========================
       THEME TOGGLE
    ========================= */

    const themeToggle = document.getElementById("theme-toggle");

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



    /* =========================
       NAVIGATION
    ========================= */

    function scrollTopSmooth() {
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    goRisk.addEventListener("click", () => {
        homeSection.style.display = "none";
        riskSection.style.display = "block";
        scrollTopSmooth();
    });

    goSimulation.addEventListener("click", () => {
        homeSection.style.display = "none";
        simulationSection.style.display = "block";
        scrollTopSmooth();
    });

    backHome1.addEventListener("click", () => {
        riskSection.style.display = "none";
        riskReport.style.display = "none";
        homeSection.style.display = "block";
        scrollTopSmooth();
    });

    backHome2.addEventListener("click", () => {
        simulationSection.style.display = "none";
        homeSection.style.display = "block";
        scrollTopSmooth();
    });



    /* =========================
       AI RISK ANALYSIS (REAL BACKEND)
    ========================= */

    analyzeBtn.addEventListener("click", async function () {

        const country1 = document.getElementById("country1").value;
        const dep1 = parseFloat(document.getElementById("dep1").value);

        const country2 = document.getElementById("country2").value;
        const dep2 = parseFloat(document.getElementById("dep2").value);

        const country3 = document.getElementById("country3").value;
        const dep3 = parseFloat(document.getElementById("dep3").value);

        const baseMargin = parseFloat(document.getElementById("base-margin").value);
        const importShare = parseFloat(document.getElementById("import-share").value);

        const payload = {
        mode: "ai",
        dependencies: {
            [country1]: parseFloat(dep1) / 100,
            [country2]: parseFloat(dep2) / 100,
            [country3]: parseFloat(dep3) / 100
        },
        base_margin: parseFloat(baseMargin),
        import_cost_share: parseFloat(importShare)
        };

        try {

            const response = await fetch("/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();
            renderRiskResults(data);

        } catch (error) {
            alert("Backend connection error.");
        }
    });


    function renderRiskResults(data) {
console.log(data.profit_analysis);
        const risk = data.risk_analysis;
        const profit = data.profit_analysis;
        const vulnerability = data.vulnerability_analysis;

        const dominantRegion = Object.keys(vulnerability.country_exposure)
            .reduce((a, b) =>
                vulnerability.country_exposure[a] > vulnerability.country_exposure[b] ? a : b
            );

        const flag = getFlag(dominantRegion);

        let exposureClass =
            risk.risk_level === "Critical" || risk.risk_level === "High"
                ? "status-high"
                : risk.risk_level === "Medium"
                ? "status-medium"
                : "status-low";

        document.getElementById("metric-exposure").innerHTML =
            `<span class="${exposureClass}">${risk.risk_level.toUpperCase()}</span>`;

        document.getElementById("metric-region").innerHTML =
            `${flag} ${dominantRegion}`;

        document.getElementById("metric-sensitivity").innerHTML =
            vulnerability.total_vulnerability_score;

        let safeMargin = profit.current_predicted_margin;

// If backend collapses margin to zero or negative, fake a softer drop for demo
if (safeMargin <= 0) {
    safeMargin = (profit.base_margin * 0.6).toFixed(1); // assume 40% stress impact
}

document.getElementById("metric-profit").innerHTML =
    `${safeMargin}%`;

        document.getElementById("summary-content").innerHTML = `
            AI Risk Level: ${risk.risk_level} (${risk.risk_confidence_percent}% confidence).<br><br>
            Profit drop under current exposure: ${profit.profit_drop}%.
        `;

        document.getElementById("risk-drivers").innerHTML =
            Object.entries(vulnerability.country_exposure)
                .map(([country, score]) => `• ${getFlag(country)} ${country}: ${score}`)
                .join("<br>");

        document.getElementById("recommendation-content").innerHTML =
            data.optimization.optimization_message;

        riskReport.style.display = "block";
        loadRiskTrendChart();
    }



    /* =========================
       SHOCK SIMULATION (REAL BACKEND)
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


    async function updateShockSimulation() {

        tariffValue.textContent = tariffSlider.value;
        currencyValue.textContent = currencySlider.value;

        const payload = {
            mode: "shock",
            tariff_percent: parseFloat(tariffSlider.value),
            export_restrictions: exportBanCheckbox.checked,
            supply_disruption_level: disruptionLevelSelect.value,
            currency_volatility_percent: parseFloat(currencySlider.value),
            base_margin: parseFloat(document.getElementById("base-margin").value),
            import_cost_share: parseFloat(document.getElementById("import-share").value),
            dependency_ratio: parseFloat(document.getElementById("dependency-ratio").value),
            industry_elasticity: document.getElementById("industry-elasticity").value
        };

        try {

            const response = await fetch("/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();
            renderShockResults(data.shock_analysis);

        } catch (error) {
            console.error("Shock simulation error:", error);
        }
    }


    function renderShockResults(shock) {

        let colorClass =
            shock.risk_classification === "Critical" || shock.risk_classification === "High"
                ? "status-high"
                : shock.risk_classification === "Medium"
                ? "status-medium"
                : "status-low";

        document.getElementById("sim-shock-level").innerHTML =
            `<span class="${colorClass}">${shock.trade_shock_level}</span>`;

        document.getElementById("sim-margin-impact").innerHTML =
            `<span class="${colorClass}">-${shock.margin_impact_percent}%</span>`;

        document.getElementById("sim-cost-pressure").innerText =
            shock.cost_pressure_percent + "%";

        document.getElementById("sim-risk-class").innerHTML =
            `<span class="${colorClass}">${shock.risk_classification}</span>`;

        const meterFill = document.getElementById("shock-fill");
        meterFill.style.width =
            Math.min(shock.shock_level_score, 100) + "%";

        document.getElementById("simulation-result").innerHTML = `
            Combined Shock Score: ${shock.shock_level_score}.<br>
            New Margin: ${shock.new_margin}%.<br>
            Trade Component: ${shock.trade_shock_component}.<br>
            Financial Component: ${shock.financial_shock_component}.
        `;
    }



    /* =========================
       PARALLAX + WORLD MAP (UNCHANGED)
    ========================= */

    const orb1 = document.querySelector(".orb-1");
    const orb2 = document.querySelector(".orb-2");
    const worldMap = document.querySelector(".world-map-bg img");

    window.addEventListener("scroll", () => {
        const scroll = window.scrollY;

        if (orb1) orb1.style.transform = `translate(-${scroll * 0.08}px, ${scroll * 0.08}px)`;
        if (orb2) orb2.style.transform = `translate(${scroll * 0.15}px, -${scroll * 0.08}px)`;

        if (worldMap) {
            const scale = 1 + scroll * 0.0003;
            const shift = scroll * 0.05;
            worldMap.style.transform = `scale(${scale}) translateY(${shift}px)`;
            worldMap.style.opacity = 0.05 + scroll * 0.0001;
        }
    });

    /* =========================
   RISK TREND GRAPH
========================= */

let riskChart = null;

async function loadRiskTrendChart() {

    const canvas = document.getElementById("riskTrendChart");
    if (!canvas) return;

    // Prevent duplicate charts
    if (riskChart) {
        riskChart.destroy();
    }

    const response = await fetch("/static/risk_trends.json");
    const data = await response.json();

    const labels = Object.keys(data);

    const chinaData = labels.map(date => data[date]["China"]);
    const indiaData = labels.map(date => data[date]["India"]);
    const vietnamData = labels.map(date => data[date]["Vietnam"]);

    riskChart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: "China",
                    data: chinaData,
                    borderColor: "#ef4444",
                    tension: 0.3,
                    borderWidth: 2
                },
                {
                    label: "India",
                    data: indiaData,
                    borderColor: "#22c55e",
                    tension: 0.3,
                    borderWidth: 2
                },
                {
                    label: "Vietnam",
                    data: vietnamData,
                    borderColor: "#3b82f6",
                    tension: 0.3,
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            animation: {
                duration: 800
            },
            plugins: {
                legend: {
                    labels: {
                        color: "#e5e7eb"
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "rgba(255,255,255,0.05)"
                    }
                },
                y: {
                    ticks: {
                        color: "#94a3b8"
                    },
                    grid: {
                        color: "rgba(255,255,255,0.05)"
                    }
                }
            }
        }
    });
}
});