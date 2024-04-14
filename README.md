py-reimplementations
====================

*Description*
-------------
- Library consisting of various package dependencies and reimplementations of various essential functions in a single library/framework for various programming languages
    + This is for Python, I might be making for other languages if these are useful
- Initially planned to be called 'py-essentials'
    + Changed because this is alot more of a nice reimplementation ground than a all-encompassing essential framework/library package

## Quick setup
### Dependencies
+ python
+ python-pip
+ python-venv
- Python Packages

### Pre-Requisites
- Create Python Virtual Environment
    - General Virtual Environment
        ```bash
        python3 -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environnent
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\bin\activate
            ```

- Install package
    - Install locally as development mode
        - Clone repository
            ```bash
            git clone https://github.com/Thanatisia/py-essentials
            ```
        - Change directory into repository
            ```bash
            cd py-essentials
            ```
        - Install python dependencies in requirements file
            ```bash
            python -m pip install -Ur requirements.txt
            ```
        - Install package
            ```bash
            python -m pip install .
            ```
    - Install as a git package/repository
        ```bash
        python -m pip install git+https://github.com/Thanatisia/py-essentials
        ```

## Documentationd

### Project Layout
- root/
    - src/
        - essentials/ : Package name
            - mathematics/ : Submodule containing Mathematics formula reimplementations (If is even, odd, prime etc etc)
                + calculus.py : Logarithms, Integration, Integrals
                + geometry.py : For Geometrical mathematic formulas
                + trigonometry.py : For math formulas regarding angles and relation
            - sciences/ : Science submodule containing Scientific formula reimplementations (Gravity etc)
                - physics/
                - chemistry/ : 
                - biology/ :
                - computer/ : Submodule for Computer Science-based formulas
                    - cryptography.py : Cryptographic formulas and algorithms
            - ...

## Resources

## References

## Remarks

