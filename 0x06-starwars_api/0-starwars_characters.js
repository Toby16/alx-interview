#!/usr/bin/node
/*
 * Star Wars Characters
 * A script that prints all characters of a Star Wars movie
 */

const request = require('request');

const arg = process.argv[2];
// console.log(arg);

// Function to make a GET request using the request module
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

makeRequest('https://swapi-api.alx-tools.com/api/films/' + arg + '/')
  .then(data => {
    // List of endpoints to characters object
    const dataCharacters = data.characters;

    const promises = dataCharacters.map(item => {
      return makeRequest(item).then(characterData => {
        console.log(characterData.name);
      });
    });

    // Wait for all promises to resolve
    return Promise.all(promises);
  })
  .catch(error => console.error('Error:', error));
