from django.db import models
from django.db.models.fields import TextField, BooleanField, IntegerField, DateField


# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=20,blank=True,null=True)
    uid = models.TextField(max_length=35,blank=True,null=True)
    email = models.TextField(max_length=35,blank=True,null=True)

class Project(models.Model):
    name = models.TextField(max_length=20,blank=True,null=True)
    creation_date = models.DateField(null=True, blank=True)
    summary = models.TextField(max_length=250,blank=True,null=True)
    include_char_sheet = models.BooleanField(default=False)
    include_text_doc = models.BooleanField(default=False)
    include_static_assets = models.BooleanField(default=False)
    include_video = models.BooleanField(default=False)
    include_audio = models.BooleanField(default=False)
    include_location = models.BooleanField(default=False)

class Book(models.Model):
    title = models.TextField(max_length=35,blank=True,null=True)
    summary = models.TextField(max_length=250,blank=True,null=True)
    category = models.TextField(max_length=35,blank=True,null=True)

class Chapter(models.Model):
    chapter_number = models.IntegerField(default=0)
    title = models.TextField(max_length=35,blank=True,null=True)
    summary = models.TextField(max_length=250,blank=True,null=True)
    body = models.TextField(blank=True,null=True)

class StaticAsset(models.Model):
    title = models.TextField(max_length=35,blank=True,null=True)
    media_type = models.TextField(max_length=35,blank=True,null=True)

class Video(models.Model):
    title = models.TextField(max_length=35,blank=True,null=True)
    summary = models.TextField(max_length=250,blank=True,null=True)
    duration = models.IntegerField(default=0)

class Audio(models.Model):
    title = models.TextField(max_length=35,blank=True,null=True)
    summary = models.TextField(max_length=250,blank=True,null=True)
    duration = models.IntegerField(default=0)

class Location(models.Model):
    name = models.TextField(max_length=35,blank=True,null=True)
    location_description = models.TextField(max_length=250,blank=True,null=True)
    description = models.TextField(max_length=250,blank=True,null=True)

class MinorLocation(models.Model):
    name = models.TextField(max_length=35,blank=True,null=True)
    location_description = models.TextField(max_length=250,blank=True,null=True)
    description = models.TextField(max_length=250,blank=True,null=True)

class Character(models.Model):
    # Main Info
    is_player_character = models.BooleanField(default=False)
    player_name = models.TextField(max_length=35,blank=True,null=True)
    name = models.TextField(max_length=35,blank=True,null=True)
    character_class = models.TextField(max_length=35,blank=True,null=True)
    level = models.IntegerField(default=0)
    race = models.TextField(max_length=35,blank=True,null=True)
    background = models.TextField(max_length=35,blank=True,null=True)
    alignment = models.TextField(max_length=35,blank=True,null=True)

    # Attributes
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)

    # General Values
    health = models.IntegerField(default=0)
    temp_hp = models.IntegerField(default=0)
    armor_class = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    proficiency_bonus = models.IntegerField(default=0)
    passive_perception = models.IntegerField(default=0)
    passive_investigation = models.IntegerField(default=0)
    death_success = models.IntegerField(default=0)
    death_fail = models.IntegerField(default=0)

    #Proficiencies
    acrobatics = models.BooleanField(default=False)
    animal_handling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleight_of_hand = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)

    # Personality Traits
    traits = models.TextField(max_length=250,blank=True,null=True)
    ideals = models.TextField(max_length=250,blank=True,null=True)
    bonds = models.TextField(max_length=250,blank=True,null=True)
    flaws = models.TextField(max_length=250,blank=True,null=True)

    # features??