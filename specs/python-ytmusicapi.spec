%global srcname ytmusicapi

Name:           python-%{srcname}
Version:        1.9.0
Release:        2%{?dist}
License:        MIT
Summary:        Unofficial API for YouTube Music
Url:            https://github.com/sigma67/%{srcname}
Source:         %{pypi_source}
#Patch0:         001-setuptools-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
ytmusicapi is a Python 3 library to send requests to the YouTube Music API. 
It emulates YouTube Music web client requests using the userâ€™s 
cookie data for authentication.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r
 
%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CONTRIBUTING.rst PKG-INFO
%{_bindir}/ytmusicapi


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Steve Cossette <farchord@gmail.com> - 1.9.0-1
- 1.9.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.24.1-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.24.1-2
- build fix for pyproject.toml
- Remove old source files

* Sat Dec 10 2022 Justin Zobel <justin@1707.io> - 0.24.1-1
- v0.24.1

* Thu Aug 25 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.22.0-1
- v0.22.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.20.0-2
- Rebuilt for Python 3.11

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.20.0-1
- Initial version of package
