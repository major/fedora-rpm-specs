Name:           python-pysubnettree
Version:        0.38.1
Release:        %autorelease
Summary:        Python Module for CIDR Lookups

# BSD-4-Clause is coming from include/patricia.h
License:        BSD-3-Clause-LBNL and BSD-4-Clause
URL:            https://github.com/zeek/pysubnettree
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# pytest plugin to collect and run *.test files without btest
Source1:        conftest.py

Provides:       pysubnettree = %{version}-%{release}
Obsoletes:      pysubnettree < 0.35-16

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  python3-pytest


%global _description %{expand:
The PySubnetTree package provides a Python data structure SubnetTree which maps
subnets given in CIDR notation (incl. corresponding IPv6 versions) to Python
objects. Lookups are performed by longest-prefix matching.}

%description %{_description}


%package -n python3-pysubnettree
Summary:        %{summary}


%description -n python3-pysubnettree %{_description}


%prep
%autosetup -n pysubnettree-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l SubnetTree _SubnetTree


%check
%pyproject_check_import
cp %{SOURCE1} testing/conftest.py
cd testing
PYTHONPATH="%{buildroot}%{python3_sitearch}:$PWD/Scripts" pytest pysubnettree/


%files -n python3-pysubnettree -f %{pyproject_files}
%doc CHANGES README


%changelog
%autochangelog
