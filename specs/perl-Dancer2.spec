Name:           perl-Dancer2
Version:        1.1.2
Release:        2%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Dancer2
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/Dancer2-%{version}.tar.gz
# https://anonscm.debian.org/cgit/pkg-perl/packages/libdancer2-perl.git/plain/debian/patches/no-phone-home.patch?id=cfa2426c2feb48bfb8b433a53449374273612f73
Patch0:         no-phone-home.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CLI::Osprey)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser)
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.21
BuildRequires:  perl(HTTP::Server::PSGI)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.16
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
# Plack::Builder version from Plack >= 1.0035 in Makefile.PL
BuildRequires:  perl(Plack::Builder) >= 1.0035
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires:  perl(Plack::Middleware::Head)
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires:  perl(Plack::Middleware::Static)
BuildRequires:  perl(Plack::MIME)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Pod::Simple::Search)
BuildRequires:  perl(Pod::Simple::SimpleTree)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Tiny)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Registry)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML) >= 0.86
# Optional run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(CGI::Deurl::XS)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(URL::Encode::XS)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
# Test::CPAN::Meta not used
BuildRequires:  perl(Test::Fatal)
# Test::NoTabs not used
# Test::Pod 1.41 not used
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional tests:
BuildRequires:  perl(Test::Memory::Cycle) >= 1.04
BuildRequires:  perl(Test::MockTime)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Exporter::Tiny)
Requires:       perl(File::Copy)
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Server::PSGI)
Requires:       perl(Moo) >= 1.003000
# Plack::Builder version from Plack >= 1.0035 in Makefile.PL
Requires:       perl(Plack::Builder) >= 1.0035
Requires:       perl(Pod::Simple::Search)
Requires:       perl(Pod::Simple::SimpleTree)
Requires:       perl(Template::Tiny)
Requires:       perl(Test::EOL)
Requires:       perl(Test::More) >= 0.92
Requires:       perl(Types::Standard)
Requires:       perl(YAML) >= 0.86

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Exporter\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Builder\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Test::More\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML\\)$

%description
Dancer2 is the new generation of Dancer, the lightweight web-framework for
Perl. It is a complete rewrite based on Moo and is meant to be easy and fun.

%prep
%setup -q -n Dancer2-%{version}
%patch 0 -p1
/usr/bin/sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' script/dancer2 share/skel/bin/+app.psgi
/usr/bin/chmod +x share/skel/bin/+app.psgi
/usr/bin/rm share/.gitignore

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc AUTHORS Changes CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n dancer2
Summary:       Dancer2 command line interface

%description -n dancer2
Dancer2 is the new generation lightweight web-framework for Perl. This tool
provides nice, easily-extendable CLI interface for it.

%files -n dancer2
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 01 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.1.2-1
- Update to 1.1.2

* Sun Aug 18 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.1.1-2
- Fix CONTRIBUTING.md filename

* Sun Aug 18 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 1.1.1-1
- Update to 1.1.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.1.0-1
- Update to 1.1.0
- Migrate to SPDX license

* Sun Oct 22 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0.0-1
- Update to 1.0.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.400001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 12 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.400001-1
- Update to 0.400001

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.400000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.400000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.400000-2
- Perl 5.36 rebuild

* Sun Mar 20 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.400000-1
- Update to 0.400000

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.301004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.301004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 06 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.301004-1
- Update to 0.301004

* Sun Jun 06 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.301003-1
- Update to 0.301003

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.301002-2
- Perl 5.34 rebuild

* Sun May 09 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.301002-1
- Update to 0.301002

* Sun Mar 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.301001-1
- Update to 0.301001

* Sun Jan 31 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 0.300005-1
- Update to 0.300005

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.300004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.300004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.300004-2
- Perl 5.32 rebuild

* Sun May 31 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.300004-1
- Update to 0.300004

* Sun Apr 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.300003-1
- Update to 0.300003

* Mon Apr 06 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.300001-1
- Update to 0.300001
- Use %%{make_install} and %%{make_build} where appropriate
- Pass NO_PERLLOCAL to Makefile.PL

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.300000-3
- Add perl(blib) for tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.300000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.300000-1
- Update to 0.300000
- Replace call to %%{__perl} with /usr/bin/perl

* Tue Dec 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.208002-1
- 0.208002 bump

* Mon Aug 05 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.208001-1
- 0.208001 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.208000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.208000-1
- 0.208000 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.207000-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.207000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.207000-1
- Update to 0.207000

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.206000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.206000-2
- Perl 5.28 rebuild

* Sun Apr 22 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.206000-1
- Update to 0.206000

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.205002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205002-2
- Disable dancer2's phone-home capabilities (#1521155)

* Wed Oct 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.205002-1
- 0.205002 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.205001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205001-1
- Update to 0.205001
- Drop Group tag

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.205000-2
- Perl 5.26 rebuild

* Sun Mar 19 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.205000-1
- Update to 0.205000

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.204004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.204004-1
- Update to 0.204004

* Sun Dec 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.204002-1
- Update to 0.204002

* Sun Oct 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.204001-1
- Update to 0.204001

* Sun Oct 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.204000-1
- Update to 0.204000

* Sun Sep 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.203001-1
- Update to 0.203001

* Thu Aug 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.203000-2
- Update to 0.203000

* Mon Aug 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.202000-2
- Added missing run-require perl(Exporter::Tiny)

* Sun Aug 14 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.202000-1
- Update to 0.202000
- Pass NO_PACKLIST to Makefile.PL
- Fix shebangs in the Dancer2 scripts

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.201000-1
- Update to 0.201000

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.166001-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.166001-1
- 0.166001 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.163000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.163000-1
- 0.163000 bump

* Fri Oct 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.162000-1
- 0.162000 bump

* Thu Aug 06 2015 Petr Pisar <ppisar@redhat.com> - 0.161000-1
- 0.161000 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.160000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.160000-2
- Perl 5.22 rebuild

* Tue Apr 28 2015 David Dick <ddick@cpan.org> - 0.160000-1
- Upgrade to 0.160000.  Numerous bugfixes and enhancements

* Sat Mar 28 2015 David Dick <ddick@cpan.org> - 0.159003-1
- Upgrade to 0.159003.  Numerous bugfixes

* Wed Jan 14 2015 David Dick <ddick@cpan.org> - 0.158000-1
- Initial release
