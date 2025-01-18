%if 0%{?rhel} >= 9
%global _lto_cflags %nil
%endif

Name: gnucash
Summary: Finance management application
Version: 5.10
URL: https://gnucash.org/
Release: 2%{?dist}
License: GPL-2.0-or-later
Source: https://downloads.sourceforge.net/sourceforge/gnucash/gnucash-%{version}.tar.bz2

ExcludeArch: %{ix86}

Patch0: rpath.patch
Patch1: no-implicit.patch
Patch2: gnucash-5.9-swig-4.3.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1563466
ExcludeArch: ppc64 s390x

BuildRequires: gcc >= 8, gcc-c++, cmake >= 3.10
BuildRequires: perl-generators, perl-podlators
BuildRequires: libxml2 >= 2.9.4, libxslt-devel, zlib-devel
BuildRequires: gtk3 >= 3.22.30, glib2 >= 2.56.1
BuildRequires: libofx-devel >= 0.9.12, aqbanking-devel >= 5.7.0, gwenhywfar-gui-gtk3-devel >= 4.20
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: guile30-devel
%global guilever 3.0
%else
BuildRequires: guile-devel
%global guilever 2.0
%endif
BuildRequires: swig >= 3.0.12
BuildRequires: desktop-file-utils, gettext >= 0.9.6
BuildRequires: libdbi-devel >= 0.8.3, libdbi-dbd-mysql, libdbi-dbd-pgsql, libdbi-dbd-sqlite
BuildRequires: libappstream-glib
BuildRequires: libsecret-devel >= 0.18
%if %{defined el8}
BuildRequires: boost-devel >= 1.66.0
%else
BuildRequires: boost-devel >= 1.67.0
%endif
BuildRequires: gtest-devel >= 1.8.0, gmock-devel >= 1.8.0
%if 0%{?rhel} >= 9
BuildRequires: webkit2gtk3-devel
%else
BuildRequires: webkit2gtk4.1-devel
%endif
BuildRequires: python3-devel >= 3.6
BuildRequires: python3-setuptools

Requires: gnucash-docs >= %{version}
Requires: dconf
Requires: perl(Finance::Quote)
Requires: perl(JSON::Parse)
Requires: perl(Getopt::Std)
Requires: gnome-icon-theme
Recommends: libdbi-dbd-sqlite
Suggests: libdbi-dbd-mysql
Suggests: libdbi-dbd-pgsql

%description
GnuCash is a personal finance manager. A check-book like register GUI
allows you to enter and track bank accounts, stocks, income and even
currency trades. The interface is designed to be simple and easy to
use, but is backed with double-entry accounting principles to ensure
balanced books.

%prep
%autosetup -p1

%build
# thanks gcc8
%if 0%{?rhel} >= 9
%global optflags %{optflags} -Wno-parentheses -Wno-error
%else
%global optflags %{optflags} -Wno-parentheses
%endif
sed -i s/3.8/%{python3_version}/g CMakeLists.txt
%cmake -D WITH_PYTHON=ON -D COMPILE_GSCHEMAS=OFF
%cmake_build

%install
%cmake_install

%find_lang %{name}

# vfolder desktop file install stuff
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/

mv $RPM_BUILD_ROOT/%{_libdir}/lib* $RPM_BUILD_ROOT/%{_libdir}/gnucash

rm -rf $RPM_BUILD_ROOT/%{_infodir} \
	$RPM_BUILD_ROOT/%{_includedir} \
	$RPM_BUILD_ROOT/%{_datadir}/aclocal \
	$RPM_BUILD_ROOT/%{_libdir}/lib*.a \
	$RPM_BUILD_ROOT/%{_libdir}/gnucash/lib*.a \
	$RPM_BUILD_ROOT/%{_bindir}/gnc-test-env \
	$RPM_BUILD_ROOT/%{_bindir}/gnc-fq-update \
	$RPM_BUILD_ROOT/%{_datadir}/guile/site/%{guilever}/tests

find $RPM_BUILD_ROOT/%{_libdir} -name *.la -delete

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnucash.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/gnucash.appdata.xml

