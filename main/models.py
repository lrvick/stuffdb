from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from utils.pyqrnative.PyQRNative import QRCode,QRErrorCorrectLevel
from urllib import urlencode
from urllib2 import urlopen

class Tag:
    name = models.CharField('Name', max_length=250)
    icon = models.ImageField(upload_to='%s/icons' % settings.MEDIA_ROOT)
    def __unicode__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag,related_name="tags",null=True,blank=True)
    def __unicode__(self):
        return self.name

class Thing(models.Model):
    name = models.CharField('Name', max_length=250)
    slug = models.SlugField(unique=True)
    short_url = models.URLField()
    domain = models.ForeignKey(Domain, related_name="things", blank=False, default=0)
    description = models.TextField('Description',blank=True,null=True)
    notes = models.TextField('Notes',blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag,related_name="tags",null=True,blank=True)
    barcode = models.ImageField(upload_to='%s/barcodes' % settings.MEDIA_ROOT)
    class Meta:
        ordering = ['date_modified', 'name']
        unique_together = ('domain', 'name')
    def __unicode__(self):
        return self.name
    def save(self):
        if not self.pk:
            self.slug = slugify(self.title)

            long_url = "%s.%s/thing/%s" % (self.domain,settings.SITE_URL,self.slug)
            buser = settings['BITLY_USERNAME']
            bpass = settings['BITLY_PASSWORD']
            bitly_url = "http://api.bit.ly/v3/shorten?login={0}&apiKey={1}&longUrl={2}&format=txt"
            req_url = urlencode(bitly_url.format(buser, bpass, long_url))
            short_url = urlopen(req_url).read()

            qr = QRCode(8, QRErrorCorrectLevel.Q)
            qr.addData(short_url)
            qr.make()
            im = qr.makeImage()
            temp_file = NamedTemporaryFile(delete=True)
            im.save(temp_file, format='png')
            self.barcode = ('%s_%s.png' % (self.domain,self.slug), File(temp_file))

        super(Thing,self).save()

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    path = models.FileField(upload_to='%s/attachments' % settings.MEDIA_ROOT)
    thing = models.ForeignKey(Thing)
    def __unicode__(self):
        return self.name
