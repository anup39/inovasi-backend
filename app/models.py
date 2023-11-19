from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


# Create your models here.


class Facility(models.Model):

    id = models.AutoField(primary_key=True)
    facilities_eq_id = models.CharField(max_length=255, help_text=_(
        "facilities_eq_id"), verbose_name=_("facilities_eq_id"), null=True)
    facilities_name = models.CharField(max_length=255, help_text=_(
        "facilities_name"), verbose_name=_("facilities_name"), null=True)
    facilities_address = models.CharField(max_length=500, help_text=_(
        "facilities_address"), verbose_name=_("facilities_address"), null=True)
    facilities_type = models.CharField(max_length=255, help_text=_(
        "facilities_type"), verbose_name=_("facilities_type"), null=True)
    facilities_lat = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="facilities_lat", verbose_name="facilities_lat",
        null=True
    )
    facilities_long = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="facilities_long", verbose_name="facilities_long",
        null=True
    )
    facilites_rspo = models.CharField(max_length=255, help_text=_(
        "facilites_rspo"), verbose_name=_("facilites_rspo"), null=True)
    facilites_date_update = models.CharField(max_length=255, help_text=_(
        "facilites_date_update"), verbose_name=_("facilites_date_update"), null=True)
    created_at = models.DateTimeField(default=timezone.now, help_text=_(
        "Creation date"), verbose_name=_("Created at"))
    geom = models.PointField(srid=4326, dim=2, null=True)
    is_display = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = GeoManager()

    class Meta:
        verbose_name = _("Facility")
        verbose_name_plural = _("Facilities")

    def __str__(self):
        return str(self.facilities_address)


class Refinery(models.Model):

    id = models.AutoField(primary_key=True)
    refinery_eq_id = models.CharField(max_length=255, help_text=_(
        "refinery_eq_id"), verbose_name=_("refinery_eq_id"), null=True)
    refinery_name = models.CharField(max_length=255, help_text=_(
        "refinery_name"), verbose_name=_("refinery_name"), null=True)
    refinery_address = models.CharField(max_length=500, help_text=_(
        "refinery_address"), verbose_name=_("refinery_address"), null=True)
    refinery_type = models.CharField(max_length=255, help_text=_(
        "refinery_type"), verbose_name=_("refinery_type"), null=True)
    refinery_lat = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="refinery_lat", verbose_name="refinery_lat",
        null=True
    )
    refinery_long = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="refinery_long", verbose_name="refinery_long",
        null=True
    )
    refinery_rspo = models.CharField(max_length=255, help_text=_(
        "refinery_rspo"), verbose_name=_("refinery_rspo"), null=True)
    refinery_date_update = models.CharField(max_length=255, help_text=_(
        "refinery_date_update"), verbose_name=_("refinery_date_update"), null=True)
    created_at = models.DateTimeField(default=timezone.now, help_text=_(
        "Creation date"), verbose_name=_("Created at"))
    geom = models.PointField(srid=4326, dim=2, null=True)
    is_display = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = GeoManager()

    class Meta:
        verbose_name = _("Refinery")
        verbose_name_plural = _("Refineries")

    def __str__(self):
        return str(self.refinery_address)


class Mill(models.Model):
    id = models.AutoField(primary_key=True)
    mill_company_name = models.CharField(max_length=255, help_text=_(
        "mill_company_name"), verbose_name=_("mill_company_name"), null=True)
    mill_company_group_id = models.CharField(max_length=255, help_text=_(
        "mill_company_group_id"), verbose_name=_("mill_company_group_id"), null=True)
    mill_company_group = models.CharField(max_length=255, help_text=_(
        "mill_company_group"), verbose_name=_("mill_company_group"), null=True)
    mill_country = models.CharField(max_length=255, help_text=_(
        "mill_country"), verbose_name=_("mill_country"), null=True)
    mill_province = models.CharField(max_length=255, help_text=_(
        "mill_province"), verbose_name=_("mill_province"), null=True)
    mill_district = models.CharField(max_length=255, help_text=_(
        "mill_district"), verbose_name=_("mill_district"), null=True)
    mill_address = models.CharField(max_length=500, help_text=_(
        "mill_address"), verbose_name=_("mill_address"), null=True)
    mill_type = models.CharField(max_length=255, help_text=_(
        "mill_type"), verbose_name=_("mill_type"), null=True)
    mill_lat = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="mill_lat", verbose_name="mill_lat",
        null=True
    )
    mill_long = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text="mill_long", verbose_name="mill_long",
        null=True
    )
    mill_rspo = models.CharField(max_length=255, help_text=_(
        "mill_rspo"), verbose_name=_("mill_rspo"), null=True)
    mill_mspo = models.CharField(max_length=255, help_text=_(
        "mill_mspo"), verbose_name=_("mill_mspo"), null=True)
    mill_capacity = models.CharField(max_length=255, help_text=_(
        "mill_capacity"), verbose_name=_("mill_capacity"), null=True)
    mill_methane_capture = models.CharField(max_length=255, help_text=_(
        "mill_methane_capture"), verbose_name=_("mill_methane_capture"), null=True)
    mill_deforestation_risk = models.CharField(max_length=255, help_text=_(
        "mill_deforestation_risk"), verbose_name=_("mill_deforestation_risk"), null=True)
    mill_legal_prf_risk = models.CharField(max_length=255, help_text=_(
        "mill_legal_prf_risk"), verbose_name=_("mill_legal_prf_risk"), null=True)
    mill_legal_production_forest = models.CharField(max_length=255, help_text=_(
        "mill_legal_production_forest"), verbose_name=_("mill_legal_production_forest"), null=True)
    mill_legal_conservation_area = models.CharField(max_length=255, help_text=_(
        "mill_legal_conservation_area"), verbose_name=_("mill_legal_conservation_area"), null=True)
    mill_legal_landuse_risk = models.CharField(max_length=255, help_text=_(
        "mill_legal_landuse_risk"), verbose_name=_("mill_legal_landuse_risk"), null=True)
    mill_complex_supplybase_risk = models.CharField(max_length=255, help_text=_(
        "mill_complex_supplybase_risk"), verbose_name=_("mill_complex_supplybase_risk"), null=True)
    mill_date_update = models.CharField(max_length=255, help_text=_(
        "mill_date_update"), verbose_name=_("mill_date_update"), null=True)
    created_at = models.DateTimeField(default=timezone.now, help_text=_(
        "Creation date"), verbose_name=_("Created at"))
    geom = models.PointField(srid=4326, dim=2, null=True)
    is_display = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = GeoManager()

    class Meta:
        verbose_name = _("Mill")
        verbose_name_plural = _("Mills")

    def __str__(self):
        return str(self.mill_address)
