# INPUT:
# 1-qator: default settings (theme lang debug) -> masalan: dark uz 1
# 2-qator: override settings (theme lang debug) -> '-' bo‘lsa o‘zgarmaydi
# debug: 1 yoki 0
# Vazifa: final settings ni 1 qatorda chiqaring: theme lang debug

# default
th1, lang1, dbg1 = input().split()
# override
th2, lang2, dbg2 = input().split()

settings = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}

# TODO
final_theme = settings['override']['theme'] if settings['override']['theme'] != '-' else settings['theme']
final_lang = settings['override']['lang'] if settings['override']['lang'] != '-' else settings['lang']
final_debug = settings['override']['debug'] if settings['override']['debug'] is not None else settings['debug']
dbg_out = '1' if final_debug else '0'
print(final_theme, final_lang, dbg_out)