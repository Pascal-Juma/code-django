# 🛒 Retail Shop Website


A fully functional **Django-powered retail shop** where users can browse products, add them to their cart, and place orders. This project showcases **secure authentication, dynamic product management, and seamless checkout**.

## 🚀 Features

✅ **User Authentication** – Register, login, and manage user profiles  
✅ **Product Management** – Add, update, and delete products (Admin only)  
✅ **Shopping Cart** – Add/remove items and view total price  
✅ **Order System** – Users can place orders and track them  
✅ **Search & Filters** – Easily find products with category-based filtering  
✅ **Secure Payments** – Integrate with Stripe/PayPal (optional)  

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)  
- **Database:** SQLite / PostgreSQL  
- **Authentication:** Django Auth (Login, Signup, Logout)  
- **Deployment:** (Optional: Heroku, AWS, or DigitalOcean)  

##

2. **Set up a virtual environment**  
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**  
   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser**  
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Server**  
   ```sh
   python manage.py runserver
   ```


## 📜 Code Snippets

### Example: Django Model for Products

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.name
```

### Example: Adding Products in Django Admin

```python
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
```

## 📌 Next Steps

- [ ] Add Stripe/PayPal payment integration  
- [ ] Implement customer reviews & ratings  
- [ ] Improve UI/UX for better experience  

---

💡 **Built with Django, love for code, and a passion for e-commerce!** If you find this useful, feel free to contribute or give feedback. 🚀  

