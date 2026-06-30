YOLO (You Only Look Once) is an object detection and image segmentation model for machine learning, based on deep learning and computer vision advancements.

### Documentation
https://docs.ultralytics.com/#where-to-start

In this testbed, I trained my own yolo11s model using Google Colab using a set of 110 photos of 6 pens and 1 mechanical pencil, in varied lighting conditions and backgrounds. I labelled each photo inside of a local Anaconda environment using Label-Studio

<img width="440" height="330" alt="explorer_6anYavOMkb" src="https://github.com/user-attachments/assets/ec436b0b-859d-4072-97ba-37b88c81331a" />
<img width="400" height="400" alt="bJHD6BYJ7L" src="https://github.com/user-attachments/assets/23ad4d65-0efb-4866-bba2-013c6ab5107a" />

I then separated the set into 100 training photos, and 10 validation photos. I trained this model with 60 epochs, at 640x480 resolution on a yolo11s model.

The first model was not a great success. It struggled with the low-lighting, different backgrounds (such as my face, and the slit in the wall) and covering of 1/4 or more of the pen.
(I closed the Colab tab before I grabbed the metrics for the training test 🥲)

<img width="426" height="240" alt="Video Project" src="https://github.com/user-attachments/assets/192d4b8a-e1be-444e-b001-fdf4864ebeca" />
<img width="300" height="400" alt="download" src="https://github.com/user-attachments/assets/724a0f09-6da3-4d3d-98d2-5cd19f1bf695" />

For the second model, I trained it for 300 epochs on a yolo11n model, since the first test ran poorly on my hardware.

<img width="480" height="240" alt="download (2)" src="https://github.com/user-attachments/assets/14f68ea4-947f-4eb0-840d-5070e42e7605" />
<img width="300" height="400" alt="download (1)" src="https://github.com/user-attachments/assets/19e22477-d5b3-44be-8fca-c95ff35defff" />

While I trained on a different model base, and the differences between yolo11s and yolo11n are not clear to me, it seems that yolo11n on 300 epochs performed significantly better with lighting conditions, and varied backgrounds.
``mAP50: 0.92, mAP50-95: 0.721, Precision: 0.878, Recall: 0.908``

I believe that with this small of a training and validation dataset, and even on 300 epochs, the model started to memorize specific orientations and images of the pens and pencils, instead of learning generalized features of the object. I noticed that when moving the pens into specific orientations, and lighting conditions, it would recognize them better than others.

I also noticed that the yolo11n model performed on my (admittedly quite constrained) hardware nearly twice as well, clocking an average of 12 fps, while yolo11s averaged about 6 fps.





