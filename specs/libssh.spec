Name:           libssh
Version:        0.12.0
Release:        %autorelease
Summary:        A library implementing the SSH protocol
License:        LGPL-2.1-or-later
URL:            http://www.libssh.org

Source0:        https://www.libssh.org/files/0.12/%{name}-%{version}.tar.xz
Source1:        https://www.libssh.org/files/0.12/%{name}-%{version}.tar.xz.asc
Source2:        https://www.libssh.org/files/0x03D5DF8CFDD3E8E7_libssh_libssh_org_gpgkey.asc#/%{name}.keyring
Source3:        libssh_client.config
Source4:        libssh_server.config

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkcs11-provider
BuildRequires:  libfido2-devel
# for testing
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  krb5-workstation
BuildRequires:  libcmocka-devel
BuildRequires:  pam_wrapper
BuildRequires:  socket_wrapper
BuildRequires:  nss_wrapper
BuildRequires:  uid_wrapper
BuildRequires:  priv_wrapper
BuildRequires:  openssh-clients
BuildRequires:  openssh-server
BuildRequires:  openssh-sk-dummy
BuildRequires:  nmap-ncat
BuildRequires:  p11-kit-devel
BuildRequires:  opensc
BuildRequires:  softhsm
BuildRequires:  gnutls-utils
BuildRequires:  hostname

Requires:       %{name}-config = %{version}-%{release}

Recommends:     crypto-policies

%ifarch aarch64 ppc64 ppc64le s390x x86_64 riscv64
Provides: libssh_threads.so.4()(64bit)
%else
Provides: libssh_threads.so.4
%endif

%description
The ssh library was designed to be used by programmers needing a working SSH
implementation by the mean of a library. The complete control of the client is
made by the programmer. With libssh, you can remotely execute programs, transfer
files, use a secure and transparent tunnel for your remote programs. With its
Secure FTP implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package config
Summary:        Configuration files for %{name}
BuildArch:      noarch
Obsoletes:      %{name} < 0.9.0-3

%description config
The %{name}-config package provides the default configuration files for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
    -DUNIT_TESTING=ON \
    -DCLIENT_TESTING=ON \
    -DSERVER_TESTING=ON \
    -DGSSAPI_TESTING=ON \
    -DWITH_PKCS11_URI=ON \
    -DWITH_PKCS11_PROVIDER=ON \
    -DWITH_FIDO2=ON \
    -DGLOBAL_CLIENT_CONFIG="%{_sysconfdir}/libssh/libssh_client.config" \
    -DGLOBAL_BIND_CONFIG="%{_sysconfdir}/libssh/libssh_server.config"

%cmake_build

%install
%cmake_install
install -d -m755 %{buildroot}%{_sysconfdir}/libssh
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libssh/libssh_client.config
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/libssh/libssh_server.config

#
# Workaround for the removal of libssh_threads.so
#
# This will allow libraries which link against libssh_threads.so or packages
# requiring it to continue working.
#
pushd %{buildroot}%{_libdir}
for i in libssh.so*;
do
    _target="${i}"
    _link_name="${i%libssh*}libssh_threads${i##*libssh}"
    if [ -L "${i}" ]; then
        _target="$(readlink ${i})"
    fi
    ln -s "${_target}" "${_link_name}"
done;
popd

%ldconfig_scriptlets

%check
# Tests are randomly failing when run in parallel
%global _smp_build_ncpus 1
%ctest

%files
%doc AUTHORS BSD CHANGELOG README
%license COPYING
%{_libdir}/libssh.so.4*
%{_libdir}/libssh_threads.so.4*

%files devel
%{_includedir}/libssh/
%{_libdir}/cmake/libssh/
%{_libdir}/pkgconfig/libssh.pc
%{_libdir}/libssh.so
%{_libdir}/libssh_threads.so

%files config
%attr(0755,root,root) %dir %{_sysconfdir}/libssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_client.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_server.config

%changelog
%autochangelog
