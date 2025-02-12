class GoalsService:
    def calculate_water_goal(self, weight: float, activity_minutes: int, temperature: float) -> float:
        base_water = weight * 30
        activity_water = (activity_minutes // 30) * 500
        temperature_water = 500 if temperature > 25 else 0
        return base_water + activity_water + temperature_water

    def calculate_calories_goal(self, weight: float, height: float, age: int, activity_level: float) -> float:
        base_calories = 10 * weight + 6.25 * height - 5 * age
        activity_calories = activity_level * 200
        return base_calories + activity_calories

