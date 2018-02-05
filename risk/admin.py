from django.contrib import admin

from risk.models import ThirdPartyTarif, ComprehensiveTarif, Risk


class RisksAdmin(admin.ModelAdmin):
    pass


class ThirdPartyTarifsAdmin(admin.ModelAdmin):
    pass


class ComprehensiveTarifsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Risk, RisksAdmin)
admin.site.register(ThirdPartyTarif, ThirdPartyTarifsAdmin)
admin.site.register(ComprehensiveTarif, ComprehensiveTarifsAdmin)
