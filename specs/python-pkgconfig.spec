%global srcname pkgconfig

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        Python interface to the pkg-config command line tool

License:        MIT
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source}

BuildArch:      noarch

%description
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 3.9+.

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
tool and supports Python 3.9+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%prep
%autosetup -n %{srcname}-%{version}
%if 0%{?rhel}
# RHEL does not have poetry-core.
# By renaming the [build-system] section we fallback to setuptools (default per PEP 517).
echo -e "from setuptools import setup\n\nsetup()" > setup.py
echo -e "[metadata]\nname=%{srcname}\nversion=%{version}" > setup.cfg
sed -i 's/\[build-system\]/[ignore-this]/' pyproject.toml
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
