%global nightly 20150709
%global _legacy_common_support 1

Name: z88dk
# We use post-release snapshot versioning, because the source code has no idea
# what version it is supposed to be. (README.1st still claims to be from version
# 1.9 when they already released 1.10 and 1.10.1.)
Version: 1.10.1
Release: 32%{?nightly:.%{nightly}cvs}%{?dist}
Summary: A Z80 cross compiler
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License: ClArtistic
URL: http://www.z88dk.org/
%if 0%{?nightly}
Source: http://nightly.z88dk.org/z88dk-%{nightly}.tgz
%else
Source: http://downloads.sourceforge.net/z88dk/z88dk-%{version}.tgz
%endif
Patch0: z88dk-1.10-makefile-usr-share.patch
Patch1: z88dk-1.10-64bit.patch
Patch2: z88dk-1.10-makefile-flags.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libxml2-devel
BuildRequires: perl-generators
# FIXME: sort out the file conflict (#823174)
Conflicts: z80asm

%description
z88dk is a Z80 cross compiler capable of generating binary files for a variety
of Z80 based machines (such as the ZX81, Spectrum, Jupiter Ace and some TI
calculators).

%prep
%setup -q -n z88dk
# Put files in %%{_datadir}/z88dk rather than /usr/lib/z88dk
# Also support DESTDIR in install-libs
%patch -P0 -p1
# 64-bit fixes
%patch -P1 -p1
# Fix improper use of CFLAGS and LDFLAGS in the makefiles
%patch -P2 -p1
find . -depth -name CVS -type d -exec rm -rf {} \;
# Separate manpages from other docs and fix their permissions
mv doc/netman .
chmod 644 netman/man3z/*
# Fix files with wrong line endings and bad permissions
find doc examples src -type f -exec sed -i -e 's/\r*$//' {} \;
find doc examples src -type f -exec chmod 644 {} \;

%build
export Z80_OZFILES=%{_builddir}/z88dk/lib/
export ZCCCFG=%{_builddir}/z88dk/lib/config/
export PATH=%{_builddir}/z88dk/bin:$PATH
%global build_type_safety_c 0
export CC="gcc -std=gnu89"
export CFLAGS="%{optflags}"
%{?__global_ldflags:export LDFLAGS="%{__global_ldflags}"}
# Note: do not use %%{?_smp_mflags} with make because the Makefiles don't support parallel builds
make clean
make
# libs are target libraries, they won't build with host CFLAGS/LDFLAGS
unset CFLAGS
export CFLAGS
unset LDFLAGS
export LDFLAGS
make libs

%install
export Z80_OZFILES=%{_datadir}/z88dk-%{version}/lib/
export ZCCCFG=%{_datadir}/z88dk-%{version}/lib/config/
make install install-libs DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man3z
cp -p netman/man3z/* %{buildroot}%{_mandir}/man3z

%files
%doc doc/*.html doc/*.gif doc/copt.man
%doc doc/compile.txt doc/cpc.txt doc/embedded.txt doc/error.txt doc/farmods.txt
%doc doc/fileio.txt doc/lib3d.txt doc/options.txt doc/packages.txt
%doc doc/platforms.txt doc/retarget.txt doc/stdio.txt doc/ti.txt doc/z80asm.txt
%doc doc/zxscrdrv.txt
%doc EXTENSIONS LICENSE
# Examples might be worth putting in subpackage
%doc examples
%{_bindir}/appmake
%{_bindir}/asmpp.pl
%{_bindir}/copt
%{_bindir}/sccz80
%{_bindir}/z*
%{_datadir}/z88dk/
%{_mandir}/man3z/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-32.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.1-31.20150709cvs
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-30.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-29.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 31 2023 Florian Weimer <fweimer@redhat.com> - 1.10.1-2820150709:.%{nightly}cvs}
- Set build_type_safety_c to 0 (#2166990)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-27.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb  3 2023 DJ Delorie <dj@redhat.com> - 1.10.1-26.20150709cvs
- Build in C89 mode (#2166990)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-25.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-24.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-23.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-22.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-21.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.10.1-20.20150709cvs
- enable common symbols to fix FTBFS (#1800290)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-19.20150709cvs
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-18.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-17.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-16.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-15.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-14.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-13.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-12.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-11.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-10.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-9.20150709cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.10.1-8.20150709cvs
- update to 20150709 nightly
- don't use make -e because it also overwrites += commands (FTBFS #1240091)
- BuildRequires: libxml2-devel
- fix improper use of CFLAGS and LDFLAGS in the makefiles
- update file list (add new binary asmpp.pl)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-7.20150221cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.10.1-6.20150221cvs
- update to 20150221 nightly (fixes licensing issue #967408 and FTBFS #1037409)
- drop z80asm hunks of 64bit patch, fixed upstream
- rebase makefile-usr-share patch
- Conflicts: z80asm until we sort out the file conflict (#823174)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.10.1-1
- update to 1.10.1 (#888202, bugfix release)

* Tue Nov 06 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.10-1
- update to 1.10 (#873591)
- clean up specfile
- use __global_ldflags if set
- rediff (unfuzz) makefile-usr-share patch
- drop makefile-fixes patch (last remaining issue fixed upstream)
- rebase 64bit patch (some parts fixed upstream)
- drop upstreamed getline-name-conflict patch

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9-1
- update to 1.9 (#512391)
- update 64bit patch (one issue fixed upstream, many left)

* Fri Apr 10 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8-3
- fix name conflict with the getline function in POSIX 2008

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8-1
- update to 1.8
- update makefile-fixes patch (most issues fixed upstream, only one left)
- update z88make.patch and rename to z88dk-1.8-makefile-usr-share.patch
- remove redundant sed (already covered by above patch)
- use DESTDIR instead of makeinstall macro (fixes buildroot in .cfg files)

* Sat Feb 9 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7-3
- rebuild for GCC 4.3

* Fri Dec 7 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7-2
- patch for 64-bit issues (#185511)
- drop ExcludeArch for 64-bit architectures (#185511)

* Thu Dec 6 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7-1
- update to 1.7
- use preferred SF URL
- mention TI calculators in description
- mkdir buildroot in install
- don't try to build target libs with host CFLAGS
- fix buggy makefiles leading to silently missing libraries

* Thu Sep 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.6-11.1
- no ppc64

* Thu Sep 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.6-11
- fix license tag (Artistic clarified)

* Thu Oct 5 2006 Christian Iseli <Christian.Iseli@licr.org> 1.6-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.6-9
- rebuild
- minor spec file changes

* Thu Mar 9 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.6-8
- Added ExcludeArch for ia64

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.6-7
- Add ExcludeArch for x86_64 machines

* Mon Oct 17 2005 Paul Howarth <paul@city-fan.org> - 1.6-6
- Use full URL for upstream tarball location
- Don't use macros in build-time command paths (see #170506 for discussion)
- Tarball expands to directory z88dk, not z88dk-%%{version}

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.6-5
- Modified the spec file to fix the rpmlint problems

* Wed Sep 14 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.6-4
- Add diff for makefile and patch aspect to spec
- rebuilt

* Wed Sep 14 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.6-3
- Fixed the spec file as it was constantly looking to /var/tmp!
- Fixed the source to point to /usr/share/z88dk for configs
- Removed `pwd` as it was causing problems

* Tue Sep 13 2005 Paul Howarth <paul@city-fan.org> - 1.6-2
- Use macros consistently
- Clean out buildroot in %%install rather than %%prep
- Include additional docs
- Tidy summary and description
- Honor %%{optflags}
- Remove CVS cruft
- Separate manpages from rest of docs
- Put target libraries, include files etc. under %%{_datadir}, not /usr/lib
- No scriptlets needed
- Fix file permissions and line endings
- Remove vendor and packager tags
- Use "Artistic" in license tag

* Tue Sep 13 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk>
- Fixes to spec file

* Mon Sep 12 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk>
- initial import and rpm builds
