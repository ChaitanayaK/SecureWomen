import math

# Time in 24 hour format
time = "20:00".split(":")
time = int(time[0]) + (int(time[1])/60)

# Number of people near the user
people = 2

# Distance of user from their home(in meters)
d_home = 21000
d_home /= 1000

# Distance of user from nearest Police Station(in meters)
d_police = 2000
d_police /= 1000

# Distance of user from nearest Populated Area(in meters)
d_pop = 4000
d_pop /= 1000

# Actual Total Risk: 5.836746223087822

def risk(time: float, people: int, d_home: float, d_police: float, d_pop: float):
    risk_time = (4 * math.cos((math.pi / 13) * (time - 3))) + 6
    print(f"Risk in Time: {risk_time}")

    # risk_people = (8/people) + 2
    # risk_people = (8 * math.exp(-0.2*people)) + 3.3
    risk_people = (8 * math.exp(-0.05*people)) + 2
    print(f"Risk in People: {risk_people}")

    risk_home = (0.32 * d_home) + 2
    # risk_home = (8 * math.exp(0.12 * d_home)) + 2
    print(f"Risk in Home: {risk_home}")

    risk_police = math.exp(0.4158 * d_police) + 2
    print(f"Risk in Police: {risk_police}")

    risk_pop = math.exp(0.4158 * d_pop) + 2
    print(f"Risk in Population: {risk_pop}\n")

    total_risk = (0.1*risk_time) + (0.2*risk_people) + (0.2*risk_home) + (0.2*risk_police) + (0.3*risk_pop)
    # total_risk = (0.2*risk_time) + (0.2*risk_people) + (0.2*risk_home) + (0.2*risk_police) + (0.2*risk_pop)

    print(f"Actual Total Risk: {total_risk}")


risk(time, people, d_home, d_police, d_pop)