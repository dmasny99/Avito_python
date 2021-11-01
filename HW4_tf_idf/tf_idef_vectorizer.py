import typing as t
import math


class CountVectorizer():
    """Converts a collection of text documents to a matrix of token counts"""
    def __init__(self) -> None:
        self.__features = []
        self.__count_matrix = []

    def fit_transform(self, coprus: t.List[str]) -> t.List[t.List[int]]:
        """Vectorizes given corpus"""
        tmp_features = []
        for word in coprus:
            tmp_features.extend(word.split())
        for word in tmp_features:
            if word.lower() not in self.__features:
                self.__features.append(word.lower())
        for text in coprus:
            parsed_sent = [x.lower() for x in text.split()]
            count_dict = dict(zip(self.__features, [0 for feature in self.__features]))
            for word in parsed_sent:
                if word in count_dict.keys():
                    count_dict[word] += 1
            self.__count_matrix.append(list(count_dict.values()))
        return self.__count_matrix

    def get_feature_names(self) -> t.List[str]:
        """Returns features names"""
        return self.__features


class TfidfTransformer():
    """Converts a collection of text documents to a matrix of token counts"""
    def __init__(self) -> None:
        self.__features = []
        self.__tf_matrix = []
        self.__idf_matrix = []

    def tf_transform(self, count_matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
        """Returns TF matrix"""
        for vector in count_matrix:
            tf_tmp = []
            for word in vector:
                tf_tmp.append(round((word / sum(vector)), 3))
            self.__tf_matrix.append(tf_tmp)
        return self.__tf_matrix

    def idf_transform(self, count_matrix: t.List[t.List[int]]) -> t.List[float]:
        """Returns IDF matrix"""
        doc_count = len(count_matrix) + 1
        for column in range(len(count_matrix[0])):
            current_sum = 0
            for row in range(len(count_matrix)):
                current_sum += bool(count_matrix[row][column])
            self.__idf_matrix.append(current_sum + 1)
        for i in range(len(self.__idf_matrix)):
            self.__idf_matrix[i] = -1 * math.log(self.__idf_matrix[i] / doc_count) + 1
        return self.__idf_matrix

    def fit_transform(self, matrix: t.List[t.List[int]]) -> t.List[t.List[float]]:
        """Vectorizes given corpus"""
        tf = self.tf_transform(matrix)
        idf = self.idf_transform(matrix)
        tf_idf_matrix = []
        for vector in tf:
            tf_idf_matrix.append([round(a * b, 3) for a, b in zip(vector, idf)])
        return tf_idf_matrix

    def get_feature_names(self) -> t.Iterable:
        """Returns features names"""
        return self.__features


class TfIdfVectorizer(CountVectorizer):
    """Convert a collection of text documents to a matrix of token counts"""
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        """Vectorizes given corpus"""
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    tf = TfIdfVectorizer()

    cp = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    print(tf.fit_transform(cp), '\n\n')
