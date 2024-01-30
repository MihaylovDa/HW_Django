from django.shortcuts import get_object_or_404

# Создание нового клиента
def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client

# Получение списка клиентов
def get_clients():
    return Client.objects.all()

# Получение клиента по его идентификатору
def get_client_by_id(client_id):
    return get_object_or_404(Client, pk=client_id)

# Обновление данных клиента
def update_client(client_id, name, email, phone_number, address):
    client = get_object_or_404(Client, pk=client_id)
    client.name = name
    client.email = email
    client.phone_number = phone_number
    client.address = address
    client.save()
    return client

# Удаление клиента
def delete_client(client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()

# Создание нового товара
def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product

# Получение списка товаров
def get_products():
    return Product.objects.all()

# Получение товара по его идентификатору
def get_product_by_id(product_id):
    return get_object_or_404(Product, pk=product_id)

# Обновление данных товара
def update_product(product_id, name, description, price, quantity):
    product = get_object_or_404(Product, pk=product_id)
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity
    product.save()
    return product

# Удаление товара
def delete_product(product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

# Создание нового заказа
def create_order(client_id, product_ids):
    client = get_object_or_404(Client, pk=client_id)
    products = Product.objects.filter(pk__in=product_ids)
    total_amount = sum(product.price for product in products)
  
      order = Order(client=client, total_amount=total_amount)
      order.save()
      order.products.set(products)
      return order

# Получение списка заказов
def get_orders():
    return Order.objects.all()

# Получение заказа по его идентификатору
def get_order_by_id(order_id):
    return get_object_or_404(Order, pk=order_id)

# Обновление данных заказа
def update_order(order_id, client_id, product_ids):
    order = get_object_or_404(Order, pk=order_id)
    client = get_object_or_404(Client, pk=client_id)
    products = Product.objects.filter(pk__in=product_ids)
    total_amount = sum(product.price for product in products)
    order.client = client
    order.total_amount = total_amount
    order.save()
    order.products.set(products)
    return order

# Удаление заказа
def delete_order(order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
