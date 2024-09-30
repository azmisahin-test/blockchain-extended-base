const Web3 = require('web3');
const { web3Provider } = require('./index');

const web3 = new Web3(new Web3.providers.HttpProvider(web3Provider));

module.exports = web3;
