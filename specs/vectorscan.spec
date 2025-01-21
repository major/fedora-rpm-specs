%global vectorscan_tag d29730e1cb9daaa66bda63426cdce83505d2c809
%global __cmake_in_source_build 1
%global _lto_cflags %{nil}

Name:           vectorscan
Version:        5.4.11
Release:        9%{?dist}
Summary:        A portable fork of hyperscan, used as a high performance pcre replacement
# note google test framework not part of shipped binary
# vectorscan is BSD-3-Clause but it utilizes boost, which is a C++ template
# library and ends up embedded in the binary. BSL is included here for
# completeness for this reason, but may not strictly be required as
# the source is contained in the boost-devel packages.
License:        BSD-3-Clause AND BSL-1.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2264465
ExcludeArch: s390x
URL:            https://github.com/VectorCamp/vectorscan
Source0:        https://github.com/VectorCamp/vectorscan/archive/%{vectorscan_tag}.tar.gz

Patch0: 0001-Change-PPC-default-to-power8.patch
Patch1: 0001-documentation-Add-cmake-option-to-build-man-pages.patch

# hyperscan is x86 only, so lets obsolete it. There is one package in the
# fedora repos that depends on hyperscan (suricata) and it appears to work
# with this vectorscan package.
Provides: hyperscan
Obsoletes: hyperscan < 5.4.7

BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  ragel
BuildRequires:  python3-sphinx
BuildRequires:  python3-breathe
BuildRequires:  doxygen
BuildRequires:  boost-devel
BuildRequires:  sqlite-devel
BuildRequires:  glibc-devel
BuildRequires:  python3-devel
BuildRequires:  libpcap-devel

%ifarch x86_64
# the doc lies about VBMI implying AVX512 implying AVX2, without AVX2 the build fails
%global fatruntime -DFAT_RUNTIME=ON -DBUILD_AVX2=ON -DBUILD_AVX512=ON -DBUILD_AVX512VBMI=ON
%else

%ifarch aarch64
%global fatruntime -DFAT_RUNTIME=ON -DBUILD_SVE=ON -DBUILD_SVE2=ON -DBUILD_SVE2_BITPERM=ON
%else
%global fatruntime -DFAT_RUNTIME=OFF
%endif

%endif

%description
A fork of Intel's Hyperscan, modified to run on more
platforms. Hyperscan is a high-performance multiple regex matching
library. It follows the regular expression syntax of the commonly-used
libpcre library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

%package devel
Summary: Development files for the vectorscan library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Provides: hyperscan-devel
Obsoletes: hyperscan-devel < 5.4.7

The vectorscan-devel package contains headers and libraries needed
to develop .

%prep
%setup -q -n vectorscan-%{vectorscan_tag}
%patch -P0 -p1
%patch -P1 -p1

%build
%cmake  -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:BOOL=ON %{fatruntime} . -Wno-dev
%cmake_build


%install
%cmake_install


%check
bin/unit-hyperscan


%files
%license COPYING
%license LICENSE
%{_libdir}/*.so.*
%doc README.md
%{_mandir}/man7/vectorscan.7.*

%files devel
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/examples/README.md
%doc %{_defaultdocdir}/%{name}/examples/*.cc
%doc %{_defaultdocdir}/%{name}/examples/*.c
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhs.pc
%{_includedir}/hs/

#------------------------------------------------------------------------------
%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-6
- Review issues, add man page updates, explicitly conflict hyperscan on x86

* Mon Feb 12 2024 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-5
- Fix fedora review issues

* Fri Feb  9 2024 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-4
- Make fedpkg lint happy

* Wed Dec  6 2023 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-3
- Enable Fat runtime on x86/aarch64

* Wed Dec  6 2023 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-2
- Change PPC compiler baseline to POWER8

* Wed Dec  6 2023 Jeremy Linton <jeremy.linton@arm.com> - 5.4.11-1
- Attempt upgrade to 5.4.11

* Thu Oct 12 2023 Jeremy Linton <jeremy.linton@arm.com> - 5.4.10-1
- Attempt upgrade to 5.4.10.1

* Fri May 13 2022 Jeremy Linton <jeremy.linton@arm.com> - 5.4.7-1
- First vectorscan package
