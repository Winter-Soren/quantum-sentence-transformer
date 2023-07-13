import pandas as pd
from torch.utils.data import Dataset, DataLoader, random_split

class CustomTextDataset(Dataset):
    def __init__(self, text, labels):
        self.labels = labels
        self.text = text

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        label = self.labels[idx]
        text = self.text[idx]
        return text, label

##########################################
# Load your dataset in a DataFrame with the required format:
# ----------------------------------
# |   text         |      label     |
# |   example 1    |        0       |
# |   example 2    |        1       |
# |     ...        |       ...      |
# -----------------------------------
##########################################

df = pd.read_pickle("your_text_dataset.pkl")
        
# Create the CustomTextDataSet object and split it into training and validation sets
# using the desired number of samples
text_dataset = CustomTextDataset(df['text'], df['label'])
train_set, validation_set = random_split(text_dataset, [282, 32])

# Create data loaders for training and validation
train_loader = DataLoader(train_set, batch_size=32, shuffle=True)
validation_loader = DataLoader(validation_set, batch_size=32, shuffle=True)

dataloaders = {
    "train": train_loader,
    "validation": validation_loader
}

dataset_sizes = {
    "train": len(train_set),
    "validation": len(validation_set)
}
