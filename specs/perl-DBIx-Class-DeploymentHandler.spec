Name:           perl-DBIx-Class-DeploymentHandler
Version:        0.002234
Release:        2%{?dist}
Summary:        Extensible DBIx::Class deployment
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/DBIx-Class-DeploymentHandler
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMCCLIMON/DBIx-Class-DeploymentHandler-%{version}.tar.gz

BuildArch:      noarch
# Build deps
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema::Loader)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual)
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(Log::Contextual::WarnLogger)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(SQL::SplitStatement)
BuildRequires:  perl(SQL::Translator::Diff)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Text::Brew)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(YAML)
BuildRequires:  perl(autodie)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test deps
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBD::SQLite) >= 1.35
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(version)
Requires:       perl(DBIx::Class::Schema::Loader)
Requires:       perl(Log::Contextual::Role::Router)
Requires:       perl(Type::Tiny)

%{?perl_default_filter}

%description
DBIx::Class::DeploymentHandler is, as its name suggests, a tool for deploying
and upgrading databases with DBIx::Class. It is designed to be much more
flexible than DBIx::Class::Schema::Versioned, hence the use of Moose and lots
of roles.

%prep
%setup -q -n DBIx-Class-DeploymentHandler-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes TODO
%license LICENSE
%{_mandir}/man3/DBIx*
%{perl_vendorlib}/DBIx/Class/DeploymentHandler*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.002234-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 18 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002234-1
- Update to 0.002234

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.002233-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.002233-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.002233-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002233-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002233-1
- Update to 0.002233
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to "make pure_install" to %%{make_install}
- Replace calls to "make" to %%{make_build}
- Pass NO_PERLLOCAL to Makefile.PL
- Add %%license tag


* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.002232-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002232-1
- Update to 0.002232

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.002231-2
- Perl 5.30 rebuild

* Sun May 12 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002231-1
- Update to 0.002231

* Sun Mar 24 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002230-1
- Update to 0.002230

* Wed Mar 13 2019 Adam Williamson <awilliam@redhat.com> - 0.002227-1
- Update to 0.002227

* Sun Mar 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002224-1
- Update to 0.002224

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.002222-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002222-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.002222-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.002222-1
- Update to 0.002222

* Sun Oct 01 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002221-1
- Update to 0.002221

* Sun Sep 03 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002220-1
- Update to 0.002220

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.002219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.002219-2
- Perl 5.26 rebuild

* Sun Mar 26 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002219-1
- Update to 0.002219

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.002218-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.002218-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.002218-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002218-2
- Take into account review comments (#1281245)

* Tue Nov 10 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002218-1
- Update to 0.002218

* Thu Oct 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002217-2
- Clean up spec file

* Sat Oct 17 2015 Adam Williamson <awilliam@redhat.com> - 0.002217-1
- initial package
