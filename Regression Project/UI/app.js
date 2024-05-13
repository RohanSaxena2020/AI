function calculateScoringAverage() {
    const sgOTT = document.getElementById('sg_ott').value;
    const sgAPP = document.getElementById('sg_app').value;
    const sgATG = document.getElementById('sg_atg').value;
    const sgPutting = document.getElementById('sg_putting').value;

    fetch('http://localhost:8000/predict/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        sg_ott: parseFloat(document.getElementById('sg_ott').value),
        sg_app: parseFloat(document.getElementById('sg_app').value),
        sg_atg: parseFloat(document.getElementById('sg_atg').value),
        sg_putting: parseFloat(document.getElementById('sg_putting').value)
    })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Predicted Scoring Average: ${data.scoring_average}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Failed to retrieve prediction.';
    });
}



