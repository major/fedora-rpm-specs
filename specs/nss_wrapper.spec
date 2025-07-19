Name:           nss_wrapper
Version:        1.1.16
Release:        %autorelease

License:        BSD-3-Clause
Summary:        A wrapper for the user, group and hosts NSS API
Url:            https://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        nss_wrapper.keyring

Patch0:         nwrap-fix-tests.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  perl-generators

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig

%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package cause this project is for
development/testing.

%package libs
Summary: nss_library shared library only

%description libs
The %{name}-libs package provides only the shared library.
For a minimal footprint, install just this package.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install

sed -i '1 s|/usr/bin/env\ perl|/usr/bin/perl|' %{buildroot}%{_bindir}/nss_wrapper.pl

%ldconfig_scriptlets

%check
%ctest

%files
%{_bindir}/nss_wrapper.pl
%dir %{_libdir}/cmake/nss_wrapper
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%{_libdir}/cmake/nss_wrapper/nss_wrapper-config.cmake
%{_libdir}/pkgconfig/nss_wrapper.pc
%{_mandir}/man1/nss_wrapper.1*

%files libs
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libnss_wrapper.so*

%changelog
%autochangelog
