%global srcname enzyme

Name:           python-%{srcname}
Version:        0.5.2
Release:        4%{?dist}
Summary:        Python module to parse video metadata
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Diaoul/enzyme
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Tests disabled
#BuildRequires:  PyYAML
#BuildRequires:  python3-PyYAML
#BuildRequires:  python2-requests
#BuildRequires:  python3-requests

%global _description %{expand:
Enzyme is a Python module to parse video metadata.}

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc

%description -n python3-%{srcname} %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Tests disabled because they try to download files
#%%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%files doc
%doc README.md docs/index.rst docs/api
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

%autochangelog
