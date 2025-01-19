Name:    hotspot
Version: 1.5.1
Release: 3%{?dist}
Summary: The Linux perf GUI for performance analysis

License: GPL-2.0-or-later
URL:     https://github.com/KDAB/hotspot

Source0: https://github.com/KDAB/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-perfparser-v%{version}.tar.gz
Source2: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-PrefixTickLabels-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libelf)
BuildRequires:  elfutils-devel
BuildRequires:  rust-zstd-devel

Recommends:     binutils
Requires:       hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KDDockWidgets-qt6)
BuildRequires:  pkgconfig(qcustomplot-qt6)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  cmake(Qt6Svg)

Provides:       bundled(hotspot-perfparser)
Provides:       bundled(hotspot-PrefixTickLabels)

%description
A standalone GUI for performance data. Attempting to provide a UI like
KCachegrind around Linux perf.


%prep
%setup -q -n %{name} -a 1 -a 2
mv perfparser/* 3rdparty/perfparser/
mv PrefixTickLabels/* 3rdparty/PrefixTickLabels/

%build
%cmake_kf6 -DQT6_BUILD=TRUE
%cmake_build


%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.kdab.hotspot.desktop

%files
%license LICENSE.GPL.txt
%{_kf6_bindir}/hotspot
%{_kf6_datadir}/icons/hicolor/*/*/hotspot*
%{_libexecdir}/hotspot-perfparser
%{_kf6_datadir}/applications/com.kdab.hotspot.desktop
%{_kf6_metainfodir}/com.kdab.Hotspot.appdata.xml
%{_kf6_datadir}/knotifications6/hotspot.notifyrc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Steve Cossette <farchord@gmail.com> - 1.5.1-2
- Fix hicolor-icon-theme mistype mistake

* Mon Nov 18 2024 Steve Cossette <farchord@gmail.com> - 1.5.1-1
- Upgrade to 1.5.1 and switchover to Qt6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 17 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.4.1-3
- Rebuilt for new kddockwidgets

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.4.1-1
- Update to version 1.4.1
- Remove unneded patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Jan Grulich <jgrulich@redhat.com> - 1.3.0-1
- 1.3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Wed Mar 20 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-1
- 1.1.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Than Ngo <than@redhat.com> - 1.0.0-3
- enable build for s390x

* Thu Jul 13 2017 Than Ngo <than@redhat.com> - 1.0.0-2
- fix build issue on ppc64
- enable ppc64 build

* Tue Jul 11 2017 Jan Grulich <jgrulich@redhat.com> - 1.0.0-1
- Initial version
