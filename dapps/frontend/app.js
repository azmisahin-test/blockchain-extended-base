// dapps/frontend/app.js
document.getElementById('connectButton').addEventListener('click', async () => {
    if (window.ethereum) {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } else {
        alert('No Ethereum wallet found');
    }
});
