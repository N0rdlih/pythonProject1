from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


def validate_even(val):
    if val <300:
        raise ValidationError('Число %(value) s so small', code='odd', params={'value': val})




class Bb(models.Model):
    title=models.CharField(max_length=50, verbose_name='Товар', validators=[validators.MinLengthValidator(3)])
    content=models.TextField(null=True, blank=True, verbose_name='Опис', validators=[validators.MinLengthValidator(3)])
    price= models.FloatField(null=True, blank=True, verbose_name='Ціна',validators=[validate_even] )
    published=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Публікація', )
    rubric=models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрики',)
    class Meta:
        verbose_name_plural = 'Обяви'
        verbose_name = 'Обява'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Names')
    def __str__ (self) :
        return self.name
    class Meta:
        verbose_name_plural='rubrics'
        verbose_name='rubric'
        ordering =['name']




