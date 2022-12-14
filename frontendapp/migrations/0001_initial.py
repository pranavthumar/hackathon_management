# Generated by Django 3.2.9 on 2021-11-24 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLeave',
            fields=[
                ('leave_id', models.IntegerField(primary_key=True, serialize=False)),
                ('leave_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('leave_status', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'apply_leave',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BranchManager',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('branch_manager_id', models.IntegerField(blank=True, null=True)),
                ('email_id', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'branch_manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('salary_id', models.IntegerField(primary_key=True, serialize=False)),
                ('allowance', models.IntegerField(blank=True, null=True)),
                ('deduction', models.IntegerField(blank=True, null=True)),
                ('total_calculated_salary', models.IntegerField(blank=True, null=True)),
                ('working_hours', models.IntegerField(blank=True, null=True)),
                ('total_leaves', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calculation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('working_hours', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('job_type', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('total_leaves', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeLeaveManagement',
            fields=[
                ('leave_id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('leave_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('leave_status', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'employee_leave_management',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_service_id', models.IntegerField(blank=True, null=True)),
                ('expenses', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=500, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'general_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HeadManager',
            fields=[
                ('head_manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('head_branch_address', models.CharField(blank=True, max_length=500, null=True)),
                ('head_branch_id', models.IntegerField(blank=True, null=True)),
                ('email_id', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'head_manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BranchDetails',
            fields=[
                ('branch_address', models.CharField(blank=True, max_length=50, null=True)),
                ('total_payout', models.IntegerField(blank=True, null=True)),
                ('total_number_of_employee', models.IntegerField(blank=True, null=True)),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='frontendapp.branchmanager')),
                ('branch_name', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'branch_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resignation',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='frontendapp.employee')),
                ('resign_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('resign_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'resignation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PastUserRecords',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='frontendapp.resignation')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('working_hours', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('job_type', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('leaving_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('total_leaves', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'past_user_records',
                'managed': False,
            },
        ),
    ]
