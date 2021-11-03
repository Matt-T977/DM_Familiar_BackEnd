from rest_framework import serializers
from .models import Audio, Book, Chapter, Character, Location, MinorLocation, StaticAsset, User, Project, Template, Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'creator_type',
            'project',
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'creation_date',
            'summary',
            'template',
        ]

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = [
            'template_type',
            'include_char_sheet',
            'character_sheets',
            'include_text_doc',
            'text_documents',
            'include_static_assets',
            'static_assets',
            'include_video',
            'videos',
            'include_audio',
            'audio'
            'include_location',
            'locations',
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'summary',
            'category',
            'chapters',
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
            'related_static_assets',
            'related_text_docs',
            'related_videos',
            'related_audio',
            'location_characters',
            'minor_locations',
        ]

class MinorLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinorLocation
        fields = [
            'name',
            'location_description',
            'description',
            'related_static_assets',
            'related_text_docs',
            'related_videos',
            'related_audio',
            'location_characters',
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
