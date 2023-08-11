

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card_info",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="CODE", max_length=10, unique=True
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, db_column="COURSE_NAME", max_length=100, null=True
                    ),
                ),
                ("cu", models.IntegerField(blank=True, db_column="CU", null=True)),
                ("lh", models.IntegerField(blank=True, db_column="LH", null=True)),
                ("ph", models.IntegerField(blank=True, db_column="PH", null=True)),
                ("th", models.IntegerField(blank=True, db_column="TH", null=True)),
                ("ch", models.IntegerField(blank=True, db_column="CH", null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True, db_column="Type", max_length=20, null=True
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, db_column="Remark", max_length=50, null=True
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, db_column="Origin", max_length=50, null=True
                    ),
                ),
                (
                    "program",
                    models.CharField(
                        blank=True, db_column="Program", max_length=50, null=True
                    ),
                ),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "course_info",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CourseInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="CODE", max_length=10, null=True
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, db_column="COURSE_NAME", max_length=100, null=True
                    ),
                ),
                ("cu", models.IntegerField(blank=True, db_column="CU", null=True)),
                ("lh", models.IntegerField(blank=True, db_column="LH", null=True)),
                ("ph", models.IntegerField(blank=True, db_column="PH", null=True)),
                ("th", models.IntegerField(blank=True, db_column="TH", null=True)),
                ("ch", models.IntegerField(blank=True, db_column="CH", null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True, db_column="Type", max_length=20, null=True
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, db_column="Remark", max_length=50, null=True
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, db_column="Origin", max_length=50, null=True
                    ),
                ),
                (
                    "program",
                    models.CharField(
                        blank=True, db_column="Program", max_length=50, null=True
                    ),
                ),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "course_info",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="YearOfStudy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="CODE", max_length=10, null=True
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, db_column="COURSE_NAME", max_length=100, null=True
                    ),
                ),
                ("cu", models.IntegerField(blank=True, db_column="CU", null=True)),
                ("lh", models.IntegerField(blank=True, db_column="LH", null=True)),
                ("ph", models.IntegerField(blank=True, db_column="PH", null=True)),
                ("th", models.IntegerField(blank=True, db_column="TH", null=True)),
                ("ch", models.IntegerField(blank=True, db_column="CH", null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True, db_column="Type", max_length=20, null=True
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, db_column="Remark", max_length=50, null=True
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, db_column="Origin", max_length=50, null=True
                    ),
                ),
                (
                    "program",
                    models.CharField(
                        blank=True, db_column="Program", max_length=50, null=True
                    ),
                ),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "course_info",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="CODE", max_length=10, null=True
                    ),
                ),
                (
                    "course_name",
                    models.CharField(
                        blank=True, db_column="COURSE_NAME", max_length=100, null=True
                    ),
                ),
                ("cu", models.IntegerField(blank=True, db_column="CU", null=True)),
                ("lh", models.IntegerField(blank=True, db_column="LH", null=True)),
                ("ph", models.IntegerField(blank=True, db_column="PH", null=True)),
                ("th", models.IntegerField(blank=True, db_column="TH", null=True)),
                ("ch", models.IntegerField(blank=True, db_column="CH", null=True)),
                (
                    "type",
                    models.CharField(
                        blank=True, db_column="Type", max_length=20, null=True
                    ),
                ),
                (
                    "remark",
                    models.CharField(
                        blank=True, db_column="Remark", max_length=50, null=True
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        blank=True, db_column="Origin", max_length=50, null=True
                    ),
                ),
                (
                    "program",
                    models.CharField(
                        blank=True, db_column="Program", max_length=50, null=True
                    ),
                ),
                ("year_of_study", models.IntegerField(blank=True, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "db_table": "course_info",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lecturer_preparedness", models.CharField(max_length=100)),
                ("lecturer_interest", models.CharField(max_length=100)),
                ("feedback_useful", models.CharField(max_length=100)),
                ("lecturers_complement", models.CharField(max_length=100)),
                ("instructional_materials", models.CharField(max_length=100)),
                ("course_organization", models.CharField(max_length=100)),
                ("confidence_in_advanced_work", models.CharField(max_length=100)),
                ("exam_measurement", models.CharField(max_length=100)),
                ("concept_understanding", models.CharField(max_length=100)),
                ("concept_understanding_feedback", models.CharField(max_length=2000)),
                ("applicability", models.CharField(max_length=100)),
                ("applicability_reasoning", models.CharField(max_length=100)),
                ("recommend_course", models.CharField(max_length=100)),
                (
                    "card_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feedback.card_info",
                        to_field="code",
                    ),
                ),
            ],
            options={
                "db_table": "student_answers",
            },
        ),
    ]
