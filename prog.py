import re
from lxml import etree

#selectionner que le texte de notre TEI
#tuto avant il faut nettoyer le fichier en remplacant par \n \t et la regex: ^ {1,}
#mettre un saut de ligne via 
#chercher </app> et remplacer par </app>\n, on peut supprimer les sauts de lignes inutiles ensuite

def ajoutLem(inFile, outFile, lem):

	parser = etree.XMLParser()
	tree = etree.parse(inFile, parser)

	path = tree.xpath('//rdg[contains(@wit, {})'.format(lem))

	for element in path:
		old_element = element.find('rdg')
		old_element.tag = "lem"
		return elem.write(outFile, encoding='utf-8')
	


ajoutLem("test.xml", "testresult", "NY")
print(tree)


"""


let $rdg := $doc//rdg
let $brl := $rdg[contains(@wit, "#brl")]
let $lem := $doc//lem

(: renommer le rdg en lem :)
for $el in $brl
return rename node $el as "lem"
"""







"""
rdg_pattern = re.compile(r'<rdg wit="([A-Z]|[a-z]|[éàèçôêâïÿ]|[,’!?./><" ]){1,}(</rdg>|/>)')
lem_pattern = re.compile(r'<lem wit="([A-Z]|[a-z]|[éàèçôêâïÿ]|[,’!?./><" ]){1,}(</lem>|/>)')




with open('text3.xml') as f:
	inFile = f.read()
	outFile = open('resultat.xml', 'w') # ouverture en écriture du fichier de sortie


	for line in inFile.split('\n'):
		if '<app>' in line:
			lem = re.search(lem_pattern, line)
			
			variants = ""
			for variant in re.finditer(rdg_pattern, line):
			    variants += f"\n\t{variant.group()}"
			outFile.write(f"<app>\n\t{lem.group()}{variants}\n</app>\n")

		else:
			outFile.write(f"{line}\n")

outFile.close()
"""