%files -f %{name}.lang
%docdir %{_datadir}/doc/gnucash
%doc %{_datadir}/doc/gnucash/*
%license LICENSE
%dir %{_sysconfdir}/gnucash
%{_bindir}/*
%{_libdir}/gnucash/
%{_libdir}/guile/%{guilever}/site-ccache/gnucash/
%{python3_sitearch}/gnucash/
%{_datadir}/glib-2.0/schemas/org.gnucash.GnuCash.*.xml
%{_datadir}/gnucash
%{_datadir}/guile/site/%{guilever}/gnucash
%{_datadir}/metainfo/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man*/*
%config(noreplace) %{_sysconfdir}/gnucash/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.10-1
- 5.10

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 5.9-4
- Rebuild for ICU 76

* Mon Nov 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.9-3
- Patch for Python accounting file bug

* Wed Oct 16 2024 Jitka Plesnikova <jplesnik@redhat.com> - 5.9-2
- Fix for SWIG 4.3.0

* Mon Sep 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.9-1
- 5.9

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.8-1
- 5.8

* Mon Jul 01 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.7-1
- 5.7

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 5.6-3
- Rebuilt for Python 3.13

* Thu May 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.6-2
- Patch for QIF import.

* Mon Apr 01 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.6-1
- 5.6

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.5-6
- Patch for SLR issue

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 5.5-5
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 5.5-2
- Rebuilt for Boost 1.83

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.5-1
- 5.5

* Mon Nov 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.4-3
- Patch for Python 3.13

* Fri Oct 27 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.4-2
- Use guile30

* Mon Sep 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.4-1
- 5.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 5.2-4
- Rebuilt for ICU 73.2

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 5.2-3
- Rebuilt for Python 3.12

* Mon Jun 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.2-2
- Requires JSON::Parse and Getopt::Std
- Upstream patch making this equivalent to 5.3

* Mon Jun 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.2-1
- 5.2

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.1-3
- Rebuilt for Python 3.12

* Thu May 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.1-2
- Move to webkit2gtk4.1

* Mon May 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.1-1
- 5.1

* Thu Apr 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0-1
- 5.0

* Thu Mar 30 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.14-1
- 4.14

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.13-7
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 4.13-6
- Rebuilt for Boost 1.81

* Mon Jan 30 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.13-5
- Patch for gcc 13.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 4.13-3
- Rebuild for ICU 72

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> = 4.13-2
- BR setuptools.

* Mon Dec 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.13-1
- 4.13

* Mon Sep 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.12-1
- 4.12

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.11-4
- Rebuilt for ICU 71.1

* Thu Jul 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.11-3
- Require gnome-icon-theme

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.11-1
- 4.11

* Thu Jun 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.10-4
- Fix schema inclusion.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.10-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 4.10-2
- Rebuilt for Boost 1.78

* Mon Apr 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.10-1
- 4.10

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.9-1
- 4.9

* Thu Dec 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.8-1
- 4.8

* Mon Sep 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.7-1
- 4.7

* Thu Sep 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.6-5
- Fix directory ownership.

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 4.6-4
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Paul Howarth <paul@city-fan.org> - 4.6-2
- Add fix for crash in transfers between accounts with different currencies
  https://bugs.gnucash.org/show_bug.cgi?id=798221
  https://bugs.gnucash.org/show_bug.cgi?id=798243
- Add fix for truncation of fund/currency prices
  https://bugs.gnucash.org/show_bug.cgi?id=798219

* Mon Jun 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.6-1
- 4.6

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.5-4
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.5-3
- Remove RPATH.

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 4.5-2
- Rebuild for ICU 69

* Fri Apr 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.5-1
- 4.5

