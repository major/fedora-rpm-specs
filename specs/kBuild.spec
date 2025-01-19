%global svn_revision 3605
%global svn_date 20240424

Name:           kBuild
Version:        0.1.9998%{?svn_revision:.r%{svn_revision}}
Release:        4%{?svn_date:.%{svn_date}}%{?dist}
Summary:        A cross-platform build environment

# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
# most tools are from NetBSD, some are from FreeBSD,
# and make and sed are from GNU
URL:            http://svn.netlabs.org/kbuild
#Generated with kBuild-snapshot.sh
Source0:        kBuild-r%{svn_revision}.%{svn_date}.tar.gz
Patch0:         kBuild-0.1.3-escape.patch
Patch1:         kBuild-pthread.patch
Patch6:         kbuild-dummy_noreturn.diff
Patch8:         kBuild-0.1.9998-portme.patch
Patch10:        assert.patch
Patch11:        relax_automake_version.patch
Patch12:        kBuild-configure-c99.patch
Patch13:        kBuild-c99.patch
Patch14:        changeset_3572.diff
Patch15:        changeset_trunk_3566.diff
Patch16:        kBuild-c99-2.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  texinfo
BuildRequires:  byacc

%description
This is a GNU make fork with a set of scripts to simplify
complex tasks and portable versions of various UNIX tools to
ensure cross-platform portability.

It is used mainly to build VirtualBox packages for RPM Fusion
repository.


%prep
%dnl %setup -q -n %{name}-%{version}%{?patchlevel:-%{patchlevel}}
%setup -q -n %{name}
%patch -P0 -p1 -b .escape
%patch -P1 -p1 -b .pthreads
%patch -P6 -p1 -b .dummy_noreturn
%ifarch ppc64
%if 0%{?rhel} && 0%{?rhel} < 7
# Found the reason why compile fails in detection of powerpc64 in centos 6
# kBuild/src/lib/kStuff/include/k/kDefs.h:356:4: error: #error "Port Me or define K_ENDIAN."
# hack for gcc < 4.6 and ppc64 only
# https://stackoverflow.com/a/40675229/778517
%patch -P8 -p1 -b .portme
%endif
%endif
%patch -P10 -p1 -b .portme3
%if 0%{?rhel} && 0%{?rhel} <= 7
%patch -P11 -p1
%endif
%patch -P12 -p1
%patch -P13 -p1
%if 0%{?rhel} && 0%{?rhel} <= 7
# we need revert this 2 commits to build VBox 6 on el7
%patch -P14 -p1 -R -b .revert
%patch -P15 -p1 -R -b .revert2
%endif
%patch -P16 -p0

%build
echo KBUILD_SVN_URL := http://svn.netlabs.org/repos/kbuild/trunk  >  SvnInfo.kmk
echo KBUILD_SVN_REV := %{svn_revision} >>  SvnInfo.kmk

%define bootstrap_mflags %{_smp_mflags} \\\
        CFLAGS="%{optflags}"            \\\
        KBUILD_VERBOSE=2                \\\
        KBUILD_VERSION_PATCH=9998

%define mflags %{bootstrap_mflags}      \\\
        NIX_INSTALL_DIR=%{_prefix}      \\\
        BUILD_TYPE=release              \\\
        MY_INST_MODE=0644               \\\
        MY_INST_BIN_MODE=0755

# The bootstrap would probably not be needed if we depended on ourselves,
# yet it is not guarranteed that new versions are compilable with older
# kmk versions, so with this we are on a safer side
find -name config.log -delete
kBuild/env.sh --full make -f bootstrap.gmk %{bootstrap_mflags}
kBuild/env.sh kmk %{mflags} rebuild


%install
export KBUILD_VERBOSE=2
kBuild/env.sh kmk %{mflags} PATH_INS=%{buildroot} install
# These are included later in files section
rm -r %{buildroot}%{_docdir}
mkdir -p %{buildroot}/%{_mandir}/man1
pod2man -c 'kBuild for Fedora/EPEL GNU/Linux' \
  -r kBuild-%{version} ./dist/debian/kmk.pod > %{buildroot}/%{_mandir}/man1/kmk.1


