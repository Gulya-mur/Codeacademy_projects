# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

conversion = {"M": 1000000,
              "B": 1000000000}

def converter_damages(lists_damages, dict_conv):
  converted_damages = []
  for i in range(len(lists_damages)):
      if "M" in lists_damages[i]:
          num_M = lists_damages[i][:-1]
          converted_damages.append(float(float(num_M) * (dict_conv["M"])))
      elif "B" in lists_damages[i]:          
          num_B = lists_damages[i][:-1]
          converted_damages.append(float(float(num_B) * (dict_conv["B"])))
      else:
          
          converted_damages.append(lists_damages[i])
  return converted_damages

# test function by updating damages
conv_damages = converter_damages(damages,conversion)

# 2 
# Create a Table
value_lists = list(zip( names, months, years, max_sustained_winds, areas_affected, deaths))

def full_info(value_lists, index_name):
  key_lists = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Deaths"]
  dict_with_full_info ={}
  for key in range(len(key_lists)):
    dict_with_full_info[key_lists[key]] = value_lists[index_name][key]
  return dict_with_full_info

print(full_info(value_lists = value_lists, index_name = names.index("Labor Day")))

# Create and view the hurricanes dictionary
hurricanes = {}

def info_hurricanes(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name" : names[i], "Month": months[i], "Year": years[i], 'Max sustained Wind': max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage":damages[i], "Deaths": deaths[i]}
  return hurricanes

dict_hurricanes = info_hurricanes(names = names, months = months, years = years, max_sustained_winds =max_sustained_winds, areas_affected =areas_affected, damages = conv_damages, deaths = deaths)
print(hurricanes)

# 3
# Organizing by Year

sorted_by_year = []

def chosen_year(year):
  for i in range(len(years)):
    if hurricanes[names[i]]["Year"] == year:
      sorted_by_year.append(hurricanes[names[i]])
  return sorted_by_year

chosen_year(1932)
print(sorted_by_year)

# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

print()
affected_areas_frequency = {}
def frequency_of_hurricanes():
  for name in hurricanes:
    for area in hurricanes[name]["Areas Affected"]:
      if area not in affected_areas_frequency:
        affected_areas_frequency[area] = 1
      else:
        affected_areas_frequency[area] +=1 
  return affected_areas_frequency

frequency_of_hurricanes()
print(affected_areas_frequency)
      

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
print()
def max_affected_area():
  max_area = affected_areas_frequency["Mexico"]
  max_area_count = 7
  for area in affected_areas_frequency:
    if affected_areas_frequency[area] > max_area_count:
      max_area = area
      max_area_count = affected_areas_frequency[area]
  return f"The most affected area by hurricanes is {max_area}, {max_area_count} times"
  

print(max_affected_area())


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def fatality():
  hurricane_name = ''
  num_of_death = 0
  for name in hurricanes:
    if hurricanes[name]['Deaths'] > num_of_death:
      num_of_death = hurricanes[name]['Deaths']
      hurricane_name = hurricanes[name]['Name']
  return f'Hurricane caused the greatest number of deaths is {hurricane_name}, death number: {num_of_death}'

print(fatality())

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0:0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# categorize hurricanes in new dictionary with mortality severity as key
dict_mortality_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

def dict_mortality():
  for name in hurricanes:
    if hurricanes[name]['Deaths'] == 0:
      dict_mortality_scale[0].append(hurricanes[name])
    elif 0 < hurricanes[name]['Deaths'] <= 100:
      dict_mortality_scale[1].append(hurricanes[name])
    elif 100 < hurricanes[name]['Deaths'] <= 500:
      dict_mortality_scale[2].append(hurricanes[name])
        
    elif 500 < hurricanes[name]['Deaths'] <= 1000:
      dict_mortality_scale[3].append(hurricanes[name])        
    elif 1000 < hurricanes[name]['Deaths'] <= 1000:
      dict_mortality_scale[4].append(hurricanes[name])        
    else:
      dict_mortality_scale[5].append(hurricanes[name])
        
  return dict_mortality_scale

dict_mortality()
print(dict_mortality_scale)