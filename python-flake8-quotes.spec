%global srcname flake8-quotes

Name:           python-%{srcname}
Version:        3.3.2
Release:        2%{?dist}
Summary:        Flake8 extension for checking quotes in python

License:        MIT
URL:            https://github.com/zheller/flake8-quotes
Source0:        https://github.com/zheller/flake8-quotes/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
This package adds flake8 warnings with the prefix Q0:

- Q000: Remove bad quotes
- Q001: Remove bad quotes from multiline string
- Q002: Remove bad quotes from docstring
- Q003: Change outer quotes to avoid escaping inner quotes}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest


%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flake8_quotes


%check
%pytest test


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Scott K Logan <logans@cottsay.net> - 3.3.2-1
- Update to 3.3.2

* Tue Nov 15 2022 Scott K Logan <logans@cottsay.net> - 3.3.1-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 3.3.1-1
- Initial package (rhbz#2141871)
