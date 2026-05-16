%global srcname ns1-python

Name:           python-%{srcname}
Version:        0.27.4
Release:        %autorelease
Summary:        Python SDK for the NS1 DNS platform

License:        MIT
URL:            https://github.com/ns1/ns1-python
Source:         %{pypi_source ns1_python}

BuildArch:      noarch

%global _description %{expand:
This package provides a python SDK for accessing the NS1 DNS platform
and includes both a simple NS1 REST API wrapper as well as a higher level
interface for managing zones, records, data feeds, and more.
It supports synchronous and asynchronous transports.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     python%{python3_version}dist(requests)
Suggests:       python%{python3_version}dist(twisted)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n ns1_python-%{version} -p1
# Tests are not distributed on PyPI
sed -i -e '/setup_requires/,+3d' setup.py

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ns1

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
