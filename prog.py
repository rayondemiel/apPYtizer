import re

#selectionner que le texte de notre TEI
#tuto avant il faut nettoyer le fichier en remplacant par \n \t et la regex: ^ {1,}
#mettre un saut de ligne via 
#chercher </app> et remplacer par </app>\n, on peut supprimer les sauts de lignes inutiles ensuite

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
