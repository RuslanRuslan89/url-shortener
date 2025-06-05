document.getElementById('shorten-btn').addEventListener('click', async () => {
  const url = document.getElementById('url-input').value;
  if (!url) return;

  const response = await fetch('http://localhost:8000/shorten', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: url })
  });

  if (response.ok) {
    const data = await response.json();
    document.getElementById('result').innerHTML = `
      <p>Ваша короткая ссылка: <a href="${data.short_url}" target="_blank">${data.short_url}</a></p>
    `;
  } else {
    alert('Ошибка!');
  }
});
