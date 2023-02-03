from django.db import models
class product(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=12,decimal_places=2)
    def _str_(self):
        return self.pname