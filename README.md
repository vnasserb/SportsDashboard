# Sports Data Scraping and Streamlit Dashboard

## Overview

This repository contains a set of Python functions for web scraping sports data related to soccer, basketball, and hockey from https://www.sports-reference.com. 
Additionally, it includes a Streamlit web application that uses some of these functions to create an interactive dashboard for displaying sports statistics and information.

## Features

### Web Scraping Functions

- **Soccer Data Scraping:** Retrieve information such as scores, player statistics, and team standings from soccer-related websites.

- **Basketball Data Scraping:** Extract scores, player stats, and team standings from basketball-related web sources.

- **Hockey Data Scraping:** Gather scores, player performance metrics, and team standings from hockey-related websites.

### Streamlit Dashboard

- **Interactive UI:** A user-friendly interface powered by Streamlit, allowing users to select their preferred sport and view relevant data.

- **Data Visualization:** Display key statistics and insights using charts, graphs, and tables for a comprehensive overview of the selected sport.

- **Real-time Updates:** Utilize the web scraping functions to fetch the latest sports data and update the dashboard dynamically.

## Getting Started

### Prerequisites

- Python installed (download from [python.org](https://www.python.org/downloads/))
- Install required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/vnasserb/SportsDashboard.git
```

2. Navigate to the project directory:

```bash
cd SportsDashboard
```

3. Run the Streamlit app:

```bash
streamlit run 1/Soccer.py
streamlit run 2/NBA.py
streamlit run 3/NHL.py
```

This will launch the web application in your default browser.

## Demo

You can access a live demo of the app [here](#) (replace with the actual link once deployed).


## Acknowledgments

- Special thanks to the Streamlit team for providing an excellent framework for building interactive web applications with Python.
