-- Create a new database
CREATE DATABASE wondermap;

-- Use the newly created database
USE wondermap;


CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    event_time TIME NOT NULL
);

INSERT INTO events (category, name, location, latitude, longitude, event_time) VALUES
    ('Romantic', 'Fireplace Cabin Experience', 'Cozy Hills Chalet', 51.5001, -0.0901,'15:00'),
    ('Romantic', 'Love Actually Cinema Screening', 'Starlight Cinema', 51.5302, -0.1102, '18:00'),
    ('Romantic', 'Stargazing Domes', 'Celestial Retreat Center', 51.5103, -0.1303, '19:00'),
    ('Family Friendly', 'Santa, Elves, and Reindeer Meet and Greet', 'Jolly Junction Square', 51.5104, -0.1204,'13:00'),
    ('Family Friendly', 'Festive Family Photoshoot', 'Frosty Frame Studio', 51.5205, -0.1005, '14:00'),
    ('Family Friendly', 'Presents Scavenger Hunt', 'Gifted Gardens Park', 51.4906, -0.0806, '12:00');


-- Show the contents of the events table
SELECT * FROM events;

