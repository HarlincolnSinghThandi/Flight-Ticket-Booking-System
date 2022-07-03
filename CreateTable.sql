CREATE DATABASE Airline_Ticket_Info;

USE Airline_Ticket_Info;

CREATE TABLE signup_info(
	unique_user_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    contact_number CHAR(13) NOT NULL,
    email_id VARCHAR(100) NOT NULL,
    user_password VARCHAR(500) CHARACTER SET BINARY NOT NULL,
    PRIMARY KEY(unique_user_id)
);

CREATE TABLE passenger_flight_info(
	unique_user_id INT NOT NULL,
    passenger_full_name VARCHAR(500),
    passenger_contact_no INT, 
    passenger_email_id VARCHAR(500), 
    passenger_passport_number CHAR, 
    passenger_unique_mark VARCHAR(500), 
    passenger_identity_proof VARCHAR(500), 
    passenger_luggage_weight INT, 
    passenger_food_type VARCHAR(500), 
    passenger_require_disability_equipment VARCHAR(3), 
	passenger_other_requirements VARCHAR(500), 
    passenger_flight_departure VARCHAR(100), 
    passenger_flight_arrival VARCHAR(100), 
    passenger_trip_type VARCHAR(10), 
    passenger_flight_selected VARCHAR(100), 
    passenger_flight_code CHAR(10), 
    passenger_flight_departure_time CHAR(10),
    passenger_flight_departure_location VARCHAR(100),
    passenger_flight_arrival_location VARCHAR(100),
    passenger_flight_average_time CHAR(15),
    passenger_flight_cost CHAR(15),
    PRIMARY KEY(unique_user_id)
);
