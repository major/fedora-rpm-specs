Summary:        Library for manipulating ID3v1 and ID3v2 tags
Name:           id3lib
Version:        3.8.3
Release:        60%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://id3lib.sourceforge.net/

Source0:        http://downloads.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
Source1:        id3lib-no_date_footer.hml

Patch0:         id3lib-dox.patch
Patch1:         id3lib-3.8.3-autoreconf.patch
Patch2:         id3lib-3.8.3-io_helpers-163101.patch
Patch3:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/10-fix-compilation-with-cpp-headers.patch
Patch4:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/15-fix-headers-of-main-functions.patch
Patch5:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/40-deal-with-mkstemp.patch
Patch6:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/50-remove-outdated-check.patch
Patch7:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/20-create-manpages.patch
Patch8:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/60-id3lib-missing-nullpointer-check.patch
Patch9:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/60-fix_make_check.patch
Patch10:        https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/61-fix_vbr_stack_smash.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires: make

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include
standards-compliant ID3v1/2 tagging capabilities in their applications.
Features include identification of valid tags, automatic size conversions,
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities. Additionally, it can tell mp3 header info, like bitrate etc.


%package devel
Summary:        Development tools for the id3lib library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel

%description devel
This package provides files needed to develop with the id3lib library.


%prep
%autosetup -p1
for i in doc/id3v2.3.0.txt doc/id3v2.3.0.html ChangeLog THANKS; do
  iconv --from-code=ISO-8859-1 --to-code=UTF8 $i --output=tmp
  sed -i -e 's/\r//' tmp
  touch --reference=$i tmp
  mv tmp $i
done
sed -i -e 's|@DOX_DIR_HTML@|%{_docdir}/%{name}-devel/api|' doc/index.html.in
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = id3lib-no_date_footer.hml,g" doc/Doxyfile.in
cp %{SOURCE1} doc


%build
autoreconf --force --install
%configure --disable-dependency-tracking --disable-static
%make_build libid3_la_LIBADD=-lz


%install
%make_install
make docs
mkdir -p __doc/doc ; cp -p doc/*.{gif,jpg,png,html,txt,ico,css}  __doc/doc
rm -f $RPM_BUILD_ROOT%{_libdir}/libid3.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1


%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog HISTORY NEWS README THANKS TODO __doc/doc/
%license COPYING
%{_libdir}/libid3-3.8.so.*
%{_bindir}/id3convert
%{_bindir}/id3cp
%{_bindir}/id3info
%{_bindir}/id3tag
%{_mandir}/man1/id3convert.1*
%{_mandir}/man1/id3cp.1*
%{_mandir}/man1/id3info.1*
%{_mandir}/man1/id3tag.1*

%files devel
%doc doc/id3lib.css doc/api/
%{_includedir}/id3.h
%{_includedir}/id3/
%{_libdir}/libid3.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.8.3-59
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Simone Caronni <negativo17@gmail.com> - 3.8.3-47
- Use macros for build, install and setup.
- Minor cleanups to SPEC file.
- Use valid URL for Debian patches.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Adrian Reber <adrian@lisas.de> - 3.8.3-44
- Added BR gcc and gcc-c++
- Switch to %%ldconfig_scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 David King <amigadave@amigadave.com> - 3.8.3-36
- Tighten subpackage dependencies
- Use license macro for COPYING
- Preserve timestamps during install
- Update man pages glob in files section
- Drop unnecessary chmod

* Fri Nov 14 2014 David King <amigadave@amigadave.com> - 3.8.3-35
- Fix typos in man page patch
- Add UTF-16 string lists patch, adapted from Debian
- Add NULL pointer check patch from Debian
- Enable check, using make check

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 David King <amigadave@amigadave.com> - 3.8.3-32
- Use autoreconf patch from mingw-id3lib package

* Wed Aug 07 2013 Adrian Reber <adrian@lisas.de> - 3.8.3-31
- Fixed "id3lib possibly affected by F-20 unversioned docdir change" (#993851)
- Remove unneeded parts (clean, defattr, buildroot) 
- Added man pages from Debian
- Fixed bogus dates

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-27
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 12 2009 Adrian Reber <adrian@lisas.de> - 3.8.3-24
- Fix "Stack smashing with vbr mp3 files" (bz #533706)
  also see https://bugs.launchpad.net/ubuntu/+source/id3lib3.8.3/+bug/444466

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Adrian Reber <adrian@lisas.de> - 3.8.3-22
- Fix "id3lib-devel multilib conflict" (bz #507700)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.8.3-20
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-19
- Fix building of id3lib and programs using it with gcc34
- Drop prebuild doxygen docs, now that doxygen is fixed to not cause multilib
  conflicts
- Convert some docs to UTF-8 

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-18
- Fix multilib api documentation conflict (bz 341551)

* Mon Aug 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-17
- Use mkstemp instead of insecure tempfile creation (bz 253553)

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-16
- Update License tag for new Licensing Guidelines compliance

* Wed Nov 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-15
- Link libid3-3.8.so.3 with -lz (bug #216783)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.8.3-14
- Taking over as maintainer since Anvil has other priorities
- FE6 Rebuild

* Sat Feb 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.8.3-13
- Don't ship static libs.
- Build with dependency tracking disabled.
- Don't use %%exclude.
- Drop unneeded cruft from docs, move API docs to -devel.
- Clean up some cosmetic rpmlint warnings.

* Sat Jul 16 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.8.3-12
- Fix UTF-16 writing bug (bug #163101, upstream #1016290).

* Thu Jun 30 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.8.3-11
- Make libtool link against libstdc++ (bug #162127).

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.8.3-10
- rebuilt

* Wed Oct 29 2003 Ville Skytta <ville.skytta at iki.fi> - 0:3.8.3-0.fdr.9
- Rebuild.

* Sun Sep 28 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.8
- Removed comment after scriptlets

* Mon May  5 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.7
- libid3-3.8.so.3.0.0 -> libid3-3.8.so.*
- {buildroot} -> RPM_BUILD_ROOT

* Sun Apr 27 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.6
- Added post/postun scriptlets

* Thu Apr 24 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.5
- Added zlib-devel require tag for -devel package

* Fri Apr  4 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.4
- Added URL in Source:

* Thu Apr  3 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.3
- added ".so" file to the devel package

* Thu Apr  3 2003 Dams <anvil[AT]livna.org> 0:3.8.3-0.fdr.2
- Added missing epoch requirement

* Wed Apr  2 2003 Dams <anvil[AT]livna.org>
- Initial build.
