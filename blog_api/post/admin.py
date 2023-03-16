from django.contrib import admin
from .models import Category, Tag, Post, Rating
# Register your models here.


admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Post)
admin.site.register(Rating)


class RatingInline(admin.TabularInline):
    model = Rating

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'get_rating')
    inlines = [RatingInline]
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title', )} # так как кортеж обязательно
    ordering = ['created_at'] # можно ждедлать в обратном порядке через -created_at
    list_filter = ['category__title']

    def get_rating(self, obj):
        from django.db.models import Avg
        result = obj.ratings.aggregate(Avg('rating')) # метод получения среднего рейтинга
        return result['rating__avg'] # создали новое поле таким образом 'rating__avg'
