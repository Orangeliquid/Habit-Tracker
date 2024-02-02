# Habit Tracker Using Pixela

A Python script for interacting with the Pixela API to create, update, and delete user-defined graphs, enabling users to track and visualize custom metrics.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- User creation via POST requests to Pixela API.
- Graph creation and configuration, supporting custom graph names, units, and colors.
- Adding pixels to graphs with dynamic date and quantity inputs.
- Updating pixels and graph units via PUT requests.
- Deleting pixels via DELETE requests.

## Getting Started

### Prerequisites

- Python 3.x installed.
- Pixela account created with a valid token.
- Pixela graph ID obtained.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Orangeliquid/pixela-api-interaction.git
   ```

2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
   
3. Set environment variables:
   ```bash
   export USERNAME="your_pixela_username"
   export TOKEN="your_pixela_token"
   export GRAPH_ID="your_pixela_graph_id"
   ```

## Usage

1. Execute the script:
   ```bash
   python habit_tracker.py
   ```
   
2. Follow the prompts to interact with the Pixela API, create graphs, add pixels, update values, and delete pixels.

3. When adding a pixel to the graph Pixela will reject 25 percent of all requests. Simply try again

## Examples

### Create User
   ```python
   # Uncomment and run to create a new Pixela user
   # response = requests.post(url=pixela_endpoint, json=user_params)
   # print(response.text)
   ```

### Create Graph
   ```python
   # Uncomment and run to create a new graph
   # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
   # print(response.text)
   ```

### Add Pixel
   ```python
   # Uncomment and run to add a pixel to the graph
   # response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
   # print(response.text)
   ```

## Screenshots
![Pixela_Example](https://github.com/Orangeliquid/Habit-Tracker/assets/127478612/999ced44-220b-41a5-a870-a5c02ea5acbc)

## License
This project is licensed under the [MIT License](LICENSE.txt).
