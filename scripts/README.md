# par-22-23-detection-raquette

Les algorithmes utilisés dans notre projet sont :

Algorithme Split: diviser une video en plusieurs frames

Algorithme Délimitation de la zone de la raquette : délimiter une zone oû la raquette doit exister avec une probabilité élevée.

Algorithme test_method: découper une image en plusieurs sous-matrices, chacune de la taille d'un bounding box ( matrice de taille 31x31)
et pour chaque bounding box essayer de voir si le critère de couleur défini est respecté. Si c'est le cas, on a de fortes chances que le bounding-box en question correspond à la raquette. Les hypothèses de l'algorithme sont : raquette noire, caméra fixe.



Algorithme convert_xml_to_csv: convertir les fichiers xml en un tableau csv avec pour chaque position de la raquette, le bounding box associé ( xmin, ymin, xmax, ymax)