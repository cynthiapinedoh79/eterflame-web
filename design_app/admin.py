from django.contrib import admin
from .models import PortfolioItem, CaseStudy


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display  = ['title', 'kicker', 'order', 'is_featured', 'is_active']
    list_editable = ['order', 'is_featured', 'is_active']
    list_filter   = ['is_featured', 'is_active', 'is_screenshot']
    ordering      = ['order']


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display        = ['__str__', 'slug', 'is_published']
    list_editable       = ['is_published']
    prepopulated_fields = {'slug': []}
    fieldsets = (
        ('Link & Identity', {
            'fields': ('portfolio_item', 'slug', 'title_line1', 'title_line2',
                       'eyebrow', 'subtitle', 'live_url', 'github_url', 'is_published')
        }),
        ('Metrics', {
            'fields': (
                ('metric_1_value', 'metric_1_label'),
                ('metric_2_value', 'metric_2_label'),
                ('metric_3_value', 'metric_3_label'),
                ('metric_4_value', 'metric_4_label'),
                ('metric_5_value', 'metric_5_label'),
            )
        }),
        ('Content', {
            'fields': ('challenge', 'approach', 'approach_bullets',
                       'approach_insight', 'deliverables',
                       'results_intro', 'result_1_desc', 'result_2_desc',
                       'result_3_desc', 'results_outro', 'cta_title')
        }),
    )
