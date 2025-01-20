%global srcname colcon-meson

Name:           python-%{srcname}
Version:        0.4.5
Release:        2%{?dist}
Summary:        Extension for colcon to support Meson packages

License:        Apache-2.0
URL:            https://github.com/colcon/colcon-meson
Source0:        https://github.com/colcon/colcon-meson/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A colcon extension for building Meson packages.}

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
%pyproject_save_files -l colcon_meson


%check
%pytest -k 'not linter' test
%pyproject_check_import colcon_meson


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Scott K Logan <logans@cottsay.net> - 0.4.5-1
- Update to 0.4.5

* Sat Apr 06 2024 Scott K Logan <logans@cottsay.net> - 0.4.3-1
- Initial package (rhbz#2117349)
