# Generated by Django 3.2.6 on 2022-06-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0008_rename_post_content_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomments',
            old_name='author',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='postcomments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_app.post'),
        ),
    ]
