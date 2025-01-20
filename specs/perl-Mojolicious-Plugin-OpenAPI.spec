Name:           perl-Mojolicious-Plugin-OpenAPI
Version:        5.09
Release:        7%{?dist}
Summary:        OpenAPI / Swagger plugin for Mojolicious
# MIT-licensed files: t/spec/v2-petstore.json, t/v3-basic.t, t/v3-nullable.t, t/v3-style-array.t
# ASL 2.0-licensed files: t/spec/bundlecheck.json.
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojolicious-Plugin-OpenAPI
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-OpenAPI-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(JSON::Validator) >= 5.13
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
# test requirements
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojolicious) >= 9.00
BuildRequires:  perl(Mojolicious::Controller)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(lib)
Requires:       perl(JSON::Validator) >= 5.00
Requires:       perl(Mojolicious::Plugin)
Recommends:     perl(Config)
Suggests:       perl(Text::Markdown)

%{?perl_default_filter}

## Filter unneeded Requires with RPM
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON::Validator\\)$

%description
Mojolicious::Plugin::OpenAPI is a Mojolicious::Plugin that add routes and
input/output validation to your Mojolicious application based on a OpenAPI
(Swagger) specification. This plugin supports both version 2.0 and 3.x,
though 3.x might have some missing features.

%prep
%setup -q -n Mojolicious-Plugin-OpenAPI-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
DUMMY_DB_ERROR= JSON_VALIDATOR_DEBUG= MOJO_OPENAPI_DEBUG= %{make_build} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 5.09-5
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 26 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 5.09-1
- Update to 5.09

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 25 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.08-1
- Update to 5.08

* Sun Aug 21 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.07-1
- Update to 5.07

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.05-2
- Perl 5.36 rebuild

* Sun Apr 03 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.05-1
- Update to 5.05

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.02-1
- Update to 5.02

* Sun Oct 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.00-1
- Update to 5.00

* Sun Sep 19 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.06-1
- Update to 4.06

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.05-1
- Update to 4.05

* Sun Jun 27 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.04-1
- Update to 4.04

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-2
- Perl 5.34 rebuild

* Sun May 16 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.03-1
- Update to 4.03

* Sun Mar 28 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.02-1
- Update to 4.02

* Sun Feb 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 4.00-1
- Update to 4.00

* Sun Jan 31 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 3.41-1
- Update to 3.41

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.40-1
- Update to 3.40

* Sun Sep 27 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.36-1
- Update to 3.36

* Sun Aug 23 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.35-1
- Update to 3.35

* Sun Aug 09 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.34-1
- Update to 3.34

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.33-2
- Perl 5.32 rebuild

* Sun Jun 14 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.33-1
- Update to 3.33

* Thu Apr 09 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.31-2
- Take into account more review feedback (#1818936)

* Wed Apr 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.31-1
- Update to 3.31
- Take into account review feedback (#1818936)

* Mon Mar 30 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.30-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
