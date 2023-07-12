%global forgeurl https://github.com/PyCQA/pylint
Version:        2.17.4
%forgemeta

Name:           pylint
Release:        %autorelease
Summary:        Analyzes Python code looking for bugs and signs of poor quality
License:        GPL-2.0-or-later
URL:            https://www.pylint.org/
Source0:        %{forgesource}
#Patch0:         7829.patch apply when rebased then re-enable tests
Patch1:         unpin-astroid.patch
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-py
# For tests
BuildRequires:  python3-astroid >= 2.12.1
BuildRequires:  python3-dill
BuildRequires:  python3-GitPython
BuildRequires:  python3-isort
BuildRequires:  python3-mccabe
BuildRequires:  python3-platformdirs
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-tomlkit
BuildRequires:  python3-typing-extensions

# For the main pylint package
Requires:       python3-%{name} = %{version}-%{release}

%global _description %{expand:
Pylint is a Python source code analyzer which looks for programming errors,
helps enforcing a coding standard and sniffs for some code smells (as defined in
Martin Fowler's Refactoring book). Pylint can be seen as another PyChecker since
nearly all tests you can do with PyChecker can also be done with Pylint.
However, Pylint offers some more features, like checking length of lines of
code, checking if variable names are well-formed according to your coding
standard, or checking if declared interfaces are truly implemented, and much
more.

Additionally, it is possible to write plugins to add your own checks.}

%description %_description

%package -n python3-%{name}
Summary:        %{summary}
Requires:       python3-setuptools
Requires:       python3-astroid >= 2.12.1
Requires:       python3-dill
Requires:       python3-mccabe
Requires:       python3-platformdirs
Requires:       python3-isort
Requires:       python3-tomlkit
Obsoletes:      python3-pylint-gui < 1.7
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/pylint/test

# Add -%%{python3_version} to the binaries and manpages for backwards compatibility
for NAME in epylint pylint pyreverse symilar; do
    mv %{buildroot}%{_bindir}/{$NAME,${NAME}-%{python3_version}}
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}-3
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}
done

#%%check
#export PYTHONPATH=%{buildroot}%{python3_sitelib}
# astroid gets confused if pylint is importable both from buildroot/sitelib
# (see above) and the location we're running the tests from, so we'll
# move it out of the way here
#mkdir src
#mv pylint src
# Skip benchmarks
#%%{__python3} -m pytest -v -k "not benchmark"

%files
%doc CONTRIBUTORS.txt
%license LICENSE
%{_bindir}/epylint
%{_bindir}/pylint
%{_bindir}/pylint-config
%{_bindir}/pyreverse
%{_bindir}/symilar

%files -n python3-%{name}
%license LICENSE
%{python3_sitelib}/pylint*
# backwards compatible versioned executables and manpages:
%{_bindir}/*-3
%{_bindir}/*-%{python3_version}

%changelog
%autochangelog
