%define __cmake_in_source_build 1

Name: libfm-qt
Version: 1.3.0
Release: 1%{?dist}
Summary: Companion library for PCManFM
License: GPLv2+
URL: https://lxqt-project.org
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: lxqt-build-tools >= 0.12.0
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qt5-qtbase-private-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(lxqt) >= 1.2.0
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: pkgconfig(libmenu-cache) >= 0.3.0
BuildRequires: libexif-devel
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif
BuildRequires: menu-cache-devel
Obsoletes: libfm-qt5 <  0.11.0
Obsoletes: libfm-qt4 <= 0.9.0
Obsoletes: libfm-qt-common <= 0.9.0
Provides: libfm-qt5 = %{version}

%description
Libfm-Qt is a companion library providing components to build
desktop file managers.

%package devel
Summary: Development files for libfm-qt
Requires: libfm-qt%{?_isa} = %{version}-%{release}
Requires: menu-cache-devel
Obsoletes: libfm-qt-devel <= 0.9.0
Obsoletes: libfm-qt5-devel < 0.11.0
Obsoletes: libfm-qt4-devel <= 0.9.0
Provides: libfm-qt5-devel = %{version}

%description devel
libfm-qt-devel package contains libraries and header files for
developing applications that use libfm-qt.


%package l10n
BuildArch:      noarch
Summary:        Translations for libfm-qt
Requires:       libfm-qt
%description l10n
This package provides translations for the libfm-qt package.

%prep
%setup -q

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..

make %{?_smp_mflags} -C %{_vpath_builddir}
%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_vpath_builddir}

# We need fix this upstream
find %{buildroot} -size 0 -delete

# The following line is an ugly workaround for upstream issue
# https://github.com/lxqt/libfm-qt/issues/350
sed -i "s/Requires:.*/Requires: Qt5Widgets Qt5X11Extras/" %{buildroot}/%{_libdir}/pkgconfig/libfm-qt.pc

%find_lang libfm-qt --with-qt

%ldconfig_scriptlets

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_libdir}/libfm-qt.so.13
%{_libdir}/libfm-qt.so.13.0.0
%{_datadir}/libfm-qt

%files devel
%{_libdir}/libfm-qt.so
%{_libdir}/pkgconfig/libfm-qt.pc
%{_includedir}/libfm-qt/
%dir %{_datadir}/cmake/fm-qt
%{_datadir}/cmake/fm-qt/*
%{_datadir}/libfm-qt/archivers.list
%{_datadir}/libfm-qt/terminals.list
%{_datadir}/mime/packages/libfm-qt-mimetypes.xml

%files l10n -f libfm-qt.lang
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%dir %{_datadir}/libfm-qt/translations

%changelog
* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 1.3.0-1
- Update version to 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 1.2.0-1
- Update version to 1.2.0

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 1.1.0-4
- Drop hardcoded Qt version requirement

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jan Grulich <jgrulich@redhat.com> - 1.1.0-2
- Rebuild (qt5)

* Fri Jul 15 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-5
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-4
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.0.0-3
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-3
- Fix FTBFS
- Fixes RHBZ#1987646

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Mon Nov 23 07:53:26 CET 2020 Jan Grulich <jgrulich@redhat.com> - 0.15.0-4
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.15.0-3
- rebuild (qt5)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.14.1-10
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.1-8
- rebuild (qt5)

* Sun Oct 06 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-7
- Move menu-cache-devel to dependencies of libfm-qt-devel
- Fixes RHBZ 1758064

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.1-6
- rebuild (qt5)

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-5
- Improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.1-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 0.14.1-2
- rebuild (qt5)

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Mon Mar 04 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.14.0-3
- Rebuild for Qt 5.12.1

* Wed Feb 13 2019 Zamir SUN <sztsian@gmail.com> - 0.14.0-2
- Add l10n sub package

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.13.1-3
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.13.1-2
- rebuild (qt5)

* Thu Aug 09 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-2
- Add menu-cache-devel as Require, otherwise cmake report 'Imported target "fm-qt" includes non-existent path'

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-13
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-12
- rebuild (qt5)

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0.11.2-11
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-9
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-8
- rebuild (qt5)

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.11.2-7
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-2
- moved translations to lxqt-l10n

* Mon Jan 16 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.2-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.1-2
- Fix some rpmlint errors

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.1-1
New package splitted from main pcmanfm-qt
