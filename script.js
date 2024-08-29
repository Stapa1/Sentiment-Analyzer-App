async function submitReview() {
    const text = document.getElementById('review').value;
    if (!text) {
        alert("Please enter a review text.");
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        const result = await response.json();
        const resultDiv = document.getElementById('result');
        resultDiv.style.display = 'block'; // Show the result div
        resultDiv.innerText = `Sentiment: ${result[0].label}, Score: ${result[0].score.toFixed(2)}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = "An error occurred while analyzing the sentiment.";
    }
}
