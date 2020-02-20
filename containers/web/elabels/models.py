from django.db import models


class AuditModel(models.Model):
    '''Abstract model meant to be inherited by objects whose creation and modification needs to be logged'''
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Label(AuditModel):
    product_name = models.CharField(max_length=30, null=True, blank=True)
    company = models.ForeignKey(
        "Company",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='label'
    )

    def __str__(self):
        return (str(self.company.name) + " - " + str(self.product_name))


class IngredientAmount(AuditModel):
    ingredient = models.ForeignKey(
        "Ingredient",
        null =False,
        blank = False,
        on_delete = models.CASCADE,
        related_name = 'ingredient_amount'
    )
    label = models.ForeignKey(
        "Label",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='ingredient_amount'
    )
    percent_of_total = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        null=False,
        blank=False,
        help_text="The percentage of ingredient included in the product. (e.g. 0.12)",
        verbose_name="percent of total"

    )
    active = models.BooleanField(
        default=True,
        help_text="Is this and active ingredient?",
        verbose_name="Active ingredient?",
        choices=((True, 'Yes'), (False, 'No'))
    )

    def __str__(self):
        return (str(self.label.product_name) + " - " + str(self.ingredient))


class Ingredient(AuditModel):
    name = models.CharField(
        max_length = 50,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name


class Company(AuditModel):
    name = models.CharField(
        max_length = 50,
        null=False,
        blank=False,
        unique = True
    )
    line_1 = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    line_2 = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    state = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
    zip_code = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Crop(AuditModel):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name


class ApplicationMethod(AuditModel):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name


class ApplicationRate(AuditModel):
    label = models.ForeignKey(
        "Label",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='application_rate'
    )
    crop = models.ForeignKey(
        "Crop",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='application_rate'
    )
    min_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name='Minumum Rate'
    )
    max_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name='Maximum Rate'
    )
    rate_units = models.ForeignKey(
        "RateUnit",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='application_rate'
    )
    application_method =  models.ForeignKey(
        "ApplicationMethod",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='application_rate'
    )


class RateUnit(AuditModel):
    acronym = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.acronym

# reason/purpose for use (fertilizer, fungicide, etc)
# Crop
# Growth stage
# Application Interval
# Application rate
# Region
# Application method
    # foliar
    # seed treatment
#