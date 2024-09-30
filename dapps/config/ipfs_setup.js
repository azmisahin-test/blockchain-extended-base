const IPFS = require('ipfs-http-client');
const { ipfs } = require('./index');

const ipfsClient = IPFS({
  host: ipfs.host,
  port: ipfs.port,
  protocol: ipfs.protocol
});

module.exports = ipfsClient;
