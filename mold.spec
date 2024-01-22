%if 0%{?el8}
# Disable annobin plugin on el8 (unusable with gcc-toolset-12)
%undefine _annotated_build
%endif

Name:		mold
Version:	2.4.0
Release:	2%{?dist}
Summary:	A Modern Linker

License:	MIT AND (Apache-2.0 OR MIT)
URL:		https://github.com/rui314/mold
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Allow building against the system-provided `xxhash.h`
Patch0:		0001-Use-system-compatible-include-path-for-xxhash.h.patch

# https://github.com/rui314/mold/pull/1176
Patch1:		0002-ELF-S390X-Skip-tests-that-still-fail-with-GCC-14.patch

# Possibly https://sourceware.org/bugzilla/show_bug.cgi?id=29655
Patch2:		0003-ELF-S390X-Skip-another-test-that-fails-with-GCC-14.patch

# Newer Fedora releases currently do not provide blake3-devel on i686
%if 0%{?fedora} >= 39
ExcludeArch:	%{ix86}
%endif

BuildRequires:	blake3-devel
BuildRequires:	cmake
%if 0%{?el8}
BuildRequires:	gcc-toolset-12
%else
BuildRequires:	gcc
BuildRequires:	gcc-c++ >= 10
%endif
BuildRequires:	libzstd-devel
BuildRequires:	mimalloc-devel
BuildRequires:	xxhash-static
BuildRequires:	zlib-devel

%if 0%{?fedora} >= 40
BuildRequires:	tbb-devel >= 2021.9
%else
# API-incompatible with older tbb 2020.3 shipped by Fedora < 40:
# https://bugzilla.redhat.com/show_bug.cgi?id=2036372
Provides:	bundled(tbb) = 2021.10
# Required by bundled oneTBB
BuildRequires:	hwloc-devel
%endif

# The following packages are only required for executing the tests
BuildRequires:	clang
BuildRequires:	gdb
BuildRequires:	glibc-static
%if ! 0%{?el8}
%ifarch x86_64
# Koji 64-bit buildroots do not contain packages from 32-bit builds, therefore
# the 'glibc-devel.i686' variant is provided as 'glibc32'.
BuildRequires: (glibc32 or glibc-devel(%__isa_name-32))
%endif
BuildRequires:	libdwarf-tools
%endif
BuildRequires:	libstdc++-static
BuildRequires:	llvm

Requires(post): %{_sbindir}/alternatives
Requires(preun): %{_sbindir}/alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1
rm -r third-party/{blake3,mimalloc,xxhash,zlib,zstd}
%if 0%{?fedora} >= 40
rm -r third-party/tbb
%endif

%build
%if 0%{?el8}
. /opt/rh/gcc-toolset-12/enable
%endif
%if 0%{?fedora} >= 40
%define tbb_flags -DMOLD_USE_SYSTEM_TBB=ON
%endif
%cmake -DMOLD_USE_SYSTEM_MIMALLOC=ON %{?tbb_flags}
%cmake_build

%install
%cmake_install

%post
if [ "$1" = 1 ]; then
  %{_sbindir}/alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 1
fi

%postun
if [ "$1" = 0 ]; then
  %{_sbindir}/alternatives --remove ld %{_bindir}/ld.mold
fi

%check
%if 0%{?el8}
. /opt/rh/gcc-toolset-12/enable
%endif
%ctest

%files
%license %{_docdir}/mold/LICENSE
%license %{_docdir}/mold/LICENSE.third-party
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/mold-wrapper.so
%{_libexecdir}/mold/ld
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
* Sun Jan 21 2024 Christoph Erhardt <fedora@sicherha.de> - 2.4.0-2
- Don't build-require files outside of permitted directories
- Drop upstreamed tbb patch
- Build against system-provided tbb where available
- Update version number of bundled tbb package to 2021.10
- Skip broken unit tests on s390x

