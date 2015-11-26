title: "Setting up Pyenv and Pyenv-virtualenv"
tags: [pyenv, python, virtualenv]
date: 2015-11-25
lastmod: 2015-11-25
description: "Installing and using Pyenv and Pyenv-virtualenv"

I want to start using python 3 but can't give up python 2.7 because of other project that rely on it. I've had a few people mention that I should use pyenv for virtual environments in the past but I didn't feel like learning another tool. Now that I want to give python 3 a try I searched around on different ways to have more than one python version on a system and Pyenv was mentioned a lot. Since I've been in the mood to try to document how I install tools, utilize tools, pickup new techniques, etc.. I felt this is a great opportunity to both document and write a quick article about it. 

Enter: [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

#### Installation and setup on *mac with homebrew*

    brew update
    brew install pyenv
    brew install pyenv-virtualenv

Add these lines to the end of your .zshrc/.bashrc

    # set paths
    export PATH=/usr/local/bin:$PATH
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    # initialize pyenv on terminal load
    eval "$(pyenv init -)"
    # auto ativate virtualenv for pyenv
    if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

    # python virtual env
    if [ -z ${VIRTUAL_ENV+x} ]
    then
    VENV_NOTICE=""
    else
    VENV_NOTICE=" (py: $(basename "$VIRTUAL_ENV"))"
    fi

#### Pyenv Commands

List all python versions downloaded

    pyenv versions

View what python version is currently activated

    pyenv version

View what python version is set to global

    pyenv global

Install python version 2.7.8 or any python version

    pyenv install 2.7.8

Rehash after instaling any python version

    pyenv rehash

Set global python version

    pyenv global 2.7.8

Set python version for current directory
This also creates a .python-version in current directory

    pyenv local 3.5.0

#### Pyenv-virtualenv Commands

Create virtualenv with python version 2.7.8 and name the env project_name

    pyenv virtualenv 2.7.8 project_name
    pyenv virtualenv [pyenv-version] [virtualenv-name]

List virtualenvs already created, also shows py version for each env

    pyenv virtualenvs

Activate a virtualenv from one thats already made

    pyenv local venv_name

Deactivate a virtualenv

    pyenv deactivate

#### Pyenv and Pyenv-virtualenv Commands

Remove a Python version or virtualenv

    pyenv uninstall <virtualenv or python-version>

#### Notable  Links

https://godjango.com/96-django-and-python-3-how-to-setup-pyenv-for-multiple-pythons/

https://www.brianthicks.com/2015/04/10/pyenv-your-python-environment-automated/

http://fgimian.github.io/blog/2014/04/20/better-python-version-and-environment-management-with-pyenv/

http://blog.froehlichundfrei.de/2014/11/30/my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper.html

http://tbb.co/managing-python-on-os-x-with-pyenv/