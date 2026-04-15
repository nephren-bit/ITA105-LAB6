import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import random

image_folder = r"C:\Users\Ngopt\Downloads\ITA105_Lab\lab6\anh_can_ho"

image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg','png','jpeg'))]
sample_paths = random.sample(image_paths, 5)

original_images = []
augmented_images = []

for path in sample_paths:
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    original_images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    aug = cv2.flip(img, 1)
    angle = random.choice([-15, 15])
    h, w = aug.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
    aug = cv2.warpAffine(aug, M, (w, h))
    factor = random.uniform(0.8, 1.2)
    aug = np.clip(aug * factor, 0, 255).astype(np.uint8)
    aug = cv2.cvtColor(aug, cv2.COLOR_BGR2GRAY)
    aug = aug / 255.0

    augmented_images.append(aug)

plt.figure(figsize=(12,6))

for i in range(5):
    plt.subplot(2,5,i+1)
    plt.imshow(original_images[i])
    plt.title("Original")
    plt.axis('off')

for i in range(5):
    plt.subplot(2,5,i+6)
    plt.imshow(augmented_images[i], cmap='gray')
    plt.title("Augmented")
    plt.axis('off')

plt.tight_layout()
plt.show()
# ----------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt


img_path = r"C:\Users\Ngopt\Downloads\ITA105_Lab\lab6\hypercar.jpg"

img = cv2.imread(img_path)

img = cv2.resize(img, (224, 224))

original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

aug = img.copy()
noise = np.random.normal(0, 25, aug.shape).astype(np.uint8)
aug = cv2.add(aug, noise)
factor = 1.1
aug = np.clip(aug * factor, 0, 255).astype(np.uint8)
angle = 10 
h, w = aug.shape[:2]
M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
aug = cv2.warpAffine(aug, M, (w, h))
use_gray = True
if use_gray:
    aug = cv2.cvtColor(aug, cv2.COLOR_BGR2GRAY)
aug = aug / 255.0

plt.figure(figsize=(6,3))

plt.subplot(1,2,1)
plt.imshow(original)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
if len(aug.shape) == 2:
    plt.imshow(aug, cmap='gray')
else:
    plt.imshow(aug)
plt.title("Augmented")
plt.axis('off')

plt.tight_layout()
plt.show()
# ------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r"C:\Users\Ngopt\Downloads\ITA105_Lab\lab6\apple.jpg"

img = cv2.imread(img_path)

img = cv2.resize(img, (224, 224))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

augmented_images = []

for i in range(9):
    aug = img.copy()

    if np.random.rand() > 0.5:
        aug = cv2.flip(aug, 1)

    h, w = aug.shape[:2]
    crop_size = int(np.random.uniform(0.7, 1.0) * h)
    x = np.random.randint(0, w - crop_size)
    y = np.random.randint(0, h - crop_size)
    aug = aug[y:y+crop_size, x:x+crop_size]
    aug = cv2.resize(aug, (224, 224))

    zoom_factor = np.random.uniform(1.0, 1.3)
    new_size = int(224 * zoom_factor)
    zoom_img = cv2.resize(aug, (new_size, new_size))

    start = (new_size - 224) // 2
    aug = zoom_img[start:start+224, start:start+224]

    angle = np.random.uniform(-20, 20)
    M = cv2.getRotationMatrix2D((112, 112), angle, 1)
    aug = cv2.warpAffine(aug, M, (224, 224))

    aug = aug / 255.0

    augmented_images.append(aug)

plt.figure(figsize=(6,6))

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(augmented_images[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
# ----------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

image_folder = r"C:\Users\Ngopt\Downloads\ITA105_Lab\lab6\anh_can_ho"

image_paths = [os.path.join(image_folder, f) 
               for f in os.listdir(image_folder) 
               if f.endswith(('jpg','png','jpeg'))]

image_paths = image_paths[:3]

original_images = []
augmented_images = []

for path in image_paths:
    img = cv2.imread(path)

    img = cv2.resize(img, (224, 224))

    original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    original_images.append(original)

    aug = img.copy()

    angle = np.random.uniform(-15, 15)
    h, w = aug.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
    aug = cv2.warpAffine(aug, M, (w, h))

    if np.random.rand() > 0.5:
        aug = cv2.flip(aug, 1)

    factor = np.random.uniform(0.8, 1.2)
    aug = np.clip(aug * factor, 0, 255).astype(np.uint8)

    aug = cv2.cvtColor(aug, cv2.COLOR_BGR2GRAY)

    aug = aug / 255.0

    augmented_images.append(aug)
    
plt.figure(figsize=(8,6))

for i in range(3):
    plt.subplot(2,3,i+1)
    plt.imshow(original_images[i])
    plt.title(f"Original {i+1}")
    plt.axis('off')

for i in range(3):
    plt.subplot(2,3,i+4)
    plt.imshow(augmented_images[i], cmap='gray')
    plt.title(f"Aug {i+1}")
    plt.axis('off')

plt.tight_layout()
plt.show()