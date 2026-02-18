# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryDinosaur(models.Model):
    pk = models.CompositePrimaryKey('id_dinosaur', 'id_category')
    id_dinosaur = models.ForeignKey('Dinosaur', models.DO_NOTHING, db_column='id_dinosaur')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = False
        db_table = 'category_dinosaur'


class Dinosaur(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    length = models.CharField(max_length=100, blank=True, null=True)
    diet = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    existed = models.CharField(max_length=255)
    region = models.CharField(max_length=200)
    type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=800)
    ispopular = models.IntegerField(db_column='isPopular')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dinosaur'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ranking(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')

    class Meta:
        managed = False
        db_table = 'ranking'


class RankingDinosaur(models.Model):
    id_dinosaur = models.ForeignKey(Dinosaur, models.DO_NOTHING, db_column='id_dinosaur')
    id_ranking = models.ForeignKey(Ranking, models.DO_NOTHING, db_column='id_ranking')
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ranking_dinosaur'


class Review(models.Model):
    id_dinosaur = models.ForeignKey(Dinosaur, models.DO_NOTHING, db_column='id_dinosaur')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    comment = models.TextField()
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    rol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
