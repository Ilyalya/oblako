from django.db import models
import qrcode

filename = "site.png"


class Qrcodes(models.Model):
    qr_name = models.TextField("Название")
    qr_link = models.TextField("Ссылка")
    qr_img = models.TextField("Изображение")

    def __str__(self):
        return self.qr_name


# пример данных
name = Qrcodes.qr_name
data = Qrcodes.qr_link
# имя конечного файла
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)