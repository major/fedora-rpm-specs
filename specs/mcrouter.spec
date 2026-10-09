%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# The test suite was never run in this package (it failed to even link in
# the autotools days). Enable once a mock run shows what it needs.
%bcond_with check

# Run the license check and stop, without the (hours long) compile: the fast
# way to find out whether a new vendor tarball needs a different License tag.
# The build then fails on purpose, so this is for local runs only, never CI.
#   mock -r fedora-rawhide-aarch64-getdeps --with license_check_only ...
%bcond_with license_check_only

# Upstream cuts a weekly tag, vYYYY.MM.DD.NN; Version is the tag without its
# v. For a snapshot past the tag, also paste the two %%global lines
# ./snapshot.sh prints (the commit and its distance from the tag): Version
# becomes <tag>^<distance>.<shortcommit>, the guidelines' <number>.<revision>
# snapshot form, and the distance keeps several snapshots between two tags in
# order. 0.41.0.20250203, the last build of the autotools-era scheme, sorts
# below.
%global basetag v2026.10.05.00
%global tagver %(echo %{basetag} | sed 's|^v||')
%if 0%{?commit:1}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo ^%{commits}.%{shortcommit}
%global archive_ref %{commit}
%global archive_dir mcrouter-%{commit}
%else
%global archive_ref %{basetag}
%global archive_dir mcrouter-%{tagver}
%endif

# The CMake conversion left the version to the builder ("0.1.0-dev" by
# default); this is what --version and the startup log print. getdeps has no
# per-project CMake defines, so it is passed to every project it builds.
# Contents of a JSON object; the macro adds the braces.
%global getdeps_extra_cmake_defines "MCROUTER_PACKAGE_VERSION": "%{version}"

# the license config the macros read: Source2, plus the EL fragment on EL
%global getdeps_licenses_toml vendor-licenses.toml

Name:           mcrouter
Version:        %{tagver}%{?snapinfo}
Release:        %autorelease
Summary:        Memcached protocol router for scaling Memcached deployments

# SourceLicense needs rpm >= 4.19; EPEL 9 (rpm 4.16) gets the full expression
# on the SRPM as before
%if !0%{?rhel} || 0%{?rhel} >= 10
SourceLicense:  MIT
%endif
# Vendored projects (getdeps-vendor.txt), as %%check's go_vendor_license report
# breaks them down; the config is getdeps-vendor-licenses.toml:
# Apache-2.0                                        folly, wangle, fbthrift
# BSD-3-Clause                                      fizz
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
# mcrouter/lib/fbi/queue.h (BSD-3-Clause and/or MIT) is covered by both.
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    CC0-1.0 AND
    (Apache-2.0 OR CC0-1.0) AND
    BSL-1.0 AND
    Zlib AND
    MIT-CMU AND
    LicenseRef-Fedora-Public-Domain
}
URL:            https://github.com/facebook/mcrouter
# GitHub ignores the last path component of an archive URL, so the file is
# named after the version, like Source1 (Packaging Guidelines, SourceURL:
# git hosting services)
Source0:        %{url}/archive/%{archive_ref}/%{name}-%{version}.tar.gz
# The dependencies getdeps cannot take from Fedora packages, at the revisions
# recorded in vendor/getdeps-vendor.txt; produced by ./vendor.sh
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
%global vendor_checked_sha512 03ce1dc3b255275bd8d074f2ed26a156806925901a8c6fbb21208ecbfa8234558ca4cf446ac0a1179b435a7097dce3be96cd6732ed2e6fa12a742ef675710268
%if "%(sha512sum %{SOURCE1} 2>/dev/null | cut -c1-128)" == "%{vendor_checked_sha512}"
%bcond_with license_full_check
%else
%bcond_without license_full_check
%endif

