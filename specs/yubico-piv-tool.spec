Name:		yubico-piv-tool
Version:	2.7.3
Release:	%autorelease
Summary:	Tool for interacting with the PIV applet on a YubiKey

License:	BSD-2-Clause
URL:		https://developers.yubico.com/yubico-piv-tool/
Source0:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg

# OpenSSL 4.0 build fixes
# https://github.com/Yubico/yubico-piv-tool/pull/583
Patch1:         0001-Fix-const-correctness-in-OpenSSL-utils.patch

BuildRequires:	pcsc-lite-devel
BuildRequires:  openssl-devel
BuildRequires:  chrpath
BuildRequires:	gnupg2 gengetopt help2man
BuildRequires:	check-devel
BuildRequires:	gcc gcc-c++
BuildRequires:	cmake
BuildRequires:	zlib-devel
Requires:		pcsc-lite-ccid

%description
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create certificate requests, and other operations. A shared library and
a command-line tool is included.

%package devel
Summary: Tool for interacting with the PIV applet on a YubiKey
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.
This package includes development files.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1

%build
%cmake \
    -DBUILD_STATIC_LIB=OFF
%cmake_build

%check
%ctest --output-on-failure

%install
%cmake_install


%files
%license COPYING
%{_bindir}/yubico-piv-tool
%{_libdir}/libykpiv.so.2*
%{_libdir}/libykcs11.so.2*
%{_mandir}/man1/yubico-piv-tool.1.gz

%files devel
%{_libdir}/libykpiv.so
%{_libdir}/libykcs11.so
%attr(0644,root,root) %{_libdir}/pkgconfig/ykpiv.pc
%attr(0644,root,root) %{_libdir}/pkgconfig/ykcs11.pc
%dir %{_includedir}/ykpiv
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv.h
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv-config.h


%changelog
%autochangelog
