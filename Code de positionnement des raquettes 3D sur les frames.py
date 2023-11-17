import bpy
import sys
import csv
from PIL import Image
C = bpy.context


# Chemin vers le fichier CSV
csv_file = 'C:\\Users\\R I B\\Desktop\\img_squelette\\result\\match_fonctionnel_tests_flore_boll_openpose.csv.csv'

# Chemin vers le dossier contenant les images
image_folder = "C:\\Users\R I B\Desktop\img_squelette\ "

#Chargement du fichier CSV
f=open(csv_file,'r')
csv_reader = csv.reader(f, delimiter=',')
line_count = 0
for row in csv_reader:
            if line_count == 0:
                # Ignorer la première ligne (en-têtes)
                line_count += 1
            else:
                frame_number = int(row[0])
                cam = bpy.context.scene.camera
                image_path = image_folder[:-1]  + str(frame_number) + ".jpg"
                img = bpy.data.images.load(image_path)
                cam.data.show_background_images = True
                bg = cam.data.background_images.new()
                bg.image = img
                img_idx = len(bpy.data.images)-1
                
                echelle=5/1920
                # Récupérer les données de position des objets pour la frame actuelle
                if int(row[6])==1 and (int(row[2])==4 or int(row[2])==7):
                    object1_position = [float(row[3])*echelle, float(row[4])*echelle]
                    object2_position = [float(row[3])*echelle, float(row[4])*echelle]
                    # Charger l'image pour cette frame
                    
                
                    # Accéder aux objets dans Blender et positionner
                    if int(row[1])==1 and int(row[2])==4:
                        obj1 = bpy.data.objects['Point.001']
                        obj1.location = object1_position
                        obj1.keyframe_insert(data_path="location", index=-1)
                        obj2.keyframe_insert(data_path="location", index=-1)
                
                    if int(row[1])==0 and int(row[2])==7:
                        obj2 = bpy.data.objects['Point.002']
                        obj2.location = object2_position
                        obj1.keyframe_insert(data_path="location", index=-1)
                        obj2.keyframe_insert(data_path="location", index=-1)
                
                
                    # Ajouter une nouvelle keyframe pour chaque objet
                    
                    # Définir l'image actuelle comme frame courante et ajouter une keyframe
                    bpy.context.scene.frame_set(frame_number)
                    bpy.data.scenes['Scene'].frame_current = frame_number
                    bpy.data.scenes['Scene'].render.image_settings.file_format = 'JPEG'
                    bpy.data.scenes['Scene'].render.filepath = image_folder + "output/frame_" + str(frame_number) + ".jpg"
                    bpy.ops.render.render(write_still=True)
                
                    line_count += 1
                    break


