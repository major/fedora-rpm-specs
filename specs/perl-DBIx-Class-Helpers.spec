Name:           perl-DBIx-Class-Helpers
Version:        2.037000
Release:        2%{?dist}
Summary:        A collection of various components for DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-Helpers
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/DBIx-Class-Helpers-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime requirements
BuildRequires:  perl(Carp::Clan) >= 6.04
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.0826
BuildRequires:  perl(DBIx::Class::Candy) >= 0.003001
BuildRequires:  perl(DBIx::Class::Candy::Exports)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Row)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Introspector) >= 0.001002
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased) >= 0.34
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::clean) >= 0.23
BuildRequires:  perl(parent)
# test requirements
BuildRequires:  perl(B)
BuildRequires:  perl(DBIx::Class::Candy::ResultSet)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Devel::Dwarn)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Roo) >= 1.003
BuildRequires:  perl(Text::Brew)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)

%{?perl_default_filter}

%description
This perl distribution contains a collection of various helper components
for DBIx::Class.


%prep
%setup -q -n DBIx-Class-Helpers-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes CONTRIBUTING.md README
%license LICENSE
%{perl_vendorlib}/DBIx*
%{_mandir}/man3/DBIx*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.037000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.037000-1
- Update to 2.037000

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 2.036000-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.036000-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.036000-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.036000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.036000-2
- Perl 5.32 rebuild

* Sun Mar 29 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.036000-1
- Update to 2.036000

* Sun Feb 23 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.035000-1
- Update to 2.035000

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.034002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.034002-1
- Update to 2.034002

* Sun Nov 03 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.034001-1
- Update to 2.034001

* Fri Aug 30 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.034000-2
- Take into account review comments (#1747138)

* Thu Jul 25 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.034000-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
