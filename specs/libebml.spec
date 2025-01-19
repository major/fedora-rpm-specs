Summary:    Extensible Binary Meta Language library
Name:       libebml
Version:    1.4.5
Release:    3%{?dist}
License:    LGPL-2.1-or-later
URL:        https://www.matroska.org/
Source:     https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
Patch0:     %{name}-use-system-utf8cpp.patch
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: utf8cpp-devel

%description
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.


%package    devel
Summary:    Development files for the Extensible Binary Meta Language library
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   cmake-filesystem
Requires:   pkgconfig

%description devel
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.

This package contains the files required to rebuild applications which
will use the Extensible Binary Meta Language library.


%prep
%setup -q
%patch 0 -p1 -b .utf8cpp
rm -r src/lib/utf8-cpp


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.LGPL
%doc NEWS.md
%{_libdir}/%{name}.so.5{,.*}

%files devel
%{_includedir}/ebml/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/EBML
%{_libdir}/cmake/EBML/EBMLConfig.cmake
%{_libdir}/cmake/EBML/EBMLConfigVersion.cmake
%{_libdir}/cmake/EBML/EBMLTargets-noconfig.cmake
%{_libdir}/cmake/EBML/EBMLTargets.cmake


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.4.5-1
- update to 1.4.5 (#2254413)
- fixes CVE-2023-52339 (#2258046, #2258047)
- use SPDX identifier in License field

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.4.4-3
- switch to plain cmake in dependencies and macros (resolves: rhbz#1731694)
- use better glob for shared library
- drop obsolete ldconfig_scriptlets macro
- fix deprecated patchN macro usage

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.4.4-1
- update to 1.4.4 (#2131232)
- drop obsolete patch

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.4.2-1
- update to 1.4.2 (#1930172)
- fixes CVE-2021-3405 (#1926991)
- fix build with GCC-11

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.4.1-1
- update to 1.4.1 (#1912485)
- fixes heap use-after-free when parsing malformed file (https://gitlab.com/mbunkus/mkvtoolnix/-/issues/2989)

* Mon Aug 10 2020 Hans de Goede <hdegoede@redhat.com> - 1.4.0-4
- Fix FTBFS, straight-forward cmake macro fix (rhbz#1863992)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.4.0-1
- update to 1.4.0 (#1851593), ABI bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.3.10-1
- update to 1.3.10 (#1782287)

* Tue Sep 10 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.3.9-1
- update to 1.3.9 (#1688001)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.3.7-1
- update to 1.3.7
- unbundle utf8cpp
- fix unowned %%{_libdir}/cmake/ebml directory

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.3.6-2
- Append curdir to CMake invokation. (#1668512)

* Mon Jul 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.3.6-1
- update to 1.3.6 (#1570224)
- add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- switch build system to cmake
- add missing dependencies to -devel subpackage
- use license and ldconfig_scriptlets macros

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.3.5-1
- update to 1.3.5 (#1483228)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.3.4-1
- update to 1.3.4 (#1352294)

* Thu Feb 18 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.3.3-3
- don't convert ChangeLog to UTF8, it already is
- use HTTPS in URLs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.3.3-1
- update to 1.3.3 (required by libmatroska 1.4.4)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.3.1-3
- rebuilt for gcc-5.0.0-0.22.fc23

* Sun Mar 01 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.3.1-2
- rebuilt for gcc-5.0

* Thu Jan 15 2015 Hans de Goede <hdegoede@redhat.com> - 1.3.1-1
- Update to 1.3.1 (rhbz#1182372)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Update to 1.3.0
- Spec file clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Thu Jul 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Mon Feb 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- New upstream release 1.2.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Hans de Goede <hdegoede@redhat.com> 1.0.0-1
- New upstream release 1.0.0 (#605571)

* Tue May 25 2010 Hans de Goede <hdegoede@redhat.com> 0.8.0-1
- New upstream release 0.8.0 (#595421)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.8-1
- New upstream release 0.7.8

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.7-5
- Autorebuild for GCC 4.3

* Tue Jan  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.7-4
- Fix building with gcc 4.3

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.7-3
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7.7-2
- Taking over as maintainer since Anvil has other priorities
- Drop static lib from -devel package
- FE6 Rebuild

* Wed Apr 12 2006 Dams <anvil[AT]livna.org> - 0.7.7-1
- Updated to 0.7.7

* Thu Mar 16 2006 Dams <anvil[AT]livna.org> - 0.7.6-2.fc5
- Release bump

* Tue Nov 29 2005 Matthias Saou <http://freshrpms.net/> 0.7.6-1
- Update to 0.7.6.
- Change URL to the project's one.
- Add a full description for the devel package.
- Some other minor spec file changes.

* Sun Jun  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.5-2
- Split development files into a devel subpackage.
- Run ldconfig at post (un)install time.
- Fix shared library file modes.

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 0.7.5-1
- update to 0.7.5 (fixes x86_64 build)
- incldue shared libs

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.7.3-3
- rebuild on all arches

* Sun Feb 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.3-2
- 0.7.3.

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-2
- Update to 0.7.2.
- Bump release to provide Extras upgrade path.

* Sun Aug 29 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.1-0.fdr.1
- Update to 0.7.1.
- Honor $RPM_OPT_FLAGS.

* Mon Jul 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.0-0.fdr.1
- Update to 0.7.0.
- Improved 64-bit arch build fix.

* Wed May  19 2004 Justin M. Forbes <64bit_fedora@comcast.net> 0:0.6.5-0.fdr.2
- Change linux makefile to use lib64 ifarch x86_64 for sane build

* Sun Apr  4 2004 Dams <anvil[AT]livna.org> 0:0.6.5-0.fdr.1
- Updated to 0.6.5

* Sun Feb 29 2004 Dams <anvil[AT]livna.org> 0:0.6.4-0.fdr.2
- Added licenses file as doc

* Thu Sep  4 2003 Dams <anvil[AT]livna.org>
- Initial build.


