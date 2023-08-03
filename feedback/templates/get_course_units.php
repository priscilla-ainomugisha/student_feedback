<?php
// get_course_units.php

// Assuming you have established a database connection already
// Replace DB_HOST, DB_USER, DB_PASS, and DB_NAME with your actual database credentials
$connection = new mysqli("localhost", "root", "", "student_feedback");

if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Get selected semester and year from the AJAX request
$selectedSemester = $_GET['semester'];
$selectedYear = $_GET['year_of_study'];

// Prepare and execute the SQL query to fetch course units based on the selected semester and year
$sql = "SELECT COURSE_NAME FROM course_info WHERE semester = $selectedSemester AND year_of_study = $selectedYear";
$result = $connection->query($sql);

// Display the course units
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<p>" . $row['COURSE_NAME'] . "</p>";
    }
} else {
    echo "<p>No course units found.</p>";
}

$connection->close();
?>
