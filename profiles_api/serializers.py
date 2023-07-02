from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
    #breakpoint()
    mobileno = serializers.IntegerField()
    REQUIRED_FIELDS = ["name", "mobileno"]
    
    
    def validate_mobileno(self, value):
        """
        """
        if value == 890:
            return value
        raise serializers.ValidationError("Blog post is not about Django")
    

    def validate(self, data):
        """
        """
        for key, value in data.items():
            if key not in self.REQUIRED_FIELDS:
                raise serializers.ValidationError("Invalid argument {}".format(key))
        
        return data
    
