mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = len(mission_names)
successful_missions = 0
missions_before_2000 = []

for name, year, success in zip(mission_names, mission_years, mission_success):
    if success:
        successful_missions += 1
    if year < 2000:
        missions_before_2000.append(name)

success_rate = (successful_missions / total_missions) * 100

print("Total number of missions:", total_missions)
print("Number of successful missions:", successful_missions)
print("Success rate: {:.2f}%".format(success_rate))
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print("-", mission)