YOLO (You Only Look Once) is an object detection and image segmentation model for machine learning, based on deep learning and computer vision advancements.

### Documentation
https://docs.ultralytics.com/#where-to-start

In this testbed, I trained my own yolo11s model using Google Colab using a set of 110 photos of 6 pens and 1 mechanical pencil, in varied lighting conditions and backgrounds. I labelled each photo inside of a local Anaconda environment using Label-Studio

<img width="440" height="330" alt="explorer_6anYavOMkb" src="https://github.com/user-attachments/assets/ec436b0b-859d-4072-97ba-37b88c81331a" />
<img width="400" height="400" alt="bJHD6BYJ7L" src="https://github.com/user-attachments/assets/23ad4d65-0efb-4866-bba2-013c6ab5107a" />

I then separated the set into 100 training photos, and 10 validation photos. I trained this model with 60 epochs, at 640x480 resolution on a yolo11s model.

The first model was not a great success. It struggled with the low-lighting, different backgrounds (such as my face, and the slit in the wall) and covering of 1/4 or more of the pen.

<img width="426" height="240" alt="Video Project" src="https://github.com/user-attachments/assets/192d4b8a-e1be-444e-b001-fdf4864ebeca" />
<img width="300" height="400" alt="download" src="https://github.com/user-attachments/assets/724a0f09-6da3-4d3d-98d2-5cd19f1bf695" />

I trained both yolo11n and yolo11s on 300 epochs as a further test. it seems that yolo11n on 300 epochs performed significantly better with lighting conditions, and varied backgrounds.

<img width="480" height="240" alt="download (2)" src="https://github.com/user-attachments/assets/14f68ea4-947f-4eb0-840d-5070e42e7605" />
<img width="300" height="400" alt="download (1)" src="https://github.com/user-attachments/assets/19e22477-d5b3-44be-8fca-c95ff35defff" />

Performance metrics @ 300 epochs:
Yolo11s: ``Completion time: 0.283 hr(Tesla T4), Params: 9.42M, Size: 19.2MB, mAP50: 0.924, mAP50-95: 0.718, Precision: 0.915, Recall: 0.0.891``
Yolo11n: ``Completion time: 0.256 hr(Tesla T4), Params: 2.58M, Size: 5.5MB, mAP50: 0.92, mAP50-95: 0.721, Precision: 0.878, Recall: 0.908``

From the metrics above, the performance from Yolo11s and Yolo11n were basically indistinguishable, even though Yolo11n had a nearly 4x smaller size.

It is worth noting however, that the training/validation images were not the same between tests, due to the script that split them. I also believe that with this small of a training and validation dataset, and even on 300 epochs, the model started to memorize specific orientations and images of the pens and pencils. I noticed that when moving the pens into different orientations, and lighting conditions, it would recognize them better than others.

The mechanical pencil class, being nearly identical to the red pen class, save for a transparent body struggled a lot on the precision and recognition portion.

I also noticed that the yolo11n model performed on my (admittedly quite constrained Ryzen 5 5500U with integrated graphics, 8gb RAM) hardware nearly twice as well, clocking an average of 12 fps, while yolo11s averaged about 6 fps.





