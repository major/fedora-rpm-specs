# spec file for package asl
# 
# Copyright (c) 2006 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Spec file for Fedora modified by Eric Smith <brouhaha@fedoraproject.org>

%global patchlevel bld134

Name:           asl
URL:            http://john.ccac.rwth-aachen.de:8000/as/index.html
Version:        1.42
Release:        0.45.%{patchlevel}%{?dist}
License:        GPLv2+
Summary:        Macro Assembler AS
Source:         http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-%{patchlevel}.tar.bz2
Patch0:         asl-Makefile.def.patch
Patch1:         asl-sysdefs.h.patch
Patch2:         asl-install.sh.patch
Patch3:         asl-Makefile-DESTDIR.patch
BuildRequires:  gcc
BuildRequires:  tex(latex)
%if 0%{?fedora} > 18 || 0%{?rhel} > 7
BuildRequires:  tex(german.sty)
BuildRequires: make
%endif


%description
AS is a portable macro cross-assembler for a variety of
microprocessors and controllers. Although it is mainly targeted at
embedded processors and single-board computers, CPU families that are
used in workstations and PCs in the target list.

%prep
# It's a shame that the directory name has 142 instead of 1.42, and Bld82
# instead of bld82. Makes use of variable substitution difficult.
# Also, sometimes the directory name is just "asl-current"
#%setup -q -n asl-142-Bld82
%setup -q -n asl-current

%patch0 -p0 -b .m-def
%patch1 -p1 -b .sysdefs
%patch2 -p1 -b .install
%patch3 -p1 -b .destdir

# German documentation can't be built on EL7 because there is no
# tex(german.sty).
%if 0%{?rhel} != 0 && 0%{?rhel} <= 7
sed -i '/doc_DE/d' Makefile
%endif

%build
# make seems to have problems with %{_smp_mflags}
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# make docs isn't SMP-safe, so can't use %{_smp_mflags}
make docs

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# convert doc files from ISO-8859-1 to UTF-8 encoding
%if 0%{?rhel} != 0 && 0%{?rhel} <= 7
%global change_encoding_files changelog doc/as-EN.txt
%else
%global change_encoding_files changelog doc/as-EN.txt doc/as-DE.txt
%endif

for f in %{change_encoding_files}
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done


%files
%{_bindir}/asl
%{_bindir}/alink
%{_bindir}/p2bin
%{_bindir}/p2hex
%{_bindir}/pbind
%{_bindir}/plist
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/include/
%{_datadir}/%{name}/lib/
%{_mandir}/man1/asl.1*
%{_mandir}/man1/p2bin.1*
%{_mandir}/man1/p2hex.1*
%{_mandir}/man1/pbind.1*
%{_mandir}/man1/plist.1*
%{_mandir}/man1/alink.1*
%license COPYING
%doc README README.LANGS TODO BENCHES changelog
%doc doc/as-EN.html doc/as-EN.txt doc/as-EN.ps doc/as-EN.pdf doc/as-EN.dvi
%if 0%{?rhel} == 0 || 0%{?rhel} > 7
%lang(de) %doc doc/as-DE.html doc/as-DE.txt doc/as-DE.ps doc/as-DE.pdf doc/as-DE.dvi
%endif

%changelog
* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.45.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.44.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.43.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.42.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.41.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.40.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.39.bld134
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.38.bld134
- Update to latest upstream snapshot.

* Mon Apr 30 2018 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.37.bld133
- Update to latest upstream snapshot.

* Fri Mar 30 2018 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.36.bld131
- Update to latest upstream snapshot.
- Update s390x sysdefs.h patch.
- Do not build German documentation on EL7 due to lack of tex(german.sty).

* Thu Mar 01 2018 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.35.bld126
- Update to latest upstream snapshot.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.34.bld115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.33.bld115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.32.bld115
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.31.bld115
- Update to latest upstream snapshot.
- Removed patch for CDP180[456], now provided upstream.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.30.bld114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Dan Horák <dan[at]danny.cz> 1.42-0.29.bld114
- update the sysdefs patch for s390(x) and ia64

* Sat Jan 07 2017 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.28.bld114
- Updated to latest upstream snapshot.
- Added patch for CDP180[456] scal instruction.

* Sun Jul 31 2016 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.27.bld110
- Updated to latest upstream snapshot.
- Remove aarch64 patch, now upstream.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-0.26.bld97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.25.bld97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.24.bld97
- Updated to latest upstream snapshot.
- Use %%license.

* Fri Sep 12 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.42-0.23.bld93
- Added AArch64 definitions

* Fri Aug 29 2014 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.21.bld93
- Updated to latest upstream snapshot.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.21.bld92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.20.bld92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.19.bld92
- Updated to latest upstream snapshot, which fixes a problem with
  string quoting.

* Wed Mar 05 2014 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.18.bld91
- Fixed problem building on EL6; don't require tex(german.sty) on EL6.

* Wed Mar 05 2014 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.17.bld91
- Updated to latest upstream snapshot.

* Thu Aug 15 2013 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.16.bld89
- Updated to latest upstream snapshot.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.15.bld88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.14.bld88
- Updated to latest upstream snapshot.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.13.bld84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.12.bld84
- Updated to latest upstream snapshot.
- Added BuildRequires for tex(german.sty), formerly part of texlive-texmf,
  but post-F18 moved into texlive-german.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.11.bld83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.11.bld83
- updated to latest upstream snapshot

* Sat Jan 21 2012 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.10.bld82
- updated to latest upstream snapshot

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.9.bld81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.8.bld81
- updated to latest upstream snapshot

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-0.7.bld79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.6.bld79
- updated to latest upstream snapshot
- upstream has removed doc_DE/dina4.sty, so we no longer need to use
  a cleaned tarball

* Sat Apr 24 2010 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.5.bld77
- rebuilding because cvs-import.sh failed to import one patch for F-12

* Wed Apr 21 2010 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.4.bld77
- use cleaned source tarball until upstream removes doc_DE/dina4.sty
- removed strcpy() patch

* Tue Apr 20 2010 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.3.bld77
- updated to latest upstream snapshot
- removed doc_DE/dina4.sty due to unacceptable license
- added lang tag for de docs
- changed BuildRequires for latex to a virtual provides name

* Mon Apr 12 2010 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.2.bld75
- removed obsolete PPC64 patch

* Sun Apr 11 2010 Eric Smith <brouhaha@fedoraproject.org> 1.42-0.1.bld75
- spec based on earlier review request 240807
- updated to latest upstream
- fixed strcpy() usage bug in KillPrefBlanks
