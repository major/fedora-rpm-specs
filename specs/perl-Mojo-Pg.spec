Name:           perl-Mojo-Pg
Version:        4.27
Release:        10%{?dist}
Summary:        Mojolicious ♥ PostgreSQL
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojo-Pg
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-%{version}.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Mojolicious) >= 8.50
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::Pg) >= 3.7.4
BuildRequires:  perl(DBI)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(SQL::Abstract::Pg) >= 1.0
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
Requires:       perl(SQL::Abstract) >= 1.85

%{?perl_default_filter}

%description
Mojo::Pg is a tiny wrapper around DBD::Pg that makes PostgreSQL a lot of
fun to use with the Mojolicious real-time web framework. Perform queries
blocking and non-blocking, use all SQL features PostgreSQL has to offer,
generate CRUD queries from data structures, manage your database schema
with migrations and build scalable real-time web applications with the
publish/subscribe pattern.

%prep
%setup -q -n Mojo-Pg-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} %{?_smp_mflags}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 4.27-8
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.27-2
- Perl 5.36 rebuild

* Sun Mar 20 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 4.27-1
- Update to 4.27

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 12 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.26-1
- Update to 4.26

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.25-2
- Perl 5.34 rebuild

* Sun Mar 07 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.25-1
- Update to 4.25

* Sun Feb 07 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.24-1
- Update to 4.24

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.23-1
- Update to 4.23

* Sun Nov 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.22-1
- Update to 4.22

* Sun Nov 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.21-1
- Update to 4.21

* Sun Oct 04 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.20-1
- Update to 4.20

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.19-2
- Perl 5.32 rebuild

* Sun May 31 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.19-1
- Update to 4.19

* Sun Feb 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.18-1
- Update to 4.18

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.17-1
- Update to 4.17

* Sun Sep 08 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.16-1
- Update to 4.16
- Replace calls to %%{__perl} with /usr/bin/perl
- Pass NO_PERLLOCAL=1 to Makefile.PL
- Replace calls to "make pure_install" with %%{make_install}
- Replace calls to make with %%{make_build}

* Sun Jul 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.15-1
- Update to 4.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.13-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.13-1
- Update to 4.13

* Sun Dec 02 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.12-1
- Update to 4.12

* Sun Oct 21 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.11-1
- Update to 4.11

* Sun Sep 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.10-1
- Update to 4.10

* Sun Aug 12 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.09-1
- Update to 4.09

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-3
- Perl 5.28 rebuild

* Tue May 15 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.08-2
- Take into account review comments (#1578151)

* Mon May 14 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 4.08-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
