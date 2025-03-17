%global modname zope.schema

Summary: Zope 3 schemas
Name: python-zope-schema
Version: 7.0.1
Release: %autorelease
License: ZPL-2.1
BuildArch: noarch
URL: http://pypi.python.org/pypi/zope.schema
Source0: %{pypi_source %{modname}}

# Compatibility with Sphinx 8
# from https://github.com/zopefoundation/zope.schema/commit/c0be2d
# Unrelated files removed
Patch: sphinx8.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package is a zope.interface extension for defining data schemas.

%package -n python3-zope-schema
Summary:        Zope 3 schemas
%{?python_provide:%python_provide python3-zope-schema}

%description -n python3-zope-schema
This package is a zope.interface extension for defining data schemas.

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# build Sphinx documents
PYTHONPATH="src" sphinx-build-%{python3_version} -b html docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -fr html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files -l zope

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} zope-testrunner --test-path=src

%files -n python3-zope-schema -f %{pyproject_files}
%doc CHANGES.rst COPYRIGHT.txt README.rst
%doc html/
%exclude %dir %{python3_sitelib}/zope
%exclude %{python3_sitelib}/zope/schema/tests/
%{python3_sitelib}/%{modname}-*-nspkg.pth


%changelog
%autochangelog
