# remirepo/fedora spec file for rnp
#
# Copyright (c) 2022-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%bcond_with         licensecheck
%bcond_without      libsexpp

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
Version:       0.17.1
Release:       4%{?dist}
# See rnp-files-by-license.txt and upstream LICENSE* files
License:       BSD-2-Clause AND Apache-2.0 AND MIT

URL:           https://github.com/rnpgp/rnp
Source0:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz.asc
# See https://www.rnpgp.org/openpgp_keys/
Source2:       %{name}-keyring.gpg
# Use --with licensecheck to generate
Source3:       %{name}-files-by-license.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
%if %{with libsexpp}
%global libsexpp_version 0.8.7
BuildRequires:  pkgconfig(sexpp) >= %{libsexpp_version}
%endif

Requires:       %{libname}%{?_isa} = %{version}-%{release}


%description
RNP is a set of OpenPGP (RFC4880) tools.

%package -n %{libname}
Summary:    Library for all OpenPGP functions
%if %{without libsexpp}
%global libsexpp_version 0.8.2
Provides:   bundled(libsexpp) = %{libsexpp_version}
%endif


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

%if %{with libsexpp}
rm -rf  src/libsexp
: check system version requirement
if ! grep -q 'sexpp>=%{libsexpp_version}' CMakeLists.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(grep 'sexpp>=' CMakeLists.txt | sed 's/.*sexp>=//;s/)//')
    exit 1
fi
%else
pushd src/libsexp
: retrieve LICENSE
cp LICENSE.md ../../LICENSE-libsexp.md
: check bundled version
if ! grep -q %{libsexpp_version} version.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(cat version.txt)
    exit 1
fi
popd
%endif

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
%if %{with libsexpp}
   -DSYSTEM_LIBSEXPP:BOOL=ON \
%else
   -DSYSTEM_LIBSEXPP:BOOL=OFF \
%endif
   -DENABLE_COVERAGE:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_FUZZERS:BOOL=OFF \
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DDOWNLOAD_RUBYRNP:BOOL=OFF

%cmake_build


%install
%cmake_install


%if %{with tests}
%check
# erratic results on koji
FILTER="s2k_iteration_tuning|test_key_add_userid|test_ffi_security_profile|EncryptElgamal|cli_tests"

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Carl George <carlwgeorge@fedoraproject.org> - 0.17.1-3
- Disable i686 build

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May  3 2024 Remi Collet <remi@remirepo.net> - 0.17.1-1
- update to 0.17.1
- drop all patches merged upstream

* Thu Feb  1 2024 Remi Collet <remi@remirepo.net> - 0.17.0-9
- ignore 3 failed tests (expiration issue) FTBFS #2261653

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep  5 2023 Remi Collet <remi@remirepo.net> - 0.17.0-7
- use system libsexpp

* Wed Jul 26 2023 Remi Collet <remi@remirepo.net> - 0.17.0-6
- refresh upstream patch to use shutil

* Wed Jul 26 2023 Remi Collet <remi@remirepo.net> - 0.17.0-5
- use upstream patch for setuptools

* Wed Jul 26 2023 Remi Collet <remi@remirepo.net> - 0.17.0-4
- use setuptools._distutils instead of distutils #2226397
  see https://github.com/rnpgp/rnp/issues/2112

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 0.17.0-3
- libsexp renamed to libsexpp

* Wed Jun 21 2023 Remi Collet <remi@remirepo.net> - 0.17.0-2
- add build option to use system libsexp (disabled)
  using patch from https://github.com/rnpgp/rnp/pull/2102

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
