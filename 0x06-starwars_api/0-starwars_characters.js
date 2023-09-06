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

async function printCharacterNames () {
  try {
    const filmData = await makeRequest('https://swapi-api.alx-tools.com/api/films/' + arg + '/');
    const dataCharacters = filmData.characters;

    for (const characterUrl of dataCharacters) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

printCharacterNames();
