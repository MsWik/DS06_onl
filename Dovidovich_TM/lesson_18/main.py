import spacy
import numpy as np

from typing import List
from string import punctuation

from spacy.lang.en import STOP_WORDS

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt

def preprocessing(file_name: str,NLP: spacy.Language) -> List:
    with open(file_name, encoding="utf-8") as f:
        text_file = f.read()

    text_file = NLP(text_file)

    text_lemmatized = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-' else word.lower_ for word in text_file]

    text_cleared = [word for word in text_lemmatized if word not in punctuation and word not in STOP_WORDS]

    return text_cleared

def vectorizing(text: List[str], NLP: spacy.Language) -> None:
    array = []
    for word in text:
        array.append(NLP(word).vector)
    return array

def graph(pca_matrix: List[List[float]], text: List[str])-> None:
    plt.figure(figsize=(10, 8))
    plt.scatter(pca_matrix[:, 0], pca_matrix[:, 1])
    for i,word in enumerate(text):
        plt.annotate(word, (pca_matrix[i, 0], pca_matrix[i, 1]))
    plt.show()

def main() -> None:
    NLP = spacy.load('en_core_web_lg')
    text = preprocessing("text.txt",NLP)
    array = vectorizing(text, NLP)
    print(len(array))


    pca = PCA(n_components=2, random_state=23)
    pca_matrix = pca.fit_transform(array)
    print("Матрица PCA:\n", pca_matrix)
    
    tsne = TSNE(n_components=2, random_state=23)
    tsne_matrix = tsne.fit_transform(np.array(array))
    print("Матрица TSNE:\n", tsne_matrix)

    graph(pca_matrix, text)
    

if __name__ == '__main__':
    main()