* Sun Dec 03 2023 Christoph Erhardt <fedora@sicherha.de> - 2.4.0-1
- Bump version to 2.4.0 (rhbz#2252444)

* Tue Nov 14 2023 Christoph Erhardt <fedora@sicherha.de> - 2.3.3-1
- Bump version to 2.3.3

* Sat Nov 11 2023 Christoph Erhardt <fedora@sicherha.de> - 2.3.2-1
- Bump version to 2.3.2 (rhbz#2240671)

* Wed Aug 23 2023 Christoph Erhardt <fedora@sicherha.de> - 2.1.0-1
- Bump version to 2.1.0 (rhbz#2231758)

* Wed Jul 26 2023 Christoph Erhardt <fedora@sicherha.de> - 2.0.0-1
- Bump version to 2.0.0
- Change license from AGPL-3.0-or-later to MIT
- Update version number of bundled tbb package to 2021.9
- Remove `ExcludeArch` as mold now supports MIPS64

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 16 2023 Christoph Erhardt <fedora@sicherha.de> - 1.11.0-1
- Bump version to 1.11.0
- Update version number of bundled tbb package to 2021.7

* Sat Jan 21 2023 Christoph Erhardt <fedora@sicherha.de> - 1.10.0-1
- Bump version to 1.10.0
- Refresh patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Christoph Erhardt <fedora@sicherha.de> - 1.9.0-1
- Bump version to 1.9.0
- Don't enforce out-of-source build since the `inttypes.h` collision is resolved

* Mon Dec 26 2022 Christoph Erhardt <fedora@sicherha.de> - 1.8.0-1
- Bump version to 1.8.0
- Drop upstreamed patch
- Refresh patch

* Sat Nov 19 2022 Christoph Erhardt <fedora@sicherha.de> - 1.7.1-1
- Bump version to 1.7.1

* Fri Nov 18 2022 Christoph Erhardt <fedora@sicherha.de> - 1.7.0-1
- Bump version to 1.7.0
- Drop upstreamed patches
- Move from `ExclusiveArch` to `ExcludeArch` as only MIPS remains unsupported
- Build with GCC 12 on el8

* Sat Oct 22 2022 Christoph Erhardt <fedora@sicherha.de> - 1.6.0-1
- Bump version to 1.6.0
- Add new supported architectures
- Drop upstreamed patch

* Thu Sep 29 2022 Christoph Erhardt <fedora@sicherha.de> - 1.5.1-1
- Bump version to 1.5.1 (#2130132)
- Switch to CMake build
- Remove obsolete dependencies
- Add new supported architectures
- Refresh patch

* Sun Sep 04 2022 Christoph Erhardt <fedora@sicherha.de> - 1.4.2-1
- Bump version to 1.4.2
- Refresh patch

* Thu Aug 18 2022 Christoph Erhardt <fedora@sicherha.de> - 1.4.1-1
- Bump version to 1.4.1 (#2119324)
- Refresh patch
- Remove superfluous directory entries from `%%files`

* Sun Aug 07 2022 Christoph Erhardt <fedora@sicherha.de> - 1.4.0-1
- Bump version to 1.4.0 (#2116004)
- Refresh patch
- Use SPDX notation for `License:` field

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Christoph Erhardt <fedora@sicherha.de> - 1.3.1-1
- Bump version to 1.3.1 (#2103365)

* Sat Jun 18 2022 Christoph Erhardt <fedora@sicherha.de> - 1.3.0-1
- Bump version to 1.3.0 (#2098316)
- Drop upstreamed patches

* Sat Apr 30 2022 Christoph Erhardt <fedora@sicherha.de> - 1.2.1-1
- Bump version to 1.2.1
- Drop upstreamed patch
- Add support for 32-bit x86 and Arm

* Sat Apr 16 2022 Christoph Erhardt <fedora@sicherha.de> - 1.2-1
- Bump version to 1.2
- Drop upstreamed patches
- Set correct version of bundled tbb
- Suppress 'comparison between signed and unsigned' warnings

* Tue Mar 08 2022 Christoph Erhardt <fedora@sicherha.de> - 1.1.1-1
- Bump version to 1.1.1

* Mon Feb 21 2022 Christoph Erhardt <fedora@sicherha.de> - 1.1-1
- Bump version to 1.1
- Drop upstreamed patches
- Update description

* Thu Feb 17 2022 Christoph Erhardt <fedora@sicherha.de> - 1.0.2-2
- Rebuild due to mimalloc soname change

* Sun Jan 23 2022 Christoph Erhardt <fedora@sicherha.de> - 1.0.2-1
- Bump version to 1.0.2.

* Sat Jan 01 2022 Christoph Erhardt <fedora@sicherha.de> - 1.0.1-1
- Initial package for version 1.0.1.
