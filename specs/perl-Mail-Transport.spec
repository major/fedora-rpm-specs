Name:		perl-Mail-Transport
Version:	3.005
Release:	13%{?dist}
Summary:	Email message exchange
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mail-Transport
Source0:	https://cpan.metacpan.org/modules/by-module/Mail/Mail-Transport-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(IO::Handle)
# Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(File::Spec) >= 0.7
BuildRequires:	perl(IO::Lines)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Mail::Reporter) >= 3
BuildRequires:	perl(Net::Config)
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(IO::Lines)
Requires:	perl(IO::Socket)
Requires:	perl(List::Util)
Requires:	perl(Net::Config)
Requires:	perl(Net::Domain)

%description
Email message exchange code, formerly part of the Mail::Box package.

%prep
%setup -q -n Mail-Transport-%{version}

%build
yes y | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Transport.3*
%{_mandir}/man3/Mail::Transport::Exim.3*
%{_mandir}/man3/Mail::Transport::Mailx.3*
%{_mandir}/man3/Mail::Transport::Qmail.3*
%{_mandir}/man3/Mail::Transport::Receive.3*
%{_mandir}/man3/Mail::Transport::SMTP.3*
%{_mandir}/man3/Mail::Transport::Send.3*
%{_mandir}/man3/Mail::Transport::Sendmail.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Tom Callaway <spot@fedoraproject.org> - 3.005-1
- update to 3.005

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Paul Howarth <paul@city-fan.org> - 3.004-3
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Drop redundant use of %%{?perl_default_filter}
  - Use %%{make_build} and %%{make_install}
  - Fix permissions verbosely
  - Make %%files list more explicit
  - Package README.md rather than README

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-1
- 3.004 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep  5 2018 Tom Callaway <spot@fedoraproject.org> - 3.003-1
- update to 3.003

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump
- Modernize spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.000-3
- Perl 5.26 rebuild

* Fri Mar 10 2017 Tom Callaway <spot@fedoraproject.org> - 3.000-2
- review cleanups

* Tue Feb  7 2017 Tom Callaway <spot@fedoraproject.org> - 3.000-1
- initial package
