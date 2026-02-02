print("🧠 AI Weekly Habit Trend Analyzer \n")

sleep = []
work = []
exercise = []

print("Enter data for 7 days\n")

for i in range(7):
    sleep.append(float(input(f"Day {i+1} sleep hours: ")))
    work.append(float(input(f"Day {i+1} work hours: ")))
    exercise.append(int(input(f"Day {i+1} exercise minutes: ")))

def analyze_trend(data):
    if data[-1] > data[0]:
        return "Improving 📈"
    elif data[-1] < data[0]:
        return "Declining 📉"
    else:
        return "Stable ➖"

print("\n📊 WEEKLY TREND ANALYSIS")

print("Sleep Trend:", analyze_trend(sleep))
print("Work Trend:", analyze_trend(work))
print("Exercise Trend:", analyze_trend(exercise))

print("\n🧭 AI Insights")

if analyze_trend(sleep) == "Declining 📉":
    print("• Improve sleep consistency")
if analyze_trend(work) == "Increasing 📈":
    print("• Monitor workload to avoid burnout")
if analyze_trend(exercise) == "Declining 📉":
    print("• Increase physical activity")
