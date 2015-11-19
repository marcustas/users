import datetime
from django import template

register = template.Library()

@register.simple_tag
def allow(birth):
	today = datetime.date.today()
	a = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
	if a > 13:
		return 'Allowed'
	else:
		return 'Blocked'

@register.simple_tag
def bizzfuzz(random):
	a = ''
	if random % 3 == 0:
		a += 'Bizz'
	if random % 5 == 0:
		a += 'Fuzz'
	if a:
		return a
	else:
		return random
