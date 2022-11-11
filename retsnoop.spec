# simfail runs on bare metal but not on Koji
%bcond_with check

%global toolchain clang

# upstream build system requires the use of libbpf and bpftool sources
# see https://github.com/anakryiko/retsnoop/issues/22
%global libbpf_url https://github.com/libbpf/libbpf
%global libbpf_version 1.0.1

%global bpftool_url https://github.com/libbpf/bpftool
%global bpftool_version 7.0.0

Name:           retsnoop
Version:        0.9.3
Release:        %autorelease
Summary:        A tool for investigating kernel error call stacks

# retsnoop: BSD-2-Clause
# bundled libbpf: LGPL-2.1-only OR BSD-2-Clause
# statically linked rust crates
#
## Apache-2.0 OR MIT
# addr2line
# backtrace
# bitflags
# cc
# cfg-if
# cfg-if 0.1
# cpp_demangle
# crc32fast
# dirs-sys
# dirs2
# fallible-iterator
# findshlibs
# flate2
# getopts
# gimli
# glob
# libc
# memmap
# object
# pest
# proc-macro2
# quote
# rustc-demangle
# rustc-serialize
# rustc-test
# rustc_version 0.3
# semver-parser
# semver
# smallvec
# stable_deref_trait
# syn
# term 0.6
# thiserror
# time 0.1
# ucd-trie
# unicode-width
# vec_map
#
## MIT
# ansi_term
# atty
# clap2
# strsim
# textwrap 0.11
# typed-arena
#
## 0BSD OR Apache-2.0 OR MIT
# adler
#
## MIT OR Unlicense
# memchr
#
## Apache-2.0 OR MIT OR Zlib
# miniz_oxide
#
## (MIT OR Apache-2.0) AND Unicode-DFS-2016
# unicode-ident
#
License:        BSD-2-Clause AND (LGPL-2.1-only OR BSD-2-Clause) AND (Apache-2.0 OR MIT) AND MIT AND (0BSD OR Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://github.com/anakryiko/retsnoop
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{libbpf_url}/archive/v%{libbpf_version}/libbpf-%{libbpf_version}.tar.gz
Source2:        %{bpftool_url}/archive/v%{bpftool_version}/bpftool-%{bpftool_version}.tar.gz
Source3:        README.Fedora

# has a Rust component
ExclusiveArch:  %{rust_arches}
# rust syn crate not compiling on 32-bit ARM
ExcludeArch:    armv7hl

BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  rust-packaging >= 21
# libbpf deps
BuildRequires:  elfutils-libelf-devel

# upstream does not support dynamic linking
Provides:       bundled(libbpf) = %{libbpf_version}

%description
retsnoop is BPF-based tool that is meant to help debugging kernel issues. It
allows to capture call stacks of kernel functions that return errors (NULL or
-Exxx) and emits every such detected call stack, along with the captured
results.


%prep
%autosetup -p1
# provide the libbpf version we specify rather than using git submodule
tar xf %{SOURCE1}
rmdir libbpf
mv libbpf-%{libbpf_version} libbpf
mv libbpf/LICENSE libbpf-LICENSE
mv libbpf/LICENSE.BSD-2-Clause  libbpf-LICENSE.BSD-2-Clause
mv libbpf/LICENSE.LGPL-2.1 libbpf-LICENSE.LGPL-2.1

# provide the bpftool version we specify rather than using git submodule
tar xf %{SOURCE2}
rmdir bpftool
mv bpftool-%{bpftool_version} bpftool
# same license files as libbpf, no-op

# README.Fedora
cp -p %{SOURCE3} .

# Rust parts
# the path is hardcoded, make sure Cargo.toml is found in the expected place
ln -s sidecar/Cargo.toml .
# the checksums in the lock file might not match
rm sidecar/Cargo.lock
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires


%build
%if 0%{?fedora} < 36
# this is only called automatically after
# https://www.fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
%set_build_flags
%endif
cd sidecar
%cargo_build
cd -
%make_build -C src HOSTCC=clang


%install
%make_install -C src prefix=%{_prefix}


%if %{with check}
%check
./src/simfail -a
%endif


%files
%license LICENSE libbpf-LICENSE*
%doc README.md TODO.md README.Fedora
%{_bindir}/retsnoop
%{_bindir}/simfail


%changelog
%autochangelog
