import math
def calculatedRisk(time: float, people: int, d_home: float, d_police: float, d_pop: float):
    risk_time = (4 * math.cos((math.pi / 13) * (time - 3))) + 6
    risk_people = (8 * math.exp(-0.05 * people)) + 2
    risk_home = (0.32 * d_home) + 2
    risk_police = math.exp(0.4158 * d_police) + 2
    risk_pop = math.exp(0.4158 * d_pop) + 2

    total_risk = (0.1 * risk_time) + (0.2 * risk_people) + (0.1 * risk_home) + (0.3 * risk_police) + (0.3 * risk_pop)

    freq = (total_risk - 7.171190576487) / 1.125
    if freq > 0:
        return (freq, total_risk)
    else:
        return (freq, total_risk)

if __name__ == "__main__":
    frequency = calculatedRisk(time=8.75, people=48, d_home=52, d_police=0.5, d_pop=0.7997)
    print(f"Frequency of Calls: {frequency[0]}\nTotal risk of Condition: {frequency[1]}")