# remirepo/fedora spec file for rnp
#
# Copyright (c) 2022-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%bcond_with         licensecheck

%if 0%{?rhel} == 8
# use openssl by default as botan2 is too old
%bcond_without      openssl
%else
# use botan2 as openssl seems experimental/wip
%bcond_with         openssl
%endif

%global libname     librnp
%global soname      0

Name:          rnp
Summary:       OpenPGP (RFC4880) tools
Version:       0.17.0
Release:       1%{?dist}
# See rnp-files-by-license.txt and upstream LICENSE* files
License:       BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MIT

URL:           https://github.com/rnpgp/rnp
Source0:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz.asc
# See https://www.rnpgp.org/openpgp_keys/
Source2:       %{name}-keyring.gpg
# Use --with licensecheck to generate
Source3:       %{name}-files-by-license.txt

# Don't install static libraries
Patch0:         %{name}-static.patch
# Upstream libsexp patch
Patch1:         %{name}-gcc13.patch

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2) 
%if %{with openssl}
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  json-c-devel >= 0.11
BuildRequires:  gtest-devel
%else
BuildRequires:  pkgconfig(botan-2) >= 2.14
BuildRequires:  cmake(json-c) >= 0.11
BuildRequires:  cmake(GTest)
%endif
BuildRequires:  python3
BuildRequires:  gnupg2
BuildRequires:  rubygem-asciidoctor
%if %{with licensecheck}
BuildRequires:  licensecheck
%endif

Requires:       %{libname}%{?_isa} = %{version}-%{release}


%description
RNP is a set of OpenPGP (RFC4880) tools.

%package -n %{libname}
Summary:    Library for all OpenPGP functions
%global libsexp_version 0.8.2
Provides:   bundled(libsexp) = %{libsexp_version}


%description -n %{libname}
%{libname} is the library used by RNP for all OpenPGP functions,
useful for developers to build against, different from GPGME.


%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.


%prep
%setup -q -n %{name}-v%{version}
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%patch -P0 -p1

pushd src/libsexp
%patch -P1 -p1
# retrieve LICENSE
cp LICENSE.md ../../LICENSE-libsexp.md
# check bundled version
grep -q %{libsexp_version} version.txt
popd

%if %{with licensecheck}
LST=$(mktemp)

licensecheck -r . | sed -e 's:^./::' >$LST
grep -v UNKNOWN $LST | sed -e 's/.*: //' | sort -u | while read lic
do
	echo -e "\n$lic\n------------"
	grep ": $lic\$" $LST | sed -e "s/: $lic//"
done  | tee %{SOURCE3}
rm $LST
%endif


%build
%cmake . \
   -DINSTALL_STATIC_LIBS:BOOL=OFF \
%if %{with openssl}
   -DCRYPTO_BACKEND:STRING=openssl \
%else
   -DCRYPTO_BACKEND:STRING=botan \
%endif
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DDOWNLOAD_RUBYRNP:BOOL=OFF

%cmake_build


%install
%cmake_install


%if %{with tests}
%check
# erratic results on koji
FILTER="s2k_iteration_tuning"

%if 0%{?rhel} == 8
%ifarch s390x
# to investigate
FILTER="$FILTER|cli_tests-Encryption|cli_tests-Misc"
%endif
%endif

%ctest --exclude-regex $FILTER
%endif


%files
%{_bindir}/rnp
%{_bindir}/rnpkeys
%{_mandir}/man1/rnp*

%files -n %{libname}
%license LICENSE*
%{_libdir}/%{libname}.so.%{soname}*

%files -n %{libname}-devel
%doc CHANGELOG.md
%{_includedir}/rnp
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/cmake/rnp
%{_mandir}/man3/librnp*


%changelog
* Tue May  2 2023 Remi Collet <remi@remirepo.net> - 0.17.0-1
- update to 0.17.0
- use bundled libsexp
- add patch to not install static libraries from
  https://github.com/rnpgp/rnp/pull/2071
- use upstream patch to fix build with GCC 13

* Thu Apr 13 2023 Remi Collet <remi@remirepo.net> - 0.16.3-1
- update to 0.16.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov  4 2022 Remi Collet <remi@remirepo.net> - 0.16.2-4
- add upstream fix to clarify license and abandoned patent

* Wed Nov  2 2022 Remi Collet <remi@remirepo.net> - 0.16.2-3
- add files by license list in package sources
- open https://github.com/rnpgp/rnp/issues/1932 missing MIT
- add man pages
- check archive signature

* Fri Oct 28 2022 Remi Collet <remi@remirepo.net> - 0.16.2-2
- switch from botan-2 to openssl on EL-8

* Thu Oct 27 2022 Remi Collet <remi@remirepo.net> - 0.16.2-1
- initial package
