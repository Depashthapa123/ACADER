const CHART = document.getElementById("lineChart");
console.log(CHART);
let lineChart = new Chart(CHART,{

    type: 'line',
    data: {
        labels: ["","Maths","Science","Nepali","English","Computer"],
        datasets:[
                    {
                    label:"First Term Dataset",
                    fill: false,
                    lineTension: 0.1,
                    backgroundColor: "rgba(75,192,192,0.4)",
                    borderColor: "rgba(75,192,192,1)",
                    borderCapStyle: 'butt',
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: 'miter',
                    pointBorderColor: "rgba(75,192,192,1)",
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: "rgba(75,192,192,1)",
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    data: [, 59, 80, 81, 56, 55, 40],
                    },
                        {
                        label:"Second Term Dataset",
                        fill: false,
                        lineTension: 0.1,
                        backgroundColor: "rgba(75,72,192,0.4)",
                        borderColor: "rgba(75,72,192,1)",
                        borderCapStyle: 'butt',
                        borderDash: [],
                        borderDashOffset: 0.0,
                        borderJoinStyle: 'miter',
                        pointBorderColor: "rgba(75,72,192,1)",
                        pointBackgroundColor: "#fff",
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: "rgba(75,72,192,1)",
                        pointHoverBorderColor: "rgba(220,220,220,1)",
                        pointHoverBorderWidth: 2,
                        pointRadius: 1,
                        pointHitRadius: 10,
                        data: [, 12, 40, 51, 26, 65, 22],
                        }
                ]
        }
});