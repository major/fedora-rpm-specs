Name: thc-ipv6
Version: 3.8
Release: 7%{?dist}
Summary: Toolkit for attacking the IPv6 protocol suite


# Automatically converted from old format: AGPLv3 with exceptions - review is highly recommended.
License: LicenseRef-Callaway-AGPLv3-with-exceptions
URL: https://github.com/vanhauser-thc/thc-ipv6
Source0: https://github.com/vanhauser-thc/thc-ipv6/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: https://github.com/vanhauser-thc/thc-ipv6/commit/5dea4ce77dbff19c53c027229365fd5aad4570d3.patch#/thc-ipv6-3.8-socket.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libpcap-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: openssl-devel
%else
BuildRequires: openssl11-devel
%endif
BuildRequires: libnetfilter_queue-devel
BuildRequires: perl-generators

%description
A complete tool set to attack the inherent protocol weaknesses of IPv6
and ICMPv6, including an easy to use packet factory library.

%prep
%autosetup -p1

%build
%if 0%{?rhel} == 7
OPENSSL_CFLAGS="$(pkg-config --cflags-only-I openssl11)"
OPENSSL_LDFLAGS="$(pkg-config --libs-only-L openssl11)"
%endif

%make_build \
  CFLAGS="%{optflags} $OPENSSL_CFLAGS -D_HAVE_SSL" \
  LDFLAGS="%{?__global_ldflags} $OPENSSL_LDFLAGS -lpcap -lssl -lcrypto"

%install
%make_install \
  PREFIX=%{_prefix} \
  STRIP=%{_bindir}/true

%files
%license LICENSE LICENSE.OPENSSL
%doc CHANGES HOWTO-INJECT README
%{_bindir}/*
%{_mandir}/man8/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Robert Scheck <robert@fedoraproject.org> - 3.8-1
- Upgrade to 3.8 (#1902857)
- Spec file modernization including support for RHEL/CentOS 7
- Remove perl(Socket6) dependency (thanks to Michal Josef Špaček)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.4-10
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.4-1
- Update to 3.4 (rhbz #1531027)
- Fix build and add SSL support

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-1
- Update to 3.0
- Add new deps
- Do not strip binaries

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 2.7-1
- Update to 2.7

* Fri Jul 25 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-2
- Rename the package properly

* Wed Apr 16 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-1
- Initial specfile
