from sentiment.get_sentiment import get_model
import numpy as np

if __name__ == '__main__':
    model, labels_encoded, labels_list = get_model(descriptions, labels)