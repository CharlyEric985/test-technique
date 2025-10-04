from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # Tous les champs du modèle seront exposés
        fields = "__all__"
