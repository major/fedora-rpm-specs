%define __cmake_in_source_build 1

Name:    lxqt-qtplugin
Summary: Qt plugin framework for LXQt Desktop Suite
Version: 1.2.0
Release: 3%{?dist}
License: LGPLv2+
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(lxqt) >= 1.2.0
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: qt5-qtbase-devel
BuildRequires: libfm-qt-devel
BuildRequires: libexif-devel
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# lxqt-qtplugin uses gui-private
BuildRequires:  qt5-qtbase-private-devel

%description
%{summary}.

%prep
%setup -q

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..

%make_build -C %{_vpath_builddir}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_vpath_builddir}


%files
%{_libdir}/qt5/plugins/platformthemes/libqtlxqt.so

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 1.2.0-1
- Update version to 1.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- new version

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-5
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-4
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-3
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Zamir SUN <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-4
- Fix FTBFS
- Fixes RHBZ#1987698

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.15.0-5
- drop hard-coded Qt5 runtime dependency

* Mon Nov 23 07:53:53 CET 2020 Jan Grulich <jgrulich@redhat.com> - 0.15.0-4
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.15.0-3
- rebuild (qt5)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.14.0-9
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.0-7
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.0-6
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.0-4
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.14.0-3
- rebuild (qt5), use %%make_build

* Mon Mar 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.14.0-2
- rebuild (qt5)

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.13.0-3
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.13.0-2
- rebuild (qt5)

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.1-13
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.1-12
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0.11.1-11
- rebuild (qt5)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 0.11.1-9
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.1-8
- rebuild (qt5)

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.1-7
- rebuild (qt5)

* Sun Aug 13 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-6
- use versioned dependency for Qt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- rebuilt

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Sun Jul 17 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-6
- No need privates after Qt 5.7.0

* Thu Jun 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-5
- add Qt5 versioned dep

* Thu Apr 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10.0-4
- Requires: lxqt-common (#1330150)
- drop exlicit BR: cmake (cmake dep pulled in via liblxqt and use of %%cmake_lxqt)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Upstream tarball updated with latest fixes

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Added missing updates in the main upstream tarball

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Unify naming as discussed on Fedora IRC

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Update for review on https://bugzilla.redhat.com/show_bug.cgi?id=1158996

* Thu Oct 30 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Rebuild on cooper

* Thu Oct 30 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Added upstream xdg patch. Thanks to Florian Hubbold from mageia

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
