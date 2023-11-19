from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


# Create your models here.


class Facility(models.Model):

    id = models.AutoField(primary_key=True)
    facilities_eq_id = models.CharField(max_length=255, help_text=_(
        "facilities_eq_id"), verbose_name=_("facilities_eq_id"), null=True)
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
