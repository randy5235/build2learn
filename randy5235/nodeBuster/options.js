'use-strict';
const package = require('./package.json');

// purposeful destructuring to remove first two elements
const [, , ...flags] = process.argv; 

module.exports = (() => {
  const flagObject = flags.reduce((prev, current, index) => {
    if (/^-h/.test(current) || /^--help/.test(current)) {
      return {...prev, help:true};
    }
    if (/^-v/.test(current) || /^--version/.test(current)) {
      return {...prev, version:true};
    }
    if (/^-{1,2}(.+)/.test(current)) {
      return {...prev, [/^-{1,2}(.*)/.exec(current)[1]]: flags[index+1]};
    }
    if (/^https?\:\/\//.test(current)) {
      return {...prev, baseUrl: current};
    }
    return {...prev};
  }, {})

  if (flagObject.version) {
    console.log(package.version);
        process.exit(0);
  }

  if (flagObject.help) {
    console.log(`
      nodeBuster [options] <baseUrl>

      -w, --wordlist    specifies the wordlist file
      -o, --output      specifies the output file
    `);
    process.exit(0);
  }
  return flagObject
})();