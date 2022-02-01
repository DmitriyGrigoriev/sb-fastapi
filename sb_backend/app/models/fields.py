import re
from pydantic import BaseModel

# https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
series_code_regex = re.compile(
    r'[A-Z-А-Я]+[0-9]{3,20}$'
)

class SeriesCode(str):
    """
    Partial UK postcode validation. Note: this is just an example, and is not
    intended for use in production; in particular this does NOT guarantee
    a postcode exists, just that it has a valid format.
    """

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(
            # simplified regex here for brevity, see the wikipedia link above
            pattern='[A-Z-А-Я]+[0-9]{3,20}$',
            # some example postcodes
            examples='ТК210001',
        )

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError('string required')
        if len(v) > 0:
            m = series_code_regex.fullmatch(v.upper())
            if not m:
                raise ValueError("Неверный формат поля «Код Серия Номеров», пример правильного формата: ТК210001")
            else:
                result = m.string
        else:
            result = ''
        # m = re.findall(r'[A-Z][0-9]{3,20}$', v.upper())
        # you could also return a string here which would mean model.post_code
        # would be a string, pydantic won't care but you could end up with some
        # confusion since the value's type won't match the type annotation
        # exactly
        return cls(result)
        # return cls(f'{m.group(1)} {m.group(2)}')

    def __repr__(self):
        return f'SeriesCode({super().__repr__()})'


# class Model(BaseModel):
#     series_code: SeriesCode
#
#
# model = Model(series_code='ТК210001')
# print(model)
# #> post_code=SeriesCode('ТК210001')
# print(model.series_code)
# #> ТК210001
# print(Model.schema())
# """
# {
#     'title': 'Model',
#     'type': 'object',
#     'properties': {
#         'series_code': {
#             'title': 'Series Code',
#             'pattern': '[A-Z-А-Я]+[0-9]{3,20}$',
#             'examples': 'ТК210001',
#             'type': 'string',
#         },
#     },
#     'required': ['series_code'],
# }
# """
