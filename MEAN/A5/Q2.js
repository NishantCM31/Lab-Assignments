const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <form action="/courses" method="POST">
            Enter course names (comma-separated): <input type="text" name="courses" /><br />
            <input type="submit" value="Submit" />
        </form>
    `);
});

app.post('/courses', (req, res) => {
    const courses = req.body.courses.split(',').map(course => course.trim());
    let courseList = '<ul>';
    courses.forEach(course => {
        courseList += `<li>${course}</li>`;
    });
    courseList += '</ul>';
    res.send(courseList);
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
