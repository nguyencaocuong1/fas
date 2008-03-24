# Dummy Plugin for FAS2

from setuptools import setup, find_packages
from turbogears.finddata import find_package_data, standard_exclude, \
        standard_exclude_directories
import os, glob

excludeFiles = ['*.cfg.in']
excludeFiles.extend(standard_exclude)
excludeDataDirs = ['']
excludeDataDirs.extend(standard_exclude_directories)

package_data = find_package_data(where='./', package='dummy_plugin', exclude=excludeFiles, exclude_directories=excludeDataDirs,)
data_files = [('__init__.py', filter(os.path.isfile, glob.glob('__init__.py'))),
              ('templates', filter(os.path.isfile, glob.glob('templates/*html')))
]
setup(
    name = "dummy_plugin",
    version = "0.1",
    packages = find_packages(),

    data_files = data_files,
    package_data = package_data,
        
    author = "Mike McGrath",
    author_email = "mmcgrath@redhat.com",
    description = "Sample plugin for FAS2",
    entry_points = {
            'fas.plugins': (
                'Dummy = dummy_plugin:DummyPlugin',
            )
    }
)
