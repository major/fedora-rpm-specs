# we don't want to either provide or require anything from _docdir, per policy
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/#_arch_specific_extensions_to_scripting_languages
%global __provides_exclude_from ^%{_docdir}/.*$
%global __requires_exclude_from ^%{_docdir}/.*$

%bcond_without tests

Name:           debhelper
Version:        13.11.6
Release:        5%{?dist}
Summary:        Helper programs for debian/rules

License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/debhelper
Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch2:         no_layout_deb.patch
BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  man-db
BuildRequires:  fakeroot
BuildRequires:  dpkg-dev >= 1.18.0
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make
# https://lists.debian.org/debian-devel/2021/05/msg00141.html
BuildRequires:  perl(:VERSION) >= 5.28
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  po4a
BuildRequires:  sed
# Run-time:
# PerlIO::gzip || gzip
BuildRequires:  gzip
# Carp not used at tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Digest::SHA not used at tests
BuildRequires:  perl(Dpkg::Arch)
# Dpkg::BuildProfiles not used at tests
# Dpkg::Changelog::Parse not used at tests
# Dpkg::Deps not used at tests
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Dpkg::BuildFlags)
BuildRequires:  perl(Dpkg::Changelog::Debian)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod)

Requires:       binutils
Requires:       dh-autoreconf >= 17
Requires:       dpkg >= 1.18.0
Requires:       dpkg-dev >= 1.18.2
Requires:       dpkg-perl >= 1.17.14
# PerlIO::gzip || gzip
Requires:       gzip
Requires:       perl(Carp)
Requires:       perl(Digest::SHA)
Requires:       perl(Dpkg::Arch)
Requires:       perl(Dpkg::BuildProfiles)
Suggests:       perl(Dpkg::BuildFlags)
Suggests:       perl(Dpkg::Changelog::Debian)
Requires:       perl(Dpkg::Changelog::Parse)
Requires:       perl(Dpkg::Deps)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       po-debconf
#Suggests:       dh-make
#Provides: dh-sequence-dwz,
#          dh-sequence-installinitramfs,
#          dh-sequence-systemd,
#Provides: dh-systemd
#Depends: autotools-dev,
#         dh-strip-nondeterminism (>= 0.028~),
#         dwz,
#         file (>= 3.23),
#         man-db,
#         ${misc:Depends},
#         ${perl:Depends}
#        cmake (<< 3.9~),
#        meson (<< 0.40.0~),

%description
A collection of programs that can be used in a debian/rules file to
automate common tasks related to building Debian packages. Programs
are included to install various files into your package, compress
files, fix file permissions, integrate your package with the Debian
menu system, debconf, doc-base, etc. Most Debian packages use debhelper
as part of their build process.

%prep
#debug
echo "debug:"
dpkg-architecture -qDEB_BUILD_GNU_TYPE
dpkg-architecture -qDEB_HOST_GNU_TYPE
dpkg --print-architecture
cc -dumpmachine

#%%setup -q -n %%{name}
%setup -q -n work
%patch -P2 -p1 -b .no-debian-layout

%build
%make_build build

%install
%make_install

# Use debhelper to install (man-pages of) debhelper...
  
./run dh_installman -P %{buildroot} --verbose -p debhelper

# Add man-pages to a .lang file:
# We cannot use "find_lang --with-man" because it only handle
# single man-page -- we have many

rm -f debhelper-mans.lang
for lang in de es fr pt ja; do
    for level in 1 7; do
        # Append to .lang file
        # Replace buildroot with the lang prefix, append '*' (for gzip, etc.)
        find %{buildroot}%{_mandir}/$lang/man$level -type f -o -type l | sed "
                s:^%{buildroot}:%%lang($lang) :
                s:\$:*:
                " >> debhelper-mans.lang
    done
done


%if %{with tests}
%check
make test
%endif


