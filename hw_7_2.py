""" Sys. info
The results are displayed in "hw_7_2.py"
"""
import logging
import platform


logging.basicConfig(level=logging.DEBUG,
                    filename="hw_7_2.log",
                    filemode='w')

logging.info(f'Version: {platform.python_version()},\nVersion tuple: {platform.python_version_tuple()},\n'
             f'Compiler: {platform.python_compiler()},\nBuild: {platform.python_build()},\n'
             f'System: {platform.system()},\nNode: {platform.node()},\nRelease: {platform.release()},\n'
             f'Version: {platform.version()},\nMachine: {platform.machine()},\nProcessor: {platform.processor()}'
             f'Interpreter: {platform.architecture()}')

