const submitBtn = document.getElementById('submitBtn');
const dataInput = document.getElementById('dataInput');
const responseOutput = document.getElementById('responseOutput');

submitBtn.addEventListener('click', async () => {
    const inputData = dataInput.value.split(',').map(item => item.trim());

    try {
        const response = await fetch('/bfhl', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: inputData })
        });

        const result = await response.json();
        responseOutput.textContent = JSON.stringify(result, null, 4);

    } catch (error) {
        responseOutput.textContent = 'Error: ' + error.message;
    }
});
