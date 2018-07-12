# Toy Reid - treid6
# Homework 1: Using Matplotlib to Graph Temperature Data
# Plots the high/average temperature over a month using PyPlot.
# Emulated the given example graph as best as possible, estimating font sizes and the like.

from numpy import arange
import matplotlib.pyplot as plt


xData = arange(1,32)
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81,75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = [86.]

# Create/print average table by looping through tData
for i in range(1, 31):
    avg.append(sum(tData[:(i + 1)]) / (i + 1))
print(avg)

# Line/markers had to be separated for proper formatting
# Day vs. high temp line
plt.plot(xData, tData, color='b', lw=1)
# Data markers for day vs. high temp line
plt.scatter(xData, tData, marker='o', color='r', edgecolor='black', lw=0.5)

# Day vs. monthly average dashed line
plt.plot(xData, avg, color='g', linestyle='dashed', dashes=(6, 6), linewidth=0.9)
# "Monthly Avg" label
plt.text(15.25, 86, "Monthly Avg", color='g', fontsize=11)

# Set axis ranges and labels
plt.axis([0, 32, 70, 95])
plt.xlabel('Day', fontsize=12)
plt.ylabel('High Temp', fontsize=12)
# Plot title
plt.title('High Temperatures for Knoxville, TN - August 2013', fontsize=13)

# Set gridlines
plt.grid(linestyle='dotted', linewidth=1, dashes=(1, 3), color='dimgray')
# Pull tickmarks inside graph and change tick text font size
plt.tick_params(axis='x', direction='in', top=True, right=True, labelsize=11)
plt.tick_params(axis='y', direction='in', top=True, right=True, labelsize=11)

# Display the final plot
plt.show()
