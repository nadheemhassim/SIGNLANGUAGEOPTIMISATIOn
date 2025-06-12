import os

def check_images(path='train'):
    for label in sorted(os.listdir(path)):
        folder = os.path.join(path, label)
        if os.path.isdir(folder):
            count = len([f for f in os.listdir(folder) if f.endswith(('.jpg', '.png', '.jpeg'))])
            print(f"{label}: {count} images")

print("Training Set:")
check_images('train')
print("\nTest Set:")
check_images('test')