# Patches to the vendored trees (vendor/<project>/...) are applied at build
# time, after Source1 is unpacked; ./vendor.sh skips them when vendoring.
# folly against OpenSSL 4.0 (Fedora 45+): facebook/folly#2706, in review
# (wangle's counterpart, facebook/wangle#254, has landed)
Patch:          0001-folly-build-against-OpenSSL-4.0.patch
# fbthrift puts relocated metadata in a .rodata section, which -fPIC/-fPIE
# makes writable; the linker then emits an RWX segment that Fedora's
# --error-rwx-segments refuses and glibc's aarch64 loader crashes on.
# facebook/fbthrift#712 landed and was reverted for an unrelated internal
# size limit; carried until it lands again.
Patch:          0003-fbthrift-keep-thrift-data-out-of-a-writable-rodata-section.patch
# folly's F14 fallback (no SSE2/NEON: ppc64le) is ambiguous against
# libstdc++ 16's own heterogeneous lookup; submitted internally from
# michel-slm/folly 4193514eb
Patch:          0004-folly-F14-fallback-forward-exact-key-lookups.patch
# mcrouter itself against current folly (explicit gflags includes) and
# Boost 1.90 (filesystem/convenience.hpp removed); submitted internally
Patch:          0005-Build-against-current-folly-and-Boost-1.90.patch
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

# ppc64le was dropped in 0.41.0.20250203 over the folly F14 fallback bug
# (rhbz#2344416); Patch2 fixes the current incarnation of it, and cachelib
# builds on ppc64le with the same patch.
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  folly-rpm-macros >= 46-11
# mcrouter's CMake links the executables with -latomic. Fedora buildroots
# have the library already; CentOS Stream 10's do not, and gcc ships only
# the /usr/lib64/libatomic.so symlink, so the x86_64 link failed with
# "cannot find /usr/lib64/libatomic.so.1.2.0" (koji task 151008378) while
# aarch64 and ppc64le happened to have it installed.
BuildRequires:  libatomic
%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif

%description
Mcrouter (pronounced mc router) is a Memcached protocol router for scaling
Memcached deployments.

Because the routing and feature logic are abstracted from the client in
mcrouter deployments, the client may simply communicate with destination
hosts through mcrouter over a TCP connection using standard memcached
protocol. Typically, little or no client modification is needed to use
mcrouter, which was designed to be a drop-in proxy between the client and
Memcached hosts.


%generate_buildrequires
%getdeps_generate_buildrequires
%getdeps_vendor_license_buildrequires -c %{getdeps_licenses_toml}


%prep
%autosetup -n %{archive_dir} -a1 -p1
cp -p %{SOURCE2} %{getdeps_licenses_toml}
%if 0%{?rhel}
tar -xf %{SOURCE3}
cat %{getdeps_vendor_dir}/getdeps-vendor-el.txt >> %{getdeps_vendor_dir}/getdeps-vendor.txt
rm -f %{getdeps_vendor_dir}/getdeps-vendor-el.txt
cat %{SOURCE4} >> %{getdeps_licenses_toml}
%endif
# delete vendored code that is neither compiled nor referenced by the build
# (the config's prune_directories: fbthrift's Go bindings)
%getdeps_vendor_prune -c %{getdeps_licenses_toml}
# autotools leftovers (FSFAP boost macros, a GPL-3.0-or-later
# ax_python_devel.m4), not used by the CMake build
rm -rf mcrouter/m4


%build
# Verify the License tag first: it only needs the unpacked trees, and a
# wrong tag then fails here in minutes rather than after the build. Not in
# %%prep, which the dynamic BuildRequires passes run more than once, before
# the detector is installed. -f adds the per-file licensecheck pass, see
# vendor_checked_sha512 above.
# -L: liboqs's LICENSE.txt sits in a versioned subdirectory of its tree
%getdeps_vendor_license_check -c %{getdeps_licenses_toml} -L %{?with_license_full_check:-f}
%{?with_license_check_only: echo "license check only: stopping before the build"; exit 1}
%getdeps_build %{?with_check:-t}


%install
%getdeps_install
%getdeps_vendor_license_install -c %{getdeps_licenses_toml}


%check
%if %{with check}
%getdeps_test
%endif


%files -f %{getdeps_vendor_license_filelist}
%doc README.md
%{_bindir}/mcrouter
%{_bindir}/mcpiper


%changelog
%autochangelog
