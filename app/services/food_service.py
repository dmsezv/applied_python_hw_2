import aiohttp
from sqlalchemy import select
from database.models import Food as FoodModel, User as UserModel, Statistics as StatisticsModel
from schemas.models import Food
from database.db import get_session
from datetime import datetime, date


class FoodService:
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org/cgi/search.pl"

    async def get_food_info(self, request):
        food = self._check_food_in_db(request)
        if food:
            return food

        url = f"{self.base_url}?action=process&search_terms={request}&json=true"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    products = data.get("products", [])
                    if products:
                        first_product = products[0]
                        product_name = first_product.get("product_name")
                        calories = first_product.get("nutriments", {}).get("energy-kcal_100g")
                        if product_name and calories:
                            food = Food(
                                request=request,
                                title=product_name,
                                calories=calories,
                            )
                            self._save_food_to_db(food)
                            return food
                        else:
                            return None
                else:
                    print(f"Ошибка: {response.status}")
                return None

    def _check_food_in_db(self, product_name):
        with get_session() as session:
            stmt = select(FoodModel).where(FoodModel.request == product_name)
            result = session.execute(stmt).scalars().first()
            if result:
                return Food(
                    request=result.request,
                    title=result.title,
                    calories=result.calories
                )
            return None

    def _save_food_to_db(self, food: Food):
        with get_session() as session:
            try:
                stmt = select(FoodModel).where(FoodModel.request == food.request)
                result = session.execute(stmt).scalar_one_or_none()

                if result:
                    return

                food_model = FoodModel(
                    request=food.request,
                    title=food.title,
                    calories=food.calories
                )
                session.add(food_model)
                session.commit()
                session.refresh(food_model)
            except Exception as e:
                print(f"Ошибка при сохранении продукта в базу данных: {e}")
