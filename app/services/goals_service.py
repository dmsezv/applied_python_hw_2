from schemas.models import User


class GoalsService:
    def calculate_water_goal(self, weight: float, activity_minutes: int, temperature: float) -> float:
        base_water = weight * 30
        activity_water = (activity_minutes // 30) * 500
        temperature_water = 500 if temperature > 25 else 0
        return base_water + activity_water + temperature_water

    def calculate_calories_goal(
        self, weight: float, height: float,
        age: int, activity_level: float, gender: str
    ) -> float:
        # Базовая формула для расчета калорий
        base_calories = 10 * weight + 6.25 * height - 5 * age

        if gender.lower() == "male":
            base_calories += 5
        elif gender.lower() == "female":
            base_calories -= 161

        activity_calories = activity_level * 50
        return base_calories + activity_calories

    def calculate_calories_burned(
        self,
        user: User,
        workout_type: str,
        duration_minutes: int
    ) -> float:
        # Уравнение для расчета метаболического эквивалента задачи
        met_values = {
            "run": 9.8,
            "cycle": 7.5,
            "swim": 8.0,
            "plank": 3.8,
            "gym": 6.0,
            "klimbing": 8.0
        }
        met = met_values.get(workout_type, 1)
        calories_per_minute = (met * user.weight * 3.5) / 200
        total_calories_burned = calories_per_minute * duration_minutes
        return total_calories_burned

    def calculate_water_burned(
        self,
        user: User,
        workout_type: str,
        duration_minutes: int
    ) -> float:
        # Уравнение для расчета воды, сжигаемой в течение задачи
        activity_coefficients = {
            "run": 0.07,
            "cycle": 0.05,
            "swim": 0.06,
            "plank": 0.03,
            "gym": 0.04,
            "klimbing": 0.06
        }
        activity_coefficient = activity_coefficients.get(workout_type, 0.03)
        water_burned_per_minute = (user.weight * activity_coefficient) / 1000
        total_water_burned = water_burned_per_minute * duration_minutes
        if user.temperature > 25:
            total_water_burned += 0.5
        return total_water_burned
