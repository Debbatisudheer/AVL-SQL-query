function executeQuery() {
    var query = document.getElementById("queryInput").value.trim().toLowerCase();

    // Normalize the query to remove extra spaces
    query = query.replace(/\s+/g, "");

    var queryResultDiv = document.getElementById("queryResult");

    // Clear previous results
    queryResultDiv.innerHTML = "";

    // Check if the query matches the expected format
    var expectedQuery = "select*fromemployees";
    expectedQuery = expectedQuery.replace(/\s+/g, "");

    if (query !== expectedQuery) {
        queryResultDiv.innerHTML = "<p>Please enter the query 'SELECT * FROM employees'.</p>";
        return;
    }

    // Assuming a mock response for demonstration
    var mockResponse = {
        result: [
            ["20A1", "Sudheer", "21", "alice@example.com", "Area1", "India"],
            ["20A2", "Suddhu", "22", "bob@example.com", "Area2", "India"],
            ["20B1", "Charlie", "23", "charlie@example.com", "Area3", "USA"],
            ["20C2", "Sudhir", "24", "david@example.com", "Area4", "India"]
        ]
    };

    // Displaying result
    var headers = ["ID", "Name", "Age", "Email", "Area", "Country"];
    var table = "<table><tr>";
    headers.forEach(header => {
        table += "<th>" + header + "</th>";
    });
    table += "</tr>";

    mockResponse.result.forEach(row => {
        table += "<tr>";
        row.forEach(cell => {
            table += "<td>" + cell + "</td>";
        });
        table += "</tr>";
    });

    table += "</table>";
    queryResultDiv.innerHTML = table;
}