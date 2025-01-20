%define username   statsdpl
%define groupname  statsdpl
%define daemon     statsd-perl

Name:           perl-Net-Statsd-Server
Version:        0.20
Release:        27%{?dist}
Summary:        Library for the Perl port of Flickr/Etsy's statsd metrics daemon
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Statsd-Server
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Statsd-Server-%{version}.tar.gz
Source1:        %{daemon}.service
Source2:        %{daemon}.js
Source3:        %{daemon}.logrotate
Patch1:         Net-Statsd-Server-0.20-makefile.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Handle::UDP)
BuildRequires:  perl(AnyEvent::Log)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Strict)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
# HTTP::Request not used at tests
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(lib)
# LWP::UserAgent not used at tests
# RRDs not used at tests
BuildRequires:  perl(Socket)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Test::More)

%description
Net::Statsd::Server is the server component of statsd. It implements a daemon
that listens on a given host/port for incoming UDP packets and dispatches them
to whatever you want, including Graphite or your console.  Look into the
Net::Statsd::Server::Backend::* name space to know all the possibilities, or
write a back-end yourself.

%prep
%setup -q -n Net-Statsd-Server-%{version}
%patch -P1 -p1
mv bin/statsd bin/%{daemon}
for F in exampleConfig.js localConfig.js logConfig.js rrdConfig.js; do
    mv bin/"$F" "$F"
done
rm -Rf t/integration-tests/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{daemon}.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{daemon}.js
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{daemon}
mkdir -p -m 750 $RPM_BUILD_ROOT%{_localstatedir}/log/%{daemon}

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
STATSD_BINARY=$RPM_BUILD_ROOT/usr/bin/%{daemon} make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n statsd-perl
Summary:        A Perl port of Flickr/Etsy's statsd metrics daemon
BuildRequires:  systemd-units
Requires:       %{name} = %{version}-%{release}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(pre):  shadow-utils
Provides:  statsd

%description -n statsd-perl
Implements a daemon that listens on a given host/port for incoming UDP packets
and dispatches them to whatever you want, including Graphite or your console.
Look into the Net::Statsd::Server::Backend::* name space to know all the
possibilities, or write a back-end yourself.

%pre -n statsd-perl
getent group %{groupname} >/dev/null || groupadd -r %{groupname}
getent passwd %{username} >/dev/null || \
useradd -r -g %{groupname} -d /run/%{daemon} \
    -s /sbin/nologin -c "Perl Statsd" %{username}
exit 0

%post -n statsd-perl
%systemd_post %{daemon}.service

%preun -n statsd-perl
%systemd_preun %{daemon}.service

%postun -n statsd-perl
%systemd_postun_with_restart %{daemon}.service

%files -n statsd-perl
%doc README exampleConfig.js localConfig.js logConfig.js rrdConfig.js
%{_mandir}/man1/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{daemon}.js
%config(noreplace) %{_sysconfdir}/logrotate.d/%{daemon}
%{_unitdir}/%{daemon}.service
%attr(750, %{username}, %{groupname}) %{_localstatedir}/log/%{daemon}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-19
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-16
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.20-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.20 rebuild

* Tue Jul 22 2014 David Dick <ddick@cpan.org> - 0.17-2
- Temporarily removed integration test directory as it was prone to errors under load

* Sat Jun 14 2014 David Dick <ddick@cpan.org> - 0.17-1
- Initial release
