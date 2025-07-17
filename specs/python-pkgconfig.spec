%global srcname pkgconfig

Name:           python-%{srcname}
Version:        1.5.5
Release:        %autorelease
Summary:        Python interface to the pkg-config command line tool

License:        MIT
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source}

BuildArch:      noarch

%description
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 2.6+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%package -n python3-%{srcname}
Summary:        Python3 interface to the pkg-config command line tool
Requires:       %{_bindir}/pkg-config

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname}
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 2.6+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
