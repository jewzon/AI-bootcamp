import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Load Dataset ----------------
df = pd.read_csv("mxmh_survey_results.csv")  # change filename if needed

# ---------------- Age Grouping ----------------
if "Age" in df.columns:
    age_bins = [10, 19, 29, 39, 49, 59, 69, 100]
    age_labels = ["Teens", "20s", "30s", "40s", "50s", "60s", "70+"]
    df["Age Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

# ---------------- Column Selection ----------------
print("\nAvailable Columns:")
for i, col in enumerate(df.columns):
    print(f"{i+1}. {col}")

choice = input("\nEnter column numbers (comma separated): ")
cols = [df.columns[int(c.strip())-1] for c in choice.split(",")]

print(f"\nYou selected: {cols}\n")

# ---------------- Graph Type Menu ----------------
graph_options = []

if len(cols) == 1:
    graph_options = ["Histogram", "Bar Chart", "Pie Chart", "Box Plot"]
elif len(cols) == 2:
    graph_options = ["Scatter Plot", "Line Plot", "Grouped Bar Chart", "Box/Violin Plot"]
elif len(cols) == 3:
    graph_options = ["Scatter Plot with Hue", "Grouped Bar Chart", "Box/Violin Plot with Hue", "Facet Grid"]
else:
    graph_options = ["Heatmap (correlation)", "Pairplot", "Stacked Bar Chart", "Radar Chart"]

print("Available Graph Types:")
for i, g in enumerate(graph_options):
    print(f"{i+1}. {g}")

graph_choice = int(input("\nEnter the graph number you want to plot: ")) - 1
selected_graph = graph_options[graph_choice]
print(f"\nYou chose: {selected_graph}\n")

# ---------------- Plotting Based on Selection ----------------
plt.figure(figsize=(8,5))

if selected_graph == "Histogram":
    sns.histplot(df[cols[0]], kde=True, bins=10)
    plt.title(f"Distribution of {cols[0]}")

elif selected_graph == "Bar Chart":
    if df[cols[0]].dtype == "object":
        sns.countplot(data=df, x=cols[0])
    else:
        df[cols[0]].value_counts().plot(kind='bar')
    plt.title(f"Bar chart of {cols[0]}")

elif selected_graph == "Pie Chart":
    df[cols[0]].value_counts().plot.pie(autopct="%1.1f%%")
    plt.title(f"Pie chart of {cols[0]}")

elif selected_graph == "Box Plot":
    sns.boxplot(data=df, y=cols[0])
    plt.title(f"Box plot of {cols[0]}")

elif selected_graph == "Scatter Plot":
    sns.scatterplot(data=df, x=cols[0], y=cols[1])
    plt.title(f"{cols[0]} vs {cols[1]}")

elif selected_graph == "Line Plot":
    sns.lineplot(data=df, x=cols[0], y=cols[1])
    plt.title(f"{cols[0]} vs {cols[1]}")

elif selected_graph == "Grouped Bar Chart":
    sns.barplot(data=df, x=cols[0], y=cols[1])
    plt.title(f"Grouped Bar: {cols[0]} vs {cols[1]}")

elif selected_graph == "Box/Violin Plot":
    sns.boxplot(data=df, x=cols[0], y=cols[1])
    plt.title(f"Box plot: {cols[0]} vs {cols[1]}")

elif selected_graph == "Scatter Plot with Hue":
    sns.scatterplot(data=df, x=cols[0], y=cols[1], hue=cols[2])
    plt.title(f"{cols[0]} vs {cols[1]} grouped by {cols[2]}")

elif selected_graph == "Box/Violin Plot with Hue":
    sns.boxplot(data=df, x=cols[0], y=cols[1], hue=cols[2])
    plt.title(f"Box plot: {cols[0]} vs {cols[1]} grouped by {cols[2]}")

elif selected_graph == "Facet Grid":
    g = sns.FacetGrid(df, hue=cols[2])
    g.map_dataframe(sns.scatterplot, x=cols[0], y=cols[1])
    g.add_legend()
    plt.title(f"{cols[0]} vs {cols[1]} by {cols[2]}")

elif selected_graph == "Heatmap (correlation)":
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")

elif selected_graph == "Pairplot":
    sns.pairplot(df[cols])
    plt.title("Pairplot")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 
