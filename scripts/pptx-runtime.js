const path = require('path');

function loadPptxGenJS() {
  try {
    return require('pptxgenjs');
  } catch (e) {
    const runtimeDir = path.join(__dirname, '..', 'assets', 'runtime');
    global.JSZip = require(path.join(runtimeDir, 'jszip.min.js'));
    return require(path.join(runtimeDir, 'pptxgen.bundle.js'));
  }
}

module.exports = { loadPptxGenJS };
