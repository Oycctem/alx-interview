#!/usr/bin/node
const fetch = require('node-fetch');

async function getMovieCharacters(movieId) {
    const baseUrl = 'https://swapi.dev/api/films/';
    try {
        const response = await fetch(`${baseUrl}${movieId}/`);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const movieData = await response.json();

        const characterUrls = movieData.characters;

        for (const url of characterUrls) {
            const charResponse = await fetch(url);
            if (!charResponse.ok) throw new Error(`HTTP error! Status: ${charResponse.status}`);
            const charData = await charResponse.json();
            console.log(charData.name);
        }
    } catch (error) {
        console.error(`Error fetching data: ${error}`);
    }
}

const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: node script.js <movie_id>');
    process.exit(1);
}

getMovieCharacters(movieId);