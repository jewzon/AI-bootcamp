# 📊 Interactive Data Visualization Tool  

This Python script allows you to interactively explore a dataset and plot different types of graphs depending on the number of columns you select. It uses **Pandas**, **Matplotlib**, and **Seaborn** for data handling and visualization.  

---

## 🚀 Features
- Load any CSV dataset.  
- Automatically group ages into categories (if an `Age` column exists).  
- Choose columns interactively.  
- Menu-based graph selection depending on the number of chosen columns.  
- Supports multiple chart types:
  - Histogram  
  - Bar Chart  
  - Pie Chart  
  - Box / Violin Plot  
  - Scatter Plot  
  - Line Plot  
  - Grouped Bar Chart  
  - Scatter Plot with Hue  
  - Facet Grid  
  - Correlation Heatmap  
  - Pairplot  

---

## 🛠️ Requirements (if using local machine)
Install dependencies before running:
```bash
pip install pandas matplotlib seaborn


## 🔧 How to Use

1. Place your dataset CSV file in the same folder as the script.  
2. Update the script with your dataset name:  
   ```python
   df = pd.read_csv("your_dataset.csv")

Run 
```bash
python visualization.py
