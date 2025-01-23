Name:           perl-PAR-Packer
Version:        1.063
Release:        5%{?dist}
Summary:        PAR Packager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PAR-Packer
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/PAR-Packer-%{version}.tar.gz
Source1:        extract_icon
Source2:        tkpp.desktop
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# myldr/Makefile.PL, myldr/file2c.pl is executed
BuildRequires:  perl(inc::Module::Install) >= 0.92
BuildRequires:  perl(Compress::Zlib) >= 1.3
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Archive::Zip) >= 1
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.05
BuildRequires:  perl(Getopt::ArgvFile) >= 1.07
BuildRequires:  perl(Module::ScanDeps) >= 1.21
BuildRequires:  perl(PAR) >= 1.020
BuildRequires:  perl(PAR::Dist) >= 0.22
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Module::Signature)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(PAR::SetupTemp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
Requires:       perl(Archive::Zip) >= 1
Requires:       perl(Compress::Zlib) >= 1.3
Requires:       perl(File::Temp) >= 0.05
Requires:       perl(Getopt::ArgvFile) >= 1.07
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Module::ScanDeps) >= 1.21
Requires:       perl(PAR) >= 1.020
Requires:       perl(PAR::Dist) >= 0.22
# This package bundles libperl.so into %%{_bindir}/parl and when executing it
# after upgrading Perl, Perl version checks in Config fail. Thus we need to
# require the same version used when building this package. Bug #1470542.
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Provides:       bundled(libperl) = %(eval "`perl -V:version`"; echo ${version:-0})

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Zip|File::Temp|Getopt::ArgvFile|Module::ScanDeps|PAR\\)\\s*$

%description
This module implements the App::Packer::Backend interface, for generating
stand-alone executables, perl scripts and PAR files.

%package Tk
Summary:        Front-end to pp written in Perl/Tk
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::Temp)
Requires:       perl(Tk::ColoredButton)
Requires:       perl(Tk::EntryCheck)
Requires:       perl(Tk::Getopt)
Requires:       perl(Tk::Pod)

%description Tk
Tkpp is a GUI front-end to pp, which can turn perl scripts into standalone
PAR files, perl scripts or executables.

%prep
%setup -q -n PAR-Packer-%{version}
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
# DEBUG variable needed to disable stripping binary
DEBUG=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
# The Makefile is not parallel-safe.
%global _smp_build_ncpus 1
%{make_build}

%install
%{make_install}
# Ensure pp(1) manpage points to the documentation from pp.pm
ln -sf %{_mandir}/man3/pp.3pm %{buildroot}%{_mandir}/man1/pp.1
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install desktop file
%{SOURCE1} < script/tkpp | convert gif:- tkpp.png
install -m644 -D tkpp.png \
    %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/tkpp.png
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%check
make test

%files
%license LICENSE
%doc AUTHORS Changes README
%{perl_vendorlib}/App*
%{perl_vendorlib}/PAR*
%{perl_vendorlib}/pp*
%{_bindir}/par.pl
%{_bindir}/parl
%{_bindir}/parldyn
%{_bindir}/pp
%{_mandir}/man1/par*.1.*
%{_mandir}/man1/pp*.1.*
%{_mandir}/man3/App::*
%{_mandir}/man3/PAR::*
%{_mandir}/man3/pp*

%files Tk
%{_bindir}/tkpp
%{_mandir}/man1/tkpp.1.*
%{_datadir}/applications/tkpp.desktop
%{_datadir}/icons/hicolor/32x32/apps/tkpp.png

%changelog
* Tue Jan 21 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1.063-5
- Rebuild for Perl 5.40.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.063-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.063-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.063-2
- Perl 5.40 rebuild

