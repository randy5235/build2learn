#!/usr/bin/env node
'use strict';

const {promisify} = require('util');

const fs = require('fs');
const readFileAsync = promisify(fs.readFile);

const optionsObject = require('./options');

async function getWordListStream(parsedOptions) {
  const {wordList} = parsedOptions;
  return await readFileAsync(wordList, {encoding: 'utf8'});
}

async function optionsParser(optionsObject) {
  return await {
    wordList: optionsObject.wordlist || optionsObject.w,
    outputFile: optionsObject.output || optionsObject.o
  };
}

optionsParser(optionsObject)
  .then(getWordListStream)
  .then(output => console.log(output));
