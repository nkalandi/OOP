from datetime import datetime
import random  # Додано для випадкового вибору погоди та настрою

# Змінні з інформацією
name = "Назарій"
location = "Львів"
activity = "працювати над цікавим проєктом"  # Більш конкретна діяльність

# Списки для випадкового вибору погоди та настрою
weather_options = ["сонячна погода", "хмарно з проясненнями", "легкий дощ", "снігопад", "теплий вітерець"]
mood_options = ["натхненно", "енергійно", "зосереджено", "спокійно", "у творчому піднесенні"]

# Випадковий вибір погоди та настрою
weather = random.choice(weather_options)
mood = random.choice(mood_options)

# Отримуємо поточний час у форматі "день.місяць.рік години:хвилини"
current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# Вивід інформації
message = f"""{">*<"*20}
{name} почав {activity} {current_time}. 
{location} — чудове місто з {weather} сьогодні. 
{name} працює {mood} і планує досягти великих результатів!
{"<*>"*20}"""

print(message)