Name:           uid_wrapper
Version:        1.3.2
Release:        %autorelease

Summary:        A wrapper for privilege separation
License:        GPL-3.0-or-later
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
# Upstream signing key from its website, completed from keyservers/WKD:
#   curl -fsSL -o key.asc https://cryptomilk.org/0x8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D_asn_cryptomilk_org_gpgkey.asc
#   sq --home=none network search --output - 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D | sq keyring filter --experimental --cert 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D --output update.pgp
#   sq keyring merge key.asc update.pgp | sq packet dearmor --output uid_wrapper.keyring.new
#   mv uid_wrapper.keyring.new uid_wrapper.keyring
#   rm -f key.asc update.pgp
Source2:        uid_wrapper.keyring

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openpgpverify
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
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
