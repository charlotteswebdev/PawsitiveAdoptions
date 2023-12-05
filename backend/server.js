// In your server.js file

const express = require('express');
const mysql = require('mysql');
const cors = require('cors'); // Import the CORS middleware

const app = express();
const port = 3000;

app.use(cors()); // Enable CORS for all routes

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Doncross1!', // Replace with your MySQL password
  database: 'wondermap'// Replace with your WonderMap database name
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    return;
  }
  console.log('Connected to MySQL');
});

// Define a route to retrieve events based on category
app.get('/api/events', (req, res) => {
    const category = req.query.category;
    let query;
  
    if (category) {
      // If a category is provided, filter events by category
      query = `SELECT * FROM events WHERE category = '${category}'`;
    } else {
      // If no category is provided, fetch all events
      query = 'SELECT * FROM events';
    }
  
    connection.query(query, (error, results) => {
      if (error) {
        console.error('Error executing query:', error);
        res.status(500).json({ error: 'Internal Server Error' });
        return;
      }
  
      res.json(results);
    });
  });
  
// Define a route to retrieve all categories
app.get('/api/categories', (req, res) => {
  const query = 'SELECT DISTINCT category FROM events';

  connection.query(query, (error, results) => {
    if (error) {
      console.error('Error executing query:', error);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }

    const categories = results.map((result) => ({ id: result.category, label: result.category }));
    res.json(categories);
  });
});


  app.get('/', (req, res) => {
    res.send('Hello, this is the WonderMap backend!');
  });

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
