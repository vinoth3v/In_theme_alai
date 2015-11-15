
from alai.layout import *
from alai.page import *

## dont implement any general hooks in theme as they will be invoked on all loaded themes


# TODO:
config = {
    'doctype'  : '<!DOCTYPE html>',
    'page_lang': '',
    'page_dir' : 'ltr',
    'logo_path': 'images/logo.png',
    'default_page' : AlaiPageBase,
}


def decide_page_class(context):
	'''Return Pages dynamically based on path/user/role/...'''
	
	return AlaiPageCS