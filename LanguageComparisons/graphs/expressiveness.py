import numpy as np
import matplotlib.pyplot as plt

# Define the categories and their respective scores for each language
categories_extended = ['Language Efficiency', 'Sociolinguistic Diversity', 'Cultural Expression', 'Linguistic Innovation', 'Expressivity']
language_efficiency = [0.7, 0.7, 0.7, 0.6, 0.9]  # English, Russian, French, German, Mandarin
sociolinguistic_diversity = [1.0, 0.8, 0.8, 0.7, 0.7]
cultural_expression = [1.0, 1.0, 1.0, 1.0, 1.0]
linguistic_innovation = [1.0, 0.7, 0.7, 0.7, 1.0]
expressivity_scores = [1.0, 0.9, 0.85, 0.9, 0.95]

# Combine the scores into a single array and transpose it for plotting
scores_extended = np.array([language_efficiency, sociolinguistic_diversity, cultural_expression, linguistic_innovation, expressivity_scores])
scores_T_extended = scores_extended.T

# Function to add each language's data to the radar chart
def add_to_radar_adjusted(language_scores, color, label):
    values = language_scores.tolist() + language_scores[:1].tolist()
    angles = [n / float(len(categories_extended)) * 2 * np.pi for n in range(len(categories_extended))]
    angles += angles[:1]
    ax.plot(angles, values, color=color, linewidth=3, linestyle='solid', label=label)
    ax.fill(angles, values, color=color, alpha=0.2)

# Setup the radar chart
plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)

# Plot each language on the radar chart
add_to_radar_adjusted(scores_T_extended[0], 'purple', 'English')  # English
add_to_radar_adjusted(scores_T_extended[1], 'blue', 'Russian')    # Russian
add_to_radar_adjusted(scores_T_extended[2], 'orange', 'French')   # French
add_to_radar_adjusted(scores_T_extended[3], 'red', 'German')      # German
add_to_radar_adjusted(scores_T_extended[4], 'yellow', 'Mandarin') # Mandarin

# Set up the chart with category labels, tick marks, and a legend
angles = [n / float(len(categories_extended)) * 2 * np.pi for n in range(len(categories_extended))]
angles += angles[:1]
plt.xticks(angles[:-1], categories_extended, color='grey', size=12)
ax.set_rlabel_position(0)
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"], color="grey", size=10)
plt.ylim(0,1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.3))

# Show the plot
plt.show()