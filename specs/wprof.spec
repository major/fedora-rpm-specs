%global forgeurl https://github.com/anakryiko/wprof
Version:        0.6
%forgemeta

# run `fedpkg prep --define 'with_skip_vendored 1'`
# to skip the vendored tarballs (e.g. so you can update them
# when prepping a new version)
%bcond skip_vendored 0

# run ./get-commit-data.sh $WPROF_CHECKOUT_DIR with
# the version to package checked out, to generate the
# commit hashes and dates. If they are different from
# what is currently set, check if you need to update the
# version by hand

# we need to declare this to show it in the version string
# since we 'backport' the first two commits after 0.5, just
# use the commit hash of the latest commit we use
%global wprof_commit 23cbea909d4365c804b1a8d3744d8afc2f314280

# upstream build system requires the use of these sources
%global blazesym_url https://github.com/libbpf/blazesym
%global blazesym_commit ae290f612af8f0243b2a3f53ec7c0cf304e0bbad 
%global blazesym_shortcommit %(c=%{blazesym_commit}; echo ${c:0:7})
%global blazesym_date 20260722
%global blazesym_version 0.2.6^%{blazesym_date}git%{blazesym_shortcommit}

%global bpftool_url https://github.com/libbpf/bpftool
%global bpftool_commit c231921d11b37056875ebc991547b63d1679568d
%global bpftool_shortcommit %(c=%{bpftool_commit}; echo ${c:0:7})
%global bpftool_date 20260727
# see bpftool/src/main.c
# libbpf version + 6 to the major version
%global bpftool_version 7.8.0~^%{bpftool_date}git%{bpftool_shortcommit}

%global libbpf_url https://github.com/libbpf/libbpf
%global libbpf_commit 34e3ebf0f062cf81882c51ac95dce720101ca5cc
%global libbpf_shortcommit %(c=%{libbpf_commit}; echo ${c:0:7})
%global libbpf_date 20260630
# see libbpf/src/libbpf_version.h
%global libbpf_version 1.8~^%{libbpf_date}git%{libbpf_shortcommit}

%global strobelight_libs_url https://github.com/facebookincubator/strobelight-libs
%global strobelight_libs_commit 8793294940192d1b4d334e69d18f57928426379b
%global strobelight_libs_shortcommit %(c=%{strobelight_libs_commit}; echo ${c:0:7})
%global strobelight_libs_date 20260717
%global strobelight_libs_version 0.0.0^%{strobelight_libs_date}git%{strobelight_libs_shortcommit}

%global usdt_url https://github.com/libbpf/usdt
%global usdt_commit b0144b02dd885941cf60b2359365c768ee602b27
%global usdt_shortcommit %(c=%{usdt_commit}; echo ${c:0:7})
%global usdt_date 20260506
%global usdt_version 0.0.0^%{usdt_date}git%{usdt_shortcommit}

%global vmlinux_h_url https://github.com/libbpf/vmlinux.h
%global vmlinux_h_commit 6f2f90028084f1b636ee669e0288e289198506ff
%global vmlinux_h_shortcommit %(c=%{vmlinux_h_commit}; echo ${c:0:7})
%global vmlinux_h_date 20260817
# see vmlinux.h/Cargo.toml
%global vmlinux_h_version 0.0.0^%{vmlinux_h_date}git%{vmlinux_h_shortcommit}

Name:           wprof
Release:        %autorelease
Summary:        High-performance system-wide BPF-based workload tracer

