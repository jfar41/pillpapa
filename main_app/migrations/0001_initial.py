import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

  initial = True

  dependencies = [
    ('auth', '0012_alter_user_first_name_max_length'),
  ]

  operations = [
    migrations.CreateModel(
      name='User',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('password', models.CharField(max_length=128, verbose_name='password')),
        ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
        ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
        ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
        ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
        ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
        ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
        ('first_name', models.CharField(max_length=25, verbose_name='First Name')),
        ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
        ('email', models.CharField(max_length=75, verbose_name='Email Address')),
        ('phone', models.CharField(max_length=25, verbose_name='Phone Number')),
        ('is_patient', models.BooleanField(default=False)),
        ('is_admin', models.BooleanField(default=False)),
        ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
        ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
      ],
      options={
        'verbose_name': 'user',
        'verbose_name_plural': 'users',
        'abstract': False,
      },
      managers=[
        ('objects', django.contrib.auth.models.UserManager()),
      ],
    ),
    migrations.CreateModel(
      name='PatientProfile',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('room_number', models.CharField(blank=True, max_length=5, verbose_name='Room Number')),
        ('dob', models.DateField(null=True, verbose_name='Date of Birth')),
        ('points', models.IntegerField(default=0)),
        ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
      ],
    ),
    migrations.CreateModel(
      name='Pill',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=75, verbose_name='Name of Medication')),
        ('dosage', models.CharField(max_length=50, verbose_name='Medication Dosage')),
        ('directions', models.TextField(max_length=250, verbose_name='Medication Directions')),
        ('prescribing_doctor', models.CharField(max_length=50, verbose_name='Prescribing Doctor')),
        ('qty', models.IntegerField(verbose_name='Initial Quantity')),
        ('refills', models.IntegerField(verbose_name='Amount of Refills')),
        ('date_prescribed', models.DateField(verbose_name='Initial Prescription Date')),
        ('dosing_total', models.IntegerField(default=0)),
        ('doses_taken', models.IntegerField(default=1)),
        ('dose_date', models.DateField(default=datetime.datetime.now)),
        ('dose_date_switch', models.IntegerField(default=0)),
        ('qty_remaining', models.IntegerField(default=273)),
        ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patientprofile')),
        ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
      ],
    ),
    migrations.CreateModel(
      name='PatientPhoto',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('url', models.CharField(max_length=200)),
        ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patientprofile')),
      ],
    ),
    migrations.CreateModel(
      name='EmergencyContact',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
        ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
        ('phone', models.CharField(max_length=25, verbose_name='Phone Number')),
        ('email', models.CharField(max_length=75, verbose_name='Email Address')),
        ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.patientprofile')),
      ],
    ),
    migrations.CreateModel(
      name='Dosing',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('time', models.TimeField()),
        ('dose', models.IntegerField()),
        ('pill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pill')),
      ],
      options={
        'ordering': ['time'],
      },
    ),
    migrations.CreateModel(
      name='AdminProfile',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('job_title', models.CharField(max_length=50, verbose_name='Job Title')),
        ('patients_list', models.ManyToManyField(blank=True, to='main_app.PatientProfile')),
        ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
      ],
    ),
    migrations.CreateModel(
      name='AdminPhoto',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('url', models.CharField(max_length=200)),
        ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.adminprofile')),
      ],
    ),
  ]