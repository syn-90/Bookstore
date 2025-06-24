from django.db import models
from user_app.models import UserModel
# Create your models here.


class ArticleModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    img1 = models.ImageField(upload_to='articles/%Y', verbose_name= 'تصویر اول')
    img2 = models.ImageField(upload_to='articles/%Y', verbose_name="تصویر دوم ")
    para1 = models.TextField(verbose_name='پاراگراف اول')
    para2 = models.TextField(verbose_name='پاراگراف دوم')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    slug = models.SlugField(verbose_name='عنوان در مرورگر', allow_unicode=True)
    author = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, null=True,verbose_name='نویسنده', editable=False)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['id']



class ArticleCommentModel(models.Model):
    user = models.ForeignKey(to = UserModel, on_delete=models.CASCADE, verbose_name='کاربر', editable=False)
    article = models.ForeignKey(to = ArticleModel, on_delete=models.CASCADE, verbose_name='مقاله')
    text = models.TextField(verbose_name='متن')
    create_at =models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    is_publish = models.BooleanField(default=False, verbose_name="انتشار")
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها '
        ordering = ['id']
    def __str__(self):
        return f'{self.user}_{self.article}'