Name:           perl-DBIx-RunSQL
Version:        0.25
Release:        2%{?dist}
Summary:        Run SQL commands from a file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-RunSQL

Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/DBIx-RunSQL-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(DBI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Load)

# Testing
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Table)

Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(Pod::Usage)


%description
This module abstracts away the "run these SQL statements to set up
a database" into a module. It also abstracts away the reading of
SQL from a file and allows for various command line parameters
to be passed in.


%prep
%setup -q -n DBIx-RunSQL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/run-sql.pl
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 21 2024 Denis Fateyev <denis@fateyev.com> - 0.25-1
- Update to 0.25 release

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.24-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Denis Fateyev <denis@fateyev.com> - 0.24-1
- Update to 0.24 release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Denis Fateyev <denis@fateyev.com> - 0.22-1
- Update to 0.22 release

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.30 rebuild

* Sat Mar 30 2019 Denis Fateyev <denis@fateyev.com> - 0.21-1
- Update to 0.21 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Denis Fateyev <denis@fateyev.com> - 0.20-1
- Update to 0.20 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.28 rebuild

* Fri May 04 2018 Denis Fateyev <denis@fateyev.com> - 0.19-1
- Update to 0.19 release

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-1
- 0.17 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.26 rebuild

* Tue Mar 21 2017 Denis Fateyev <denis@fateyev.com> - 0.16-1
- Update to 0.16 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 19 2016 Denis Fateyev <denis@fateyev.com> - 0.15-1
- Update to 0.15 release

* Wed May 25 2016 Denis Fateyev <denis@fateyev.com> - 0.14-1
- Update to 0.14 release

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Denis Fateyev <denis@fateyev.com> - 0.13-1
- Update to 0.13 release

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-3
- Perl 5.22 rebuild

* Tue Oct 07 2014 Denis Fateyev <denis@fateyev.com> - 0.12-2
- Small spec improvements

* Fri Sep 12 2014 Denis Fateyev <denis@fateyev.com> - 0.12-1
- Initial release
