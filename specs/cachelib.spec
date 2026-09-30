%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# The test suite has not been run in this package for years (it was built
# but never executed). Enable once a mock run shows which tests need the
# SysV/POSIX shm and NUMA facilities a build chroot lacks.
%bcond_with check

# Run the license check and stop, without the (hours long) compile: the fast
# way to find out whether a new vendor tarball needs a different License tag.
# The build then fails on purpose, so this is for local runs only, never CI.
#   mock -r fedora-rawhide-aarch64-getdeps --with license_check_only ...
%bcond_with license_check_only

# Upstream identifies a release by two numbers: kCachelibVersion, the
# API/format major in cachelib/allocator/CacheVersion.h (%%major_ver), and the
# weekly tag. Version joins them, major first: <major>.<tag without its v>,
# a plain dotted version like ImageMagick's four-part one (layout suggested
# by Carl George). For a snapshot past the tag, also paste the two %%global
# lines ./snapshot.sh prints (the commit and its distance from the tag):
# Version becomes <major>.<tag>^<distance>.<shortcommit>, the guidelines'
# <number>.<revision> snapshot form, and the distance keeps several snapshots
# between two tags in order. 17^20250203, the last build of the old scheme,
# sorts below.
%global basetag v2026.09.28.00
%global tagver %(echo %{basetag} | sed 's|^v||')
%if 0%{?commit:1}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo ^%{commits}.%{shortcommit}
%global archive_ref %{commit}
%global archive_dir CacheLib-%{commit}
%else
%global archive_ref %{basetag}
%global archive_dir CacheLib-%{tagver}
%endif

# see cachelib/allocator/CacheVersion.h's kCachelibVersion
%global major_ver 19

# getdeps has no per-project CMake defines, so these apply to every project
# it builds: LIB_INSTALL_DIR is the fbcode_builder-wide name for the library
# directory (getdeps looks in both lib and lib64 of its dependencies), the
# other two are only read by cachelib's own CMakeLists. Contents of a JSON
# object; the macro adds the braces (rpm would strip them from the value).
%global getdeps_extra_cmake_defines "LIB_INSTALL_DIR": "%{_lib}", "CACHELIB_MAJOR_VERSION": "%{major_ver}", "CONFIGS_INSTALL_DIR": "share/%{name}/test_configs"

Name:           cachelib
Version:        %{major_ver}.%{tagver}%{?snapinfo}
Release:        %autorelease
Summary:        Pluggable caching engine for scale high performance cache services

# cachelib itself is Apache-2.0. Vendored (see getdeps-vendor.txt in the
# license directory): folly, wangle, fbthrift Apache-2.0; fizz BSD-3-Clause;
# mvfst MIT with BSD-2-Clause and BSD-3-Clause third_party code; magic_enum
# and sparse-map MIT. Verified by %%getdeps_vendor_license_check in %%check.
# SourceLicense needs rpm >= 4.19; EPEL 9 (rpm 4.16) gets the full expression
# on the SRPM as before
%if !0%{?rhel} || 0%{?rhel} >= 10
SourceLicense:  Apache-2.0
%endif
# Vendored projects (getdeps-vendor.txt), as %%check's go_vendor_license report
# breaks them down; the config is getdeps-vendor-licenses.toml:
# Apache-2.0                                        folly, wangle, fbthrift
# BSD-3-Clause                                      fizz
# MIT                                               magic_enum
# MIT AND BSD-2-Clause AND BSD-3-Clause             mvfst (third-party code)
# MIT AND CC0-1.0 AND (Apache-2.0 OR CC0-1.0)       liboqs (Kyber/ML-KEM only)
# CC0-1.0 is liboqs' aarch64 Kyber code, as in Fedora's own liboqs License tag.
# Per-file licenses that the license files do not show, found by licensecheck
# (the full check below): folly/hash/detail/Crc32cDetail.cpp is Zlib, mvfst's
# quic/common/third-party/{expected.hpp,optional.h} are BSL-1.0, liboqs's
# common/sha3 brg_endian.h is MIT-CMU and its common/aes implementations are
# public domain, all compiled in. GPL-2.0 CMake find modules for LMDB and re2
# and an NCSA CheckAtomic.cmake under build/fbcode_builder and the projects'
# cmake/ directories are build-system helpers, nothing from them is compiled
# or shipped; the license config excludes them.
License:        %{shrink:
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    CC0-1.0 AND
    MIT AND
    (Apache-2.0 OR CC0-1.0) AND
    BSL-1.0 AND
    Zlib AND
    MIT-CMU AND
    LicenseRef-Fedora-Public-Domain
}
URL:            https://github.com/facebook/CacheLib
# GitHub ignores the last path component of an archive URL, so the file is
# named after the version, like Source1 (Packaging Guidelines, SourceURL:
# git hosting services)
Source0:        %{url}/archive/%{archive_ref}/%{name}-%{version}.tar.gz
# Third-party sources getdeps cannot take from Fedora packages, produced by
# ./vendor.sh (getdeps.py vendor); one directory per project plus
# getdeps-vendor.txt listing each project's pinned revision.
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        getdeps-vendor-licenses.toml
# The per-file licensecheck pass of the license check is expensive; run it
# only when Source1 is not the tarball it last passed on. After a full pass
# on a new tarball, copy its sha512 here from the sources file. (Plain rpm:
# this also runs when the SRPM is built, without folly-rpm-macros.)
%global vendor_checked_sha512 d024cc25d384a1625eb92ed2a642174f513cb247ddbb8436c3d1167771353566cb300e69e3f5996be0fb0193278b4010666f05af63cbbd7fbb399a12ca4475ea
%if "%(sha512sum %{SOURCE1} 2>/dev/null | cut -c1-128)" == "%{vendor_checked_sha512}"
%bcond_with license_full_check
%else
%bcond_without license_full_check
%endif
# Patches below apply to the vendored trees under vendor/ and to
# build/fbcode_builder. Each is an upstream fix the revisions this tag pins
# do not include yet; drop them as the pins move past the landed commits.
# v2026.09.28.00 picked up folly's FindLibDwarf fix (facebook/folly#2707,
# 51590144c), wangle's OpenSSL 4.0 fix (facebook/wangle#254) and the
# cachebench binary_trace_gen link fix (facebook/CacheLib#498, 1a643ff6), so
# those three patches are gone.
#
# OpenSSL 4.0 (Fedora 45+) made ASN1_STRING opaque and the X509_get_*
# accessors return const; folly does not compile against it.
# facebook/folly#2706, not landed. fizz's matching fix
# (facebookincubator/fizz#171) only touches a test header the dependency
# build never compiles, so it is not carried.
Patch:          0002-folly-build-against-OpenSSL-4.0.patch
# libcachelib_nvmitem.so is the one library built without a SOVERSION; facebook/CacheLib#500
Patch:          0005-cmake-give-cachelib_nvmitem-a-SOVERSION.patch
# fbthrift puts relocated metadata in a .rodata section, which -fPIC makes
# writable; the linker then emits an RWX text segment and glibc's aarch64
# loader crashes on it (BTI note + RWX). Rename the section to RELRO; facebook/fbthrift#712
Patch:          0006-fbthrift-keep-thrift-data-out-of-a-writable-rodata-section.patch
# --shared-lib dropped $LDFLAGS from the shared library links; facebook/CacheLib#499
Patch:          0007-getdeps-keep-LDFLAGS-on-the-shared-library-links.patch
# folly's F14 fallback (no SSE2/NEON: ppc64le) is ambiguous against
# libstdc++ 16's own heterogeneous lookup; fix on Michel's fork, submitted
# internally
Patch:          0008-folly-F14-fallback-forward-exact-key-lookups.patch
# getdeps-vendor.txt gains the version of each vendored project, from which
# the bundled() Provides are versioned (applied by vendor.sh before vendoring)
Patch:          0009-getdeps-record-the-checked-out-commit-and-a-version.patch

