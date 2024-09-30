require('dotenv').config();

module.exports = {
  web3Provider: process.env.WEB3_PROVIDER_ENDPOINT,
  ipfs: {
    host: process.env.IPFS_HOST || 'localhost',
    port: process.env.IPFS_PORT || '5001',
    protocol: process.env.IPFS_PROTOCOL || 'http'
  },
  leveldbPath: './leveldb'
};
