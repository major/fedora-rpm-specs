%global commit0 56d01798c210db75f21f4f77ad447e8dde50f3c2
%global date 20240112
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       c-icap-modules
Version:    0.5.7
Release:    4.%{date}git%{shortcommit0}%{?dist}
Summary:    Services for the c-icap server
License:    LGPL-2.0-or-later
URL:        http://c-icap.sourceforge.net/

Source0:    https://github.com/c-icap/c-icap-modules/archive/%{commit0}.tar.gz#/c-icap-modules-%{shortcommit0}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel >= %{version}
BuildRequires:  clamav-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  make

Requires:   c-icap >= %{version}

%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. Most of the commercial HTTP proxies must support the ICAP protocol,
the open source Squid 3.x proxy server supports it too.

Currently the following services have been implemented for the c-icap server:
  - virus_scan, an antivirus ICAP service
  - url_check, an URL blacklist/whitelist icap service
  - srv_content_filtering, a score based content filtering icap service

%prep
%autosetup -p1 -n c-icap-modules-%{commit0}

# See RECONF
echo "master-%{shortcommit0}" > VERSION.m4
autoreconf -vif

%build
%configure \
  --disable-static \
  --enable-shared \
  --enable-virus_scan-profiles \
  --with-clamav \
  --with-lmdb

%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/c-icap

%make_install

rm -f %{buildroot}%{_libdir}/c_icap/*.la

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default

%files
%license COPYING
%attr(640,root,c-icap) %config(noreplace) %{_sysconfdir}/c-icap/*.conf
%{_bindir}/c-icap-mods-sguardDB
%{_libdir}/c_icap/clamav_mod.so
%{_libdir}/c_icap/clamd_mod.so
%{_libdir}/c_icap/srv_content_filtering.so
%{_libdir}/c_icap/srv_url_check.so
%{_libdir}/c_icap/virus_scan.so
%{_datadir}/c_icap/templates/srv_content_filtering/en/BLOCK
%{_datadir}/c_icap/templates/srv_url_check/en/DENY
%{_datadir}/c_icap/templates/virus_scan/en/VIRUS_FOUND
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_HEAD
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_PROGRESS
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_TAIL
%{_datadir}/c_icap/templates/virus_scan/en/VIR_MODE_VIRUS_FOUND
%{_mandir}/man8/c-icap-mods-sguardDB.8*
%{_mandir}/man8/c-icap-mktcb.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-4.20240112git56d0179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 0.5.7-3.20240112git56d0179
- Rebuild for clamav 1.4.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2.20240112git56d0179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 17 2024 Frank Crawford <frank@crawford.emu.id.au> - 0.5.7-1.20240112gite50f3c2
- Updated to equivalent to 0.5.7 release.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-6.20230212gitfd1a1b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-5.20230212gitfd1a1b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 0.5.6-4.20230212gitfd1a1b7
- Rebuild for updated c-icap.

* Tue Sep 26 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.5.6-3.20230212gitfd1a1b7
- Rebuilt for clamav 1.0

* Mon Jul 10 2023 Simone Caronni <negativo17@gmail.com> - 0.5.6-2.20230212gitfd1a1b7
- Add missing BuildRequires.

* Wed May 24 2023 Simone Caronni <negativo17@gmail.com> - 0.5.6-1.20230212gitfd1a1b7
- Switch to LMDB.
- Update to latest snapshot.

* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 0.5.5-2
- Initial import.
