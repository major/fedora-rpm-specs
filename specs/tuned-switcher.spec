Name: tuned-switcher
Version: 0.7.2
Release: 5%{?dist}

# Main code - GPL-3.0-or-later.
# Icon - Apache-2.0.
License: GPL-3.0-or-later AND Apache-2.0
Summary: Simple utility to manipulate the Tuned service
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: pandoc

Requires: hicolor-icon-theme
Requires: tuned

%description
Tuned Switcher is a simple utility for managing performance profiles using
the Tuned service.

Tuned is a daemon for monitoring and adaptive tuning of system devices.
In order to use this program, a daemon must be installed on your system.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc docs/*
%license COPYING licenses/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_metainfodir}/*.metainfo.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.2-1
- Updated to version 0.7.2.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.1-1
- Updated to version 0.7.1.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Updated to version 0.7.0.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Fri Aug 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Thu Jul 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Mon Mar 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Thu Mar 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Initial SPEC release.
