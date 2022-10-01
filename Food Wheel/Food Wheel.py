# Import necessary libraries
from matplotlib import pyplot as plt
import pandas as pd

# Create restaurants dataframe
restaurants = pd.read_csv('restaurants.csv')

# Inspect restaurant dataframe
restaurants.head()

# Check number of unique cuisines
restaurants.cuisine.nunique()

# Group count by cuisine
cuisines = restaurants.groupby('cuisine').name.count().reset_index()
# Inspect cuisine_counts dataframe
cuisine_counts

# Create a pie chart
plt.pie(cuisines.name.values,
       labels=cuisines.cuisine.values,
       autopct='%d%%')
plt.axis('equal')
plt.title('Cuisines offered by FoodWheel')
plt.show()

# Create orders dataframe
orders = pd.read_csv('orders.csv')

# Inspect orders dataframe
restaurants.head()

# Create new month column
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
# Inspect new orders dataframe
orders.head()

# Create average order by month dataframe
avg_order = orders.groupby('month').price.mean().reset_index()
# Inspect avg_order dataframe
avg_order

# Create standard deviation dataframe
std_order = orders.groupby('month').price.std().reset_index()
# Inspect std_order
std_order

# Create barplot
ax = plt.subplot()
plt.bar(range(len(avg_order)),
       avg_order.price,
       yerr=std_order.price,
       capsize=5)
ax.set_xticks(range(len(avg_order)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Amount')
plt.title('Average Order Amount Over Time')
plt.show()

# Create customer amount dataframe
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
# Inspect customer amount
customer_amount.head()

# Create histogram
plt.hist(customer_amount.price.values,
        range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.show()

# View the unique neighborhoods
restaurants['neighborhood'].unique()

# Calculate the value counts of the neighborhood variable
restaurants['neighborhood'].value_counts()

# Create a list of the neighborhood count values
restaurants['neighborhood'].value_counts().values

# Create barplot
fig, ax = plt.subplots(figsize=(20,15))
#ax = plt.subplot(figsize=(20,15))
plt.bar(restaurants['neighborhood'].unique(),
        restaurants['neighborhood'].value_counts().values,
       capsize=5)
ax.set_xticks(range(len(restaurants['neighborhood'].unique())))
ax.set_xticklabels(['Downtown', 'Brooklyn', 'Midtown', 'Chinatown', 'Uptown', 'Queens', 'UWS'], fontsize=18)
plt.ylabel('Restaurant Count', fontsize=20)
plt.title('Neighborhood by Restaurant Count', fontsize=20)
plt.show()