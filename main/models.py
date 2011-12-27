from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from utils.pyqrnative.PyQRNative import QRCode,QRErrorCorrectLevel
from urllib import urlencode
from urllib2 import urlopen
from cStringIO import StringIO

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    path = models.FileField(upload_to='%s/attachments' % settings.MEDIA_ROOT)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Name', max_length=250)
    icon = models.ImageField(upload_to='%s/icons' % settings.MEDIA_ROOT,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __unicode__(self):
        return self.name

class Thing(models.Model):
    name = models.CharField('Name', max_length=250)
    slug = models.SlugField()
    short_url = models.URLField()
    domain = models.ForeignKey(Domain, related_name="things", blank=False, null=True)
    description = models.CharField('Short Description',max_length=250,blank=True,null=True)
    notes = models.TextField('Notes',blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag,related_name="tags",null=True,blank=True)
    attachments = models.ManyToManyField(Attachment,related_name="attachments",null=True,blank=True)
    barcode = models.ImageField(upload_to='%s/barcodes' % settings.MEDIA_ROOT)
    class Meta:
        ordering = ['date_modified', 'name']
    def __unicode__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            long_url = str("http://%s/thing/%s" % (self.domain.name,self.slug))
            buser = settings.BITLY_USERNAME
            bpass = settings.BITLY_PASSWORD
            bitly_url = "http://api.bit.ly/v3/shorten?"
            bitly_vals = {
                'login' : buser,
                'apiKey' : bpass,
                'longUrl' : long_url,
                'format' : 'txt'
            }
            req_url = '%s%s' % (bitly_url,urlencode(bitly_vals))
            short_url = urlopen(req_url).read()

            qr = QRCode(8, QRErrorCorrectLevel.Q)
            qr.addData(short_url)
            qr.make()
            im = qr.makeImage()
            temp_file = StringIO()
            im.save(temp_file, format='png')
            contents = ContentFile(temp_file.getvalue())
            ##self.barcode.save('%s_%s.png' % (self.domain,self.slug), contents)

        super(Thing,self).save(*args,**kwargs)
