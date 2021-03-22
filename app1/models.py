# from django.db import models

# create your models here.
from django.db import models

# create your models here.
from django import forms

from django.utils import timezone

# from concurrency.fields import autoincversionfield


mymultichoices = (
    ('a', 'abc'),
    ('b', 'bcd'),
    ('c', 'cde'),
)

mymultichoices2 = (
    ('会社名1', '会社名1'),
    ('会社名2', '会社名2'),
    ('会社名3', '会社名3'),
)
# yourmultichoice2 = models.CharField(max_length=50,choices=mymultichoices2,blank=True,verbose_name="選択肢４")

class Person(models.Model):
    sw_name = models.CharField(max_length=130,verbose_name="ソフトウェア名称",blank=False, null=True)
    sw_lic_id = models.CharField(max_length=20,verbose_name="ソフトウェアライセンスｉｄ", blank=False, null=True)
    sw_mnt_id = models.CharField(max_length=20,verbose_name="ソフトウェア保守ｉｄ", blank=False, null=True)
    sw_not_use = models.BooleanField(verbose_name=('利用終了'), default=False)
    sw_version = models.CharField(max_length=20,verbose_name="ソフトウェアバージョン番号",blank=True, null=True)
    sw_quantity = models.IntegerField( verbose_name='数量', blank=True, null=True, default=0) 
                #, validators=[validators.minvaluevalidator(0), validators.maxvaluevalidator(100)]) 
                #    , [validators.minvaluevalidator(0.01), validators.maxvaluevalidator(100.00)])
    sw_dev_comp = models.CharField(max_length=50,verbose_name="開発元", blank=True)

    # sw_lic_price= models.decimalfield( verbose_name='購入金額', decimal_places=0, max_digits=1000000000, blank=True, null=True, default=0)
    # sw_mnt_price= models.decimalfield( verbose_name='保守金額', decimal_places=0, max_digits=1000000000, blank=True, null=True, default=0)
    sw_lic_price= models.IntegerField( verbose_name='購入金額', blank=True, null=True, default=0)
    sw_mnt_price= models.IntegerField( verbose_name='保守金額', blank=True, null=True, default=0)

    sw_lic_date = models.DateField(default=timezone.now,verbose_name="購入日付")
    sw_mnt_init_date = models.DateField(default=timezone.now,verbose_name="保守開始日付")
    sw_mnt_update_date = models.DateField(default=timezone.now,verbose_name="保守契約更新日付")
    # sw_sup_date = models.datefield(default=timezone.now,verbose_name="保守期限",blank=True)
    sw_sup_date = models.DateField(verbose_name="保守期限",blank=True, null=True)
    sw_banker = models.CharField(max_length=20,verbose_name="銀行担者当者名", blank=False, null=True)
    sw_vender_comp = models.CharField(max_length=20,verbose_name="ベンダー名",blank=False, null=True)
    sw_vender_rep = models.CharField(max_length=20,verbose_name="ベンダー担当者名",blank=False, null=True)
    sw_vender_mail = models.EmailField(blank=True,verbose_name="eメール")
    sw_vender_tel = models.CharField(max_length=20,verbose_name="電話番号",blank=False, null=True)
    sw_installed = models.CharField(max_length=100,verbose_name="導入pc", blank=True)
    sw_other = models.CharField(max_length=50,verbose_name="その他", blank=True)

    # version = integerversionfield( )
    # version = autoincversionfield( )

    def save(self, *args, **kwargs):
        # print("=== {} ======================".format(self.ifnochoice)  )
        # if not self.yourmultichoice2:
        #     self.yourmultichoice2 = self.ifnochoice
        super().save(*args, **kwargs)  # call the "real" save() method.
        # do_something_else()
    
