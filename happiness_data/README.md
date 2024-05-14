
# Interactive Data Exploration

This Streamlit application allows exploration and visualisation of relationships between various factors that contribute to happiness scores across countries. It uses the World Happiness Report dataset to uncover insights about how elements like GDP, social support, life expectancy, and others impact happiness levels.

This was created as a means for me to explore some features from streamlit, as I have primarily used non-interactive Jupyter notebooks during my bootcamp.

## Features

- **Interactive Visualisation:**  Create scatter plots to analyze how two chosen factors correlate with each other.
- **Customisable Axes:** Select any two variables from the dataset (e.g., Happiness vs. GDP, Life Expectancy vs. Freedom) to display on the x and y axes.
- **Streamlit Interface:** An intuitive web interface for easy data exploration.
- **Powered by Plotly:** Utilises Plotly's graphing library for visually appealing plots.

## Installation & Setup

1. **Clone Repository:**
   ```bash
   git clone https://github.com/CriticallyDave/codingTasks/happiness_data.git
   cd happiness_data
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt 
   ```

3. **Data Preparation:**
   - Ensure that the happiness data in a CSV file named `happy.csv` is within the project directory. 

## Usage

1. **Start the App:**
   ```bash
   streamlit run main.py 
   ```

2. **Explore the Data:**
   - The app will open in your web browser.
   - Use the dropdown menus to select the x-axis and y-axis variables.
   - The scatter plot will update automatically to display your chosen data.


## Dataset

The World Happiness Report dataset is used for this project. You can find the data and details on the official report website: [https://worldhappiness.report/](https://worldhappiness.report/)
