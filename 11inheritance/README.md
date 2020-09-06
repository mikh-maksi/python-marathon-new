class DataField:  
&nbsp;&nbsp;&nbsp;&nbsp;field_description = "General"  

&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, value):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.value = None  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.validate(value)  

&nbsp;&nbsp;&nbsp;&nbsp;def validate(self, value):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.value = value  

&nbsp;&nbsp;&nbsp;&nbsp;def __contains__(self, item):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return item in self.value  


class FirstNameField(DataField):  
&nbsp;&nbsp;&nbsp;&nbsp;field_description = "**Name**"  


class CityField(DataField):  
&nbsp;&nbsp;&nbsp;&nbsp;field_description = "City"  