# как будто это не списки, а файлы БД, которые лежат на сервере
users = []
products = []
recipes = []

recipe_categories = {
    1: 'первые блюда',
    2: 'вторые блюда',
    3: 'выпечка'
}

product_categories = {
    1: ('бакалея', 'RGB-code'),
    2: ('мясо и птица', 'RGB-code')
}

units = {
    1: 'г',
    2: 'мл',
    3: 'шт.'
}


class Product:
    id = 0

    def __init__(self, name, category_id, unit_id):
        Product.id += 1
        self.name = name
        self.category_id = category_id
        self.unit = unit_id
        products.append(self)


class ListItem:
    def __init__(self, product, quantity):
        """
        Принимает объект класса Product и его количество
        :param product:
        :param quantity:
        """
        self.product = product
        self.quantity = quantity


class AnyList:

    def __init__(self, list_name):
        """
        При инициировании создаётся пустой словарь self.items
        Ключи - объекты класса Product, значения - количество продуктов
        :param user_id:
        :param name:
        """
        self.name = list_name
        self.items = dict()

    def add_item(self, name, quantity):
        """
        Ищет в products объект класса Product с self.name = name

        Если такого элемента в products нет,
        то дополнительно запрашивает у пользователя категорию продукты и единицу измерения,
        создаёт новый продукт и добавляет его в products и в self.items списка продуктов.

        Если такой продукт есть в products, то
        проходит по ключам словаря (self.items), проверяет, нет ли уже среди ключей такого объекта класса Product.

        Если нет - добавляет новый элекмент.
        Если есть, то не добавляет новый элемент, а увеличивает количество.

        :param name:
        :return:
        """
        pass

    def delete_item(self, product):
        """
        Получает на вход объект класса Product
        и удаляет элемент с таким ключом из словаря self.items
        :param product:
        :return:
        """
        pass


class ShoppingList(AnyList):
    def __init__(self, user_id, name):
        super().__init__(name)
        self.user_id = user_id

    def add_products_from_recipe(self, recipe, portions_num):
        """
        Принимает объект класса Recipe и количество порций
        :param recipe:
        :param portions_num:
        :return:
        """
        items_to_add = recipe.items
        items_to_add.update((key, value * portions_num) for key, value in items_to_add.items)
        for product in self.items.keys():
            if product in items_to_add:
                self.items[product] += items_to_add.pop(product)

        self.items.update(items_to_add)


class Recipe(AnyList):
    id = 0

    def __init__(self, name, instruction, recipe_category_id, url=None):
        Recipe.id += 1
        super().__init__(name)
        self.instruction = instruction
        self.recipy_category_id = recipe_category_id
        self.url = url
        recipes.append(self)


class UserRecipe(AnyList):
    """
    Отличается от Recipe тем, что не добавляет себя в recipes и не имеет url
    """
    def __init__(self, list_name, instruction, recipe_category_id):
        super().__init__(list_name)
        self.instruction = instruction
        self.recipe_category_id = recipe_category_id
        self.recipy_category_id = recipe_category_id


class User:
    id = 0

    def __init__(self, id, email, password, name):
        User.id += 1
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.shopping_lists = []
        self.recipes = []
        users.append(self)

    def set_password(self):
        pass

    def set_email(self):
        pass

    def set_name(self):
        pass

    def create_shopping_list(self, list_name):
        new_shopping_list = ShoppingList(self.id, list_name)
        self.shopping_lists.append(new_shopping_list)

    def delete_shopping_list(self, list_name):
        pass

    def create_new_recipe(self, recipe_name, recipe_instruction, recipe_category_id):
        """
        Метод создаёт объект класса UserRecipe (отличается от Recipe тем, что не добавляется в общую базу recipes)
        :param recipe_name:
        :return:
        """
        new_recipe = UserRecipe(recipe_name, recipe_instruction, recipe_category_id)
        self.recipes.append(new_recipe)

    def add_recipe_by_url(self, url):
        """
        Метод принимает url
        проверяет, нет ли в recipes уже рецепта с таким url.
        Если нет, то парсит его, создает новый объект класса Recipe и добавляет его в self.recipes пользователя
        Если уже есть, то просто добавляет его в self.recipes пользователя
        """
        pass

    def add_recipe_from_database(self, recipe):
        """
        Метод принимает объект класса Recipe, и если такого нет в self.recipes, то добавляет его
        :param recipe:
        :return:
        """
        pass

    def delete_recipe(self, recipe):
        """
        Метод принимает объект класса Recipe или UserRecipe,
        находит его в self.recipes и удаляет его оттуда.

        :return:
        """
        pass
