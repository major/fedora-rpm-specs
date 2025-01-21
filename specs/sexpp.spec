# remirepo/fedora spec file for sexpp
#
# Copyright (c) 2023-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%bcond_with         licensecheck

%global libname     libsexpp
%global soname      0

Name:          sexpp
Summary:       S-expressions parser and generator tools
Version:       0.9.0
Release:       2%{?dist}
License:       MIT

URL:           https://github.com/rnpgp/%{name}
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
# Use --with licensecheck to generate
Source3:       %{name}-files-by-license.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?rhel} == 8
BuildRequires:  gtest-devel
%else
BuildRequires:  cmake(GTest)
%endif
%if %{with licensecheck}
BuildRequires:  licensecheck
%endif

Requires:       %{libname}%{?_isa} = %{version}-%{release}


%description
S-expressions parser and generator tools.


%package -n %{libname}
Summary:    S-expressions parser and generator library

%description -n %{libname}
%{libname} is a C++ library for working with S-expressions.

This implementation is derived from the reference SEXP C library developed by
Professors Ronald Rivest and Butler Lampson of MIT LCS (now CSAIL).


%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.


%prep
%setup -q

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
%if %{with tests}
   -DWITH_SEXP_TESTS:BOOL=ON \
%else
   -DWITH_SEXP_TESTS:BOOL=OFF \
%endif
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DWITH_SEXP_CLI:BOOL=ON \
   -DWITH_SANITIZERS:BOOL=OFF \
   -DWITH_COVERAGE:BOOL=OFF \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DDOWNLOAD_GTEST:BOOL=OFF

%cmake_build


%install
%cmake_install


%if %{with tests}
%check
%ctest
%endif


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%license LICENSE*
%{_libdir}/%{libname}.so.%{soname}*

%files -n %{libname}-devel
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Remi Collet <remi@remirepo.net> - 0.9.0-1
- update to 0.9.0

* Fri Jul 26 2024 Remi Collet <remi@remirepo.net> - 0.8.8-3
- Disable i686 build

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Remi Collet <remi@remirepo.net> - 0.8.8-1
- update to 0.8.8

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 0.8.7-1
- update to 0.8.7
- rename to sexpp

* Fri Jun 23 2023 Remi Collet <remi@remirepo.net> - 0.8.6-1
- update to 0.8.6
- drop patch merged upstream

* Wed Jun 21 2023 Remi Collet <remi@remirepo.net> - 0.8.5-1
- update to 0.8.5
- open https://github.com/rnpgp/sexp/pull/37 define SOVERSION

* Thu May  4 2023 Remi Collet <remi@remirepo.net> - 0.8.4-1
- initial package
- open https://github.com/rnpgp/sexp/issues/32 build as shared
- open https://github.com/rnpgp/sexp/issues/33 clarify license
