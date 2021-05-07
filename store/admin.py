from django.contrib import admin
from .models import Book, Coupon

class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'description', 'publish_date')

admin.site.register(Book, BookAdmin)

class CouponAdmin(admin.ModelAdmin):
   list_display = ('title', 'description', 'coupon_code', 'expiry_date')

admin.site.register(Coupon, CouponAdmin)