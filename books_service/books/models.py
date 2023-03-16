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
        return f'Продукт: {self.name} | Категория: {self.category.name}'
