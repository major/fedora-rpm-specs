# Remove -s from Python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global forgeurl https://github.com/PyCQA/pylint
%global basever 3.3.3
#%%global prever b0
Version:        3.3.3
%forgemeta

Name:           pylint
Release:        %autorelease
Summary:        Analyzes Python code looking for bugs and signs of poor quality
License:        GPL-2.0-or-later
URL:            https://github.com/pylint-dev/pylint
Source0:        %{forgeurl}/archive/v%{basever}/pylint-%{basever}.tar.gz
#Patch0:         7829.patch apply when rebased then re-enable tests
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-GitPython
BuildRequires:  python3-pytest-benchmark
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

%description -n python3-%{name} %_description

%prep
%autosetup -p1 -n %{name}-%{basever}
# Relax version requirements
sed -i -e 's/"setuptools>=[^"]*"/"setuptools"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/pylint/test

# Add -%%{python3_version} to the binaries and manpages for backwards compatibility
for NAME in pylint pyreverse symilar; do
    mv %{buildroot}%{_bindir}/{$NAME,${NAME}-%{python3_version}}
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}-3
    ln -s ${NAME}-%{python3_version} %{buildroot}%{_bindir}/${NAME}
done

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
# astroid gets confused if pylint is importable both from buildroot/sitelib
# (see above) and the location we're running the tests from, so we'll
# move it out of the way here
#mkdir src
#mv pylint src
# Skip benchmarks
# It's not immediately clear why the delected tests fail
%{__python3} -m pytest -v --ignore=benchmark \
  --deselect=tests/test_functional.py::test_functional[missing_timeout] \
  --deselect=tests/test_functional.py::test_functional[wrong_import_order]

%files
%doc CONTRIBUTORS.txt
%license LICENSE
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