%files -f debhelper-mans.lang
%doc examples/ doc/
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_bindir}/dh*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/autoscripts
%{perl_vendorlib}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 02 2023 Sérgio Basto <sergio@serjux.com> - 13.11.6-1
- Update debhelper to 13.11.6

* Mon Aug 14 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 13.11.5-1
- Update to 13.11.5 (#2231971)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Sérgio Basto <sergio@serjux.com> - 13.11.4-2
- Migrate to SPDX license format

* Sun Jan 22 2023 Sérgio Basto <sergio@serjux.com> - 13.11.4-1
- Update debhelper to 13.11.4 (#2133214)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 02 2022 Sérgio Basto <sergio@serjux.com> - 13.9.1-1
- Update debhelper to 13.9.1 (#2103468)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 13.7.1-3
- Perl 5.36 rebuild

* Wed May 25 2022 Jitka Plesnikova <jplesnik@redhat.com> - 13.7.1-2
- Add missing BR: perl(JSON::PP) for tests

* Fri Apr 22 2022 Sérgio Basto <sergio@serjux.com> - 13.7.1-1
- Update debhelper to 13.7.1 (#2034267)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Sérgio Basto <sergio@serjux.com> - 13.5.2-3
- changing "use v5.28" in Dh_lib.pm to "use v5.24". (#2031534)

* Tue Nov 02 2021 Sérgio Basto <sergio@serjux.com> - 13.5.2-2
- Make clear that we need Perl 5.28 which not exist in rhel 8, Perl there is 5.26

* Mon Nov 01 2021 Sérgio Basto <sergio@serjux.com> - 13.5.2-1
- Update debhelper to 13.5.2 (#1994808)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 13.3.4-2
- Perl 5.34 rebuild

* Thu May 13 2021 Sérgio Basto <sergio@serjux.com> - 13.3.4-1
- Update to 13.3.4 (#1792739)

* Mon Feb 15 2021 Sérgio Basto <sergio@serjux.com> - 12.7.3-8
- Build with fix on dpkg (#1923609) and (#1714442)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 12.7.3-5
- Perl 5.32 rebuild

* Thu Mar 12 2020 Petr Pisar <ppisar@redhat.com> - 12.7.3-4
- Specify all dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Sérgio Basto <sergio@serjux.com> - 12.7.3-2
- html2text is not needed since version 9.20130604

* Sun Jan 05 2020 Sérgio Basto <sergio@serjux.com> - 12.7.3-1
- Update to 12.7.3 (#1763530)

* Tue Oct 08 2019 Sérgio Basto <sergio@serjux.com> - 12.6.1-1
- Update to 12.6.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 11.4-4
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Sérgio Basto <sergio@serjux.com> - 11.4-2
- Skip failing test on arm, workaround (#1134914)

* Fri Sep 21 2018 Sérgio Basto <sergio@serjux.com> - 11.4-1
- Update to 11.4 (#1536769)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 11.1.2-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Sérgio Basto <sergio@serjux.com> - 11.1.2-1
- Update to 11.1.2 (#1532223)

* Mon Jan 08 2018 Sérgio Basto <sergio@serjux.com> - 11.1.1-1
- Update to 11.1.1

* Sun Jan 07 2018 Sérgio Basto <sergio@serjux.com> - 11.1-1
- Update to 11.1
- Add no_layout_deb.patch

* Sun Oct 01 2017 Sérgio Basto <sergio@serjux.com> - 10.9-2
- Print also dpkg --print-architecture to debug FTBFS in armv7 and ppc64le

* Wed Sep 20 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 10.9-1
- Update to 10.9 (#1493320)

* Sun Sep 10 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 10.8-1
- Update to 10.8 (#1490078)

* Wed Aug 02 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 10.7.2-1
- Update to 10.7.2 (#1477385)

* Tue Aug 01 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 10.7.1-1
- Update to 10.7.1 (#1448667)

* Mon Jul 31 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 10.7-1
- Update to 10.7 (#1448667)
- Drop patch0 pod2man, now, already have --utf8
- Drop patch2 , upstream wrote to me that is fixed
  https://github.com/Debian/debhelper/commit/580bc09d41ddc8542515f50d40ff8c8477711d3d#commitcomment-22972851
  (I have fixed it now for unrelated reasons)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 10.2.5-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 10.2.5-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sérgio Basto <sergio@serjux.com> - 10.2.5-1
- Update debhelper to 10.2.5 (#1293111)
- Add debhelper-10.2.5-revert-partial-580bc09d41.patch to fix build
- Add debhelper-10.2.5-ignore-dh-systemd-transitional-package.patch to fix build
- Add BuildRequires man-db and fakeroot
- Force use dpkg-dev > 1.18 it is one advise of upstream

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 9.20150628-4
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.20150628-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Petr Pisar <ppisar@redhat.com> - 9.20150628-2
- Specify all dependencies (bug #1272893)

* Mon Jul 13 2015 Sérgio Basto <sergio@serjux.com> - 9.20150628-1
- Update to 9.20150628

* Mon Jul 13 2015 Sérgio Basto <sergio@serjux.com> - 9.20150507-2
- Debhelper requires dpkg-dev (#1242630) and dpkg-dev requires dpkg-perl

* Sat Jun 20 2015 Sérgio Basto <sergio@serjux.com> - 9.20150507-1
- Update to 9.20150507

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.20150101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 9.20150101-3
- Perl 5.22 rebuild

* Sat Apr 25 2015 Sérgio Basto <sergio@serjux.com> - 9.20150101-2
- Fix, properly, pt man pages.
- Added dpkg-architecture comands to debug test failures on arm builders.

* Fri Apr 24 2015 Sérgio Basto <sergio@serjux.com> - 9.20150101-1
- Update to 9.20150101

* Fri Nov 07 2014 Petr Pisar <ppisar@redhat.com> - 9.20140613-4
- Build-require perl-podlators for pod2man tool (bug #1161450)

* Wed Sep 17 2014 Petr Pisar <ppisar@redhat.com> - 9.20140613-3
- Rebuild against perl 5.20

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 9.20140613-2
- Perl 5.20 rebuild

* Mon Jul 28 2014 Sérgio Basto <sergio@serjux.com> - 9.20140613-1
- Update to 9.20140613

* Wed Jun 11 2014 Sérgio Basto <sergio@serjux.com> - 9.20140228-1
- Update 9.20140228

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.20131227-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Sérgio Basto <sergio@serjux.com> - 9.20131227-2
- Fix %%{perl_vendorlib} directory ownership

* Mon Feb 10 2014 Sérgio Basto <sergio@serjux.com> - 9.20131227-1
- Update to 9.20131227, most of the work by Sandro Mani <manisandro@gmail.com>
- Drop debhelper-find-perm.patch, fixed upstream.
- Drop debhelper-fr.po.patch, fixed upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.20120909-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 9.20120909-2
- Perl 5.18 rebuild

* Fri May 10 2013 Oron Peled <oron@actcom.co.il> - 9.20120909-1
- Update to latest Debian/wheezy version
- Fix find_lang for man-pages
- Added 'de' to language list

* Thu Mar 29 2012 Oron Peled <oron@actcom.co.il> - 9.20120322-3
- Fix testing BR -- perl(Test::...)
- Now make test works as intended

* Wed Mar 28 2012 Oron Peled <oron@actcom.co.il> - 9.20120322-2
- Avoid auto-requires under _docdir
- Prepare for make test (but don't fail yet, as we miss perl-Test-More)

* Mon Mar 26 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 9.20120322
- New version

* Wed Sep 29 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 7.4.20-4
- Fix locale

* Fri Aug 13 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 7.4.20-3
- Fix description

* Thu May 13 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 7.4.20-2
- Include es/fr man pages
- Update to newer version from Debian Sid
- Fix package requirements

* Tue May 11 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 7.0.15-1
- First package
