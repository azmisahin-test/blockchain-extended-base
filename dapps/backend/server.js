const express = require('express');
const cors = require('cors');
const web3 = require('../config/web3_setup');
const ipfs = require('../config/ipfs_setup');
const db = require('../config/leveldb_setup');

const app = express();
app.use(express.json());
app.use(cors());

app.get('/api', (req, res) => {
  res.send('Blockchain project is running');
});

app.get('/blockchain', async (req, res) => {
  try {
    const blockNumber = await web3.eth.getBlockNumber();
    res.json({ blockNumber });
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching block number');
  }
});

app.listen(3000, () => {
  console.log('DApp backend running on port 3000');
});
