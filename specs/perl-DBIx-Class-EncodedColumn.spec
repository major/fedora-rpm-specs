Name:           perl-DBIx-Class-EncodedColumn
Version:        0.00020
Release:        16%{?dist}
Summary:        Automatically encode columns
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-EncodedColumn
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WREIS/DBIx-Class-EncodedColumn-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt)
# Unused BuildRequires:  perl(Crypt::OpenPGP)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::TimeStamp)
BuildRequires:  perl(Dir::Self)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(Digest::SHA)

%{?perl_default_filter}

%description
This DBIx::Class component can be used to automatically encode a column's
contents whenever the value of that column is set.

%prep
%setup -q -n DBIx-Class-EncodedColumn-%{version}
# Crypt::OpenPGP is not available in Fedora.
# It cannot be packaged because its dependency, Crypt::RIPEMD160,
# cannot be packaged.  See rhbz#182235.
rm lib/DBIx/Class/EncodedColumn/Crypt/OpenPGP.pm

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/DBIx/Class/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.00020-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.00020-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.00020-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.00020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00020-1
- 0.00020 bump

* Fri Sep 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00019-1
- 0.00019 bump

* Tue Sep 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00018-1
- 0.00018 bump

* Wed Sep 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00017-1
- 0.00017 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.00016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00016-1
- 0.00016 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.00015-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.00015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.00015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.00015-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.00015-7
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.00015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.00015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.00015-4
- Perl 5.26 rebuild

* Fri May 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.00015-3
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.00015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.00015-1
- 0.00015 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.00013-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.00013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.00013-2
- Perl 5.22 rebuild

* Wed Dec 10 2014 Petr Šabata <contyk@redhat.com> - 0.00013-1
- 0.00013 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.00011-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Petr Pisar <ppisar@redhat.com> - 0.00011-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.00011-2
- Perl mass rebuild

* Wed Apr 20 2011 Iain Arnell <iarnell@gmail.com> 0.00011-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.00010-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 29 2010 Iain Arnell <iarnell@gmail.com> 0.00010-2
- disable Module::AutoInstall

* Sun Aug 29 2010 Iain Arnell <iarnell@gmail.com> 0.00010-1
- update to latest upstream
- new BR perl(Crypt::Eksblowfish::Bcrypt)
- new BR perl(Test::Exception)

* Thu May 20 2010 Iain Arnell <iarnell@gmail.com> 0.00009-1
- update to latest upstream

* Sat May 01 2010 Iain Arnell <iarnell@gmail.com> 0.00008-1
- update to latest upstream
- use perl_default_filter and DESTDIR
- BR perl(Dir::Self)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.00006-2
- Mass rebuild with perl-5.12.0

* Sun Jan 17 2010 Iain Arnell <iarnell@gmail.com> 0.00006-1
- update to latest upstream version

* Mon Jan 11 2010 Iain Arnell <iarnell@gmail.com> 0.00005-3
- fix source0 location (was BADURL)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.00005-2
- rebuild against perl 5.10.1

* Sun Oct 18 2009 Iain Arnell <iarnell@gmail.com> 0.00005-1
- update to latest upstream

* Sat Sep 05 2009 Iain Arnell <iarnell@gmail.com> 0.00004-1
- update to latest upstream (minor documentation fix)

* Wed Sep 02 2009 Iain Arnell <iarnell@gmail.com> 0.00003-1
- update to latest upstream (copyright notice added)
- remove temporary BRs due to BZ #499768

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.00002-2
- fix duplicate directory ownership (perl-DBIx-Class owns %%{perl_vendorlib}/DBIx/Class/)

* Mon May 04 2009 Iain Arnell <iarnell@gmail.com> 0.00002-1
- Specfile autogenerated by cpanspec 1.77.
- Disable support for OpenPGP since it's not available in Fedora
- Additional BRs due to BZ #499768
