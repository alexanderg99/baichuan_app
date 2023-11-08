function submitText() {
    let inputText = document.getElementById('inputText').value;
    console.log('Response from FastAPI:');

    fetch('localhost:8000/infer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({inputText: inputText}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerHTML = "<strong>Result:</strong> " + data.result;\
        console.log('Response from FastAPI:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}