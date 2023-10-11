#!/usr/bin/python3
"""
creating a shared package package 
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
