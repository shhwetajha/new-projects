from django.db import models

# Create your models here.

tds_section_choice=(
   ( '120a','120a'),
   ('120b','120b'),
   ('120c','120c'),
)

class party(models.Model):
    party_name=models.CharField(max_length=100,null=True,blank=True)
    party_address=models.CharField(max_length=100,null=True,blank=True)
    tds_section=models.CharField(max_length=100,choices=tds_section_choice, null=True,blank=True)
    tds_pct=models.FloatField(default=0)
    pan_no=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.party_name




