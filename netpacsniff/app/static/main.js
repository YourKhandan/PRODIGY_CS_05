const socket = io();

socket.on('packet', data => {
    const table = document.getElementById('packetTable');
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${data.time}</td>
        <td>${data.domain}</td>
        <td>${data.protocol}</td>
        <td>${data.ip}</td>`;
    table.prepend(row);
});

