const express = require('express');
const app = express();

app.use(express.static('frontend'));

app.listen(3000, () => {
    console.log('DApp backend server running on http://localhost:3000');
});