%files
%doc ChangeLog kBuild/doc/QuickReference*
%license COPYING kBuild/doc/COPYING-FDL-1.3
%{_bindir}/*
%{_datadir}/kBuild
%{_mandir}/man1/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3605-4.20240424
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.9998.r3605-3.20240424
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3605-2.20240424
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3605-1.20240424
- Update to Revision 3605

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3589-5.20230220
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3589-4.20230220
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Florian Weimer <fweimer@redhat.com> - 0.1.9998.r3589-3.20230220
- Fix another C compatibility issue (#2154544)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3589-2.20230220
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3589-1.20230220
- new version
- revert changeset 3572 and 3566 to build VBox 6 on el7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3572-3.20221024
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 0.1.9998.r3572-2.20221024
- C99 compatibility fixes (#2154544)

* Mon Oct 24 2022 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3572-1.20221024
- Update to r3572.20221024
- Allow build with automake 1.13.4 on epel7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3564-2.20220308
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 08 2022 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3564-1.20220308
- Update kBuild to r3564.20220308

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-9.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-8.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-7.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-6.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 0.1.9998.r3296-5.20190122
- Use strsignal, not sys_siglist

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-4.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3296-3.20190122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3296-2.20190122
- Trust in the upstream that has the correct support for aarch64 and ppc64le

* Mon Feb 11 2019 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3296-1.20190122
- Update to 0.1.9998.r3296-1.20190122

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3290-2.20190106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3290-1.20190106
- Update to 0.1.9998.r3290-1.20190106
- Add manpage (copied from Debian IIRC)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3129-4.20180106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3129-3.20180106
- Fix build on el6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998.r3129-2.20180106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Sérgio Basto <sergio@serjux.com> - 0.1.9998.r3129-1.20180106
- Update kBuild to svn rev 3129
- New versioning, we need define svn version that we may need

* Sun Dec 03 2017 Sérgio Basto <sergio@serjux.com> - 0.1.9998-16.r3127
- Fix one implicit-function-declaration

* Sat Dec 02 2017 Sérgio Basto <sergio@serjux.com> - 0.1.9998-15.r3127
- Update kBuild to svn rev 3127
- arm and kbuild-wrong-memset patches fixed in upstream way
        deleted:    kBuild-0.1.98-arm.patch
        deleted:    kbuild-wrong-memset.patch
- Rebased aarch64 not sure if needed, ppc64le much more simple
        modified:   kBuild-0.1.9998-aarch64.patch
        modified:   kBuild-0.1.9998-ppc64le.patch
        modified:   kBuild-pthread.patch
- kbuild-glob.patch fixes build in rawhide (F28)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998-14.r3050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998-13.r3050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Sérgio Basto <sergio@serjux.com> - 0.1.9998-12.r3025
- Update kBuild to revison 3025
- Upstream already fixed these 2:
  deleted:    kBuild-0.1.9998-glob.patch
  deleted:    kbuild-PKMKCCEVALPROG.patch
- Rebased:
  modified:   kBuild-0.1.98-arm.patch
  modified:   kBuild-0.1.9998-aarch64.patch
  modified:   kBuild-0.1.9998-ppc64le.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998-11.r2814
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Sérgio Basto <sergio@serjux.com> - 0.1.9998-10.r2814
- Fix el6 build

* Tue Jul 26 2016 Sérgio Basto <sergio@serjux.com> - 0.1.9998-9.r2814
- add BR:bison

* Fri Apr 29 2016 Sérgio Basto <sergio@serjux.com> - 0.1.9998-8.r2814
- Update kBuild to svn rev 2814

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9998-7.r2784
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.9998-6.r2784
- Add support for aarch64 (#1291091).

* Mon Jun 22 2015 Sérgio Basto <sergio@serjux.com> - 0.1.9998-5.r2784
- Update to trunk HEAD version.
- Rework patch for glob issue.
- Add kBuild-0.1.9998-ppc64le.patch to add support for ppc64le.
- Add kbuild-wrong-memset.patch, fix one warning.
- Fix License macro.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9998-4.r2730
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9998-3.r2730
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9998-2.r2730
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Sérgio Basto <sergio@serjux.com> - 0.1.9998-1.r2730
- Update to trunk HEAD version, have a fix for gcc >= 4.7 (http://trac.netlabs.org/kbuild/ticket/112)
- Drop kBuild-0.1.5-dprintf.patch patch, upstream source also have a fix in their own way.
- add kBuild-0.1.9998-gl_.patch to fix a regression on compiling in Linux
  (http://trac.netlabs.org/kbuild/ticket/117), partially reverses changeset 2702 . 

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.98-6.r1
- Bulk sad and useless attempt at consistent SPEC file formatting
- Fix ARM build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.98-5.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.98-4.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.98-3.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.98-2.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.1.98-1.r1
- Later patchset

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-7.p2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-6.p2
- Fix build
- Update to later patch level

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-6.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-5.p1
- Update to later patchlevel to support VirtualBox 2.2.0

* Mon Apr 13 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-4
- Fix typoes (Robert P. J. Day, #495393)
- Comment out the colliding dprintf

* Sun Mar 1 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-3
- Fix up BRs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-1
- Update to new upstream release

* Tue Dec 30 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.1.5-0.1.20081106svn
- Update to build VirtualBox OSE 2.1.0

* Fri Sep 19 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.1.4-1
- New upstream release

* Thu Aug 28 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.1.3-2
- Add gettext-devel to BRs for autopoint

* Sun Aug 17 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.1.3-1
- New upstream version
- Install into FHS hierarchy
- Honour optflags
- No need to be arch specific

* Tue Oct 30 2007 Till Maas <opensource till name> - 0.1.0-0.3.20070627svn
- add support for x86_64
- add BR: autoconf, automake

* Wed Jun 27 2007 Till Maas <opensource till name> - 0.1.0-0.2.20070627svn
- Update to a new version
- just copy the bin files to %%{_libexecdir}, kmk install does not work

* Sun Feb 18 2007 Till Maas <opensource till name> - 0.1.0-0.1.20070218svn
- Initial spec for fedora extras
