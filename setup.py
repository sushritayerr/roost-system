from setuptools import find_packages, setup

install_requires = [
    "torch",
    ### data ###
    "pytz",             # time zone, 2021.1
    "ephem",            # 3.7.7.1
    "geopy",            # 2.1.0
    ### system ###
    'wsrlib',
    'detectron2',
    'imageio',          # saving gif, 2.9.0
    'scikit-learn',     # nearest neighbor search using ball tree for wind farm, 0.24.2
]

setup(
    name="roosts",
    version="0.1.0",
    description="The Pytorch repo implements a machine learning system for detecting and tracking "
                "communal bird roosts in weather surveillance radar data. ",
    packages=find_packages(),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6.0",
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
    ]
)
