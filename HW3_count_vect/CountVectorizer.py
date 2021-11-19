from typing import Iterable


class CountVectorizer():
    """Converts a collection of text documents to a matrix of token counts"""

    def fit_transform(self, coprus: Iterable) -> Iterable:
        """Vectorizes given corpus"""
        tmp_features = []
        for elem in coprus:
            tmp_features.extend(elem.split(' '))
        self.__features = []
        [self.__features.append(elem.lower()) for elem in tmp_features if elem.lower() not in self.__features]
        self.__count_matrix = []
        for elem in coprus:
            parsed_sent = [x.lower() for x in elem.split(' ')]
            count_dict = dict(zip(self.__features, [0 for feature in self.__features]))
            for word in parsed_sent:
                if word in count_dict.keys():
                    count_dict[word] += 1
            self.__count_matrix.append(list(count_dict.values()))
        return self.__count_matrix

    def get_feature_names(self) -> Iterable:
        """Returns features names"""
        return self.__features


if __name__ == '__main__':
    cv = CountVectorizer()

    cp = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    print(cv.fit_transform(cp))

    print(cv.get_feature_names())
