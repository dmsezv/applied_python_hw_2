import aiohttp


class FoodService:
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org/cgi/search.pl"

    async def get_food_info(self, product_name):
        url = f"{self.base_url}?action=process&search_terms={product_name}&json=true"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    products = data.get("products", [])
                    if products:
                        first_product = products[0]
                        return {
                            "name": first_product.get("product_name", "Неизвестно"),
                            "calories": first_product.get("nutriments", {}).get("energy-kcal_100g", 0),
                        }
                else:
                    print(f"Ошибка: {response.status}")
                return None
