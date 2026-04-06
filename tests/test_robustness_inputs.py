from sklearn.feature_extraction.text import TfidfVectorizer


def test_empty_string_ok():
    vec = TfidfVectorizer()
    X = vec.fit_transform(["xin chao", ""])
    assert X.shape[0] == 2


def test_whitespace_only():
    vec = TfidfVectorizer()
    X = vec.fit_transform(["xin chao", "   "])
    assert X.shape[0] == 2


def test_long_text():
    vec = TfidfVectorizer()
    long_text = "xin chao " * 10000
    X = vec.fit_transform(["hello", long_text])
    assert X.shape[0] == 2


def test_weird_chars_ok():
    vec = TfidfVectorizer()
    X = vec.fit_transform(["😄!!!", "###@@@ ???"])
    assert X.shape[0] == 2


def test_emoji():
    vec = TfidfVectorizer()
    X = vec.fit_transform(["😊🔥💯", "test"])
    assert X.shape[0] == 2


def test_teencode():
    vec = TfidfVectorizer()
    X = vec.fit_transform(["ko bt j lun", "khong biet gi"])
    assert X.shape[0] == 2