from distutils.core import setup

setup(
  name = 'spmlab',         # How you named your package folder (MyLib)
  packages = ['spmlab'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Utility tools for reading, analyzing, and plotting scanning probe microscopy data.",   # Give a short description about your library
  author = 'Ben Campbell',                   # Type in your name
  author_email = 'bhc1010@pm.me',      # Type in your E-Mail
  url = 'https://github.com/hollenlab/spmlab',   # Provide either the link to your github or to your website
  keywords = ['stm', 'spym', 'sm4', 'scanning tunneling microscope', 'spm', 'microscopy'],   # Keywords that define your package best
  install_requires=[            
          'numpy',
          'matplotlib',
          'spym',
      ],
  classifiers=[
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.11',
  ],
)