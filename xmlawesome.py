import dicttoxml
from xml.dom.minidom import parseString

class xmlawesome:
	def listtoxml(items, root, pretty=False):
		item_name = type(items[0]).__name__
		dicts = []
		for item in items:
			dicts.append(item.__dict__)
		
		get_item_name = lambda x: item_name
		xml = dicttoxml.dicttoxml(dicts, attr_type=False, custom_root=, item_func=get_item_name)
		if pretty:
			return parseString(xml).toprettyxml()
			
		return xml
