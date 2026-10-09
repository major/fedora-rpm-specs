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
%global basetag v2026.10.05.00
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

# the license config the macros read: Source2, plus the EL fragment on EL
%global getdeps_licenses_toml vendor-licenses.toml

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
# EL needs two dependencies from source that Fedora takes from the system,
# because EPEL's versions are older than the manifests pin: glog, 0.3.5
# against a post-0.6.0 commit, and fast_float, 6.1.6 against 8.0.0, whose
# parse_options_t constructor folly's Conv.cpp needs. Rather than a second
# full vendor tree, this tarball holds only what EL builds additionally need;
# %%prep unpacks it there and appends its manifest to getdeps-vendor.txt, so
# the bundled() Provides, the license install and the license check cover it.
# Declared unconditionally on purpose: a Source inside %%if 0%%{?rhel} would
# be absent from an SRPM built on Fedora, and that SRPM could then not be
# rebuilt for EL at all. Fedora builds carry the 140 kB and ignore it.
# Its licenses are not covered by the per-file pass of any build: Fedora
# builds never unpack it, and EL has no licensecheck. They were scanned by
# hand on Fedora: glog is BSD-3-Clause throughout, plus an Apache-2.0 fuzzer
# source and an MIT Windows header, neither compiled; fast_float is
# Apache-2.0 OR MIT OR BSL-1.0, its license files in a versioned subdirectory
# (hence -L). Redo that scan whenever either pin moves.
Source3:        %{name}-%{version}-vendor-el.tar.xz
# The glog override the above tarball needs, kept apart because an override
# for a file that is not present is an error: %%prep appends it to a copy of
# Source2 on EL, and every license macro reads that copy.
Source4:        getdeps-vendor-licenses-el.toml
# The per-file licensecheck pass of the license check is expensive; run it
# only when Source1 is not the tarball it last passed on. After a full pass
# on a new tarball, copy its sha512 here from the sources file. (Plain rpm:
# this also runs when the SRPM is built, without folly-rpm-macros.)
%global vendor_checked_sha512 4da31af2482892790d02438ce0c0758a93a493b8e6b84541d06bdf0b08975c10e90a83e0c91384639c824b44c3502be1cdf4005d0601dfc861db5589861f6143
%if "%(sha512sum %{SOURCE1} 2>/dev/null | cut -c1-128)" == "%{vendor_checked_sha512}"
%bcond_with license_full_check
%else
%bcond_without license_full_check
%endif
# Patches below apply to the vendored trees under vendor/ and to
# build/fbcode_builder. Each is an upstream fix the revisions this tag pins
# do not include yet; drop them as the pins move past the landed commits.
# v2026.10.05.00 contains the getdeps change that records each vendored
# project's commit and version in getdeps-vendor.txt, so that patch is gone;
# v2026.09.28.00 had already taken folly's FindLibDwarf fix
# (facebook/folly#2707), wangle's OpenSSL 4.0 fix (facebook/wangle#254) and
# the cachebench binary_trace_gen link fix (facebook/CacheLib#498).
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
# The manifests build fmt, gflags, googletest, benchmark and Boost from
# source on EL although EPEL 10 has them, and they get zlib and lz4-static
# wrong there; submitted internally from michel-slm/CacheLib
# 21baa410 (applied by vendor.sh before vendoring, so the vendored set
# matches what each distro builds)
Patch:          0010-getdeps-map-the-EL-10-system-packages.patch
# glog's manifest forced BUILD_SHARED_LIBS=ON, so the vendored glog EL builds
# use came out shared and the executables linked it: the rpm then required
# libglog.so.1, which nothing ships (EPEL 10's glog is 0.3.5, soname 0).
# folly and fbthrift only set it under feature_shared_libs; submitted
# internally from michel-slm/CacheLib 6ad39916
Patch:          0011-getdeps-build-glog-shared-only-on-request.patch

ExclusiveArch:  x86_64 aarch64 ppc64le
# -devel (last shipped as 17^20250203 in Fedora, 16^20230424 in EPEL 9) is gone:
# cachelib's headers include folly and fbthrift headers that Fedora no longer
# packages, so there is nothing usable to ship. No Provides on purpose.
Obsoletes:      %{name}-devel < 19.2026.09.14.00

BuildRequires:  folly-rpm-macros >= 46-11
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
%getdeps_vendor_license_buildrequires -c %{getdeps_licenses_toml}


%prep
%autosetup -n %{archive_dir} -a1 -p1
# delete vendored code that is neither compiled nor referenced by the build
# (the config's prune_directories: fbthrift's Go bindings)
cp -p %{SOURCE2} %{getdeps_licenses_toml}
%if 0%{?rhel}
tar -xf %{SOURCE3}
cat %{getdeps_vendor_dir}/getdeps-vendor-el.txt >> %{getdeps_vendor_dir}/getdeps-vendor.txt
rm -f %{getdeps_vendor_dir}/getdeps-vendor-el.txt
cat %{SOURCE4} >> %{getdeps_licenses_toml}
%endif
%getdeps_vendor_prune -c %{getdeps_licenses_toml}


%build
# Verify the License tag first: it only needs the unpacked trees, and a
# wrong tag then fails here in minutes rather than after the build. Not in
# %%prep, which the dynamic BuildRequires passes run more than once, before
# the detector is installed. -f adds the per-file licensecheck pass, see
# vendor_checked_sha512 above.
# -L: liboqs's LICENSE.txt sits in a versioned subdirectory of its tree (as
# did sparse-map's while it was vendored)
%getdeps_vendor_license_check -c %{getdeps_licenses_toml} -L %{?with_license_full_check:-f}
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
%getdeps_vendor_license_install -c %{getdeps_licenses_toml}


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
