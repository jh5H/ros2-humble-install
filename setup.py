from setuptools import find_packages, setup

package_name = 'thread'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='per',
    maintainer_email='per@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'thread_test1 = thread.thread_test1:main',
            'thread_test2 = thread.thread_test2:main',
            'thread_test3 = thread.thread_test3:main',
        ],
    },
)
