%undefine __cmake_in_source_build

Name:		yubihsm-shell
Version:	2.7.3
Release:	%autorelease
Summary:	Tools to interact with YubiHSM 2

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0 
URL:		https://github.com/Yubico/%{name}/
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg
# https://github.com/Yubico/yubihsm-shell/pull/411
Patch2:	yubihsm-shell-2.5.0-pcsc-lite.patch
# OpenSSL 4.0 build fixes
Patch3: 0001-Add-const-qualifiers-in-attest-example.patch

BuildRequires:	cmake
BuildRequires:	cppcheck
BuildRequires:	gcc
%if 0%{?fedora}
BuildRequires:	lcov
%endif
BuildRequires:	gengetopt
BuildRequires:	help2man
BuildRequires:	openssl-devel
BuildRequires:	libcurl-devel
BuildRequires:	libedit-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	clang
BuildRequires:	pkg-config
BuildRequires:	libusb-compat-0.1-devel
BuildRequires:	chrpath
BuildRequires:	gnupg2

%description
This package contains most of the components used to interact with
the YubiHSM 2 at both a user-facing and programmatic level.

%package devel
Summary: Development tools for interacting with YubiHSM 2
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for working with yubihsm 2.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1


%build
%set_build_flags
# https://bugzilla.redhat.com/show_bug.cgi?id=1865658#c6
# The generated code fails to build on s390x in Fedora 33
# For now, disable this particular check when building this arch
%ifarch s390x
export CFLAGS="$CFLAGS -Wno-error=format-overflow"
%endif
# OpenSSL 3.0 deprecates a lot of functions still widely used here
export CFLAGS="$CFLAGS -Wno-error=deprecated-declarations"
%cmake -DCMAKE_SKIP_INSTALL_RPATH=ON \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64}
   %endif
   %{nil}
%cmake_build


%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-shell
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-wrap
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/pkcs11/yubihsm_pkcs11.so


%files
%license LICENSE
%{_bindir}/yubihsm-auth
%{_bindir}/yubihsm-shell
%{_bindir}/yubihsm-wrap
%{_libdir}/libyubihsm.so.2
%{_libdir}/libyubihsm.so.2.*
%{_libdir}/libyubihsm_http.so.2
%{_libdir}/libyubihsm_http.so.2.*
%{_libdir}/libyubihsm_usb.so.2
%{_libdir}/libyubihsm_usb.so.2.*
%{_libdir}/libykhsmauth.so.2
%{_libdir}/libykhsmauth.so.2.*
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/yubihsm_pkcs11.so
%doc 
%{_mandir}/man1/yubihsm-auth.1.*
%{_mandir}/man1/yubihsm-shell.1.*
%{_mandir}/man1/yubihsm-wrap.1.*

%files devel
%{_libdir}/libyubihsm.so
%{_libdir}/libyubihsm_http.so
%{_libdir}/libyubihsm_usb.so
%{_libdir}/libykhsmauth.so
%{_includedir}/yubihsm.h
%{_includedir}/ykhsmauth.h
%dir %{_includedir}/pkcs11
%{_includedir}/pkcs11/pkcs11.h
%{_includedir}/pkcs11/pkcs11y.h
%{_includedir}/pkcs11/pkcs11f.h
%{_includedir}/pkcs11/pkcs11t.h
%{_datadir}/pkgconfig/yubihsm.pc
%{_datadir}/pkgconfig/ykhsmauth.pc

%changelog
%autochangelog
