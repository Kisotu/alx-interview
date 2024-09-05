#!/usr/bin/node

const req = require('req');
const STWARS_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  req(`${STWARS_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charsURL = JSON.parse(body).characters;
    const charsName = charsURL.map(
      url => new Promise((resolve, reject) => {
        req(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charsName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
