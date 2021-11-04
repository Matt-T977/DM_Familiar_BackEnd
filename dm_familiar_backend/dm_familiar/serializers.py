from rest_framework import serializers
from .models import Audio, Book, Chapter, Character, Location, MinorLocation, StaticAsset, User, Project, Template, Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'creator_type',
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'creation_date',
            'summary',
        ]

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = [
            'template_type',
            'include_char_sheet',
            'include_text_doc',
            'include_static_assets',
            'include_video',
            'include_audio',
            'include_location',
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'summary',
            'category',
        ]

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'chapter_number',
            'title',
            'summary',
            'category',
            'body',
        ]

class StaticAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticAsset
        fields = [
            'title',
            'media_type',
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'title',
            'summary',
            'duration',
        ]

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            'title',
            'summary',
            'duration',
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'name',
            'location_description',
            'description',
        ]

class MinorLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinorLocation
        fields = [
            'name',
            'location_description',
            'description',
        ]

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'is_player_character',
            'player_name',
            'name',
            'character_class',
            'level',
            'race',
            'background',
            'alignment',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
            'health',
            'temp_hp',
            'armor_class',
            'initiative',
            'speed',
            'proficiency_bonus',
            'passive_perception',
            'passive_investigation',
            'death_success',
            'death_fail',
            'acrobatics',
            'animal_handling',
            'arcana',
            'athletics',
            'deception',
            'history',
            'insight',
            'intimidation',
            'medicine',
            'nature',
            'perception',
            'performance',
            'persuasion',
            'religion',
            'sleight_of_hand',
            'stealth',
            'survival',
            'traits',
            'ideals',
            'bonds',
            'flaws',
        ]
