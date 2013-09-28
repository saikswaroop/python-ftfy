import codecs
from encodings import normalize_encoding

_cache = {}


def search_function(encoding):
    if encoding in _cache:
        return _cache[encoding]

    norm_encoding = normalize_encoding(encoding)
    more_norm_encoding = norm_encoding.replace('_', '')
    codec = None
    if more_norm_encoding in ('utf8variants', 'utf8variant', 'utf8var', 'cesu8'):
        from ftfy.bad_codecs.utf8_variants import CODEC_INFO
        codec = CODEC_INFO
    elif norm_encoding.startswith('sloppy_'):
        from ftfy.bad_codecs.sloppy import CODECS
        return CODECS.get(norm_encoding)

    if codec is not None:
        _cache[encoding] = codec

    return codec


codecs.register(search_function)
