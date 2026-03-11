Name:           python-types-setuptools
Version:        82.0.0.20260210
Release:        %autorelease
Summary:        Typing stubs for setuptools

License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         %{pypi_source types_setuptools}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a PEP 561 type stub package for the boto package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
boto. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/boto. All fixes for types
and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

%description %_description

%package -n     python3-types-setuptools
Summary:        %{summary}

%description -n python3-types-setuptools %_description

%prep
%autosetup -p1 -n types_setuptools-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%py3_check_import setuptools-stubs

%files -n python3-types-setuptools
%{python3_sitelib}/setuptools-stubs
%{python3_sitelib}/distutils-stubs
%{python3_sitelib}/types_setuptools-%{version}.dist-info/

%changelog
%autochangelog
