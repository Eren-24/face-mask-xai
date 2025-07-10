import os
import pandas as pd

data = []
base_dir = 'RMFD'

for label, category in enumerate(['Unmasked', 'Masked']):
    category_path = os.path.join(base_dir, category)
    for img_name in os.listdir(category_path):
        data.append((os.path.join(category_path, img_name), label))

df = pd.DataFrame(data, columns=["filepath", "label"])
