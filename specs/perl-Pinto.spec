Name:           perl-Pinto
Epoch:          1
Version:        0.14
Release:        23%{?dist}
Summary:        Curate a repository of Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pinto
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Pinto-%{version}.tar.gz
Source1:        pintod.service
Source2:        pintod.conf
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Apache::Htpasswd)
BuildRequires:  perl(App::Cmd) >= 0.323
BuildRequires:  perl(App::Cmd::Command::help)
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(App::cpanminus) >= 1.6920
BuildRequires:  perl(Archive::Extract) >= 0.68
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(CPAN::Checksums)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Cwd::Guard)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::TimeZone::Local::Unix)
BuildRequires:  perl(DateTime::TimeZone::OffsetOnly)
BuildRequires:  perl(DBD::SQLite) >= 1.33
BuildRequires:  perl(DBIx::Class) >= 0.08200
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Dist::Metadata) >= 0.924
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::NFSLock)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::PSGI)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Prompt)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::PP) >= 2.27103
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(Module::CoreList) >= 5.20160720
BuildRequires:  perl(Module::Faker::Dist) >= 0.014
BuildRequires:  perl(Module::Metadata) >= 1.000031
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::ClassAttribute) >= 0.27
BuildRequires:  perl(MooseX::Configuration)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Plack) >= 1.0028
BuildRequires:  perl(Plack::Middleware::Auth::Basic)
BuildRequires:  perl(Plack::MIME)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Proc::Fork)
BuildRequires:  perl(Proc::Terminator)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Router::Simple)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Format)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::LWP::UserAgent) >= 0.018
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Throwable::Error) >= 0.200005
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(utf8)
BuildRequires:  perl(UUID::Tiny)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  systemd
Requires:       perl(App::cpanminus) >= 1.6920
Requires:       perl(App::Cmd) >= 0.323
Requires:       perl(Archive::Extract) >= 0.68
Requires:       perl(Authen::Simple::Passwd)
Requires:       perl(DBD::SQLite) >= 1.33
Requires:       perl(DBIx::Class) >= 0.08200
Requires:       perl(DBIx::Class::Core)
Requires:       perl(DBIx::Class::Schema)
Requires:       perl(Dist::Metadata) >= 0.924
Requires:       perl(Encode)
Requires:       perl(File::Spec)
Requires:       perl(IO::Prompt)
Requires:       perl(JSON::PP) >= 2.27103
Requires:       perl(Module::CoreList) >= 5.20160720
Requires:       perl(Module::Metadata) >= 1.000031
Requires:       perl(MooseX::ClassAttribute) >= 0.27
Requires:       perl(Plack) >= 1.0028
Requires:       perl(Starman) >= 0.3014
Requires:       perl(Throwable::Error) >= 0.200005

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Extract\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Dist::Metadata\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Module::CoreList\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::ClassAttribute\\)\s*$

%description
Pinto is an application for creating and managing a custom CPAN-like
repository of Perl modules. The purpose of such a repository is to provide
a stable, curated stack of dependencies from which you can reliably build,
test, and deploy your application using the standard Perl tool chain. Pinto
supports various operations for gathering and managing distribution
dependencies within the repository, so that you can control precisely which
dependencies go into your application.

%prep
%setup -q -n Pinto-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/pintod.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pintod

%{_fixperms} %{buildroot}/*

%check
make test

%post
%systemd_post pintod.service

%preun
%systemd_preun pintod.service

%postun
%systemd_postun_with_restart pintod.service

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/pinto
%{_bindir}/pintod
%{_unitdir}/pintod.service
%config(noreplace) %{_sysconfdir}/sysconfig/pintod

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-13
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:0.14-12
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.14-1
- 0.14 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.12-1
- 0.12 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11000-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.11000-1
- 0.11 bump

* Tue Jul 28 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09999-2
- Add systemd service unit file and default configuration.

* Thu Jul 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09999-1
- Specfile autogenerated by cpanspec 1.78.
