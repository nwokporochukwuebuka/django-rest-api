from rest_framework import serializers

#from test_app.models import TestModel

#class SimpleObject():
#    def __init__(self, name):
#        self.name = name

'''class SimpleSerializer(serializers.Serializer):
    Make sure it tallies with what is in the models.py file
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.IntegerField()
    is_alive = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)

    # To specify that we don't really need this when validating our data
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)'''

    #def create(self, validated_data):
        #Because of this we don't need the create method in the views.py file
        #hence we overide the create method in the serializers class. 
        
        #In doing this we have created a model with another validated data.
        #return TestModel.objects.create(**validated_data)
    
    #def update(self, instance, validated_data):
        #TestModel.objects.filter(id=instance.id).update(**validated_data)
        #return TestModel.objects.get(id=instance.id)


'''def run_data():
    simple_var = SimpleObject('Henry')
    simple_var_serializer = SimpleObjectSerializer(simple_var)
    print(simple_var_serializer.data)'''

'''class SimpleSerializer(serializers.ModelSerializer):
    This will help us to inherit from the model and will not 
    require us not to inherit from the models.py file
    
    Wow! This is so amazing, there is no need to create the create method and 
    even the update method.

    class Meta:
        model = TestModel
        fields = "__all__"
        '''