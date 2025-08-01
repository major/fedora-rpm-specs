# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kamoso
Summary: Application for taking pictures and videos from a webcam
Version: 25.07.90
Release: 1%{?dist}

License: GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:     https://userbase.kde.org/Kamoso

Source0: https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Kirigami)

%if 0%{?tests}
BuildRequires: mesa-libGL
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif
BuildRequires: make

# currently not linked, needs qml resources
Requires: kf6-purpose%{?_isa}
Requires: kf6-kirigami%{?_isa}
Requires: qt6-qtdeclarative%{?_isa}

%description
Kamoso is an application to take pictures and videos out of your webcam.


%prep
%autosetup -p1


%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} -Wno-dev

%cmake_build


%install
%cmake_install

%find_lang kamoso --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kamoso.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kamoso.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest"
%endif


%files -f kamoso.lang
%doc AUTHORS
%license LICENSES/*
%{_kf6_metainfodir}/org.kde.kamoso.appdata.xml
%{_kf6_datadir}/applications/org.kde.kamoso.desktop
%{_kf6_bindir}/kamoso
%{_kf6_datadir}/icons/hicolor/*/apps/kamoso.*
%{_kf6_datadir}/icons/hicolor/*/actions/*
%{_kf6_datadir}/knotifications6/%{name}*


%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sun Jan 07 2024 Alessandro Astone <ales.astone@gmail.com> - 24.01.85-1
- 24.01.85

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 23 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- Update to 22.04.2

* Tue May 17 2022 Rex Dieter <rdieter@fedoraproject.org> 22.04.1-2
- https://src.fedoraproject.org/rpms/kamoso/pull-request/3

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Mon Apr 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Wed Feb 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Sat Jun 13 2020 Marie Loise Nolden <loise@kde.org> - 20.04.2-2
- 20.04.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.03.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.03.80-1
- 18.03.80 (part of kde-apps now)

* Fri Mar 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.2.2-6
- use %%_kf5_metainfodir, %%make_build, %%find_lang --with-html

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.2-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.2.2-1
- 3.2.2, update URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.2-1
- 3.2, update URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Rex Dieter <rdieter@fedoraproject.org> 3.1.0-3
- install/validate appdata, Requires: kf5-purpose

* Wed Dec 30 2015 Rex Dieter <rdieter@fedoraproject.org> 3.1.0-2
- BR: boost, udev

* Wed Dec 30 2015 Rex Dieter <rdieter@fedoraproject.org> 3.1.0-1
- kamoso-3.1

* Mon Sep 28 2015 Rex Dieter <rdieter@fedoraproject.org> 3.0-1
- kamoso-3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-23.20140902git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.2-22.20140902git
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 19 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-21.20140902git
- git snapshot, Webcam not working in kamoso (#1163698)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.2-19
- use the latest GStreamer 1 patch from git.reviewboard.kde.org

* Wed Jul 23 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.2-18
- build against GStreamer 1 and QtGStreamer 1 on F21+ (#1092655)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-16
- rebuild (kde-4.13)

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.0.2-15
- simplify -runtime dep, .spec cleanup

* Wed Nov  6 2013 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.2-14
- Requires: kde-runtime (#986964)

* Tue Nov  5 2013 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.2-13
- Requires: oxygen-icon-theme (#986964)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-11
- rebuild (libkipi)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-9
- fix build for older libkipi

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-8
- Kamoso has a missing icon for the pictures button (848079)
- pull in upstream fix for broken about dialog

* Wed Nov 21 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-7
- fix build against libkipi-4.9.50+ (kde#307147)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-5
- rename icons to avoid conflict with kdeplasma-addons' krunner plugin

* Tue May 29 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.2-4
- fix build against libkipi-4.8.80

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-2
- s/libkipi-devel/pkgconfig(libkipi)/

* Mon May 30 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0.2-1
- kamoso-2.0.2

* Sun May 29 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0-1
- kamoso-2.0-final
- License: GPLv2+

* Wed Feb 23 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0-0.4.beta1
- kamoso-2.0-beta1

* Tue Feb 22 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0-0.3.alpha2
- BR: libkipi-devel

* Fri Feb  4 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0-0.2.alpha2
- License: GPLv2+ and GPLv3+

* Thu Feb  3 2011 Alexey Kurov <nucleo@fedoraproject.org> - 2.0-0.1.alpha2
- Initial RPM release
