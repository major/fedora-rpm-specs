Name:       perl-rpm-build-perl 
Version:    0.82
Release:    48%{?dist}
# ConstOptree/ConstOptree.pm:   GPL-2.0-or-later
# lib/B/Clobbers.pm:            GPL-2.0-or-later
# lib/B/PerlReq.pm:             GPL-2.0-or-later
# lib/B/Walker.pm:              GPL-2.0-or-later
# lib/PerlReq/Utils.pm:         LGPL-2.0-or-later
# perl.prov:        LGPL-2.0-or-later
# perl.prov.files:  GPL-2.0-or-later
# perl.req:         LGPL-2.0-or-later
# perl.req.files:   GPL-2.0-or-later
# README:       GPL-2.0-or-later
## Added with Port-to-OpSIBLING-like-macros-required-since-Perl-5..patch
# ConstOptree/ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-2.0-or-later AND LGPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
Summary:    Perl compiler back-end to extract Perl dependencies 
Url:        https://metacpan.org/release/rpm-build-perl
Source:     https://cpan.metacpan.org/authors/id/A/AT/ATOURBIN/rpm-build-perl-%{version}.tar.gz 
# Perl 5.18 compatibility, CPAN RT#85411
Patch0:     rpm-build-perl-0.82-Fix-non-deterministic-failures-on-newer-perls.patch
# Perl 5.22 compatibility, bug #1231258, CPAN RT#104885
Patch1:     rpm-build-perl-0.82-Adjust-to-perl-5.22.patch
# Perl 5.26 compatibility, CPAN RT#117350
Patch2:     rpm-build-perl-0.82-Port-to-OpSIBLING-like-macros-required-since-Perl-5..patch
# Perl 5.36 compatibility, CPAN RT#142772
Patch3:     rpm-build-perl-0.82-Adapt-tests-to-Perl-5.35.12.patch
# Perl 5.38 compatibility, bug #2222640, CPAN RT#148982
Patch4:     rpm-build-perl-0.82-Adjust-to-Perl-5.38.0.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(attributes)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(autouse)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(dumpvar.pl)
BuildRequires:  perl(encoding)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(version)

%{?perl_default_filter}
# Do not export private modules
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(fake\\)

%description
B::PerlReq is a back-end module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%package scripts
Summary:        Perl RPM prov/req scripts
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description scripts
The provides/requires scripts packaged along with perl-rpm-build-perl.

%package tests
Summary:        Tests for %{name}
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-scripts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(attributes)
Requires:       perl(AutoLoader)
Requires:       perl(autouse)
Requires:       perl(base)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(dumpvar.pl)
Requires:       perl(encoding)
Requires:       perl(fields)
Requires:       perl(File::Basename)
Requires:       perl(File::Glob)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(POSIX)
Requires:       perl(Socket)
Requires:       perl(Tie::Hash)
Requires:       perl(Tie::StdHash)
Requires:       perl(Try::Tiny)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n rpm-build-perl-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Adjust paths to executed scripts
perl -i -pe 's{-Mblib }{%{_bindir}/}' \
    %{buildroot}%{_libexecdir}/%{name}/t/{02-perlreq.t,03-perlprov.t}
# Remove the only remaining use of -Mblib so that we dont have to fake ./blib
# tree.
perl -i -pe 's{-Mblib }{}' \
    %{buildroot}%{_libexecdir}/%{name}/t/01-B-PerlReq.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc README* Changes perl5-alt-rpm-macros macros.env
%dir %{perl_vendorarch}/auto/B
%dir %{perl_vendorarch}/auto/B/ConstOptree
%{perl_vendorarch}/auto/B/ConstOptree/ConstOptree.so
%dir %{perl_vendorarch}/B
%{perl_vendorarch}/B/Clobbers.pm
%{perl_vendorarch}/B/ConstOptree.pm
%{perl_vendorarch}/B/PerlReq.pm
%{perl_vendorarch}/B/Walker.pm
%dir %{perl_vendorarch}/PerlReq
%{perl_vendorarch}/PerlReq/Utils.pm
%{perl_vendorarch}/fake.pm
%{_mandir}/man3/B::Clobbers.3*
%{_mandir}/man3/B::ConstOptree.3*
%{_mandir}/man3/B::PerlReq.3*
%{_mandir}/man3/B::Walker.3*
%{_mandir}/man3/PerlReq::Utils.3*

%files scripts
%{_bindir}/perl.clean
%{_bindir}/perl.prov
%{_bindir}/perl.prov.files
%{_bindir}/perl.req
%{_bindir}/perl.req.files
%{_mandir}/man1/perl.prov.1*
%{_mandir}/man1/perl.req.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-46
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Petr Pisar <ppisar@redhat.com> - 0.82-43
- Restore compatibility with Perl 5.38 (bug #2222640)
- Convert a license tag to SPDX
- Package the tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-41
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-38
- Perl 5.36 rebuild

* Mon May 16 2022 Petr Pisar <ppisar@redhat.com> - 0.82-37
- Perl 5.36 compatibility (CPAN RT#142772)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-34
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-31
- Perl 5.32 rebuild

* Wed Mar 11 2020 Petr Pisar <ppisar@redhat.com> - 0.82-30
- Specify all dependencies

* Mon Feb 10 2020 Petr Pisar <ppisar@redhat.com> - 0.82-29
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-26
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-23
- Perl 5.28 rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.82-22
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-18
- Perl 5.26 rebuild

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 0.82-17
- Restore compatibility with Perl 5.26.0 (CPAN RT#117350)

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-16
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-14
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 0.82-12
- Other perl-5.22 fix for GV to IV optimization (bug #1231258)

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 0.82-11
- Make adjustments for perl-5.22 compatible with older perls (bug #1231258)

* Tue Jun 16 2015 Petr Pisar <ppisar@redhat.com> - 0.82-10
- Adjust to perl-5.22 (bug #1231258)

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-9
- Perl 5.22 rebuild

* Tue Nov 18 2014 Petr Pisar <ppisar@redhat.com> - 0.82-8
- Specify more dependencies (bug #1165197)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.82-3
- Perl 5.18 rebuild
- Perl 5.18 compatibility (CPAN RT#85411)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Petr Pisar <ppisar@redhat.com> - 0.82-1
- 0.82 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.80-2
- Perl 5.16 rebuild
- Specify all dependencies
- Adapt tests to perl 5.16 (RT #77778)

* Fri Jan 27 2012 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.74-1
- update to 0.74, clean spec, fix tests for 5.14.1

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.72-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.72-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.72-1
- Mass rebuild with perl-5.12.0 & update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.6.8-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.6.8-1
- update for submission
- split scripts off into their own package

* Tue Nov 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.6.8-0.1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.5)
