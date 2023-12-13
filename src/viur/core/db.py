import importlib
from viur.core.config import conf

if conf.db_engine == "viur.datastore":
    from viur.datastore import *
else:
    globals().update(importlib.import_module(conf.db_engine).__dict__)

KeyClass = Key

__all__ = [KEY_SPECIAL_PROPERTY, DATASTORE_BASE_TYPES, SortOrder, Entity, Key, KeyClass, Put, Get, Delete, AllocateIDs,
           CollisionError, keyHelper, fixUnindexableProperties, GetOrInsert, Query, QueryDefinition, IsInTransaction,
           acquireTransactionSuccessMarker, RunInTransaction, config, startDataAccessLog, endDataAccessLog, Count,
           cache]
