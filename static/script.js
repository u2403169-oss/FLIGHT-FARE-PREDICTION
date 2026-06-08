document.getElementById("fareForm").addEventListener("submit", async function(e){

    e.preventDefault();

    const data = {
        Total_Stops: parseInt(document.getElementById("Total_Stops").value),
        Journey_day: parseInt(document.getElementById("Journey_day").value),
        Journey_month: parseInt(document.getElementById("Journey_month").value),
        Dep_hour: parseInt(document.getElementById("Dep_hour").value),
        Dep_min: parseInt(document.getElementById("Dep_min").value),
        Arrival_hour: parseInt(document.getElementById("Arrival_hour").value),
        Arrival_min: parseInt(document.getElementById("Arrival_min").value),
        Duration_hours: parseInt(document.getElementById("Duration_hours").value),
        Duration_mins: parseInt(document.getElementById("Duration_mins").value),
        Airline: document.getElementById("Airline").value,
        Source: document.getElementById("Source").value,
        Destination: document.getElementById("Destination").value
    };

    const response = await fetch("/predict", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
`💰 Estimated Fare: ₹ ${result.predicted_fare}`;
});