ExclusiveArch:  x86_64 aarch64 ppc64le
# -devel (last shipped as 17^20250203 in Fedora, 16^20230424 in EPEL 9) is gone:
# cachelib's headers include folly and fbthrift headers that Fedora no longer
# packages, so there is nothing usable to ship. No Provides on purpose.
Obsoletes:      %{name}-devel < 19.2026.09.14.00

BuildRequires:  folly-rpm-macros >= 46-9
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif
# everything else comes from %%getdeps_generate_buildrequires below


%global _description %{expand:
CacheLib is a C++ library providing in-process high performance caching
mechanism. CacheLib provides a thread safe API to build high throughput, low
overhead caching services, with built-in ability to leverage DRAM and SSD
caching transparently.}

%description %{_description}

%generate_buildrequires
%getdeps_generate_buildrequires
%getdeps_vendor_license_buildrequires -c %{SOURCE2}


%prep
%autosetup -n %{archive_dir} -a1 -p1
# delete vendored code that is neither compiled nor referenced by the build
# (the config's prune_directories: fbthrift's Go bindings)
%getdeps_vendor_prune -c %{SOURCE2}


%build
# Verify the License tag first: it only needs the unpacked trees, and a
# wrong tag then fails here in minutes rather than after the build. Not in
# %%prep, which the dynamic BuildRequires passes run more than once, before
# the detector is installed. -f adds the per-file licensecheck pass, see
# vendor_checked_sha512 above.
# -L: liboqs's LICENSE.txt sits in a versioned subdirectory of its tree (as
# did sparse-map's while it was vendored)
%getdeps_vendor_license_check -c %{SOURCE2} -L %{?with_license_full_check:-f}
%{?with_license_check_only: echo "license check only: stopping before the build"; exit 1}
%getdeps_build %{?with_check:-t}


%install
%getdeps_install
# cachelib installs its CMake config under lib/ regardless of LIB_INSTALL_DIR;
# %%getdeps_install only prunes %%{_libdir}
rm -rf %{buildroot}%{_prefix}/lib/cmake
# converts CSV key-value traces into cachebench's binary replay format; give
# the generic upstream name a package prefix
mv %{buildroot}%{_bindir}/binary_trace_gen %{buildroot}%{_bindir}/cachelib_binary_trace_gen
%if %{with check}
# test binaries are installed to <prefix>/tests; they are run from the
# build tree in %%check and not shipped
rm -rf %{buildroot}%{_prefix}/tests
%endif
%getdeps_vendor_license_install -c %{SOURCE2}


%check
%if %{with check}
%getdeps_test
%endif


%files -f %{getdeps_vendor_license_filelist}
%doc BENCHMARKS.md CHANGELOG.md README.md examples
%{_bindir}/cachebench
%{_bindir}/cachelib_binary_trace_gen
%{_datadir}/%{name}


%changelog
%autochangelog
