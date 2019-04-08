from NewsLitter.forms import NewsletterForm,NewsCreationForm

def render_for_forms(request):
	form1 = NewsletterForm()
	form2 = NewsCreationForm()
	context = {
		'newscreateform':form2,
		'newslatterform':form1,
	}
	return context