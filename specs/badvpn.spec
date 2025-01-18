Name:           badvpn
Version:        1.999.130
Release:        13%{?dist}
Summary:        Peer-to-peer VPN solution

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ambrop72/badvpn
Source0:        https://github.com/ambrop72/badvpn/archive/1.999.130/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel

%description
BadVPN is a layer 2 peer-to-peer VPN solution.


%prep
%autosetup -p1


%build
# Use cmake macro but don't override BUILD_SHARED_LIBS as it breaks the build
%define mycmake %(echo '%{cmake}' | sed 's/-DBUILD_SHARED_LIBS:BOOL=ON//')
%mycmake

%cmake_build


%install
%cmake_install


%files
%license COPYING
%{_bindir}/badvpn-client
%{_bindir}/badvpn-flooder
%{_bindir}/badvpn-ncd
%{_bindir}/badvpn-ncd-request
%{_bindir}/badvpn-server
%{_bindir}/badvpn-tun2socks
%{_bindir}/badvpn-tunctl
%{_bindir}/badvpn-udpgw
%{_mandir}/man7/badvpn.7*
%{_mandir}/man8/badvpn-client.8*
%{_mandir}/man8/badvpn-server.8*
%{_mandir}/man8/badvpn-tun2socks.8*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.999.130-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.999.130-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.999.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Pete Walter <pwalter@fedoraproject.org> - 1.999.130-1
- Update to 1.999.130
- Switch to new cmake macros
- Switch to autosetup
- Add gcc BuildRequires
- Remove no longer needed buildroot cleaning in install section

* Sat Oct 25 2014 Pete Walter <pwalter@fedoraproject.com> - 1.999.129-1
- First Fedora build
