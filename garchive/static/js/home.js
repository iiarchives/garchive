"use strict";
// home.html
// Subtitle
void function () {
    // Variables
    let subtitleElement = document.getElementById("subtitle");
    let index = 0;
    let subtitles = [
        "A Minecraft server made of geese, by geese, for geese!",
        "The warden can eat my fat a-",
        "Has DmmD joined yet?",
        "Geesecraft? More like craft.",
        "Whats up logeese!",
        "Bread.",
        "Only the finest members allowed.",
        "What's that? You like jazz?",
        "HONK!",
        "Geese have wings."
    ];
    // Update Subtitle
    setInterval(() => {
        index = (index + (Math.floor(Math.random() * subtitles.length) || 1)) % subtitles.length;
        subtitleElement.style.opacity = "0";
        setTimeout(() => {
            subtitleElement.innerText = subtitles[index];
            subtitleElement.style.opacity = "";
        }, 1000);
    }, 10000);
}();
// Status
void async function () {
    // Variables
    let styleDeclaration = getComputedStyle(document.body);
    let buttonDay = document.getElementById("status-day");
    let buttonWeek = document.getElementById("status-week");
    let buttonMonth = document.getElementById("status-month");
    let latencyElement = document.getElementById("latency");
    let latencyData = await fetchLatencyData();
    // @ts-ignore
    let chart = new Chart(latencyElement, {
        data: {
            datasets: [{
                    data: latencyData.map(entry => entry.value),
                    label: "Latency (ms)",
                    borderWidth: 1
                }],
            labels: latencyData.map(entry => entry.label)
        },
        options: {
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    displayColors: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: `rgb(${styleDeclaration.getPropertyValue("--theme-gray-dim")})`
                    }
                }
            }
        },
        type: "line"
    });
    // Buttons
    buttonDay.onclick = buttonWeek.onclick = buttonMonth.onclick = async () => {
        latencyData = await fetchLatencyData();
        updateChart();
    };
    // Functions
    function updateChart() {
        chart.data.datasets[0].data = latencyData.map(entry => entry.value);
        chart.data.labels = latencyData.map(entry => entry.label);
        chart.update();
    }
}();
// Temporary Functions
async function fetchLatencyData() {
    return [
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
        {
            "label": "May 10, 3:30",
            "value": Math.floor(Math.random() * 100)
        },
    ];
}
