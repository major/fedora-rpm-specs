# Perform tests that need the Internet
%bcond_with perl_LWP_Protocol_https_enables_internet_test

Name:           perl-LWP-Protocol-https
Version:        6.14
Release:        4%{?dist}
Summary:        Provide HTTPS support for LWP::UserAgent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Protocol-https
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(parent)
BuildRequires:  perl(IO::Socket::SSL) >= 1.970
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::http::SocketMethods)
BuildRequires:  perl(Mozilla::CA) >= 20180117
BuildRequires:  perl(Net::HTTPS) >= 6
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::UserAgent) >= 6.06
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
%if %{with perl_LWP_Protocol_https_enables_internet_test}
BuildRequires:  perl(Test::RequiresInternet)
%endif
# Optional tests:
BuildRequires:  perl(IO::Socket::SSL) >= 1.953
BuildRequires:  perl(IO::Socket::SSL::Utils)
Requires:       perl(IO::Socket::SSL) >= 1.54
Requires:       perl(Mozilla::CA) >= 20180117
Requires:       perl(Net::HTTPS) >= 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::HTTPS\\)\\s*$

%description
The LWP::Protocol::https module provides support for using HTTPS schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n LWP-Protocol-https-%{version}
%if !%{with perl_LWP_Protocol_https_enables_internet_test}
rm t/example.t
perl -i -ne 'print $_ unless m{^t/example.t}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.14-1
- 6.14 bump

* Tue Feb 06 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.13-1
- 0.13 bump

* Wed Jan 24 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.12-1
- 0.12 bump

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.11-1
- 6.11 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Michal Josef Špaček <mspacek@redhat.com> - 6.10-8
- Package tests
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.10-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.10-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Petr Pisar <ppisar@redhat.com> - 6.10-1
- 6.10 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Petr Pisar <ppisar@redhat.com> - 6.09-2
- Remove unused build-time dependencies

* Fri Jul 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.09-1
- 6.09 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-12
- Perl 5.32 rebuild

* Fri Feb 14 2020 Petr Pisar <ppisar@redhat.com> - 6.07-11
- Disable tests that need the Internet by default

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-2
- Perl 5.26 rebuild

* Mon Feb 20 2017 Petr Pisar <ppisar@redhat.com> - 6.07-1
- 6.07 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Petr Pisar <ppisar@redhat.com> - 6.06-2
- Fix CVE-2014-3230 (incorrect handling of SSL certificate verification if
  HTTPS_CA_DIR or HTTPS_CA_FILE environment variables are set) (bug #1094442)

* Wed Apr 23 2014 Petr Pisar <ppisar@redhat.com> - 6.06-1
- 6.06 bump

* Thu Jan 16 2014 Petr Pisar <ppisar@redhat.com> - 6.04-4
- Modernize spec file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 6.04-2
- Perl 5.18 rebuild

* Thu May 02 2013 Petr Pisar <ppisar@redhat.com> - 6.04-1
- 6.04 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 6.03-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.03-1
- 6.03 bump
- Enable tests by default, they detect connectivity now

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 6.02-4
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.02-3
- Perl mass rebuild

* Tue Mar 29 2011 Petr Pisar <ppisar@redhat.com> - 6.02-2
- Disable tests because they need network access

* Mon Mar 28 2011 Petr Pisar <ppisar@redhat.com> 6.02-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
