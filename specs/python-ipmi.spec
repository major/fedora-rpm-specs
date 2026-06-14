%global pypi_name python-ipmi
%global srcname ipmi

Name:           python-%{srcname}
Version:        0.5.8
Release:        %autorelease
Summary:        Pure python IPMI library
License:        LGPL-2.1-or-later
URL:            https://github.com/kontron/python-ipmi
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pytest)

%description
Pure Python IPMI Library.

%package -n     python3-%{srcname}
Summary:        %{summary}
Requires:       python3dist(pyyaml)

%description -n python3-%{srcname}
Pure Python IPMI Library.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
echo "__version__ = '%{version}'" > pyipmi/version.py

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'
sed -i 's/from mock import/from unittest.mock import/g' tests/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyipmi

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst
%{_bindir}/ipmitool.py

%changelog
%autochangelog
