# Bconds are needed for Python bootstrap
%bcond docs %{undefined rhel}
%bcond tests 1

# Install doc subpackage files into the main package doc directory
%global _docdir_fmt %{name}

Name:		python-zope-interface
Version:	7.2
Release:	%autorelease
Summary:	Zope 3 Interface Infrastructure
License:	ZPL-2.1
URL:		https://pypi.io/project/zope.interface
Source0:	%{pypi_source zope.interface}

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%package -n python3-zope-interface
Summary:	Zope 3 Interface Infrastructure

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel

%description -n python3-zope-interface
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%if %{with docs}
%package doc
Summary:        Documentation for zope.interface
BuildArch:      noarch
BuildRequires:  python3-docs

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n zope.interface-%{version} -p1

# Remove version limit from setuptools
sed -i '/setuptools/s/<.*"/"/' pyproject.toml

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

# Do not run coverage tests in Fedora
sed -i "/coverage/d" setup.py

%generate_buildrequires
%pyproject_buildrequires %{?with_docs: -x docs} %{?with_tests: -x test}

%build
%pyproject_wheel

%if %{with docs}
# build the sphinx documents
PYTHONPATH=$PWD/src make -C docs html
rm -f docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files -l zope

%check
%py3_check_import zope.interface
%if %{with tests}
# We have to run tests installed together with the package
# https://github.com/zopefoundation/zope.interface/issues/196
pushd %{buildroot}%{python3_sitearch}
PURE_PYTHON=1 python3 -m unittest discover -vv -s zope/interface -t .
popd
%endif

%files -n python3-zope-interface -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license COPYRIGHT.txt
%exclude %{python3_sitearch}/zope/interface/tests/
%exclude %{python3_sitearch}/zope/interface/common/tests/
# C files don't need to be packaged
%exclude %{python3_sitearch}/zope/interface/*.c
%{python3_sitearch}/zope.interface-*-nspkg.pth

%if %{with docs}
%files doc
%doc docs/_build/html/
%endif

%changelog
%autochangelog
