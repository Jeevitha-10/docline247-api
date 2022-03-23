from django.db import migrations


def create_category(apps, schema_editor):
    Category = apps.get_model('core', 'Category')

    Category.objects.bulk_create([
        Category(
            name='Cardiology',
            icon='categories/image_53.png'
        ),
        Category(
            name='Neurology',
            icon='categories/image_54.png'
        ),
    ])


def delete_category(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    Category.objects.get(name='Cardiology').delete()
    Category.objects.get(name='Neurology').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_category, reverse_code=delete_category)
    ]