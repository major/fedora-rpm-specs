Name:           python-dacite
Version:        1.9.2
Release:        %autorelease
Summary:        Simple creation of data classes from dictionaries

License:        MIT
URL:            https://github.com/konradhalas/dacite
Source:         %{url}/archive/v%{version}/dacite-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install):  --assert-license dacite

BuildArch:      noarch
BuildRequires:  python3-devel
# tests
BuildRequires:  python3-pytest


%global _description %{expand:
This module simplifies creation of data classes (PEP 557) from dictionaries.
}

%description %_description

%package -n     python3-dacite
Summary:        %{summary}

%description -n python3-dacite %_description


%prep -a
# v1.9.2 tag still has version="1.9.1" in setup.py
sed -i 's/version="1.9.1"/version="%{version}"/' setup.py

%check -a
%pytest --override-ini="addopts=" --ignore=tests/performance \
  --deselect tests/core/test_union.py::test_from_dict_with_union_and_wrong_data

%files -n python3-dacite -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
