Name:           nsca-ng
Version:        1.6
Release:        14%{?dist}
Summary:        Add-on for transferring check results (and other commands) to Nagios or Icinga

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://nsca-ng.org
Source:         https://github.com/weiss/nsca-ng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
# Common
BuildRequires:  openssl-devel
BuildRequires:  libev-devel
BuildRequires:  libbsd-devel

%description
%{summary}.

%package client
Summary:        %{SUMMARY} (client)
Conflicts:      nsca-client

%description client
%{summary}.

%package server
Summary:        %{SUMMARY} (server)
BuildRequires:  libconfuse-devel
BuildRequires:  systemd-devel
Requires:       user(nagios)

%description server
%{summary}.

%prep
%autosetup
# Bundled stuff
sed -i -e "/lib\/ev\/libev.m4/d" m4/ev.m4
sed -r -i -e "/lib\/(ev|pidfile)\/Makefile/d" configure.ac
sed -r -i -e "/^MAYBE_(EV|PIDFILE)/d" lib/Makefile.am
rm -vr lib/{pidfile,ev}

%build
autoreconf -vfi
%configure \
  --enable-client \
  --enable-server \
  --with-ev=external \
  %{nil}
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} etc/nsca-ng.{service,socket}

%check
%make_build check

%files client
%license COPYING
%doc README NEWS PROTOCOL
%{_sbindir}/send_nsca
%{_mandir}/man8/send_nsca.8*
%config(noreplace) %{_sysconfdir}/send_nsca.cfg
%{_mandir}/man5/send_nsca.cfg.5*

%files server
%license COPYING
%doc README NEWS PROTOCOL
%{_unitdir}/nsca-ng.{socket,service}
%{_sbindir}/nsca-ng
%{_mandir}/man8/nsca-ng.8*
%attr(0640,nagios,nagios) %config(noreplace) %{_sysconfdir}/nsca-ng.cfg
%{_mandir}/man5/nsca-ng.cfg.5*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6-2
- Make sure that nsca-ng.cfg is owned by appropriate user

* Wed Dec 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6-1
- Initial package
