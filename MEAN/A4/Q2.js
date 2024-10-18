const fs = require('fs');

fs.readFile('yp.py', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
