# Migratsiya fayli (0003_add_initial_data.py)
from django.db import migrations

def add_initial_data(apps, schema_editor):
    Crossword = apps.get_model('krossvord', 'Crossword')
    CrosswordClue = apps.get_model('krossvord', 'CrosswordClue')
    
    # Fizika fanidan krossvord yaratish
    crossword = Crossword.objects.create(
        title='Fizika fanidan krossvord o\'yin metodi',
        description='Mexanika bo\'limi bo\'yicha asosiy atamalar va tushunchalar.',
        difficulty='medium'
    )
    
    # Gorizontal chiziqlardagi savollar
    CrosswordClue.objects.create(
        crossword=crossword,
        number=1,
        clue='Jismning inertlik o\'lchovini xarakterlovchi fizik kattalik nima?',
        answer='MASSA',
        row=1,
        col=0,
        direction='across'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=2,
        clue='Zaryadlangan zarrachalarning tartibli yoki tartibsiz harakatiga elektr …i deb aytiladi. Nuqtalar o\'rnini to\'ldiring?',
        answer='TOK',
        row=3,
        col=0,
        direction='across'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=3,
        clue='Mashina Qarshidan Toshkentga qarab yo\'l oldi, ushbu holatda mashinani moddiy nuqta deb hisoblash mumkinmi?',
        answer='HA',
        row=5,
        col=0,
        direction='across'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=4,
        clue='Yo\'nalishi va son qiymati jihatdan xarakterlanuvchi fizik kattaliklar qanday nomlanadi?',
        answer='VEKTOR',
        row=7,
        col=0,
        direction='across'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=5,
        clue='O\'lchov birligi kilogram bo\'lgan fizik kattalik qanday nomlanadi?',
        answer='MASSA',
        row=9,
        col=0,
        direction='across'
    )
    
    # Vertikal chiziqlardagi savollar    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=1,
        clue='Mexanik energiyaning o\'lchov birligi qanday?',
        answer='JOUL',
        row=0,
        col=0,
        direction='down'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=2,
        clue='Yuza birligiga tik ravishda qo\'yilgan kuchga to\'g\'ri keladigan fizik kattalik?',
        answer='BOSIM',
        row=0,
        col=2,
        direction='down'
    )
    
    CrosswordClue.objects.create(
        crossword=crossword,
        number=3,
        clue='1 metr kub hajmli idishda 1000 kg suyuqlik joylashgan. Bu qaysi suyuqlik?',
        answer='SUV',
        row=0,
        col=4,
        direction='down'
    )

def reverse_func(apps, schema_editor):
    Crossword = apps.get_model('krossvord', 'Crossword')
    Crossword.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('krossvord', '0002_add_initial_data'), # Oldingi migratsiya nomi to'g'ri ko'rsatilishi kerak
    ]
    
    operations = [
        migrations.RunPython(add_initial_data, reverse_func),
    ]