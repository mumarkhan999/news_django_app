from django.contrib import admin

from .models import Article, Comment


# there is also another option available here
# like admin.StackedInline
class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
