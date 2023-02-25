%global srcname pynetbox

Name:           python-%{srcname}
Version:        7.0.1
Release:        %autorelease
Summary:        Python API client library for Netbox

License:        ASL 2.0
URL:            https://github.com/netbox-community/pynetbox
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pytest)
BuildRequires:  (python3dist(requests) >= 2.20 with python3dist(requests) < 3)
BuildRequires:  python3dist(packaging)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -vv tests/test_*.py tests/unit

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
%autochangelog
