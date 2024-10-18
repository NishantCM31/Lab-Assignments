const fs = require('fs');

fs.writeFile('newfile.txt', 'This is Node Assignment for creation of new file and data', (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File created and data written successfully.');
});
