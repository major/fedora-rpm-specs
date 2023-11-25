%global commit0 36f5625141cbb4e1707e0f4ed9ece0ce0c2c0cc9
%global shortcommit %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20231120.081305

Name:    pulseaudio-qt
Summary: Qt bindings for PulseAudio
Version: 1.3^%{gitdate}.%{shortcommit}
Release: 2%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/libraries/pulseaudio-qt
Source:  https://invent.kde.org/libraries/pulseaudio-qt/-/archive/%{commit0}/pulseaudio-qt-%{commit0}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5DBus)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package qt5-devel
Summary: Development files for %{name} (Qt5)
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Provides: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
%description qt5-devel
%{summary}.

%package qt5
Summary: Qt5 bindings for PulseAudio
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}
%description qt5
%{summary}.

%package qt6-devel
Summary: Development files for %{name} (Qt6)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.  

%package qt6
Summary: Qt6 bindings for PulseAudio
%description qt6
%{summary}.



%prep
%autosetup -n %{name}-%{commit0}

%build
mkdir %{name}_qt5
pushd %{name}_qt5
%cmake_kf5 -DQT_MAJOR_VERSION=5 -S../
%cmake_build
popd
mkdir %{name}_qt6
pushd %{name}_qt6
%cmake_kf6 -DQT_MAJOR_VERSION=6 -S../
%cmake_build
popd

%install
pushd %{name}_qt5
%cmake_install
popd
pushd %{name}_qt6
%cmake_install
popd
rm %{buildroot}%{_kf6_includedir}/pulseaudioqt_version.h
rm %{buildroot}%{_kf5_includedir}/pulseaudioqt_version.h

%files qt5
%license LICENSES/*.txt
%doc README.md
%{_kf5_libdir}/libKF5PulseAudioQt.so.4
%{_kf5_libdir}/libKF5PulseAudioQt.so.1.3.0

%files qt5-devel
%{_kf5_includedir}/KF5PulseAudioQt/
%{_kf5_libdir}/libKF5PulseAudioQt.so
%{_kf5_libdir}/cmake/KF5PulseAudioQt/
%{_kf5_libdir}/pkgconfig/KF5PulseAudioQt.pc

%files qt6
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.4
%{_kf6_libdir}/libKF6PulseAudioQt.so.1.3.0

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc

%changelog
* Tue Nov 21 2023 Steve Cossette <farchord@gmail.com> - 1.3^20231120.081305.36f5625-2
- Fixing bad requirements

* Tue Nov 21 2023 Steve Cossette <farchord@gmail.com> - 1.3^20231120.081305.36f5625-1
- Qt6 Build

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.3-1
- update to new version 1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2-4
- use new %%cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2-1
- first try

