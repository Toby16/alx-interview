#!/usr/bin/node
/*
 * Star Wars Characters
 * A script that prints all characters of a Star Wars movie
 */

const arg = process.argv[2];
// console.log(arg);

fetch('https://swapi-api.alx-tools.com/api/films/' + arg + '/')
  .then(response => response.json())
  .then(data => {
    // List of endpoints to characters object
    const dataCharacters = data.characters;

    dataCharacters.forEach(item => {
      fetch(item)
        .then(response => response.json())
        .then(data => {
          console.log(data.name);
        })
        .catch(error => console('Error:', error));
    });
  })
  .catch(error => console.error('Error:', error));
