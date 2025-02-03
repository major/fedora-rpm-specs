Name: libnetconf2
Version: 3.5.5
Release: 2%{?dist}
Summary: NETCONF protocol library
Url: https://github.com/CESNET/libnetconf2
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libyang) >= 2
BuildRequires:  curl-devel

%package devel
Summary:    Headers of libnetconf2 library
Conflicts:  libnetconf-devel
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Headers of libnetconf library.

%description
libnetconf2 is a NETCONF library in C intended for building NETCONF clients and
servers. NETCONF is the NETwork CONFiguration protocol introduced by IETF.


%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc README.md FAQ.md
%{_libdir}/libnetconf2.so.*
%{_datadir}/yang/modules/libnetconf2/*.yang

%files devel
%doc CODINGSTYLE.md
%{_libdir}/libnetconf2.so
%{_libdir}/pkgconfig/libnetconf2.pc
%{_includedir}/*.h
%{_includedir}/libnetconf2/*.h
%dir %{_includedir}/libnetconf2/


%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 3.5.5-2
- Add explicit BR: libxcrypt-devel

* Fri Jan 31 2025 Michal Ruprich <mruprich@redhat.com> - 3.5.5-1
- New version 3.5.5

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.25-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.25-1
- New upstream version

* Fri Jul 29 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.18-1
- New upstream version
- New dependency pam-devel

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.11-1
- New upstream version

* Thu Apr 21 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.1.7-1
- New upstream version

* Mon Nov 15 2021 Jakub Ružička <jakub.ruzicka@nic.cz> - 2.0.24-1
- Initial Packaging
