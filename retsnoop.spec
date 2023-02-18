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
Version:        0.9.5
Release:        %autorelease
Summary:        A tool for investigating kernel error call stacks

# retsnoop: BSD-2-Clause
# bundled libbpf: LGPL-2.1-only OR BSD-2-Clause
# statically linked rust crates
# taken from LICENSE.dependencies on Fedora
#
# 0BSD OR MIT OR Apache-2.0: adler v1.0.2
# Apache-2.0 OR MIT: addr2line v0.18.0
# Apache-2.0 OR MIT: cpp_demangle v0.3.5
# Apache-2.0 OR MIT: object v0.29.0
# MIT OR Apache-2.0: backtrace v0.3.66
# MIT OR Apache-2.0: bitflags v1.3.2
# MIT OR Apache-2.0: cfg-if v0.1.10
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: crc32fast v1.3.2
# MIT OR Apache-2.0: dirs v2.0.2
# MIT OR Apache-2.0: dirs-sys v0.3.7
# MIT OR Apache-2.0: fallible-iterator v0.2.0
# MIT OR Apache-2.0: findshlibs v0.10.2
# MIT OR Apache-2.0: flate2 v1.0.24
# MIT OR Apache-2.0: getopts v0.2.21
# MIT OR Apache-2.0: gimli v0.26.2
# MIT OR Apache-2.0: glob v0.3.1
# MIT OR Apache-2.0: libc v0.2.139
# MIT OR Apache-2.0: memmap v0.7.0
# MIT OR Apache-2.0: rustc-demangle v0.1.21
# MIT OR Apache-2.0: rustc-serialize v0.3.24
# MIT OR Apache-2.0: rustc-test v0.3.1
# MIT OR Apache-2.0: smallvec v1.10.0
# MIT OR Apache-2.0: stable_deref_trait v1.2.0
# MIT OR Apache-2.0: term v0.6.1
# MIT OR Apache-2.0: time v0.1.45
# MIT OR Apache-2.0: unicode-width v0.1.10
# MIT OR Apache-2.0: vec_map v0.8.2
# MIT OR Zlib OR Apache-2.0: miniz_oxide v0.5.3
# MIT: ansi_term v0.12.1
# MIT: atty v0.2.14
# MIT: clap v2.34.0
# MIT: strsim v0.10.0
# MIT: textwrap v0.11.0
# MIT: typed-arena v2.0.2
# Unlicense OR MIT: memchr v2.5.0
License:        BSD-2-Clause AND (LGPL-2.1-only OR BSD-2-Clause) AND (Apache-2.0 OR MIT) AND MIT AND (0BSD OR Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Apache-2.0)
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
Provides:       bundled(bpftool) = %{bpftool_version}
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
%if 0%{?fedora}
%{cargo_license} > ../LICENSE.dependencies
%endif
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
%if 0%{?fedora}
%license LICENSE.dependencies
%endif
%doc README.md TODO.md README.Fedora
%{_bindir}/retsnoop
%{_bindir}/simfail


%changelog
%autochangelog
