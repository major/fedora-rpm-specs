%global commit 47f8ccf50c0933742847e657c4be9f5ba796c1a4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          openvpn-otp
Version:       1.0^20230731git%{shortcommit}
Release:       5%{?dist}
Summary:       OpenVPN OTP authentication support
License:       GPL-1.0-or-later AND Apache-2.0 AND Apache-1.0 AND APSL-2.0
URL:           https://github.com/evgeny-gridasov/%{name}
Source:        https://github.com/evgeny-gridasov/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source:        Apache-1.0.txt
Source:        Apache-2.0.txt
Source:        APSL-2.0.txt
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bash
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: openssl-devel >= 1.1.0
BuildRequires: openvpn-devel
BuildRequires: sed
# This is a plugin not linked against a lib, so hardcode the requirement
# since we require the parent configuration and plugin directories
Requires: openvpn >= 2.0

%description
This plug-in adds support for time based OTP (totp) and HMAC based OTP (hotp)
tokens for OpenVPN. Compatible with Google Authenticator software token, other
software and hardware based OTP tokens.

%prep
%autosetup -n %{name}-%{commit}
sed -n -e '/@APPLE_LICENSE_HEADER_START@/,/@APPLE_LICENSE_HEADER_END@/p' < src/base64.c > base64_copyright
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
./autogen.sh
%configure --with-openvpn-plugin-dir=%{_libdir}/openvpn/plugins/
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/openvpn/plugins/*.la

%files
%license LICENSE Apache-1.0.txt Apache-2.0.txt APSL-2.0.txt base64_copyright
%doc README.md
%{_libdir}/openvpn/plugins/openvpn-otp.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^20230731git47f8ccf-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^20230731git47f8ccf-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^20230731git47f8ccf-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0^20230731git47f8ccf-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Christian Schuermann <spike@fedoraproject.org> 1.0^20230731git47f8ccf-1
- Initial package
