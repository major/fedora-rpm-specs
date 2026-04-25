# Remove -s from Python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

%global forgeurl https://github.com/PyCQA/pylint
%global basever 4.0.5
#%%global prever b0
Version:        4.0.5
%forgemeta

Name:           pylint
Release:        %autorelease
Summary:        Analyzes Python code looking for bugs and signs of poor quality
License:        GPL-2.0-or-later
URL:            https://github.com/pylint-dev/pylint
Source0:        %{forgeurl}/archive/v%{basever}/pylint-%{basever}.tar.gz
#Patch0:         7829.patch apply when rebased then re-enable tests
Patch:          pep639.patch
# Astroid version dep bumps, backported to 4.0.5
# Upstream 83741dd1d6344924088e7a81652f35988fc364f2
Patch:          0001-Bump-astroid-to-4.0.3.patch
# Upstream 40817ce1a1b62a41486d81eff5b2db3bd9c23755
Patch:          0002-Bump-astroid-to-4.1.1-10843.patch
# Upstream e525835b22b36f95d209d73a16341b35846cf9db
Patch:          0003-Bump-astroid-from-4.1.1-to-4.1.2.patch
# Fix test failures with Python 3.15
# https://github.com/pylint-dev/pylint/issues/10982
Patch:          python315.patch
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-GitPython
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-typing-extensions
BuildRequires:  graphviz

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
# Skip benchmarks
# Deselect all tests failing with Python 3.14
%pytest -v --ignore=tests/benchmark \
  -n auto \
  --deselect=tests/test_functional.py::test_functional[missing_timeout] \
  --deselect=tests/test_functional.py::test_functional[wrong_import_order] \
  --deselect=tests/test_self.py::TestRunTC::test_do_not_import_files_from_local_directory[args0] \
  --deselect=tests/test_self.py::TestRunTC::test_do_not_import_files_from_local_directory[args1] \
  --deselect=tests/test_self.py::TestRunTC::test_progress_reporting

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
