# Generated by Django 2.2.6 on 2019-11-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfm_model', '0002_customerdata_customer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='rfmAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Champions', models.IntegerField(null=True)),
                ('Loyal_Customers', models.IntegerField(null=True)),
                ('Potential_Loyalist', models.IntegerField(null=True)),
                ('Recent_Customers', models.IntegerField(null=True)),
                ('Promising', models.IntegerField(null=True)),
                ('Customers_Needing_Attention', models.IntegerField(null=True)),
                ('About_to_Sleep', models.IntegerField(null=True)),
                ('At_Risk', models.IntegerField(null=True)),
                ('Cant_Lose_Them', models.IntegerField(null=True)),
                ('Hibernating', models.IntegerField(null=True)),
                ('Lost', models.IntegerField(null=True)),
            ],
        ),
    ]
