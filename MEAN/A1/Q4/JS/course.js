document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const course = urlParams.get('course');

    const courseTitle = document.getElementById('course-title');
    const courseDescription = document.getElementById('course-description');
    const admissionDetails = document.getElementById('admission-details');

    const courses = {
        physics: {
            title: 'Physics',
            description: 'The study of matter, energy, and the interaction between them.',
            details: [
                'Intake: 60 students',
                'Fees: INR 50,000 per year',
                'Eligibility: 12th pass with minimum 60% marks'
            ]
        },
        chemistry: {
            title: 'Chemistry',
            description: 'The study of substances, their properties, and reactions.',
            details: [
                'Intake: 60 students',
                'Fees: INR 50,000 per year',
                'Eligibility: 12th pass with minimum 60% marks'
            ]
        },
        // Add other courses similarly
    };

    if (courses[course]) {
        courseTitle.textContent = courses[course].title;
        courseDescription.textContent = courses[course].description;
        admissionDetails.innerHTML = courses[course].details.map(detail => `<li>${detail}</li>`).join('');
    }
});
