Name:           perl-Capture-Tiny
Version:        0.50
Release:        3%{?dist}
Summary:        Capture STDOUT and STDERR from Perl, XS or external programs
License:        Apache-2.0
URL:            https://metacpan.org/release/Capture-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
# PerlIO is optional
BuildRequires:  perl(Scalar::Util)
# Tests only:
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(PerlIO::scalar)
# Test::Differences is optional
BuildRequires:  perl(Test::More) >= 0.62

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Cases\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((TieEvil\|TieLC\|Utils)\\)

%description
Capture::Tiny provides a simple, portable way to capture anything sent to
STDOUT or STDERR, regardless of whether it comes from Perl, from XS code or
from an external program. Optionally, output can be teed so that it is
captured while being passed through to the original handles. Yes, it even
works on Windows. Stop guessing which of a dozen capturing modules to use
in any particular situation and just use this one.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Capture-Tiny-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes examples README Todo
%{perl_privlib}/Capture*
%{_mandir}/man3/Capture::Tiny*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-1
- 0.50 bump (rhbz#2333321)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-18
- Package tests

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-14
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Petr Pisar <ppisar@redhat.com> - 0.48-9
- Modernize a spec file

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-1
- 0.48 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.46-2
- Perl 5.26 rebuild

* Mon Feb 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.46-1
- 0.46 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-1
- 0.44 bump

* Wed Jun 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-1
- 0.42 bump

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.24 rebuild

* Mon Feb 29 2016 Petr Šabata <contyk@redhat.com> - 0.36-1
- 0.36 bump

* Fri Feb 19 2016 Petr Šabata <contyk@redhat.com> - 0.34-1
- 0.34 bump, metadata changes only

* Fri Feb 19 2016 Petr Šabata <contyk@redhat.com> - 0.32-1
- 0.32 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.22 rebuild

* Mon May 18 2015 Petr Šabata <contyk@redhat.com> - 0.30-1
- 0.30 bump
- Windows fixes only

* Fri Feb 13 2015 Petr Šabata <contyk@redhat.com> - 0.28-1
- 0.28 bump

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 0.27-1
- 0.27 bump
- META changes only

* Tue Nov 04 2014 Petr Šabata <contyk@redhat.com> - 0.26-1
- 0.26 bump
- Test suite enhancements only

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.20 rebuild

* Mon Aug 18 2014 Petr Šabata <contyk@redhat.com> - 0.25-1
- 0.25 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Petr Šabata <contyk@redhat.com> - 0.24-1
- 0.24 bump, fix CVE-2014-1875

* Thu Oct 24 2013 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump

* Thu Sep 05 2013 Petr Šabata <contyk@redhat.com> - 0.22-4
- Avoid circular dependencies when bootstrapping (#1004376)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Perl 5.18 rebuild

* Thu Mar 28 2013 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Petr Pisar <ppisar@redhat.com> - 0.21-1
- 0.21 bump

* Thu Oct 04 2012 Petr Šabata <contyk@redhat.com> - 0.20-1
- 0.20 bump

* Wed Aug 08 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Perl 5.16 rebuild

* Mon May 07 2012 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Thu Feb 23 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Mon Feb 13 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump

* Mon Dec 05 2011 Petr Šabata <contyk@redhat.com> - 0.13-1
- 0.13 bump

* Fri Dec 02 2011 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-2
- Perl mass rebuild

* Fri May 20 2011 Petr Sabata <psabata@redhat.com> - 0.11-1
- 0.11 bump
- Removing defattr

* Wed Feb 09 2011 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump
- Remove BuildRoot stuff
- Migrate from Module::Build to ExtUtils::MakeMaker
- Install into perl core directory

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jun 21 2010 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump (bug #606277)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- Mass rebuild with perl-5.12.0

* Wed Jan 27 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-1
- update

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-1
- update

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
