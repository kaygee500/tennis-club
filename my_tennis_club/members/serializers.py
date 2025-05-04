from rest_framework import serializers
from .models import Member

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','firstname', 'lastname', 'phone', 'joined_date']
