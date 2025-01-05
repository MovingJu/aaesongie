document.getElementById('fetchData').addEventListener('click', () => {
    fetch('http://127.0.0.1:5000/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('serverData').textContent = data.message;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
