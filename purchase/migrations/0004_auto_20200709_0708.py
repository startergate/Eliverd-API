# Generated by Django 3.0.7 on 2020-07-09 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200707_0913'),
        ('store', '0006_auto_20200618_0658'),
        ('purchase', '0003_auto_20200708_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='stocks',
        ),
        migrations.RemoveField(
            model_name='order',
            name='store',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User'),
        ),
        migrations.CreateModel(
            name='PartialOrder',
            fields=[
                ('poid', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ready', 'Ready'), ('delivering', 'Delivering'), ('delivered', 'Delivered')], default='pending', max_length=16)),
                ('stocks', models.ManyToManyField(to='purchase.OrderedStock')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='partials',
            field=models.ManyToManyField(to='purchase.PartialOrder'),
        ),
    ]
