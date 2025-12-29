# Generated migration for renaming _ua fields to _uk

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_alter_lesson_content_html_and_more'),
    ]

    operations = [
        # Lesson model
        migrations.RenameField(
            model_name='lesson',
            old_name='title_ua',
            new_name='title_uk',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='content_html_ua',
            new_name='content_html_uk',
        ),
        # Question model
        migrations.RenameField(
            model_name='question',
            old_name='text_ua',
            new_name='text_uk',
        ),
        # Choice model
        migrations.RenameField(
            model_name='choice',
            old_name='text_ua',
            new_name='text_uk',
        ),
    ]
