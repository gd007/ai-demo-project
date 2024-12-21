import pandas as pd

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "location": ["New York", "Paris", "Berlin", "London"],
    "age": [24, 13, 53, 33],
}

df = pd.DataFrame(data)

df.head(2)

df.replace("New York", "NYC")

print("Hello World")
