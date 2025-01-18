import pandas as pd

data = pd.Series([1, 2, 3, 4, 5])

population_dict = {
    "California": 38332521,
    "Texas": 26448193,
    "New York": 19651127,
    "Florida": 19552860,
    "Illinois": 12882135
}

area_dict = {
    "California": 423967,
    "Texas": 695662,
    "New York": 141297,
    "Florida": 170312,
    "Illinois": 149995
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)

states = pd.DataFrame({"population": population, "area": area})

states["density"] = states["population"] / states["area"]

print(states)