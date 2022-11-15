# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class FormatTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "number",
            "password",
            "byte",
        }
        
        class properties:
            
            
            class number(
                schemas.NumberSchema
            ):
                pass
            byte = schemas.StrSchema
            date = schemas.DateSchema
            
            
            class password(
                schemas.StrSchema
            ):
                pass
            
            
            class integer(
                schemas.IntSchema
            ):
                pass
            int32 = schemas.Int32Schema
            
            
            class int32withValidations(
                schemas.Int32Schema
            ):
                pass
            int64 = schemas.Int64Schema
            
            
            class _float(
                schemas.Float32Schema
            ):
                pass
            float32 = schemas.Float32Schema
            
            
            class double(
                schemas.Float64Schema
            ):
                pass
            float64 = schemas.Float64Schema
            
            
            class arrayWithUniqueItems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'arrayWithUniqueItems':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class string(
                schemas.StrSchema
            ):
                pass
            binary = schemas.BinarySchema
            dateTime = schemas.DateTimeSchema
            uuid = schemas.UUIDSchema
            uuidNoExample = schemas.UUIDSchema
            
            
            class pattern_with_digits(
                schemas.StrSchema
            ):
                pass
            
            
            class pattern_with_digits_and_delimiter(
                schemas.StrSchema
            ):
                pass
            noneProp = schemas.NoneSchema
            __annotations__ = {
                "number": number,
                "byte": byte,
                "date": date,
                "password": password,
                "integer": integer,
                "int32": int32,
                "int32withValidations": int32withValidations,
                "int64": int64,
                "float": _float,
                "float32": float32,
                "double": double,
                "float64": float64,
                "arrayWithUniqueItems": arrayWithUniqueItems,
                "string": string,
                "binary": binary,
                "dateTime": dateTime,
                "uuid": uuid,
                "uuidNoExample": uuidNoExample,
                "pattern_with_digits": pattern_with_digits,
                "pattern_with_digits_and_delimiter": pattern_with_digits_and_delimiter,
                "noneProp": noneProp,
            }
    
    date: MetaOapg.properties.date
    number: MetaOapg.properties.number
    password: MetaOapg.properties.password
    byte: MetaOapg.properties.byte
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer"]) -> MetaOapg.properties.integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32"]) -> MetaOapg.properties.int32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32withValidations"]) -> MetaOapg.properties.int32withValidations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int64"]) -> MetaOapg.properties.int64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> MetaOapg.properties._float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float32"]) -> MetaOapg.properties.float32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float64"]) -> MetaOapg.properties.float64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arrayWithUniqueItems"]) -> MetaOapg.properties.arrayWithUniqueItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string"]) -> MetaOapg.properties.string: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["binary"]) -> MetaOapg.properties.binary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> MetaOapg.properties.dateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuidNoExample"]) -> MetaOapg.properties.uuidNoExample: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_with_digits"]) -> MetaOapg.properties.pattern_with_digits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_with_digits_and_delimiter"]) -> MetaOapg.properties.pattern_with_digits_and_delimiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["noneProp"]) -> MetaOapg.properties.noneProp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["number", "byte", "date", "password", "integer", "int32", "int32withValidations", "int64", "float", "float32", "double", "float64", "arrayWithUniqueItems", "string", "binary", "dateTime", "uuid", "uuidNoExample", "pattern_with_digits", "pattern_with_digits_and_delimiter", "noneProp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integer"]) -> typing.Union[MetaOapg.properties.integer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int32"]) -> typing.Union[MetaOapg.properties.int32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int32withValidations"]) -> typing.Union[MetaOapg.properties.int32withValidations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int64"]) -> typing.Union[MetaOapg.properties.int64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float"]) -> typing.Union[MetaOapg.properties._float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float32"]) -> typing.Union[MetaOapg.properties.float32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double"]) -> typing.Union[MetaOapg.properties.double, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float64"]) -> typing.Union[MetaOapg.properties.float64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arrayWithUniqueItems"]) -> typing.Union[MetaOapg.properties.arrayWithUniqueItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["string"]) -> typing.Union[MetaOapg.properties.string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["binary"]) -> typing.Union[MetaOapg.properties.binary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[MetaOapg.properties.dateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuidNoExample"]) -> typing.Union[MetaOapg.properties.uuidNoExample, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pattern_with_digits"]) -> typing.Union[MetaOapg.properties.pattern_with_digits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pattern_with_digits_and_delimiter"]) -> typing.Union[MetaOapg.properties.pattern_with_digits_and_delimiter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["noneProp"]) -> typing.Union[MetaOapg.properties.noneProp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["number", "byte", "date", "password", "integer", "int32", "int32withValidations", "int64", "float", "float32", "double", "float64", "arrayWithUniqueItems", "string", "binary", "dateTime", "uuid", "uuidNoExample", "pattern_with_digits", "pattern_with_digits_and_delimiter", "noneProp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, float, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        byte: typing.Union[MetaOapg.properties.byte, str, ],
        integer: typing.Union[MetaOapg.properties.integer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32: typing.Union[MetaOapg.properties.int32, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32withValidations: typing.Union[MetaOapg.properties.int32withValidations, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int64: typing.Union[MetaOapg.properties.int64, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        float32: typing.Union[MetaOapg.properties.float32, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        double: typing.Union[MetaOapg.properties.double, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        float64: typing.Union[MetaOapg.properties.float64, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        arrayWithUniqueItems: typing.Union[MetaOapg.properties.arrayWithUniqueItems, list, tuple, schemas.Unset] = schemas.unset,
        string: typing.Union[MetaOapg.properties.string, str, schemas.Unset] = schemas.unset,
        binary: typing.Union[MetaOapg.properties.binary, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.properties.dateTime, str, datetime, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        uuidNoExample: typing.Union[MetaOapg.properties.uuidNoExample, str, uuid.UUID, schemas.Unset] = schemas.unset,
        pattern_with_digits: typing.Union[MetaOapg.properties.pattern_with_digits, str, schemas.Unset] = schemas.unset,
        pattern_with_digits_and_delimiter: typing.Union[MetaOapg.properties.pattern_with_digits_and_delimiter, str, schemas.Unset] = schemas.unset,
        noneProp: typing.Union[MetaOapg.properties.noneProp, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormatTest':
        return super().__new__(
            cls,
            *_args,
            date=date,
            number=number,
            password=password,
            byte=byte,
            integer=integer,
            int32=int32,
            int32withValidations=int32withValidations,
            int64=int64,
            float32=float32,
            double=double,
            float64=float64,
            arrayWithUniqueItems=arrayWithUniqueItems,
            string=string,
            binary=binary,
            dateTime=dateTime,
            uuid=uuid,
            uuidNoExample=uuidNoExample,
            pattern_with_digits=pattern_with_digits,
            pattern_with_digits_and_delimiter=pattern_with_digits_and_delimiter,
            noneProp=noneProp,
            _configuration=_configuration,
            **kwargs,
        )
