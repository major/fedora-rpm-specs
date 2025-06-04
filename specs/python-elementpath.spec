%global _without_tests 1
%global pypi_name elementpath
Name:           python-%{pypi_name}
Version:        4.8.0
Release:        %autorelease
Summary:        XPath 1.0/2.0 parsers and selectors for ElementTree and lxml

License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source0:        %{url}/archive/v%{version}/elementpath-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

# Circular test dependency on xmlschema and self
%bcond_without tests
%if %{with tests}
BuildRequires:  glibc-langpack-en
%endif

%global _description %{expand:
The proposal of this package is to provide XPath 1.0, 2.0 and 3.0 selectors for
Python's ElementTree XML data structures, both for the standard ElementTree
library and for the lxml.etree library.

For lxml.etree this package can be useful for providing XPath 2.0 selectors,
because lxml.etree already has it's own implementation of XPath 1.0.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}  %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove an upstream workaround for the mypy tests
# https://github.com/sissaschool/elementpath/commit/3431f6d907bda73512edbe1d68507f675b234384
# Upstream has been notified: https://github.com/sissaschool/elementpath/issues/64#issuecomment-1696519082
sed -i '/lxml-stubs/d' tox.ini

# Unset environment variable which enables a test requiring a network connection
sed -i '/TEST_UNICODE_INSTALLATION/d' tox.ini

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
# The C.utf-8 locale fails with some straße related tests
# We could use a German locale, but English works fine
export LANG=en_US.utf-8
%tox
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
%autochangelog