SourceLicense:  BSD-3-Clause
# blazesym: BSD-3-Clause
# bpftool: GPL-2.0-only OR BSD-2-Clause
# libbpf: LGPL-2.1-only OR BSD-2-Clause
# strobelight-libs: LGPL-2.1-only OR BSD-2-Clause
# usdt: BSD-2-Clause
# vmlinux.h: GPL-2.0-only
## Vendored dependncies
### blazesym
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-3-Clause
# CDLA-Permissive-2.0
# ISC
# LGPL-2.1-only OR BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
### src/demangle 
# MIT OR Apache-2.0
### src/wpb
# Apache-2.0
# Apache-2.0 OR MIT
# MIT
License:        %{shrink:
  BSD-3-Clause
  AND (GPL-2.0-only OR BSD-2-Clause)
  AND (LGPL-2.1-only OR BSD-2-Clause)
  AND BSD-2-Clause
  AND GPL-2.0-only
  AND (0BSD OR MIT OR Apache-2.0)
  AND Apache-2.0
  AND (Apache-2.0 OR BSL-1.0)
  AND (Apache-2.0 OR ISC OR MIT)
  AND (Apache-2.0 OR MIT)
  AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
  AND CDLA-Permissive-2.0
  AND ISC
  AND MIT
  AND (MIT OR Zlib OR Apache-2.0)
  AND MPL-2.0
  AND Unicode-3.0
  AND (Unlicense OR MIT)
  AND Zlib
}
URL:            %{forgeurl}
Source0:        %{forgesource}
# TODO: switch to system-packaged blazesym
Source1:        %{blazesym_url}/archive/%{blazesym_commit}/blazesym-%{blazesym_version}.tar.gz
Source2:        %{bpftool_url}/archive/%{bpftool_commit}/bpftool-%{bpftool_version}.tar.gz
Source3:        %{libbpf_url}/archive/%{libbpf_commit}/libbpf-%{libbpf_version}.tar.gz
Source4:        %{vmlinux_h_url}/archive/%{vmlinux_h_commit}/vmlinux.h-%{vmlinux_h_version}.tar.gz
Source5:        %{strobelight_libs_url}/archive/%{strobelight_libs_commit}/strobelight-libs-%{strobelight_libs_version}.tar.gz
Source6:        %{usdt_url}/archive/%{usdt_commit}/usdt-%{usdt_version}.tar.gz
# one extra ../ because `fedpkg prep` / `centpkg prep` now nests inside a build directory
# (cd blazesym && cargo vendor)
# tar cfz ../../blazesym-%%{blazesym_version}-vendor.tar.gz blazesym/vendor
Source100:      blazesym-%{blazesym_version}-vendor.tar.gz
# (cd src/demangle && cargo vendor)
# tar cfz ../../wprof-demangle-%%{version}-vendor.tar.gz src/demangle/vendor
Source101:      wprof-demangle-%{version}-vendor.tar.gz
# (cd src/wpb && cargo vendor)
# tar cfz ../../wprof-wpb-%%{version}-vendor.tar.gz src/wpb/vendor
Source102:      wprof-wpb-%{version}-vendor.tar.gz

# share the bundled vmlinux header, don't try to fetch it again
Patch:          wprof-blazesym-shared-vmlinux.diff

# strobelight-libs only supports x86_64 and aarch64
ExclusiveArch:  x86_64 aarch64

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  elfutils-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Wprof is a low-overhead BPF-based tracer and profiler with the focus on holistic
system-level performance data capture and analysis. It employs powerful and
flexible model of split data capture vs analysis/visualization phases, which
allows to iterate on captured performance data with exactly the same original
data. Wprof generates Perfetto-based traces and provides many options for
filtering and narrowing down exact subset of data to be visualized.


%prep
%autosetup -N
tar xf %{SOURCE1}
tar xf %{SOURCE2}
tar xf %{SOURCE3}
tar xf %{SOURCE4}
tar xf %{SOURCE5}
tar xf %{SOURCE6}

rmdir blazesym
mv blazesym-%{blazesym_commit} blazesym

rmdir bpftool
mv bpftool-%{bpftool_commit} bpftool

rmdir libbpf
mv libbpf-%{libbpf_commit} libbpf

rmdir vmlinux.h
mv vmlinux.h-%{vmlinux_h_commit} vmlinux.h

rmdir strobelight-libs
mv strobelight-libs-%{strobelight_libs_commit} strobelight-libs

rmdir usdt
mv usdt-%{usdt_commit} usdt

%autopatch -p1
%if %{without skip_vendored}
tar xf %{SOURCE100}
tar xf %{SOURCE101}
tar xf %{SOURCE102}

# Rust parts
pushd blazesym
%cargo_prep -v vendor
popd

pushd src/demangle
%cargo_prep -v vendor
popd

pushd src/wpb
%cargo_prep -v vendor
popd
%endif


%build
%if 0%{?rhel} && 0%{?rhel} < 10
# build flags not set by default
%set_build_flags
%endif
%make_build -C src GIT_SHA=%{wprof_commit}

for proj in blazesym src/demangle src/wpb; do
  pushd ${proj}
  echo === ${proj} ===
  %{cargo_license_summary}
  %{cargo_license} > LICENSE.`basename ${proj}`.dependencies
  popd
done

for proj in blazesym bpftool libbpf strobelight-libs usdt; do
  mv ${proj}/LICENSE ./LICENSE.${proj}
  # collect license texts, first one wins
  if ls ${proj}/LICENSE.* >/dev/null 2>&1; then
    mv -n ${proj}/LICENSE.* .
  fi
done


%install
%if 0%{?rhel} && 0%{?rhel} < 10
# build flags not set by default
%set_build_flags
%endif
%make_install -C src prefix=%{_prefix} GIT_SHA=%{wprof_commit}


%files
%license LICENSE*
# blazesym vendored deps already got collected earlier
%license src/demangle/LICENSE.demangle.dependencies src/wpb/LICENSE.wpb.dependencies
%doc README.md UTRACE.md
%{_bindir}/wprof


%changelog
%autochangelog
