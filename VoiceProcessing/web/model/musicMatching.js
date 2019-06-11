const spawn = require('child_process').spawn;
const path = require('path');

let getSongName = (filename) => {
  return new Promise((resolve, reject) => {
    let pyProgram = spawn('python3', ['/home/doxanh/VoiceProcessing/web/controller/music_matching/main.py', filename]);
    pyProgram.stdout.on('data', data => {
      let tmp = new Buffer.from(String.fromCharCode.apply(null, data));
      let tmp2 = tmp.toString();
      resolve(tmp2);
    });

    pyProgram.stderr.on('data', data => {
      let tmp = String.fromCharCode.apply(null, data);
      let tmp2 = tmp.toString();
      reject(tmp2);
    });
  })
};

exports.getSongName = getSongName;