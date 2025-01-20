Name:           perl-Web-Paste-Simple
Version:        0.002
Release:        30%{?dist}
Summary:        Simple PSGI-based pastebin-like web site
# CONTRIBUTING:             GPL+ or Artistic or CC-BY-SA
# lib/Web/Paste/Simple.pm   GPL+ or Artistic
License:        (GPL+ or Artistic) and (GPL+ or Artistic or CC-BY-SA)
URL:            https://metacpan.org/release/Web-Paste-Simple
Source0:        https://cpan.metacpan.org/modules/by-module/Web/Web-Paste-Simple-%{version}.tar.gz
Source1:        web-paste-simple.service
# We don't like /usr/bin/env in shellbangs
Patch0:         Web-Paste-Simple-0.002-Do-not-use-usr-bin-env.patch
# Allow to redefine path to the storage
Patch1:         Web-Paste-Simple-0.002-Configure-storage-path-from-environment.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# Run-time:
BuildRequires:  perl(aliased)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(HTML::HTML5::Entities)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Moo) >= 1.000000
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Text::Template)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(Moo) >= 1.000000

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moo\\)$

%description
Web::Paste::Simple is a lightweight PSGI application for operating
a pastebin-like web site. It provides syntax highlighting via the CodeMirror
JavaScript library. It should be fast enough for deployment via CGI.

%package server
Summary:        Simple pastebin-like web server
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# unit directory ownership
Requires:       systemd
Requires(pre):  shadow-utils

%description server
This is web-paste-simple daemon for Web::Paste::Simple web service.

%global storage %{_sharedstatedir}/webpastesimple

%prep
%setup -q -n Web-Paste-Simple-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Set storage path for the daemon
sed -e '/^ExecStart=/iEnvironment=WEB_PASTE_SIMPLE_STORAGE=%{storage}' \
    < %{SOURCE1} > web-paste-simple.service

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Daemon
install -d %{buildroot}%{_unitdir}
install -m 0644 web-paste-simple.service %{buildroot}%{_unitdir}
install -d %{buildroot}%{storage}

%check
make test

%post server
%systemd_post apache-httpd.service

%pre server
getent group webpastesimple >/dev/null || groupadd -r webpastesimple
getent passwd webpastesimple >/dev/null || \
    useradd -r -g webpastesimple -d %{storage} -s /sbin/nologin \
        -c "web-paste-simple daemon" webpastesimple
exit 0

%preun server
%systemd_preun apache-httpd.service

%postun server
%systemd_postun_with_restart apache-httpd.service 

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files server
%{_bindir}/*
%{_unitdir}/*
%dir %attr(750, webpastesimple, webpastesimple) %{storage}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.002-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-19
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.002-18
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-15
- Perl 5.32 rebuild

* Fri Feb 07 2020 Petr Pisar <ppisar@redhat.com> - 0.002-14
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 10 2015 Petr Pisar <ppisar@redhat.com> 0.002-1
- Specfile autogenerated by cpanspec 1.78.
