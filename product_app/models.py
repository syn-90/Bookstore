from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیر فعال")
    slug = models.SlugField(verbose_name="عنوان در مرورگر")
    def __str__(self) :
        return self.title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class AuthorModel(models.Model):
    image = models.ImageField(upload_to='authors/', verbose_name="تصویر")
    name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    birth = models.IntegerField( verbose_name="تاریخ تولد(سال) ")
    language = models.CharField(max_length=50, verbose_name="زبان", null=True)
    number_books = models.IntegerField(verbose_name="تعداد کتاب های نویسنده")
    number_awards = models.IntegerField(verbose_name="تعداد جوایز نویسنده")
    category = models.ManyToManyField(to=CategoryModel, verbose_name="ژانر کتاب های  نویسنده")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(verbose_name="عنوان در مرورگر")

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"





class ProductModel(models.Model) :
    image = models.ImageField(upload_to='products/', verbose_name="تصویر")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    publication_date = models.DateField(auto_now_add=False, verbose_name="تاریخ انتشار")
    publisher = models.CharField(max_length=50, verbose_name="ناشر")
    length = models.IntegerField(verbose_name="طول کتاب")
    version = models.IntegerField(verbose_name="نسخه")
    ISBN = models.IntegerField(verbose_name="شابک")
    language = models.CharField(max_length=50, verbose_name="زبان")
    author = models.ForeignKey(to=AuthorModel,on_delete=models.CASCADE,  verbose_name="نویسنده")
    category = models.ForeignKey(to=CategoryModel, on_delete=models.CASCADE, verbose_name="دسته بندی کتاب")
    description = models.TextField(verbose_name="توضیحات")
    seller = models.CharField(max_length=50, verbose_name="فروشنده")
    is_off = models.IntegerField(blank=True, verbose_name="تخفیف(بصورت درصد)")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیر فعال")
    slug = models.SlugField(verbose_name= "عنوان در مرورگر", allow_unicode=True)
    def seprator(self):
        return "{:,}".format(self.price)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

