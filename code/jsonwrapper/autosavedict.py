from __future__ import annotations
import os
import json
from typing import (
    Any,
    Dict,
    Tuple,
    Mapping,
    Optional,
    Iterable,
    MutableMapping,
)


__all__ = (
    'AutoSaveDict',
)


class AutoSaveDict(dict[Any, Any]):
    def __init__(self,
                 file_path: Optional[os.PathLike[Any]] = None,
                 **pairs: Any):
        self.file_path = file_path
        self.__default = pairs

        if self.file_path is None:
            self._pairs = pairs
        elif not os.path.exists(self.file_path):
            self._pairs = pairs
        else:
            self._pairs = self._read()
        super(AutoSaveDict, self).__init__(**self._pairs)

    def __setitem__(self, __key: Any, __value: Any) -> None:
        data = self._read()
        data[__key] = __value
        self._write(data)
        super().__setitem__(__key, __value)

    def __delitem__(self, __key: Any) -> None:
        data = self._read()
        del data[__key]
        self._write(data)
        return super().__delitem__(__key)

    def __or__(self, __value: Mapping[Any, Any]) -> AutoSaveDict:
        data = self._pairs | __value
        return AutoSaveDict(None, **data)

    def _write(self, content: Dict[Any, Any]) -> None:
        with open(self.file_path, mode='w') as f:  # type: ignore
            json.dump(content, f, indent=4)
        self._pairs = content

    def _read(self) -> Dict[Any, Any]:
        with open(self.file_path, mode='r') as f:  # type: ignore
            data: Dict[Any, Any] = json.load(f)
            return data

    @classmethod
    def fromkeys(cls, __iterable: Iterable[Any], __value: Any = None,
                 file_path: Optional[os.PathLike[Any]] = None) -> AutoSaveDict:
        data = {}
        for key in __iterable:
            data[key] = __value
        return cls(file_path, **data)

    @classmethod
    def frommapping(cls, __mapping: Mapping[Any, Any],
                    file_path: Optional[os.PathLike[Any]] = None)\
            -> AutoSaveDict:
        data = dict(__mapping)
        return cls(file_path, **data)

    @classmethod
    def fromfile(cls, src: os.PathLike[Any],
                 dst: Optional[os.PathLike[Any]] = None) -> AutoSaveDict:
        with open(src, mode='r') as f:
            data = json.load(f)
        return AutoSaveDict(dst, **data)

    def init(self) -> None:
        if not os.path.exists(self.file_path):  # type: ignore
            self._write(self._pairs)
        else:
            self._pairs = self._read()

    def restore(self) -> None:
        self.clear()
        self.update(self.__default)
        self.init()

    def copy(self,
             file_path: Optional[os.PathLike[Any]] = None) -> AutoSaveDict:
        data = {}
        for key, val in self.items():
            data[key] = val
        return AutoSaveDict(file_path, **data)

    def pop(self, __key: Any) -> Any:  # type: ignore
        data = self._read()
        data.pop(__key)
        self._write(data)
        return super().pop(__key)

    def popitem(self) -> Tuple[Any, Any]:
        key = tuple(self._read().keys())[-1]
        value = self.pop(key)
        super().popitem()
        return (key, value)

    def clear(self) -> None:
        self._write({})
        super().clear()

    def update(self, __m: Mapping[Any, Any]) -> MutableMapping:  # type: ignore
        for k, v in __m.items():
            self[k] = v
        super().update(__m)
