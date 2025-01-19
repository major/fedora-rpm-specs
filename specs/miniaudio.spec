%global debug_package %{nil}

Name:           miniaudio
Version:        0.11.21
Release:        3%{?dist}
Summary:        Audio playback and capture library

License:        MIT-0
URL:            https://miniaud.io/
Source0:        https://github.com/mackron/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%package devel
Summary: %summary
Provides:       miniaudio-static = %{version}-%{release}
BuildArch:      noarch

%description
%summary

%description devel
%summary

%prep
%autosetup


%build


%check
# The package does include tests but they are interactive so we cannot use them


%install
mkdir -p %{buildroot}%{_includedir}
install -p %{name}.h %{buildroot}%{_includedir}/


%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 13 2024 Christian Birk <mail@birkc.de> - 0.11.21-1
- Update to 0.11.21

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Jonathan <jonathan@knownhost.com> - 0.11.14
- Initial package build
