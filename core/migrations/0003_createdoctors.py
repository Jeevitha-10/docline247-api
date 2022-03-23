from django.db import migrations


def create_doctors(apps, schema_editor):
    Doctor = apps.get_model('core', 'Doctor')
    Category = apps.get_model('core', 'Category')
    Doctor.objects.bulk_create([
        Doctor(
            name='Herbert',
            gender='M',
            category=Category.objects.get(name='Cardiology'),
            age=45,
            year_of_employment=2010,
            profile_pic='doctors/image_59.png'
        ),
        Doctor(
            name='Alena',
            gender='F',
            category=Category.objects.get(name='Cardiology'),
            age=35,
            year_of_employment=2017,
            profile_pic='doctors/image_60.png'
        ),
        Doctor(
            name='William',
            gender='M',
            category=Category.objects.get(name='Neurology'),
            age=43,
            year_of_employment=2014,
            profile_pic='doctors/image_59.png'
        ),
        Doctor(
            name='John',
            gender='M',
            category=Category.objects.get(name='Neurology'),
            age=39,
            year_of_employment=2017,
            profile_pic='doctors/image_59.png'
        ),
        Doctor(
            name='Abraham',
            gender='M',
            category=Category.objects.get(name='Cardiology'),
            age=46,
            year_of_employment=2009,
            profile_pic='doctors/image_59.png'
        ),
    ])


def delete_doctors(apps, schema_editor):
    Doctor = apps.get_model('core', 'Doctor')
    Doctor.objects.get(name='Herbert').delete()
    Doctor.objects.get(name='Alena').delete()
    Doctor.objects.get(name='William').delete()
    Doctor.objects.get(name='John').delete()
    Doctor.objects.get(name='Abraham').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_createcategories'),
    ]

    operations = [
        migrations.RunPython(create_doctors, reverse_code=delete_doctors)
    ]
