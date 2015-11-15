
class AlaiLayoutBase(In.core.page.PageLayout):
	'''Alai layout'''
	


@IN.register('AlaiLayoutBase', type = 'Themer')
class AlaiLayoutBaseThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-4-6 i-margin-large-top')
		
		obj['sidebar1'].css.append('i-width-medium-1-6 i-margin-large-top')
		obj['sidebar2'].css.append('i-width-medium-1-6 i-margin-large-top')
		
		obj['sidebar1'].css.append('i-margin-large-top')
		obj['sidebar2'].css.append('i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		


class AlaiLayoutContentOnly(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutContentOnly', type = 'Themer')
class AlaiLayoutContentOnlyThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-1-1 i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		

class AlaiLayoutContentOnlyFluid(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutContentOnlyFluid', type = 'Themer')
class AlaiLayoutContentOnlyFluidThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-1-1 i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		

class AlaiLayoutSCCS(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutSCCS', type = 'Themer')
class AlaiLayoutSCCSThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-2-6 i-margin-large-top')
		obj['content2'].css.append('i-width-medium-2-6 i-margin-large-top')
		
		obj['sidebar1'].css.append('i-width-medium-1-6')
		obj['sidebar2'].css.append('i-width-medium-1-6')
		
		super().theme_items(obj, format, view_mode, args)
		
	def theme_process_variables(self, obj, format, view_mode, args):
		super().theme_process_variables(obj, format, view_mode, args)
		args['content2'] = args['children']['content2']['content']



class AlaiLayoutSCC(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutSCC', type = 'Themer')
class AlaiLayoutSCCThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-3-6 i-margin-large-top')
		obj['content2'].css.append('i-width-medium-2-6 i-margin-large-top')
		
		obj['sidebar1'].css.append('i-width-medium-1-6')
		
		obj['sidebar1'].css.append('i-margin-large-top')
		#obj['sidebar2'].css.append('i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		
	def theme_process_variables(self, obj, format, view_mode, args):
		super().theme_process_variables(obj, format, view_mode, args)
		args['content2'] = args['children']['content2']['content']


class AlaiLayoutCC(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutCC', type = 'Themer')
class AlaiLayoutCCThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-1-2 i-margin-large-top')
		obj['content2'].css.append('i-width-medium-1-2 i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		
	def theme_process_variables(self, obj, format, view_mode, args):
		super().theme_process_variables(obj, format, view_mode, args)
		args['content2'] = args['children']['content2']['content']


class AlaiLayoutCCFluid(AlaiLayoutCC):
	'''Alai layout'''
	
	

class AlaiLayoutCS(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutCS', type = 'Themer')
class AlaiLayoutCSThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-4-6 i-margin-large-top')
		obj['sidebar2'].css.append('i-width-medium-2-6')
		
		#obj['sidebar1'].css.append('i-margin-large-top')
		obj['sidebar2'].css.append('i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		
	def theme_process_variables(self, obj, format, view_mode, args):
		super().theme_process_variables(obj, format, view_mode, args)
		args['sidebar2'] = args['children']['sidebar2']['content']


class AlaiLayoutCSFluid(AlaiLayoutCS):
	'''Alai layout'''
	
	
	

class AlaiLayoutSC(AlaiLayoutBase):
	'''Alai layout'''
	
@IN.register('AlaiLayoutSC', type = 'Themer')
class AlaiLayoutSCThemer(In.themer.PageLayoutThemer):
	''''''
	
	def theme_items(self, obj, format, view_mode, args):
		
		obj['promotion'].css.append('i-width-1-1')
		
		obj['content'].css.append('i-width-medium-4-6 i-margin-large-top')
		obj['sidebar1'].css.append('i-width-medium-2-6')
		
		obj['sidebar1'].css.append('i-margin-large-top')
		#obj['sidebar2'].css.append('i-margin-large-top')
		
		super().theme_items(obj, format, view_mode, args)
		
	def theme_process_variables(self, obj, format, view_mode, args):
		super().theme_process_variables(obj, format, view_mode, args)
		args['sidebar1'] = args['children']['sidebar1']['content']


class AlaiLayoutSCFluid(AlaiLayoutSC):
	'''Alai layout'''
	