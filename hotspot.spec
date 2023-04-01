%undefine __cmake_in_source_build

Name:    hotspot
Version: 1.4.1
Release: 1%{?dist}
Summary: The Linux perf GUI for performance analysis

License: GPLv2+
URL:     https://github.com/KDAB/hotspot

Source0: https://github.com/KDAB/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kitemmodels-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  kddockwidgets-devel

BuildRequires:  qcustomplot-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  elfutils-devel
BuildRequires:  elfutils-debuginfod-client-devel

Recommends:     rust-cpp_demangle


%description
A standalone GUI for performance data. Attempting to provide a UI like
KCachegrind around Linux perf.


%prep
%autosetup -n %{name}-v%{version} -p1


%build
%{cmake_kf5}

%cmake_build


%install
%cmake_install

%files
%license LICENSE.GPL.txt
%{_kf5_bindir}/hotspot
%{_kf5_datadir}/icons/hicolor/*/*/hotspot*
%{_libexecdir}/hotspot-perfparser
%{_libexecdir}/elevate_perf_privileges.sh
%{_kf5_libexecdir}/kauth/hotspot-auth-helper
%{_kf5_datadir}/applications/com.kdab.hotspot.desktop
%{_kf5_datadir}/dbus-1/system-services/com.kdab.hotspot.perf.service
%{_kf5_datadir}/dbus-1/system.d/com.kdab.hotspot.perf.conf
%{_kf5_datadir}/knotifications5/hotspot.notifyrc
%{_kf5_metainfodir}/com.kdab.Hotspot.appdata.xml
%{_kf5_datadir}/polkit-1/actions/com.kdab.hotspot.perf.policy


%changelog
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
