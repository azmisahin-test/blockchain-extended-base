const level = require('level');
const { leveldbPath } = require('./index');

const db = level(leveldbPath);

module.exports = db;
