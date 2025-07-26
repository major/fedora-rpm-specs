Name:           uid_wrapper
Version:        1.3.2
Release:        %autorelease

Summary:        A wrapper for privilege separation
License:        GPL-3.0-or-later
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        uid_wrapper.keyring

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package doesn't have a devel package cause this project is for
development/testing.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%check
%ctest

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libuid_wrapper.so*
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/uid_wrapper
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config.cmake
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/uid_wrapper.pc
%{_mandir}/man1/uid_wrapper.1*

%changelog
%autochangelog
