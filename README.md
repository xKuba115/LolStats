# LolStats-API
LolStats-API is a web application that allows you to retrieve your League of Legends (LoL) game statistics by providing your LoL username. 
It interacts with the Riot Games API to fetch data from your recent 20 games, compiles the information into a JSON file, and displays it through a Flask-based API on a simple webpage.

## Features
Retrieve Game Stats: Simply input your LoL username, and the application will fetch and display the statistics from your most recent 20 games.

JSON Data: All game statistics are compiled into a JSON file for easy access and further analysis.

Web Interface: The results are presented on a user-friendly webpage, making it easy to view and share your LoL stats.

## Project Structure
The project consists of the following components:

Backend in Python: The backend is built using Python, with Flask serving as the web framework.

Riot Games API Integration: The application communicates with the Riot Games API to access your LoL game data.

JSON Data: Game statistics are collected and stored in a JSON file for easy access and further processing.

Webpage: The frontend is a simple webpage built using HTML/CSS/JS. It allows users to input their LoL username and fetch game statistics.

## Dependencies
Python  
Flask  
Riot Games API key  
# Usage
Input your LoL username in the provided field on the webpage.

Click the "Get Stats" button to fetch and display your game statistics.

