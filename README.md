# par-22-23-detection-raquette
Description des codes utilisés : 
Train.py ( disponible via ce lien : https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/models/YOLOv5_trained/train.py) : ce code est la base de l’entraînement. Il est constitué d’une fonction “ train” qui permet d’initialiser le réseau de neurones, les poids, le learning rate pour le gradient Descent et d’affecter les données d’entrée ( nos datas) au réseau de neurones.
!python train.py --batch 32 --epochs 150 --data 'data/raquette_data.yaml' --weights 'yolov5s6.pt' --project 'runs_raquette' --name 'feature_extraction' --cache --freeze 12
 
On appelle cette fonction via la ligne ( ci dessus) en précisant respectivement : 
Le batch : hyperparamètre qui précise la fréquence d’ajustement des poids ( après feedforward et rétropropagation)
Epochs : le nombre de fois que le code passe sur les données par étape d’entraînement.
Weights : fichier dans lequel on stocke les valeurs des poids lorsque l’algorithme de descente du gradient converge.
Project/ name : le dossier où stocker le résultat de la détection.


Val.py ( disponible via le lien Github suivant : https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/models/YOLOv5_trained/val.py)
: permet de choisir le modèle avec les paramètres les plus optimisés. Il est constitué principalement de la fonction main() qui permet d’optimiser les poids du réseau de neurones.
!python val.py --weights 'runs_raquette/fine_tuning/weights/best.pt' --batch 64 --data 'data/raquette_data.yaml' --task test --project 'runs_raquette' --name 'validation_on_test_data' --augment
La ligne ci-dessous permet d'exécuter le code val.py en lui passant comme paramètres:
Les poids résultant du fine-tuning ( éviter le sur apprentissage) ( fichier best.pt) , le batch, la data ( le fichier yaml contenant le nombre de classes d’objets à détecter et leurs noms).


Et les autres paramètres spécifient le dossier de sauvegarde.


detect.py ( disponible via ce lien Github : https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/models/YOLOv5_trained/detect.py) : ce code permet de tester notre modèle sur le test set et sur des vidéos pour avoir une détection en temps réel.
!python detect.py --weights 'runs_raquette/fine_tuning/weights/best.pt'  --conf 0.6 --source 'match_Trim.mp4' --project 'runs_raquette' --name 'detect_test' --augment --line=3
 
La ligne du code ci-dessus permet de spécifier les paramètres en entrée du code detect.py ( les poids du modèle, la source qu’est les images ou les vidéos à tester, et le path d’enregistrement.
Les résultats du tracking sur la data du test est disponible via ce lien Github : https://github.com/centralelyon/par-22-23-detection-raquette/tree/main/runs_raquettes/detect_test
). Les résultats du tracking sur des vidéos sont disponibles via ce lien gitHub : 

Metrics.py ( disponible via ce lien : https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/models/YOLOv5_trained/utils/metrics.py )
: code qui permet de tracer les métriques en fonction des epochs pour l’entraînement. On trace la précision donnée par la relation : 
Précision=TP(true positives)/TP+FP( false positives) 

Le modèle nous donne aussi la matrice de confusion dans notre cas, ce qui constitue une bonne base de quantification des erreurs de l’apprentissage.
Toutes les métriques sont tracées et disponibles via le lien Github suivant  : https://github.com/centralelyon/par-22-23-detection-raquette/tree/main/runs_raquettes/validation_on_test_data)

general.py(disponible via ce lien : https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/models/YOLOv5_trained/utils/general.py)
: code qui permet de tracer les bounding boxes sur les images et vidéos à tester.

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Description des différents dossiers:
scripts : contient les différents codes python utilisés notamment pour la division d'une vidéo en plusieurs frames, les tests statistiques de traitement d'images et les algorithmes associés aux modèle YOLO ( une description plus détaillée est disponible  en suivant ce lien :
https://github.com/centralelyon/par-22-23-detection-raquette/tree/main/scripts ).
datasets: contient l'ensemble des images utilisées pour entraîner, tester et valider nos modèles de détection.
datasets
    |_____raquette_data : images issues de vidéos de matchs de  tennis    de table et leurs labels.
    |_____raquette_plusieurs_vues : dataset personnalisée générée avec Keras avec plusieurs angles de vue d'une raquette.
models : contient l'ensemble des modèles déployés pour la détection avec tous les codes, les fichiers, les requirements nécessaires.
models
   |____YOLOv5 trained : la documentation de ce modèle a été appuyée sur le lien GitHub suivant : https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data et sur le site suivant : https://blog.paperspace.com/train-yolov5-custom-data/. 
   |____YOLOv5_trained_with_roboflow : l'entraînement de ce modèle a été réalisée avec le site roboflow qui est un framework open source pour entraîner "from scratch" son modèle. ( voir le site en cliquant sur ce lien : https://universe.roboflow.com/ ).

Data augmentation : contient l'ensemble des résultats de la data augmentation ( rotation, changement de scale, de luminosité, de contraste, symétrie, normalisation etc). Nous passons d'une dataset de 450 images à 900 images sans annotations supplémentaires.

![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/Data%20augmentation/contrast_image.png?raw=true)
![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/Data%20augmentation/flipped_horizontal_image.png?raw=true)
![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/Data%20augmentation/normalized_image.png?raw=true)
![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/Data%20augmentation/flipped_image.png?raw=true)


tracking_results : contient les résultats de détection de nos modèles sur plusieurs samples ( vidéos). On réalise une inférence du modèle établi sur ces vidéos avec le code detect.py décrit ci-dessus.

runs_raquettes: contient les principaux résultats d'entraînement et de test de nos modèles, notamment les poids du réseau de neurones profond de YOLO, l'ensemble de métriques ( précision, rappel) et éventuellement la matrice de confusion associée qui donne une image claire de la robustesse du modèle.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Description des différents notebooks
Data_augmentation_with_pytorch:  réalise plusieurs modifications de nos images ( redimensionnement, symétrie, rotation, normalisation etc).

Flip_Horizontal_dataset : utilise seulement la symétrie horizontale de la data augmentation ( vue son utilité pour s'affranchir d'annoter plusieurs raquettes).

Modèle_avec_Data_augmentation : déploie un modèle basé sur YOLOv5 + data augmentation. Il  initialise les poids, prépare les données de train, de validation et de test, entraîne le modèle, le valide ou "Fine tune", le teste et réalise des inférences sur de nouvelles vidéos.

Pipeline : décrit la démarche suivie pour la détection d'une raquette : 
    - Dégager les features intéressants.
    - Préparer notre dataset ( jeu de données).
    - Décrire l'architecture du réseau de neurones.
    - Déployer le modèle.
    - Valider le modèle.

Résultats obtenus:

YOLOv3:
Avec ce modèle, nous avons obtenu une précision de :
82% sur la data d'entraînement.
75% sur la data de test.
Le temps de calcul est de 15 minutes.

![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/exemple_detection_yolov3.png?raw=true)
![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/exemple_detection_yolov3_1.png?raw=true)

YOLOv5:
Avec ce modèle, nous avons obtenu une précision de :
85% sur la data de test.
Le temps de calcul est aussi de 20 minutes.

![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/exemple_detection.png?raw=true)
![alt text](https://github.com/centralelyon/par-22-23-detection-raquette/blob/main/exemple_detection_v5_1.png?raw=true)
Limites du modèle:
Détection d'une seule raquette (recherche dans une zone limitée de l'image).
Précsion biaisée ( la test set a des caractéristiques similaires que la training set) ( la précision se dégrade lorsque la distance de la caméra varie, la luminosité ou le contraste change etc).