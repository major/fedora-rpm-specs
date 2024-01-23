Name:           perl-Git-PurePerl
Version:        0.53
Release:        24%{?dist}
Summary:        Pure Perl interface to Git repositories
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Git-PurePerl
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BROQ/Git-PurePerl-%{version}.tar.gz
Patch0:         Git-PurePerl-0.53-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config::GitLike)
BuildRequires:  perl(Data::Stream::Bulk)
BuildRequires:  perl(Data::Stream::Bulk::Array)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(IO::Digest)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Class)
# Tests only
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::utf8)
Requires:       perl(Config::GitLike)

%description
This module is a Pure Perl interface to Git repositories.

%prep
%setup -q -n Git-PurePerl-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-20
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-17
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-14
- Perl 5.32 rebuild

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-13
- Add perl(FindBin) for build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-4
- Perl 5.26 rebuild

* Fri May 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-3
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Jan Pazdziora <jpazdziora@redhat.com> - 0.53-1
- 1377506 - Rebase to upstream version 0.53.

* Wed Jun 15 2016 Jan Pazdziora <jpazdziora@redhat.com> - 0.52-1
- 1346506 - Rebase to upstream version 0.52.

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-6
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-5
- Remove redeclare "my" in "my" (CPAN RT#106772)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-2
- Perl 5.22 rebuild

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 0.51-1
- 0.51 bump

* Fri Nov 28 2014 Petr Šabata <contyk@redhat.com> - 0.50-1
- 0.50 bump

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 0.48-7
- apply patch for RT#86018

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.48-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream
- remove test tarballs from documentation

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.47-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.47-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 30 2010 Iain Arnell <iarnell@gmail.com> 0.47-1
- update to latest upstream

* Mon Jul 19 2010 Iain Arnell <iarnell@gmail.com> 0.46-2
- update spec for modern rpmbuild

* Wed Jun 23 2010 Iain Arnell 0.46-1
- Specfile autogenerated by cpanspec 1.78.
