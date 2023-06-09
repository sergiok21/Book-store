from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Name: {self.name}'


class Book(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='books_images', null=True, blank=True)
    category = models.ForeignKey(to=BookCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        book = Book.objects.filter(id=self.id)
        if book.exists():
            book.get(id=self.id).image.delete(False)
        return super(Book, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f'Name: {self.name} | Category: {self.category.name} | Price: {self.price} | Quantity: {self.quantity}'


class Preview(models.Model):
    book = models.OneToOneField(to=Book, related_name='previews', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='books_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Preview'
        verbose_name_plural = 'Previews'
        ordering = ['id']

    def __str__(self):
        return f'Name: {self.book.name}'


class Recommendation(models.Model):
    book = models.OneToOneField(to=Book, related_name='recommendations', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='books_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'
        ordering = ['id']

    def __str__(self):
        return f'Name: {self.name}'


class Partner(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='partners_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        ordering = ['id']

    def __str__(self):
        return f'Company: {self.name}'


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    house = models.SmallIntegerField(default=0)
    corps = models.SmallIntegerField(default=0)
    postal = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['id']

    def __str__(self):
        return f'Email: {self.email} | Phone: {self.phone} | Country: {self.country}'


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['id']

    def __str__(self):
        return f'Email: {self.email} | Message: {self.message}'
