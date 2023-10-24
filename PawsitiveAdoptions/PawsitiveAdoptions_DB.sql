-- Creating the database
CREATE DATABASE IF NOT EXISTS PawsitiveAdoptions;


-- Switching to the database
USE PawsitiveAdoptions;

-- Creating the shelter table
CREATE TABLE IF NOT EXISTS shelter (
    shelter_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    shelter_name VARCHAR(100) NOT NULL,
    location VARCHAR(50) NOT NULL,
    contact VARCHAR(20)
);

-- Creating the dog_details table
CREATE TABLE IF NOT EXISTS dog_details (
    details_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    age ENUM ("Puppy (<1 year)", "Adult (1-7 years)", "Senior (7< years)") NOT NULL,
    size ENUM ("Small", "Medium", "Large", "Giant") NOT NULL,
    sex ENUM ("Male", "Female") NOT NULL,
    breed VARCHAR(50)
);

-- Creating the rescued_dogs table with a foreign key to dog_details
CREATE TABLE IF NOT EXISTS rescued_dogs (
    rescued_dog_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    dog_name VARCHAR(50) NOT NULL,
    temperament VARCHAR(200),
    shelter_id INTEGER,
    details_id INTEGER UNIQUE, -- Making dog_id unique
    FOREIGN KEY (shelter_id) REFERENCES shelter(shelter_id),
    FOREIGN KEY (details_id) REFERENCES dog_details(details_id)
);

-- creating table for members mailing list subscription
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email_address VARCHAR(100) NOT NULL
);

-- creating index in the most used fields (to make them faster)
CREATE INDEX idx_age ON dog_details(age);
CREATE INDEX idx_size ON dog_details(size);
CREATE INDEX idx_sex ON dog_details(sex);
CREATE INDEX idx_shelter_id ON rescued_dogs(shelter_id);
CREATE INDEX idx_details_id ON rescued_dogs(details_id);

-- Inserting data for shelters
INSERT INTO shelter (shelter_name, location, contact)
VALUES
    ("Paws Sanctuary", "London", "123-456-7890"),
    ("Woof Heaven", "Belfast", "987-654-3210");

-- Inserting data for dog_details
INSERT INTO dog_details (age, size, sex, breed)
VALUES
    ("Puppy (<1 year)", "Small", "Male", "Labrador"),
    ("Adult (1-7 years)", "Medium", "Female", "Mixed breed"),
    ("Senior (7< years)", "Large", "Male", "German Shepherd"),
    ("Puppy (<1 year)", "Small", "Female", "Mixed breed"),
    ("Adult (1-7 years)", "Medium", "Male", "Golden Retriever"),
    ("Senior (7< years)", "Large", "Female", "Husky"),
    ("Adult (1-7 years)", "Giant", "Male", "Great Dane"),
    ("Puppy (<1 year)", "Medium", "Male", "Mixed breed"),
    ("Adult (1-7 years)", "Giant", "Female", "Boxer"),
    ("Senior (7< years)", "Small", "Male", "Dachshund"),
    ("Puppy (<1 year)", "Large", "Female", "French Bulldog"),
    ("Adult (1-7 years)", "Medium", "Male", "Cocker Spaniel"),
    ("Senior (7< years)", "Large", "Female", "Mixed breed"),
    ("Adult (1-7 years)", "Medium", "Male", "Mixed breed"),
    ("Adult (1-7 years)", "Large", "Male", "Bernese Mountain Dog");
    
-- Linking dogs to shelters and connecting them to dog_details
INSERT INTO rescued_dogs (dog_name, temperament, shelter_id, details_id)
VALUES
        ('Buddy', 'Friendly', 1, 1),
	('Lacy', 'Energetic', 1, 2), 
	('Max', 'Calm', 1, 3),
	('Nina', 'Playful', 1, 4),
	('Milo', 'Anxious', 1, 5),
	('Kira', 'Playful', 1, 6),
	('Joe', 'Calm', 1, 7),
	('Rocky', 'Spirited', 2, 8),
	('Bella', 'Gentle', 2, 9),
	('Dobby', 'Adventurous', 2, 10),
	('Luna', 'Sweet', 2, 11),
	('Zeus', 'Curious', 2, 12),
	('Rosie', 'Playful', 2, 13),
	('Oliver', 'Calm', 2, 14),
        ('Rigel', 'Crazy', 2, 15);

-- inserting data into members table
INSERT INTO members (full_name, email_address)
VALUES
    ("Emma White", "emmwhite@gmail.com"),
    ("Joe FitzGerald", "jofitz16@outlook.com"),
    ("Kyle Sloan", "sloank8@gmail.com"),
    ("Liz Tanner", "lltanner@gmail.com"),
    ("Maxine Trujillo", "max1jantrujillo@hotmail.com");
    
