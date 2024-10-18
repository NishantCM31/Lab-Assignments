/* const http = require('http');

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    const currentDate = new Date();
    res.write("Current Date and Time: " + currentDate.toString());
    res.end();
}).listen(3000);

console.log('Server running at http://localhost:3000/');
 */

const getFormattedDate = () => {
    const now = new Date();
    const date = now.toLocaleDateString();
    const time = now.toLocaleTimeString();
    return `Date: ${date}, Time: ${time}`;
};

console.log("Current Date and Time:", getFormattedDate());
