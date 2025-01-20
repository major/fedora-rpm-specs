%global srcname flake8-class-newline

Name:           python-%{srcname}
Version:        1.6.0
Release:        5%{?dist}
Summary:        Flake8 extension to check for new lines after class definitions

License:        MIT
URL:            https://github.com/AlexanderVanEck/flake8-class-newline
Source0:        https://github.com/AlexanderVanEck/flake8-class-newline/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
PEP8 says we should surround every class method with a single blank line.
However flake8 is ambiguous about the first method having a blank line above
it. This plugin was made to enforce that it should.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flake8_class_newline


%check
%{py3_test_envvars} %{__python3} -m unittest -v


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Scott K Logan <logans@cottsay.net> - 1.6.0-4
- Switch from tox to directly invoking unittest

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Nov 22 2022 Scott K Logan <logans@cottsay.net> - 1.6.0-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 1.6.0-1
- Initial package (rhbz#2141868)
