%global use_gcc_toolset 0%{?el8}
%global use_system_tbb  0%{?fedora} >= 40 || 0%{?rhel} >= 10

# 32-bit x86 is supported by RHEL < 10 and Fedora (the latter is implicitly
# covered by the conditional expression)
%global has_32bit_support 0%{?rhel} < 10

Name:           mold
Version:        2.36.0
Release:        %autorelease
Summary:        A Modern Linker

License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://github.com/rui314/mold
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Allow building against the system-provided `xxhash.h`
Patch0:         0001-Use-system-compatible-include-path-for-xxhash.h.patch

# Possibly https://sourceware.org/bugzilla/show_bug.cgi?id=29655
Patch1:         0002-ELF-S390X-Skip-tests-that-fail-due-to-buggy-code-pro.patch

# Fix static PIE on aarch64: https://github.com/rui314/mold/issues/1407
Patch2:         0003-Define-__rela_iplt_-start-end-as-absolute-symbols-if.patch

BuildRequires:  blake3-devel
BuildRequires:  cmake
%if %{use_gcc_toolset}
BuildRequires:  gcc-toolset-13
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++ >= 10
%endif
BuildRequires:  libzstd-devel
BuildRequires:  mimalloc-devel
BuildRequires:  xxhash-static
BuildRequires:  zlib-devel

%if %{use_system_tbb}
BuildRequires:  tbb-devel >= 2021.9
%else
# API-incompatible with older tbb 2020.3 shipped by Fedora < 40:
# https://bugzilla.redhat.com/show_bug.cgi?id=2036372
Provides:       bundled(tbb) = 2022.0
# Required by bundled oneTBB
BuildRequires:  hwloc-devel
%endif

# The following packages are only required for executing the tests
BuildRequires:  clang
BuildRequires:  gdb
BuildRequires:  glibc-static
%if ! 0%{?el8}
%ifarch x86_64
%if %{has_32bit_support}
# Koji 64-bit buildroots do not contain packages from 32-bit builds, therefore
# the 'glibc-devel.i686' variant is provided as 'glibc32'.
BuildRequires: (glibc32 or glibc-devel(%__isa_name-32))
%endif
%endif
BuildRequires:  libdwarf-tools
%endif
BuildRequires:  libstdc++-static
BuildRequires:  llvm
BuildRequires:  perl-interpreter

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
%if %{use_system_tbb}
rm -r third-party/tbb
%endif

%build
%if %{use_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
%if %{use_system_tbb}
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
%if %{use_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
%ctest

%files
%license %{_docdir}/mold/LICENSE
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/mold-wrapper.so
%{_libexecdir}/mold/ld
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
%autochangelog
