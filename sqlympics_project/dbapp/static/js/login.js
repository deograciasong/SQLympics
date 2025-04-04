// JavaScript for Login Handling

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const category = document.getElementById('category').value;

    if (email === "" || password === "") {
        alert("Please fill in all the fields.");
        return;
    }

    // Mock authentication
    if (category === "student") {
        window.location.href = "student_dashboard.html";
    } else if (category === "instructor") {
        window.location.href = "instructor_dashboard.html";
    } else {
        alert("Invalid category selected.");
    }
});