* Mon Mar 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.063-1
- 1.063 bump (rhbz#2269706)

* Wed Mar 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.062-1
- 1.062 bump (rhbz#2267917)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.061-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.061-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.061-1
- 1.061 bump (rhbz#2254730)

* Thu Nov 30 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.059-2
- Rebuild for Perl 5.38.2

* Fri Jul 21 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.059-1
- 1.059 bump (rhbz#2224383)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-2
- Perl 5.38 rebuild

* Mon Jun 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-1
- 1.058 bump

* Wed Apr 26 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.057-3
- Rebuild for Perl 5.36.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.057-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.057-1
- 1.057 bump

* Tue Sep 06 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.056-1
- 1.056 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.055-1
- 1.055 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.054-4
- Perl 5.36 rebuild

* Wed Mar 16 2022 Paul Howarth <paul@city-fan.org> - 1.054-3
- Re-rebuild for Perl 5.34.1 (#2064642)

* Wed Mar 16 2022 Paul Howarth <paul@city-fan.org> - 1.054-2
- Rebuild for Perl 5.34.1

* Mon Jan 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.054-1
- 1.054 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.052-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.052-1
- 1.052 bump

* Mon Nov 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.051-1
- 1.051 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.050-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.050-3
- Perl 5.32 rebuild

* Tue Jun 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.050-2
- Rebuild for Perl 5.30.3

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.050-1
- 1.050 bump

* Wed Mar 11 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.049-5
- Add BR perl(blib)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.049-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.049-3
- Rebuild for Perl 5.30.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.049-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.049-1
- 1.049 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-2
- Perl 5.30 rebuild

* Tue Apr 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-1
- 1.048 bump

* Tue Apr 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-5
- Rebuild for Perl 5.28.2

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.047-4
- Remove obsolete requirements for %%post/%%postun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Paul Howarth <paul@city-fan.org> - 1.047-2
- Rebuild for Perl 5.28.1

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-1
- 1.047 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-2
- Perl 5.28 rebuild

* Wed Jun 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-1
- 1.045 bump

* Thu Jun 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.044-1
- 1.044 bump

* Tue Apr 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.043-1
- 1.043 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.041-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.041-2
- Rebuilt for switch to libxcrypt

* Thu Nov 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.041-1
- 1.041 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.040-1
- 1.040 bump

* Mon Oct 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.039-1
- 1.039 bump

* Wed Sep 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-8
- Rebuild for Perl 5.26.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.037-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.037-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.037-5
- Require the same Perl version used for building (bug #1470542)

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 1.037-3
- Convert icon file to PNG format

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-2
- Perl 5.26 rebuild

* Mon May 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-1
- 1.037 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-1
- 1.036 bump

* Mon Jul 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.035-1
- 1.035 bump

* Tue Jul 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.034-1
- 1.034 bump

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.033-1
- 1.033 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.032-2
- Perl 5.24 rebuild

* Mon May 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.032-1
- 1.032 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 1.031-1
- 1.031 bump

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.030-1
- 1.030 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Petr Šabata <contyk@redhat.com> - 1.029-1
- 1.029 bump

* Thu Nov 19 2015 Petr Šabata <contyk@redhat.com> - 1.028-1
- 1.028 bump

* Mon Jul 20 2015 Petr Šabata <contyk@redhat.com> - 1.026-1
- 1.026 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.025-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.025-2
- Perl 5.22 rebuild

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 1.025-1
- 1.025 bump

* Mon Dec 01 2014 Petr Šabata <contyk@redhat.com> - 1.024-2
- Use pp(3pm) docs for pp(1), as was most likely intended (#1163390)

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 1.024-1
- 1.024 bump

* Tue Nov 04 2014 Petr Šabata <contyk@redhat.com> - 1.023-1
- 1.023 bump

* Mon Sep 29 2014 Petr Šabata <contyk@redhat.com> - 1.022-1
- 1.022 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Petr Šabata <contyk@redhat.com> - 1.019-1
- 1.019 bugfix bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Petr Šabata <contyk@redhat.com> - 1.018-1
- 1.018 bump

* Thu Dec 05 2013 Petr Pisar <ppisar@redhat.com> - 1.017-1
- 1.017 bump

* Mon Dec 02 2013 Petr Pisar <ppisar@redhat.com> - 1.016-1
- 1.016 bump

* Fri Oct 11 2013 Petr Šabata <contyk@redhat.com> - 1.015-1
- 1.015 bugfix bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.014-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Petr Pisar <ppisar@redhat.com> - 1.014-1
- 1.014 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.013-1
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Petr Pisar <ppisar@redhat.com> - 1.012-2
- Poke icon cache

* Mon Dec 05 2011 Petr Pisar <ppisar@redhat.com> - 1.012-1
- 1.012 bump

* Fri Dec 02 2011 Petr Pisar <ppisar@redhat.com> - 1.011-1
- 1.011 bump (fixes CVE-2011-4114)
- Specify run-time dependencies versions
- Sub-package tkpp into perl-PAR-Packer-Tk
- Create Free Desktop menu entry

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.010-2
- Perl mass rebuild

* Thu Jul 14 2011 Petr Sabata <contyk@redhat.com> - 1.010-1
- 1.010 bump
- Removing defattr

* Fri May  6 2011 Petr Sabata <psabata@redhat.com> - 1.009-1
- 1.009 bump
- Removing buildroot garbage

* Fri Feb 25 2011 Petr Pisar <ppisar@redhat.com> - 1.008-3
- Do not strip binaries

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Petr Sabata <psabata@redhat.com> - 1.008-1
- New upstream release, v1.008
- New source URL

* Wed Sep 29 2010 jkeating - 1.007-2
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Petr Sabata <psabata@redhat.com> - 1.007-1
- New release, v1.007

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 1.005-2
- rebuild

* Fri Jun 11 2010 Petr Sabata <psabata@redhat.com> - 1.005-1
- Update to the latest release, fixing #602933

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.991-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.991-5
- rebuild against perl 5.10.1

* Wed Sep 23 2009 Stepan Kasal <skasal@redhat.com> - 0.991-4
- too hard to build without stripping (#524894)

* Mon Sep 21 2009 Stepan Kasal <skasal@redhat.com> - 0.991-3
- patch to use $RPM_OPT_FLAGS
- patch to submit the third parameter to open()

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.991-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.991-1
- Specfile autogenerated by cpanspec 1.78.
