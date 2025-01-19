%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

Name:    kuserfeedback
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 1.3.0
Release: 7%{?dist}

License: MIT
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-E0A3EB202F8E57528E13E72FD7574483BB57B18D.gpg

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Charts)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: bison
BuildRequires: flex

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  qt5-qtbase-private-devel
Requires:       qt5-qtcharts%{?_isa}

%description    console
Analytics and administration tool for UserFeedback servers.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf5 \
   -DENABLE_DOCS:BOOL=OFF \
   %{?with_kf6_compat:-DENABLE_CLI=OFF}

%cmake_build


%install
%cmake_install

%find_lang userfeedbackconsole5 --with-qt
%find_lang userfeedbackprovider5 --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop


%files -f userfeedbackprovider5.lang
%doc README.md
%license COPYING.LIB
%if %{without kf6_compat}
%{_bindir}/userfeedbackctl
%endif
%{_libdir}/libKUserFeedbackCore.so.1*
%{_libdir}/libKUserFeedbackWidgets.so.1*
%{_kf5_qmldir}/org/kde/userfeedback/
%{_kf5_datadir}/qlogging-categories5/org_kde_UserFeedback.categories


%files devel
%{_includedir}/KUserFeedback/
%{_libdir}/libKUserFeedbackCore.so
%{_libdir}/libKUserFeedbackWidgets.so
%{_kf5_libdir}/cmake/KUserFeedback/
%{_kf5_archdatadir}/mkspecs/modules/qt_KUserFeedback*.pri


%files console -f userfeedbackconsole5.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_kf5_metainfodir}/org.kde.kuserfeedback-console.appdata.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Alessandro Astone <ales.astone@gmail.com> - 1.3.0-5
- Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 18 2023 Alessandro Astone <ales.astone@gmail.com> - 1.3.0-2
- kf6 compatibility support

* Thu Nov 02 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.3.0-1
- version 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-7
- Bring back dependency on qt5-qtcharts

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-6
- Drop hardcoded Qt version requirement

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-4
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-3
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-2
- Rebuild (qt5)

* Fri Feb 04 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.2.0-1
- update to 1.2.0

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-11
- -console: uses qt5-qtcharts private api
- -devel: use cmake-style deps instead of hard-coding qt5-qtbase

* Thu Feb 03 2022 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-10
- backport crash fix recommended by upstream
- cleanup macros
- simplify %%files
- BR: bison flex (enables Survey targeting expressions support)
- drop BR: qt5-qtbase-private-devel (no private api use detected)
- drop non-autodetected runtime deps

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 21:50:41 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-6
- track Qt private api usage

* Tue Nov 24 13:19:14 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-5
- rebuild due to new Qt version

* Sun Sep 20 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-4
- one more rebuild

* Sat Sep 19 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-3
- rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-1
- first spec for version 1.0.0

