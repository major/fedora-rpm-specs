# RHEL8 does not have libpskc, softhsm, ocserv yet
%if 0%{?rhel} && 0%{?rhel} == 8
%define use_tokens 0
%define use_ocserv 0
%define use_softhsm 0
%else
%define use_tokens 1
%define use_ocserv 1
%define use_softhsm 1
%endif

Name:       openconnect
Version:    9.12
Release:    9%{?dist}
Summary:    Open multi-protocol SSL VPN client
License:    LGPL-2.1-or-later
URL:        https://www.infradead.org/%{name}/

Source0:    %{url}/download/%{name}-%{version}.tar.gz
Source1:    %{url}/download/%{name}-%{version}.tar.gz.asc
Source2:    gpgkey-BE07D9FD54809AB2C4B0FF5F63762CDA67E2F359.asc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(socket_wrapper)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(uid_wrapper)
BuildRequires:  xdg-utils
%if %{use_softhsm}
BuildRequires:  softhsm
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  glibc-langpack-cs
%endif

%if %{use_ocserv}
BuildRequires:  ocserv
%endif

%if %{use_tokens}
BuildRequires:  pkgconfig(stoken)
BuildRequires:  pkgconfig(libpskc)
%endif

Obsoletes:      %{name}-lib-compat < %{version}-%{release}
Requires:       vpnc-script

%description
This package provides a multi-protocol VPN client for Cisco AnyConnect, Juniper
SSL VPN, Pulse/Ivanti Pulse Connect Secure, F5 BIG-IP, Fortinet Palo Alto
Networks GlobalProtect SSL VPN, Array Networks SSL VPN.

%package devel
Summary:        Development package for OpenConnect VPN authentication tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the core HTTP and authentication support from the
OpenConnect VPN client, to be used by GUI authentication dialogs for
NetworkManager etc.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure\
    --disable-dsa-tests \
    --htmldir=%{_pkgdocdir} \
    --with-default-gnutls-priority="@OPENCONNECT,SYSTEM" \
    --with-vpnc-script=/etc/vpnc/vpnc-script \
    --without-gnutls-version-check

%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/lib%{name}.la
rm -f %{buildroot}/%{_libexecdir}/%{name}/tncc-wrapper.py
rm -f %{buildroot}/%{_libexecdir}/%{name}/hipreport-android.sh
%find_lang %{name}

%check
%if 0%{?rhel} >= 10
# RSA key exchange disabled in DEFAULT crypto config
make VERBOSE=1 check XFAIL_TESTS="obsolete-server-crypto pfs"
%elif 0%{?fedora} || 0%{?rhel} >= 9
# 3DES and MD5 really are just gone.
make VERBOSE=1 check XFAIL_TESTS=obsolete-server-crypto
%else
make VERBOSE=1 check
%endif

%files -f %{name}.lang
%license COPYING.LGPL
%doc %{_pkgdocdir}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man8/*
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/%{name}/
%{_sbindir}/%{name}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 04 2025 Simone Caronni <negativo17@gmail.com> - 9.12-8
- Clean up SPEC file, drop EOL distro conditionals and macros.
- Fix Source URL, the old one is no longer valid.
- Use macros everywhere.
- Sort BuildRequires, files, configure parameters, etc.
- Be consistent with macros and variables.
- Trim changelog.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 9.12-5
- Cleanup spec, drop EOL release consditionals

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 20 2023 David Woodhouse <dwmw2@infradead.org> - 9.12-1
- Update to 9.12 release

* Wed May 17 2023 David Woodhouse <dwmw2@infradead.org> - 9.11-1
- Update to 9.11 release

* Thu May 04 2023 David Woodhouse <dwmw2@infradead.org> - 9.10-1
- Update to 9.10 release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 9.01-2
- Compile with support for browser / xdg-open

* Fri Apr 29 2022 David Woodhouse <dwmw2@infradead.org> - 9.01-1
- Update to 9.01 release

* Tue Apr 19 2022 David Woodhouse <dwmw2@infradead.org> - 8.20-2
- Merge upstream patch to fix loglevel (OC #401).

* Sun Feb 20 2022 David Woodhouse <dwmw2@infradead.org> - 8.20-1
- Update to 8.20 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
