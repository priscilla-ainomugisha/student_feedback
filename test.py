import matplotlib.pyplot as plt

# Data for the pie chart
labels = ["Category A", "Category B", "Category C", "Category D"]
sizes = [30, 25, 20, 25]  # Percentages for each category
colors = ["blue", "green", "orange", "red"]
explode = (0.1, 0, 0, 0)  # Explode the first slice (Category A)

# Create a pie chart
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
plt.axis("equal")  # Equal aspect ratio ensures the pie is circular

# Add a title
plt.title("Distribution of Categories")

# Show the pie chart
plt.show()
