Name:           perl-Mojo-RabbitMQ-Client
Version:        0.3.1
Release:        17%{?dist}
Summary:        Mojo::IOLoop based RabbitMQ client
# Automatically converted from old format: Artistic 2.0 and BSD - review is highly recommended.
License:        Artistic-2.0 AND LicenseRef-Callaway-BSD

URL:            https://metacpan.org/release/Mojo-RabbitMQ-Client
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/Mojo-RabbitMQ-Client-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(strict)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::Home)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Parameters)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Net::AMQP) >= 0.06
BuildRequires:  perl(Net::AMQP::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# test requirements
BuildRequires:  perl(Test::Exception) >= 0.43
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Mojo::EventEmitter)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Net::AMQP) >= 0.06

%{?perl_default_filter}

## Filter unneeded Requires with RPM
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::AMQP\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$

%description
Mojo::RabbitMQ::Client is a rewrite of AnyEvent::RabbitMQ to work on top of
Mojo::IOLoop.

%prep
%setup -q -n Mojo-RabbitMQ-Client-%{version}
rm -rf inc

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_RMQ='' MOJO_RABBITMQ_DEBUG="" MOJO_CONNECT_TIMEOUT="" ./Build test

%files
%doc examples Changes README.md
%license LICENSE
%{perl_vendorlib}/auto
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Adam Williamson <awilliam@redhat.com> - 0.3.1-1
- New release 0.3.1
- Drop merged patch
- Drop tarball modification now non-free file is removed upstream

* Tue Aug 20 2019 Adam Williamson <awilliam@redhat.com> - 0.2.4-1
- New release 0.2.4 (fixes annoying log warning spam)

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 0.2.3-2
- Backport PR #35 to allow EXTERNAL as well as AMQPLAIN auth

* Sun Jul 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.2.3-1
- Update to 0.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.2.2-4
- Take into account more review comments (#1726432)

* Fri Jul 05 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.2.2-3
- Take into account review comments (#1726432)

* Wed Jul 03 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.2.2-2
- Source modified to not include share/fixed_amqp0-8.xml (#1726432)

* Fri Jun 21 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.2.2-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
