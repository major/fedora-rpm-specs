Name:       ibus-qt
Version:    1.3.4
Release:    14%{?dist}
Summary:    Qt IBus library and Qt input method plugin
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus/wiki
Source0:    https://github.com/ibus/ibus-qt/releases/download/%{version}/%{name}-%{version}-Source.tar.gz

#Patch0:     %%{name}-HEAD.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  qt4-devel
BuildRequires:  dbus-devel
BuildRequires:  ibus-devel
BuildRequires:  libicu-devel
BuildRequires:  doxygen
Requires:       ibus

%description
Qt IBus library and Qt input method plugin.

%package devel
Summary:    Development tools for ibus qt
Requires:   %{name} = %{version}-%{release}

%description devel
The ibus-qt-devel package contains the header files for ibus qt library.

%package docs
Summary:    Development documents for ibus qt
Requires:   %{name} = %{version}-%{release}

%description docs
The ibus-qt-docs package contains developer documentation for ibus qt library.

%prep
%autosetup -S git -n %{name}-%{version}-Source

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_usr} \
    -DLIBDIR=%{_libdir}
%cmake_build
%cmake_build -- docs

%install
%cmake_install

%ldconfig_scriptlets

%files
# -f {name}.lang
%doc AUTHORS README INSTALL
%{_libdir}/libibus-qt.so.*
%{_libdir}/qt4/plugins/inputmethods/libqtim-ibus.so

%files devel
%{_includedir}/*
%{_libdir}/libibus-qt.so

%files docs
%doc %__cmake_builddir/docs/html

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.3.4-13
- Rebuild for ICU 76

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.3.4-11
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.3.4-7
- Rebuilt for ICU 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.3.4-5
- Rebuild for ICU 72

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.4-4
- Migrate license tag to SPDX

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.4-3
- Rebuilt for ICU 71.1

* Sat Jul 30 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.4-2
- Bump to 1.3.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-31
- Rebuild for ICU 69

* Mon May 17 2021 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.3-30
- Resolves: #1832098 Fix Wayland display variable

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.3-28
- Resolves: #1863871 replace make with cmake_build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-25
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-23
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-19
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-18
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.3.3-16
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.3-12
- Rebuilt to work with the latest Qt4 environment

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.3.3-11
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.3.3-9
- rebuild for ICU 56.1

* Wed Sep 02 2015 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.3-8
- Changed URL

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.3.3-5
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.3.3-4
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.3-1
- Updated to 1.3.3.

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 1.3.2-6
- rebuild for new ICU

* Thu Aug 08 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.2-5
- Fixed installed but unpackaged files with rpm-build 4.11.1 and %%doc.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.2-3
- Fixed misc issues.

* Thu Mar 21 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.2-2
- Added ibus-qt-HEAD.patch to fix bug 921164.

* Mon Mar 11 2013 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.2-1
- Updated to 1.3.2.

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.3.1-13
- Rebuild for icu 50

* Wed Nov 21 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-12
- Bumped for a misc issue.

* Tue Jul 31 2012 Than Ngo <than@redhat.com> - 1.3.1-11
- rebuild for icu-49.1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-9
- Rebuilt for icu-49.1.1

* Tue Mar 06 2012 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-8
- Rebuilt for ibus 1.4.99.20120304

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 10 2011 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-6
- Rebuilt for icu 4.8

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> - 1.3.1-5
- rebuild for icu 4.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-3
- Fixed Bug 631043 - s/qt-devel/qt4-devel/ in BuildRequires
- Added ibus-qt-HEAD.patch
  Fixed Bug 655530 - Selected text gets deleted in KDE

* Mon Aug 23 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.1-1
- Update to 1.3.1.

* Fri Jul 23 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.0-2
- Fix Bug 616277 - hangul text color is not properly set in kwrite

* Fri Jul 16 2010 Takao Fujiwara <tfujiwar@redhat.com> - 1.3.0-1
- Update to 1.3.0.

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.0.20091217-2
- rebuild for icu 4.4

* Thu Dec 17 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091217-1
- Update to 1.2.0.20091217.

* Sun Dec 06 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091206-1
- Update to 1.2.0.20091206.

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0.20091014-2
- rebuild (for qt-4.6.0-rc1, f13+)

* Wed Oct 14 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20091014-1
- Update to 1.2.0.20091014.

* Sat Aug 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090822-2
- Update the tarball
- Link qt immodule with libicu

* Sat Aug 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090822-1
- Update to 1.2.0.2009822
- Fix compose key problem.

* Mon Jul 27 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090728-1
- The first version.
