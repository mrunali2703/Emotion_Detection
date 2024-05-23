async function detectEmotions() {
    const text = document.getElementById('text-input').value;
    console.log("Text to analyze:", text);  // Log the text input

    try {
        const response = await fetch('http://localhost:5000/detect_emotions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        if (response.ok) {
            const result = await response.json();
            console.log("Response from server:", result);  // Log the response from the server
            document.getElementById('result').innerText = 'Detected Emotions: ' + result.emotions;
        } else {
            console.error('Error in response:', response.statusText);  // Log error response
            document.getElementById('result').innerText = 'Error detecting emotions: ' + response.statusText;
        }
    } catch (error) {
        console.error('Error during fetch:', error);  // Log any errors from fetch
        document.getElementById('result').innerText = 'Error detecting emotions: ' + error.message;
    }
}
