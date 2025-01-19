Name:           perl-CPAN-Checksums
Version:        2.14
Release:        10%{?dist}
Summary:        Write a CHECKSUMS file for a directory as on CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Checksums
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-Checksums-%{version}.tar.gz
# Upstream's key to verify MANIFEST, bug #1083915
Source1:        A317C15D.pub
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5) >= 2.36
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(Safe)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  coreutils
BuildRequires:  gnupg
# Config not used
# Digest::SHA1 not used if Digest::SHA is available
# Digest::SHA::PurePerl not used if Digest::SHA is available
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Module::Signature) >= 0.79
# Time::HiRes not useful
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.18
Requires:       perl(IO::File) >= 1.14
Requires:       perl(Safe)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::File\\)$

%description
Write a CHECKSUMS file for a directory as on CPAN.

%prep
%setup -q -n CPAN-Checksums-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# test checks MANIFEST -  would fail because of debug files
rm -rf ./elfbins.list ./debugfiles.list ./debuglinks.list ./debugsources.list
export GNUPGHOME=$(mktemp -d)
gpg --import '%{SOURCE1}'
make test
rm -r "$GNUPGHOME"

%files
%doc Changes README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-1
- 2.14 bump

* Mon Nov 29 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-1
- 2.13 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-15
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-1
- 2.12 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-2
- Perl 5.24 rebuild

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 2.11-1
- 2.11 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-2
- Perl 5.22 rebuild

* Mon Apr 13 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-1
- 2.10 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-4
- Perl 5.20 rebuild

* Tue Jul 08 2014 Petr Pisar <ppisar@redhat.com> - 2.09-3
- Add upstream's key to verify MANIFEST (bug #1083915)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-1
- 2.09 bump

* Thu Apr 03 2014 Petr Pisar <ppisar@redhat.com> - 2.08-9
- Fix test skip-condition to pass in mock (bug #1083915)

* Wed Apr 02 2014 Petr Pisar <ppisar@redhat.com> - 2.08-8
- Remove more debuginfo remnants before running tests

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 2.08-7
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.08-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Petr Sabata <contyk@redhat.com> - 2.08-1
- 2.08 bump
- Drop now obsolete BuildRoot and defattr

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.07-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Petr Sabata <psabata@redhat.com> - 2.07-1
- New upstream release, v2.07

* Wed Oct 27 2010 Petr Pisar <ppisar@redhat.com> - 2.06-3
- 2.06 bump

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 2.05-2
- Do POD tests

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 2.05-1
- 2.05 bump
- Add missing BuildRequires that overlay perl package Provides

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.04-2
- rebuild against perl 5.10.1

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 2.04-1
- Specfile autogenerated by cpanspec 1.78.
