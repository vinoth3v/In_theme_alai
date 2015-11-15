

class AlaiPageBase(In.core.page.Page):
	'''Base Page class for Alai theme.'''
	
	__page_layout_type__ = 'AlaiLayoutBase'
	def_content_panel = 'content'

	def __init__(self, data = None, items = None, **args):

		super().__init__(data, items, **args)
		
		header = self['header']

		header.css.append('i-width-1-1 i-grid i-grid-small i-container i-container-center i-padding-remove')
		header.css.remove('site-header')
		
		header.item_wrapper = Object.build_object('TextDiv', {
			'id' : 'header-wrapper',
			'css' : ['site-header i-width-1-1']
		})
		
		#self['sidebar1'].css.append('i-padding-remove')

		self['sidebar3'].css.append('i-offcanvas-bar i-offcanvas-bar-over i-contrast')
		
		self['sidebar4'].css.append('i-offcanvas-bar i-offcanvas-bar-flip i-offcanvas-bar-over i-contrast')
		
		self['footer'].css.append('i-grid i-container-center')


@IN.register('AlaiPageBase', type = 'Themer')
class AlaiPageBaseThemer(In.themer.PageThemer):

	def theme_process_variables(self, obj, format, view_mode, args = None):
		super().theme_process_variables(obj, format, view_mode, args)

		for k, c in args['children'].items():
			args[k] = c['content']


class AlaiPageContentOnly(AlaiPageBase):

	__page_layout_type__ = 'AlaiLayoutContentOnly'

class AlaiPageContentOnlyFluid(AlaiPageBase):

	__page_layout_type__ = 'AlaiLayoutContentOnlyFluid'

class AlaiPageSCCS(AlaiPageBase):

	__page_layout_type__ = 'AlaiLayoutSCCS'

	def __init__(self, data = None, items = None, **args):
		
		super().__init__(data, items, **args)

		self['content2'] = Object.build_object('Section', {
			'id' : 'content2',
			'css' : ['content-2'],
			'weight' : 0,
		})

@IN.register('AlaiPageSCCS', type = 'Themer')
class AlaiPageSCCSThemer(In.themer.PageThemer):

	def ajax_replaceable_elements(self):
		return ['promotion', 'content', 'content2', 'sidebar1', 'sidebar2']
		

class AlaiPageSCC(AlaiPageSCCS):

	__page_layout_type__ = 'AlaiLayoutSCC'

@IN.register('AlaiPageSCC', type = 'Themer')
class AlaiPageSCCThemer(In.themer.PageThemer):

	def ajax_replaceable_elements(self):
		return ['promotion', 'content', 'content2', 'sidebar1']
		

class AlaiPageCC(AlaiPageSCCS):

	__page_layout_type__ = 'AlaiLayoutCC'

@IN.register('AlaiPageCC', type = 'Themer')
class AlaiPageCCThemer(In.themer.PageThemer):

	def ajax_replaceable_elements(self):
		return ['promotion', 'content', 'content2']
		
class AlaiPageCCFluid(AlaiPageCC):

	__page_layout_type__ = 'AlaiLayoutCCFluid'



class AlaiPageCS(AlaiPageSCCS):

	__page_layout_type__ = 'AlaiLayoutCS'

@IN.register('AlaiPageCS', type = 'Themer')
class AlaiPageCSThemer(In.themer.PageThemer):

	def ajax_replaceable_elements(self):
		return ['promotion', 'content', 'sidebar2']
		
class AlaiPageCSFluid(AlaiPageCS):

	__page_layout_type__ = 'AlaiLayoutCSFluid'


class AlaiPageSC(AlaiPageSCCS):

	__page_layout_type__ = 'AlaiLayoutSC'

@IN.register('AlaiPageSC', type = 'Themer')
class AlaiPageSCThemer(In.themer.PageThemer):

	def ajax_replaceable_elements(self):
		return ['promotion', 'content', 'sidebar1']
		
class AlaiPageSCFluid(AlaiPageSC):

	__page_layout_type__ = 'AlaiLayoutSCFluid'
