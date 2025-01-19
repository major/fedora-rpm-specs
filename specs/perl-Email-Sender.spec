Name:           perl-Email-Sender
Epoch:          1
Version:        2.601
Release:        4%{?dist}
Summary:        A library for sending email
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Email-Sender
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Sender-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny) >= 0.08
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Email::Abstract) >= 3.006
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Simple) >= 1.998
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.000008
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Net::SMTP::SSL)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Throwable::Error) >= 0.200003
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
Requires:       perl(Email::Abstract) >= 3.006
Requires:       perl(Net::SMTP::SSL)
Requires:       perl(Throwable::Error) >= 0.200003

%{?perl_default_filter}

%description
Email::Sender replaces the old and sometimes problematic Email::Send library,
which did a decent job at handling very simple email sending tasks, but was not
suitable for serious use, for a variety of reasons.

%prep
%setup -q -n Email-Sender-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 %{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Email*
%{_mandir}/man3/Email*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.601-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1:2.601-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1:2.601-1
- Update to 2.601

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.600-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.600-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.600-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 1:2.600-1
- Update to 2.600

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.500-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.500-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.500-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.500-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1:2.500-1
- Update to 2.500

* Sun Jun 27 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1:1.500-1
- Update to 1.500

* Sat Jun 19 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300036-1
- Update to 1.300036

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.300035-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.300035-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300035-1
- Update to 1.300035

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.300034-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.300034-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.300034-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300034-1
- Update to 1.300034

* Sun Dec 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300033-1
- Update to 1.300033
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to "make pure_install" with %%{make_install}
- Replace calls to "make" with %%{make_build}

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.300031-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.300031-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.300031-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.300031-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.300031-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.300031-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.300031-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.300031-2
- Perl 5.26 rebuild

* Sun Apr 09 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300031-1
- Update to 1.300031

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.300030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300030-1
- Update to 1.300030

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.300028-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Apr 28 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300028-1
- Update to 1.300028

* Tue Apr 05 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300027-1
- Update to 1.300027

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.300021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300021-1
- Update to 1.300021

* Sun Sep 06 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300020-1
- Update to 1.300020
- Drop Group tag
- Use %%license
- Re-enable pod coverage test
- Tighten file listing
- Minor clean up of the spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.300018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.300018-2
- Perl 5.22 rebuild

* Sun Jun 07 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.300018-1
- Update to 1.300018

* Fri Oct 31 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.300016-1
- 1.300016 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.120002-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.120002-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.120002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Iain Arnell <iarnell@gmail.com> 0.120002-1
- update to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.120001-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.110005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.110005-2
- Perl 5.16 rebuild

* Sun Mar 11 2012 Iain Arnell <iarnell@gmail.com> 0.110005-1
- update to latest upstream version

* Thu Feb 23 2012 Iain Arnell <iarnell@gmail.com> 0.110004-1
- update to latest upstream version

* Fri Feb 03 2012 Iain Arnell <iarnell@gmail.com> 0.110003-1
- update to latest upstream version

* Wed Feb 01 2012 Iain Arnell <iarnell@gmail.com> 0.110002-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.110001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.110001-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.110001-1
- update to latest upstream version

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> 0.110000-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102370-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.102370-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 30 2010 Iain Arnell <iarnell@gmail.com> 0.102370-1
- update to latest upstream
- drop Sys::Hostname::Long BR

* Tue Jun 29 2010 Iain Arnell <iarnell@gmail.com> 0.101760-2
- re-enable t/a-perl-minver.t

* Tue Jun 29 2010 Iain Arnell <iarnell@gmail.com> 0.101760-1
- update to latest upstream (fixes bz#608958)
- BR perl(Capture::Tiny) >= 0.08

* Sat May 08 2010 Iain Arnell <iarnell@gmail.com> 0.100460-4
- disable t/a-perl-minver.t (fails under perl 5.12.0)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100460-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100460-2
- Mass rebuild with perl-5.12.0

* Sat Mar 13 2010 Iain Arnell <iarnell@gmail.com> 0.100460-1
- update to latest upstream version
- use perl_default_filter and DESTDIR
- br perl(Pod::Coverage::TrustPod)
- remove failing pod coverage test

* Mon Feb 15 2010 Iain Arnell <iarnell@gmail.com> 0.100450-1
- update to latest upstream version

* Thu Jan 14 2010 Iain Arnell 0.100110-1
- Specfile autogenerated by cpanspec 1.78.
