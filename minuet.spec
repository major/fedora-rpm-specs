Name:           minuet
Version:        22.08.3
Release:        1%{?dist}
Summary:        A KDE Software for Music Education
#OFL license for bundled Bravura.otf font
#and BSD license for cmake/FindFluidSynth.cmake
License:        GPLv2+ and OFL
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= 5.15.0
BuildRequires:  kf5-filesystem
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui) >= 5.7.0
BuildRequires:  cmake(Qt5Qml) >= 5.7.0
BuildRequires:  cmake(Qt5Quick) >= 5.7.0
BuildRequires:  cmake(Qt5QuickControls2) >= 5.7.0
BuildRequires:  cmake(Qt5Svg) >= 5.7.0
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  libappstream-glib
# Runtime requirement
Requires:       qt5-qtquickcontrols2
Requires:       hicolor-icon-theme
Requires:       %{name}-data

Provides:       bundled(font(bravura))

%description
Application for Music Education.

Minuet aims at supporting students and teachers in many aspects
of music education, such as ear training, first-sight reading,
solfa, scales, rhythm, harmony, and improvisation.
Minuet makes extensive use of MIDI capabilities to provide a
full-fledged set of features regarding volume, tempo, and pitch
changes, which makes Minuet a valuable tool for both novice and
experienced musicians.

%package devel
Summary:        Minuet: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for Minuet.

%package data
Summary:        Minuet: Data files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
Data files for Minuet.

%prep
%autosetup -p1
chmod -x src/app/org.kde.%{name}.desktop

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%doc README*
%license COPYING*
%{_datadir}/applications/org.kde.%name.desktop
%{_kf5_metainfodir}/org.kde.%name.appdata.xml
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_libdir}/libminuetinterfaces.so.*
%{_qt5_plugindir}/%{name}

%files devel
%doc README*
%license COPYING*
%{_includedir}/%{name}
%{_kf5_libdir}/libminuetinterfaces.so

%files data
%{_kf5_datadir}/%{name}


%changelog
* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Sun Aug 21 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.08.0-1
- Update to 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Tue Apr 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.0-1
- Update to 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.2-1
- Update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.1-1
- Update to 21.12.1

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.0-1
- Update to 21.12.0

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.1-1
- Update to 21.08.1

* Mon Aug 23 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.0-1
- Update to 21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.3-1
- Update to 21.04.3

* Wed Jun 16 2021 Vasiliy Glazov <vascom2@gmail.com> - 21.04.2-2
- fluidsynth so bump

* Fri Jun 11 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.2-1
- Update to 21.04.2

* Wed May 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.1-1
- Update to 21.04.1

* Thu Apr 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.0-1
- Update to 21.04.0

* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.3-1
- Update to 20.12.3

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.3-1
- Update to 20.04.3

* Sat Jun 13 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.2-1
- Update to 20.04.2

* Thu May 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.1-1
- Update to 20.04.1

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 19.12.1-3
- Rebuild against fluidsynth2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 19.12.1-1
- Update to 19.12.1

* Thu Nov 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.08.2-1
- Update to 19.08.2
- Enable LTO

* Fri Sep 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.08.1-1
- Update to 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-2
- Added gcc-c++ to BR
- Data in separate subpackage
- Correct licensing

* Mon May 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-1
- First release for fedora
