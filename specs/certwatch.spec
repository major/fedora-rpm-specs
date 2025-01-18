Name:           certwatch
Version:        1.2
Release:        18%{?dist}
Summary:        SSL/TLS certificate expiry warning generator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/notroj/certwatch
Source0:        https://github.com/notroj/certwatch/archive/v%{version}.tar.gz#/certwatch-%{version}.tar.gz
Source1:        notyetvalid.pem
BuildRequires:  gcc, openssl-devel, xmlto, autoconf, automake
BuildRequires:  perl(Test), perl(Test::Harness), perl(Test::Output), /usr/bin/openssl
BuildRequires: make
Obsoletes:      crypto-utils < 2.5-7

%description
This package provides a utility for generating warnings when SSL/TLS
certificates are soon to expire. 

%package mod_ssl
Summary: SSL/TLS certificate expiry warnings for mod_ssl
Requires: crontabs, mod_ssl, certwatch = %{version}-%{release}, /usr/sbin/sendmail

%description mod_ssl
The certwatch-mod_ssl package contains a cron script which runs a
daily check for any expired or soon-to-expire certificates listed in
the mod_ssl configuration.

%prep
%setup -q
autoreconf -i
cp %{SOURCE1} t/notvalid.pem

%build
%configure
%make_build

%install
%make_install
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 755 -p certwatch.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/certwatch

%check
export TZ=UTC
make check || true

%files
%{_bindir}/certwatch
%license LICENSE
%{_mandir}/man1/*

%files -n certwatch-mod_ssl
%ghost %{_sysconfdir}/sysconfig/certwatch
%config(noreplace) %{_sysconfdir}/cron.daily/certwatch
%{_mandir}/man5/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2-9
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Joe Orton <jorton@redhat.com> - 1.2-7
- fix FTBFS (#1923387)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug  4 2020 Joe Orton <jorton@redhat.com> - 1.2-5
- re-enable LTO (#1863318)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1.2-3
- Disable LTO on s390x for now

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Joe Orton <jorton@redhat.com> - 1.2-1
- Initial revision

