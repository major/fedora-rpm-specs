Name:           perl-DBIx-Introspector
Version:        0.001005
Release:        17%{?dist}
Summary:        Detect what database you are connected to
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Introspector
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/DBIx-Introspector-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(DBI::Const::GetInfoType) >= 1.628
BuildRequires:  perl(Moo) >= 1.003001
# test requirements
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI) >= 1.628
BuildRequires:  perl(Test::More) >= 0.99
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Roo) >= 1.002
Requires:       perl(DBI::Const::GetInfoType) >= 1.628
Provides:       perl(DBIx::Introspector::Driver) = %{version}

%{?perl_default_filter}

%description
DBIx::Introspector is a module factored out of the DBIx::Class database
detection code. Most code that needs to detect which database it is
connected to assumes that there is a one-to-one mapping from database
drivers to database engines. Unfortunately reality is rarely that simple.
For instance, DBD::ODBC is typically used to connect to SQL Server, but
ODBC can be used to connect to PostgreSQL, MySQL, and Oracle. Additionally,
while ODBC is the most common way to connect to SQL Server, it is not the
only option, as DBD::ADO can also be used.

%prep
%setup -q -n DBIx-Introspector-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.001005-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.001005-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.001005-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001005-4
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.001005-2
- Take into account review comments (#1738398)

* Thu Jul 25 2019 Emmanuel Seyman <emmanuel@seyman.fr> 0.001005-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.