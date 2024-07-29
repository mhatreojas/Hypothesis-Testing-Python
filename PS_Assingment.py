import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data from the CSV file
data = pd.read_csv("hypothesis_test.csv")

# Filter data for females
female_data = data[data['Gender ?'] == 'Female']

# Set significance level
alpha = 0.05

# Calculate mean ratings for hungriness at 4-6pm for population and females
mean_rating_population_4_6 = data['hungriness_4_6'].mean()
mean_rating_female_4_6 = female_data['hungriness_4_6'].mean()

# Perform hypothesis testing for hungriness at 4-6pm
t_statistic_4_6, p_value_4_6 = stats.ttest_ind(data['hungriness_4_6'], female_data['hungriness_4_6'], equal_var=False)

# Print results for hungriness at 4-6pm
print("================= Hypothesis Testing Results (4-6 pm) =================")
print("Mean rating for hungriness at 4-6pm for population:", mean_rating_population_4_6)
print("Mean rating for hungriness at 4-6pm for females:", mean_rating_female_4_6)
print("T-statistic (4-6 pm):", t_statistic_4_6)
print("P-value (4-6 pm):", p_value_4_6)

# Check if null hypothesis is rejected for hungriness at 4-6pm
if p_value_4_6 < alpha:
    print("Reject the null hypothesis for 4-6 pm (Ho)")
else:
    print("Fail to reject the null hypothesis for 4-6 pm (Ho)")

# Calculate mean ratings for hungriness at 8-10am for population and females
mean_rating_population_8_10 = data['hungriness_8_10'].mean()
mean_rating_female_8_10 = female_data['hungriness_8_10'].mean()

# Perform hypothesis testing for hungriness at 8-10am
t_statistic_8_10, p_value_8_10 = stats.ttest_ind(data['hungriness_8_10'], female_data['hungriness_8_10'], equal_var=False)

# Print results for hungriness at 8-10am
print("================= Hypothesis Testing Results (8-10 am) =================")
print("Mean rating for hungriness at 8-10am for population:", mean_rating_population_8_10)
print("Mean rating for hungriness at 8-10am for females:", mean_rating_female_8_10)
print("T-statistic (8-10 am):", t_statistic_8_10)
print("P-value (8-10 am):", p_value_8_10)

# Check if null hypothesis is rejected for hungriness at 8-10am
if p_value_8_10 < alpha:
    print("Reject the null hypothesis for 8-10 am (Ho)")
else:
    print("Fail to reject the null hypothesis for 8-10 am (Ho)")

# Plot bar graph and pie chart for 8-10 am
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Bar graph for 8-10 am
axes[0].bar(['Population', 'Females'], [mean_rating_population_8_10, mean_rating_female_8_10], color=['skyblue', 'pink'])
axes[0].set_xlabel('Group')
axes[0].set_ylabel('Mean Rating')
axes[0].set_title('Mean Rating of Hungriness at 8-10am')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].set_ylim(0, 10)
axes[0].tick_params(axis='both', which='major', labelsize=12)

# Pie chart for distribution of population vs females (8-10 am)
labels_8_10 = ['Population', 'Females']
sizes_8_10 = [len(data), len(female_data)]
colors_8_10 = ['skyblue', 'pink']
explode_8_10 = (0, 0.1)

axes[1].pie(sizes_8_10, explode=explode_8_10, labels=labels_8_10, colors=colors_8_10, autopct='%1.1f%%', shadow=True, startangle=140)
axes[1].set_title('Distribution of Population vs Females (8-10 am)')
axes[1].axis('equal')

plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing between subplots

plt.show()

# Plot bar graph and pie chart for 4-6 pm
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Bar graph for 4-6 pm
axes[0].bar(['Population', 'Females'], [mean_rating_population_4_6, mean_rating_female_4_6], color=['skyblue', 'pink'])
axes[0].set_xlabel('Group')
axes[0].set_ylabel('Mean Rating')
axes[0].set_title('Mean Rating of Hungriness at 4-6pm')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].set_ylim(0, 10)
axes[0].tick_params(axis='both', which='major', labelsize=12)

# Pie chart for distribution of population vs females (4-6 pm)
labels_4_6 = ['Population', 'Females']
sizes_4_6 = [len(data), len(female_data)]
colors_4_6 = ['skyblue', 'pink']
explode_4_6 = (0, 0.1)

axes[1].pie(sizes_4_6, explode=explode_4_6, labels=labels_4_6, colors=colors_4_6, autopct='%1.1f%%', shadow=True, startangle=140)
axes[1].set_title('Distribution of Population vs Females (4-6 pm)')
axes[1].axis('equal')

plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing between subplots

plt.show()
