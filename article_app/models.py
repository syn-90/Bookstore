from django.db import models

# Create your models here.


class ArticleModel(models.Model):
    title = models.CharField(max_length=150 , verbose_name='عنوان')
    craete_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ')
    author = models.CharField(max_length=50, verbose_name='نویسنده')
    img1 = models.ImageField(upload_to='articles/%Y', verbose_name='اصویر اول')
    img2 = models.ImageField(upload_to='articles/%Y', verbose_name='تصویر دوم')
    para1 = models.TextField(null=True, blank=True, verbose_name='پاراگراف دوم')
    para2 = models.TextField(null=True, blank=True, verbose_name='پاراگراف دوم')
    slug = models.SlugField(null=True, verbose_name='عنوان در مرورگر')

    def __str__(self) :
        return self.title
    class Meta:
        verbose_name = "مقاله "
        verbose_name_plural = "مقالات"