* Sat Feb 13 2021 Bill Nottingham <notting@splat.cc> - 4.4-2
- fix build with glib 2.67.3+ (#1927622)

* Sat Jan 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.4-1
- 4.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jonathan Wakely <jwakely@redhat.com> - 4.2-5
- Fix __STRICT_ANSI__ issue exposed by gcc-11

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 4.2-4
- Rebuilt for Boost 1.75

* Wed Oct 28 2020 Jeff Law <law@redhat.com> - 4.2-3
- Fix volatile issue exposed by gcc-11

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 4.2-2
- Fix misleading indentation warning from gcc-11

* Sun Oct 11 2020 Bill Nottingham <notting@splat.cc> - 4.2-1
- update to 4.2

* Mon Sep 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.1-3
- Build with guile 2.2

* Thu Aug 06 2020 Stefan Bluhm <stefan.bluhm@clacee.eu> 4.1-2
- Updated "Source" to https.
- Updated requirements.
- Removed ktoblzcheck-devel requirement.

* Mon Jul 27 2020 Bill Nottingham <notting@splat.cc> - 4.1-1
- update to 4.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Bill Nottingham <notting@splat.cc> - 4.0-1
- update to 4.0

* Fri Jun  5 2020 Peter Oliver <rpm@mavit.org.uk> - 3.10-5
- Add weak dependencies on optional storage providers.

* Thu Jun 04 2020 Jonathan Wakely <jwakely@redhat.com> - 3.10-4
- Rebuilt and patched for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.10-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Pete Walter <pwalter@fedoraproject.org> - 3.10-2
- Rebuild for ICU 67

* Mon Apr 13 2020 Bill Nottingham <notting@splat.cc> - 3.10-1
- update to 3.10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.8-2
- rebuild (aqbanking)

* Tue Jan 21 2020 Kalev Lember <klember@redhat.com> - 3.8-1
- Update to 3.8

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 3.7-3
- Rename one instance of struct _iterate to struct __iterate to
  avoid ODR problems with LTO

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.7-2
- Rebuild for ICU 65

* Mon Sep  9 2019 Bill Nottingham <notting@splat.cc> - 3.7-1
- update to 3.7

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Bill Nottingham <notting@splat.cc> - 3.6-1
- update to 3.6

* Fri May  3 2019 Bill Nottingham <notting@splat.cc> - 3.5-3
- add (another) upstream patch for https://bugzilla.redhat.com/show_bug.cgi?id=1698706

* Mon Apr 15 2019 Bill Nottingham <notting@splat.cc> - 3.5-2
- add upstream patch for https://bugzilla.redhat.com/show_bug.cgi?id=1698706

* Tue Apr  2 2019 Bill Nottingham <notting@splat.cc> - 3.5-1
- update to 3.5

* Wed Feb 20 2019 Bill Nottingham <notting@splat.cc> - 3.4-4
- reenable (and apply patch for) python bindings

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4-3
- Backport strncpy overflow-warning fix.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  8 2019 Bill Nottingham <notting@splat.cc> - 3.4-1
- update to 3.4

* Thu Dec 06 2018 Kalev Lember <klember@redhat.com> - 3.3-2
- Fix gnucash to show up in appstream metadata (#1656631)

* Mon Oct  1 2018 Bill Nottingham <notting@splat.cc> - 3.3-1
- update to 3.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.2-2
- Rebuild for ICU 62

* Sun Jul 01 2018 Bill Nottingham <notting@splat.cc> - 3.2-1
- update to 3.2

* Tue May 15 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1-4
- Rebuild for ICU 61.1

* Mon Apr 30 2018 Bill Nottingham <notting@splat.cc> - 3.1-3
- rebuild with respun tarball

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1-2
- Rebuild for ICU 61.1

* Mon Apr 30 2018 Bill Nottingham <notting@splat.cc> - 3.1-1
- update to 3.1

* Tue Apr 03 2018 Bill Nottingham <notting@splat.cc> - 3.0-1
- update to 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.19-2
- Remove obsolete scriptlets

* Mon Dec 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.19-1
- 2.6.19

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.6.18-3
- Rebuild for ICU 60.1

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 2.6.18-2
- Drop the explicit dependnecy on rubypick.

* Tue Sep 26 2017 Bill Nottingham <notting@splat.cc> - 2.6.18-1
- update to 2.6.18

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Bill Nottingham <notting@splat.cc> - 2.6.17-2
- bundle webkitgtk (#1375812)

* Mon Jul  3 2017 Bill Nottingham <notting@splat.cc> - 2.6.17-1
- update to 2.6.17

* Tue Apr 11 2017 Bill Nottingham <notting@splat.cc> - 2.6.16-1
- update to 2.6.16

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Bill Nottingham <notting@splat.cc> - 2.6.15-1
- update to 2.6.15

* Fri Nov 04 2016 Bill Nottingham <notting@splat.cc> - 2.6.14-1
- update to 2.6.14

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.13-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul  7 2016 Bill Nottingham <notting@splat.cc> - 2.6.13-1
- update to 2.6.13

* Sat Jun  4 2016 Bill Nottingham <notting@splat.cc> - 2.6.12-2
- add upstream fix for price editor crash (#1334089, #1337078, #1342719)

* Tue Apr 19 2016 Bill Nottingham <notting@splat.cc> - 2.6.12-1
- update to 2.6.12 (#1321562)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Bill Nottingham <notting@splat.cc> - 2.6.11-1
- update to 2.6.11 (#1297771)

* Sun Dec 27 2015 Bill Nottingham <notting@splat.cc> - 2.6.10-1
- update to 2.6.10 (#1293505, #1178516)

* Wed Oct  7 2015 Bill Nottingham <notting@splat.cc> - 2.6.9-1
- update to 2.6.9

* Tue Oct  6 2015 Bill Nottingham <notting@splat.cc> - 2.6.8-1
- update to 2.6.8 (#1266794)

* Mon Jun 29 2015 Bill Nottingham <notting@splat.cc> - 2.6.7-1
- update to 2.6.7 (#1236432)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Bill Nottingham <notting@splat.cc> - 2.6.6-1
- update to 2.6.6 (#1207447)

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 2.6.5-2
- Use better AppData screenshots

* Thu Jan  8 2015 Bill Nottingham <notting@splat.cc> - 2.6.5-1
- update to 2.6.5 (#1176892) which fixes guile cache issues (#1151870) and charts (#1157203)

* Tue Sep 30 2014 Bill Nottingham <notting@splat.cc> - 2.6.4-1
- update to 2.6.4 (#1147844, #1123943, #1116500)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr  3 2014 Bill Nottingham <notting@splat.cc> - 2.6.3-1
- update to 2.6.3 (#1082288)

* Mon Mar 10 2014 Bill Nottingham <notting@splat.cc> - 2.6.2-1
- update to 2.6.2 (#1071911)

* Mon Jan 27 2014 Bill Nottingham <notting@redhat.com> - 2.6.1-1
- update to 2.6.1 (#1057990)
- add dconf requires (#1058218)

* Tue Jan 21 2014 Bill Nottingham <notting@redhat.com> - 2.6.0-3
- fix %%postun (#1056721)
- rebuild for libdbi

* Fri Jan 17 2014 Bill Nottingham <notting@redhat.com> - 2.6.0-2
- package upstream appdata file

* Thu Jan 16 2014 Bill Nottingham <notting@redhat.com> - 2.6.0-1
- update to 2.6.0

* Mon Sep 23 2013 Bill Nottingham <notting@redhat.com> - 2.4.13-5
- rebuild against new libofx

* Tue Sep  3 2013 Bill Nottingham <notting@redhat.com> - 2.4.13-4
- add appstream metadata from upstream git head

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.4.13-2
- Perl 5.18 rebuild

* Tue Apr 23 2013 Bill Nottingham <notting@redhat.com> - 2.4.13-1
- update to 2.4.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Bill Nottingham <notting@redhat.com> - 2.4.11-1
- update to 2.4.11

* Tue Jul 10 2012 Bill Nottingham <notting@redhat.com> - 2.4.10-2
- rebuild for ofx ABI bump

* Wed Feb 29 2012 Bill Nottingham <notting@redhat.com> - 2.4.10-1
- update to 2.4.10
- enable ktobzlcheck support (#783849)

* Thu Jan 19 2012 Bill Nottingham <notting@redhat.com> - 2.4.9-1
- update to 2.4.9

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Bill Nottingham <notting@redhat.com> - 2.4.8-1
- update to 2.4.8

* Fri Oct 14 2011 Bill Nottingham <notting@redhat.com> - 2.4.7-4
- update the last fix (#703249, #742202, #744310)

* Tue Oct 11 2011 Bill Nottingham <notting@redhat.com> - 2.4.7-3
- when scanning modules, don't unload them (#703249, #742202, #744310)

* Tue Aug  9 2011 Bill Nottingham <notting@redhat.com> - 2.4.7-2
- fix python bindings on 64bit (#729454)

* Wed Jul  6 2011 Bill Nottingham <notting@redhat.com> - 2.4.7-1
- update to 2.4.7 (#712268)

* Mon Jun 13 2011 Bill Nottingham <notting@redhat.com> - 2.4.5-4
- re-enable python bindings (#712621)

* Fri May 13 2011 Bill Nottingham <notting@redhat.com> - 2.4.5-3
- fix it to at least compile with guile-2.0 (does not work yet) (#704527)

* Thu May  5 2011 Bill Nottingham <notting@redhat.com> - 2.4.5-2
- fix tips (#702391)

* Tue Apr 19 2011 Bill Nottingham <notting@redhat.com> - 2.4.5-1
- update to 2.4.5

* Fri Mar 18 2011 Bill Nottingham <notting@redhat.com> - 2.4.4-2
- fix configure.ac to correctly use WEBKIT_LIBS from pkg-config (#670001, <q3aiml@gmail.com>)

* Wed Mar 16 2011 Bill Nottingham <notting@redhat.com> - 2.4.4-1
- update to 2.4.4

* Thu Mar  3 2011 Bill Nottingham <notting@redhat.com> - 2.4.3-1
- update to 2.4.3

* Fri Feb 11 2011 Bill Nottingham <notting@redhat.com> - 2.4.2-1
- update to 2.4.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Bill Nottingham <notting@redhat.com> - 2.4.0-3
- don't ship gnc-fq-update; updates should be handled by normal packaging

* Wed Jan 12 2011 Bill Nottingham <notting@redhat.com> - 2.4.0-2
- remove 'this is a development version' warning

* Mon Jan  3 2011 Bill Nottingham <notting@redhat.com> - 2.4.0-1
- update to 2.4.0

* Thu Oct 21 2010 Bill Nottingham <notting@redhat.com>
- don't ship gnc-test-env (#644933, CVE-2010-3999)

* Mon Aug 23 2010 Bill Nottingham <notting@redhat.com> - 2.3.15-1
- update to 2.3.15
- include upstream patch for config migration (#571621)

* Tue Jul  6 2010 Bill Nottingham <notting@redhat.com> - 2.3.13-2
- rebuild against newer webkitgtk

* Thu Jun  3 2010 Bill Nottingham <notting@redhat.com> - 2.3.13-1
- update to 2.3.13

* Tue May 18 2010 Bill Nottingham <notting@redhat.com> - 2.3.12-3
- fix finding of dbi drivers (#593090)

* Fri Apr 30 2010 Bill Nottingham <notting@redhat.com> - 2.3.12-2
- update to 2.3.12

* Fri Mar 19 2010 Bill Nottingham <notting@redhat.com> - 2.3.11-1
- update to 2.3.11

* Wed Feb 24 2010 Bill Nottingham <notting@redhat.com> - 2.3.10-2
- rebuild against new goffice

* Thu Feb 18 2010 Bill Nottingham <notting@redhat.com> - 2.3.10-1
- update to 2.3.10

* Mon Feb 15 2010 Bill Nottingham <notting@redhat.com> - 2.3.9-1
- update to 2.3.9

* Thu Jan 21 2010 Bill Nottingham <notting@redhat.com> - 2.3.8-2
- Rebuild against latest aqbanking

* Thu Dec 10 2009 Bill Nottingham <notting@redhat.com> - 2.3.8-1
- update to 2.3.8

* Tue Dec  1 2009 Bill Nottingham <notting@redhat.com> - 2.3.7-1
- Update to development version.
- Fix accelerators (#533019, #541915)

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.2.9-3
- Use lzma compressed upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Bill Nottingham <notting@redhat.com> - 2.2.9-1
- update to 2.2.9

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Bill Nottingham <notting@redhat.com> - 2.2.8-2
- fix crash resulting from earlier crash fix (#474511, <jik@kamens.brookline.ma.us>)

* Tue Dec 16 2008 Bill Nottingham <notting@redhat.com> - 2.2.8-1
- update to 2.2.8

* Fri Dec  5 2008 Bill Nottingham <notting@redhat.com> - 2.2.7-2
- fix crash with glib-2.19 (#474511, <jik@kamens.brookline.ma.us>)

* Tue Sep 30 2008 Bill Nottingham <notting@redhat.com> - 2.2.7-1
- update to 2.2.7

* Tue Sep  9 2008 Bill Nottingham <notting@redhat.com> - 2.2.6-2
- rebuild against new aqbanking

* Fri Aug  1 2008 Bill Nottingham <notting@redhat.com> - 2.2.6-1
- update to 2.2.6

* Tue Apr 29 2008 Bill Nottingham <notting@redhat.com> - 2.2.5-1
- update to 2.2.5

* Mon Mar  3 2008 Bill Nottingham <notting@redhat.com> - 2.2.4-1
- update to 2.2.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.3-3
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Bill Nottingham <notting@redhat.com> - 2.2.3-2
- rebuild against new goffice

* Tue Jan  8 2008 Bill Nottingham <notting@redhat.com> - 2.2.3-1
- update to 2.2.3

* Tue Dec 18 2007 Bill Nottingham <notting@redhat.com> - 2.2.2-1
- update to 2.2.2

* Thu Oct 25 2007 Bill Nottingham <notting@redhat.com> - 2.2.1-4
- multilib fixes (#341331, #357161, #246382)

* Wed Oct 10 2007 Bill Nottingham <notting@redhat.com> - 2.2.1-3
- silence binreloc warning

* Wed Aug 29 2007 Bill Nottingham <notting@redhat.com> - 2.2.1-2
- fix build

* Tue Aug 21 2007 Bill Nottingham <notting@redhat.com> - 2.2.1-1
- update to 2.2.1

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Mon Jul 23 2007 Bill Nottingham <notting@redhat.com> - 2.2.0-2
- fix icon (#248492)

* Mon Jul 16 2007 Bill Nottingham <notting@redhat.com> - 2.2.0-1
- update to 2.2.0

* Mon Jul  2 2007 Bill Nottingham <notting@redhat.com> - 2.1.5-1
- update to 2.1.5

* Mon Jun 25 2007 Bill Nottingham <notting@redhat.com> - 2.1.4-1
- update to RC version 2.1.4
  - switch to using goffice04, and stock gtkhtml3
  - no more g-wrap or libtool-ltdl - use swig

* Tue Mar 13 2007 Bill Nottingham <notting@redhat.com> - 2.0.5-3
- require gtkhtml38 include file to pull in the proper gtkhtml version
- fix build when libofx and ofx tools are separate

* Mon Feb 19 2007 Bill Nottingham <notting@redhat.com> - 2.0.5-1
- update to 2.0.5
- fixes: CVE-2007-0007 (#223233)

* Tue Feb 13 2007 Bill Nottingham <notting@redhat.com> - 2.0.4-5
- split off docs package

* Mon Jan 15 2007 Bill Nottingham <notting@redhat.com> - 2.0.4-4
- fix perl requirement noise
- fix libgsf-gnome buildreq
- fix %%post
- better rpath fixing

* Thu Jan 11 2007 Bill Nottingham <notting@redhat.com> - 2.0.4-3
- build against separate goffice
- various spec cleanups
- fix gconf scriplets

* Mon Jan  8 2007 Bill Nottingham <notting@redhat.com> - 2.0.4-1
- update to 2.0.4

* Wed Oct 11 2006 Bill Nottingham <notting@redhat.com> - 2.0.2-1
- update to 2.0.2
- update docs to 2.0.1

* Mon Aug 28 2006 Bill Nottingham <notting@redhat.com> - 2.0.1-6
- rebuild against new libofx

* Sat Aug 26 2006 Karsten Hopp <karsten@redhat.com> - 2.0.1-5
- buildrequire intltool which was previously pulled in by scrollkeeper but
  dropped this requirement because of bz #203606

* Tue Aug 22 2006 Bill Nottingham <notting@redhat.com> - 2.0.1-4
- require perl-Crypt-SSLeay (#203050)

* Fri Aug 11 2006 Bill Nottingham <notting@redhat.com> - 2.0.1-3
- require yelp (#202266)

* Tue Aug  8 2006 Bill Nottingham <notting@redhat.com> - 2.0.1-2
- fix schema list

* Tue Aug  1 2006 Bill Nottingham <notting@redhat.com> - 2.0.1-1
- update to 2.0.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.0-2.1
- rebuild

* Tue Jul 11 2006 Bill Nottingham <notting@redhat.com> - 2.0.0-2
- rebuild against new aqbanking

* Mon Jul 10 2006 Bill Nottingham <notting@redhat.com> - 2.0.0-1
- update to 2.0.0. Woo.

* Mon Jun 19 2006 Bill Nottingham <notting@redhat.com> - 1.9.8-1
- update to 1.9.8

* Tue Jun  6 2006 Bill Nottingham <notting@redhat.com> - 1.9.7-1
- update to 1.9.7
- use official docs tarball, not svn snapshot

* Thu May 25 2006 Bill Nottingham <notting@redhat.com> - 1.9.6-2
- update docs to latest svn (gets rid of extraneous configure check
  for db185)

* Wed May 17 2006 Bill Nottingham <notting@redhat.com> - 1.9.6-1
- update to 1.9.6

* Tue May  9 2006 Bill Nottingham <notting@redhat.com> - 1.9.5-3
- rebuild against new guile (<mlichvar@redhat.com>)
- silence warnings

* Mon Apr 17 2006 Bill Nottingham <notting@redhat.com> - 1.9.5-1
- update to 1.9.5

* Thu Apr  6 2006 Bill Nottingham <notting@redhat.com> - 1.9.4-1
- update to 1.9.4

* Tue Apr  4 2006 Bill Nottingham <notting@redhat.com> - 1.9.3-2
- fix conflict with qof (#187267)

* Mon Mar 27 2006 Bill Nottingham <notting@redhat.com> - 1.9.3-1
- update to 1.9.x

* Mon Feb 20 2006 Bill Nottingham <notting@redhat.com> - 1.8.12-3
- rebuild against g-wrap-1.9.6

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.8.12-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8.12-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Bill Nottingham <notting@redhat.com> 1.8.12-2
- disable postgres backend (#177646)

* Thu Dec 22 2005 Bill Nottingham <notting@redhat.com> 1.8.12-1
- update to 1.8.12

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Sep  9 2005 Bill Nottingham <notting@redhat.com> 1.8.11-4
- with new slib, umb-scheme is no longer needed. Switch requirement.

* Tue Apr 12 2005 Bill Nottingham <notting@redhat.com> 1.8.11-3
- require umb-scheme explicitly (#151465)
- rebuild against new postgresql
- use full path to icon (#154587)

* Mon Mar  7 2005 Bill Nottingham <notting@redhat.com> 1.8.11-2
- rebuild against bonobo-less Guppi, gtkhtml

* Wed Feb  9 2005 Bill Nottingham <notting@redhat.com> 1.8.11-1
- update to 1.8.11
- update docs to 1.8.5
- remove info file (#123444)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 13 2004 Bill Nottingham <notting@redhat.com> 1.8.9-1
- update to 1.8.9

* Sat Mar 20 2004 Bill Nottingham <notting@redhat.com> 1.8.8-5
- reinstate libtool helper files (#118495)

* Fri Mar 12 2004 Bill Nottingham <notting@redhat.com> 1.8.8-4
- rebuild against separate libofx/openhbci

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Dec 23 2003 Bill Nottingham <notting@redhat.com>
- add a 64-bit patch from mandrake

* Wed Dec  3 2003 Bill Nottingham <notting@redhat.com> 1.8.8-2
- rebuild

* Tue Dec  2 2003 Bill Nottingham <notting@redhat.com> 1.8.8-1
- update to 1.8.8

* Tue Sep 23 2003 Bill Nottingham <notting@redhat.com> 1.8.7-1
- update to 1.8.7
- fix docs build

* Wed Aug 20 2003 Bill Nottingham <notting@redhat.com> 1.8.5-1
- update to 1.8.5

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 28 2003 Bill Nottingham <notting@redhat.com> 1.8.4-1
- update to 1.8.4

* Mon May 19 2003 Bill Nottingham <notting@redhat.com> 1.8.3-1
- update to 1.8.3

* Mon Mar 24 2003 Bill Nottingham <notting@redhat.com> 1.8.2-1
- update to 1.8.2

* Thu Mar 20 2003 Tim Waugh <twaugh@redhat.com> 1.8.1-4
- Build requires openjade-devel (new openjade sub-package).
- Rebuild against new OpenSP.

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Sun Feb 23 2003 Bill Nottingham <notting@redhat.com> 1.8.1-2
- fix crash on hiding accounts (#84931, patch from upstream)

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 1.8.1-1
- update to 1.8.1

* Wed Feb  5 2003 Bill Nottingham <notting@redhat.com> 1.8.0-3
- fix desktop entry (#82804)
- add startup-notification

* Tue Feb  4 2003 Bill Nottingham <notting@redhat.com> 1.8.0-1
- 1.8.0

* Tue Jan 28 2003 Bill Nottingham <notting@redhat.com> 1.7.8-3
- rebuild everywhere

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Bill Nottingham <notting@redhat.com> 1.7.8-1
- 1.7.8

* Tue Jan 14 2003 Bill Nottingham <notting@redhat.com> 1.7.7-1
- update to 1.7.7
- add libofx, openhbci support

* Fri Dec  6 2002 Tim Waugh <twaugh@redhat.com> 1.7.5-3
- Fix desktop file (bug #69422).

* Wed Dec  4 2002 Bill Nottingham <notting@redhat.com> 1.7.5-2
- fix omf file ref to buildroot

* Tue Dec  3 2002 Bill Nottingham <notting@redhat.com> 1.7.5-1
- update to 1.7.5-1, split off postgres backend

* Mon Nov 18 2002 Bill Nottingham <notting@redhat.com> 1.6.8-3
- guile is everywhere, build everywhere
- except hammer (postgres)

* Mon Nov 11 2002 Tim Powers <timp@redhat.com> 1.6.8-2
- rebuild against guile-1.4

* Thu Nov  7 2002 Bill Nottingham <notting@redhat.com> 1.6.8-1
- update to 1.6.8-1
- stop using db1

* Thu Oct 24 2002 Jeremy Katz <katzj@redhat.com>
- build against new gtkhtml

* Sat Aug 10 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- bzip2 source

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 16 2002 Bill Nottingham <notting@redhat.com>
- autoconf fun

* Mon Apr  8 2002 Bill Nottingham <notting@redhat.com>
- rebuild in new environment against fixed guile, g-wrap

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com>
- rebuild in new environment

* Mon Mar 11 2002 Bill Nottingham <notting@redhat.com>
- update to 1.6.6

* Fri Feb 22 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Dec 17 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.5

* Mon Oct  1 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.4

* Mon Sep 24 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.3

* Mon Aug 13 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.2

* Thu Aug  9 2001 Bill Nottingham <notting@redhat.com>
- add patch to fix triple imports of prices from 1.4 files
  (<dave@krondo.com>)

* Thu Jul 19 2001 Bill Nottingham <notting@redhat.com>
- tweak buildprereqs

* Sun Jul  8 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.1
- fix info dir (#47646)
- fix library dependencies

* Fri Jun 29 2001 Bill Nottingham <notting@redhat.com>
- don't own %%{_infodir}/dir

* Wed Jun 27 2001 Bill Nottingham <notting@redhat.com>
- add info dir entry

* Mon Jun 18 2001 Bill Nottingham <notting@redhat.com>
- update to 1.6.0, merge in stuff from included spec file

* Mon Feb  5 2001 Adrian Havill <havill@redhat.com>
- added Japanese locale

* Thu Jan 11 2001 Tim Powers <timp@redhat.com>
- exclude ia64

* Wed Dec  6 2000 Tim Powers <timp@redhat.com>
- updated to 1.4.9

* Mon Oct 23 2000 Tim Powers <timp@redhat.com>
- update to 1.4.8

* Wed Sep 13 2000 Tim Powers <timp@redhat.com>
- update to 1.4.6

* Wed Aug 2 2000 Tim Powers <timp@redhat.com>
- rebuilt against libpng-1.0.8

* Mon Jul 31 2000 Tim Powers <timp@redhat.com>
- updated to 1.4.3, bugfix release

* Tue Jul 25 2000 Tim Powers <timp@redhat.com>
- ExcludeArch alpha

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- fixed defattr for the stuff in /usr/bin

* Wed Jul 12 2000 Tim Powers <timp@redhat.com>
- update to 1.4.2

* Tue Jul 11 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jul 05 2000 Preston Brown <pbrown@redhat.com>
- adopted for Powertools 7.0
