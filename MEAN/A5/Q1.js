const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <form action="/greet" method="POST">
            First Name: <input type="text" name="firstName" /><br />
            Last Name: <input type="text" name="lastName" /><br />
            <input type="submit" value="Submit" />
        </form>
    `);
});

app.post('/greet', (req, res) => {
    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    res.send(`Hello ${firstName} ${lastName}`);
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
