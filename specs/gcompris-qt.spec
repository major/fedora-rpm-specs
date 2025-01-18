Name:           gcompris-qt
Version:        4.3
Release:        2%{?dist}
Summary:        Educational software suite for children aged 2 to 10

License:        AGPL-3.0-only
URL:            http://gcompris.net
Source0:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  openssl-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       qt5-qtmultimedia
Requires:       qt5-qtquickcontrols 
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtsvg
Requires:       qt5-qtimageformats
Requires:       qt5-qtcharts
Requires:       hicolor-icon-theme
Requires:       %{name}-activities = %{version}-%{release}

Obsoletes:      gcompris <= 15.10-16

%description
GCompris-Qt is an educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New
activities can be added, and an activity can implement its own game
scheme.

This version is a rewrite of GCompris using the QtQuick
technology.


%package activities
Summary:        Activity files for %{name}
License:        GPLv3 and MPLv2.0 and Public Domain and CC0 and CC-BY and CC-BY-SA and GFDL and OFL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description activities
This package contains the bundle of activities for %{name}.
More than 100 activities are available.


%prep
%autosetup


%build
# qml-box2d in not available in Fedora
%cmake_kf5 \
  -DQML_BOX2D_MODULE=disabled
%cmake_build


%install
%cmake_install

# Validate desktop file
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/org.kde.gcompris.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.gcompris.appdata.xml

%find_lang %{name} --all-name --with-qt --with-html


%files -f %{name}.lang
%{_kf5_bindir}/%{name}
%dir %{_kf5_datadir}/%{name}
%{_kf5_metainfodir}/org.kde.gcompris.appdata.xml
%{_kf5_datadir}/applications/org.kde.gcompris.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
%license LICENSES/AGPL-3.0-only.txt LICENSES/GPL-3.0-or-later.txt
%doc README 

%files activities
%{_kf5_datadir}/%{name}/rcc
%license LICENSES/AGPL-3.0-only.txt LICENSES/GPL-3.0-or-later.txt


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Andrea Musuruane <musuruan@gmail.com> - 4.3-1
- Updated to new upstream release

* Sat Sep 21 2024 Andrea Musuruane <musuruan@gmail.com> - 4.2-1
- Updated to new upstream release

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1-2
- convert license to SPDX

* Mon May 27 2024 Andrea Musuruane <musuruan@gmail.com> - 4.1-1
- Updated to new upstream release

* Sat Feb 24 2024 Andrea Musuruane <musuruan@gmail.com> - 4.0-1
- Updated to new upstream release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 10 2023 Andrea Musuruane <musuruan@gmail.com> - 3.3-1
- Updated to new upstream release

* Tue May 23 2023 Andrea Musuruane <musuruan@gmail.com> - 3.2-2
- Added missing qt5-qtimageformats dependency (BZ# 2209119)

* Sat Apr 01 2023 Andrea Musuruane <musuruan@gmail.com> - 3.2-1
- Updated to new upstream release

* Sun Jan 22 2023 Andrea Musuruane <musuruan@gmail.com> - 3.1-1
- Updated to new upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Andrea Musuruane <musuruan@gmail.com> - 2.4-1
- Updated to new upstream release

* Sun Feb 27 2022 Andrea Musuruane <musuruan@gmail.com> - 2.3-1
- Updated to new upstream release

* Fri Feb 25 2022 Andrea Musuruane <musuruan@gmail.com> - 2.2-1
- Updated to new upstream release

* Fri Jan 21 2022 Andrea Musuruane <musuruan@gmail.com> - 2.1-1
- Updated to new upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Andrea Musuruane <musuruan@gmail.com> - 2.0-1
- Updated to new upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Andrea Musuruane <musuruan@gmail.com> - 1.1-1
- Updated to new upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 19:10:16 CET 2020 Andrea Musuruane <musuruan@gmail.com> - 1.0-1
- Updated to new upstream release

* Thu Aug 06 2020 Andrea Musuruane <musuruan@gmail.com> - 0.97-6
- Fixed FTBFS for F33 (BZ #1863600)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Andrea Musuruane <musuruan@gmail.com> - 0.97-3
- Added missing qt5-qtsvg dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Andrea Musuruane <musuruan@gmail.com> - 0.97-1
- Updated to new upstream release

* Sat Aug 17 2019 Andrea Musuruane <musuruan@gmail.com> - 0.96-3
- Obsoletes gcompris package (BZ #1740801)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Andrea Musuruane <musuruan@gmail.com> - 0.96-1
- Updated to new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Andrea Musuruane <musuruan@gmail.com> - 0.95-1
- Updated to new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Andrea Musuruane <musuruan@gmail.com> - 0.91-1
- Updated to new upstream release

* Sun Mar 18 2018 Andrea Musuruane <musuruan@gmail.com> - 0.90-1
- Updated to new upstream release
- Made a separate package for activities
- Added gcc-c++ dependency
- Added kf5-kdoctools-devel to BR to enable the documentation

* Sun Feb 04 2018 Andrea Musuruane <musuruan@gmail.com> - 0.81-2
- Removed obsolete scriptlets

* Sun Dec 17 2017 Andrea Musuruane <musuruan@gmail.com> - 0.81-1
- First release

