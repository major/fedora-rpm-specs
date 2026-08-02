Name:           retis
Version:        1.6.4
Release:        %autorelease
Summary:        Tracing packets in the Linux networking stack
SourceLicense:  GPL-2.0-only
# Additional license terms from statically-linked Rust dependencies, from the
# output of %%{cargo_license_summary}:
#
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# GPL-2.0-only
# LGPL-2.1-only OR BSD-2-Clause
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    BSD-2-Clause AND
    GPL-2.0-only AND
    (LGPL-2.1-only OR BSD-2-Clause) AND
    LGPL-2.1-or-later AND
    MIT AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
    }

URL:            https://github.com/retis-org/retis
Source:         https://github.com/retis-org/retis/archive/v%{version}/%{name}-%{version}.tar.gz
# Manually created to use the rpm profile when building and installing the
# release target.
Patch:          retis-release-profile.diff
# Manually created to:
# - Remove the rbpf dependency (was in the unused 'debug' feature).
# - Remove the dev-dependencies.
# - Downgrade the libbpf-rs/cargo and pcap dependencies.
Patch:          retis-fix-deps.diff
# dep: bump pyo3 to 0.29
# https://github.com/retis-org/retis/commit/6e39a020ce8b3ca68163423e143e951a39929c87
# cherry-picked on v1.6.4, without changes to Cargo.lock
Patch:          0001-dep-bump-pyo3-to-0.29.patch

ExclusiveArch:  x86_64 aarch64

Requires:       python3

BuildRequires:  rust-packaging
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  python3-devel

%description
Tracing packets in the Linux networking stack, using eBPF and interfacing with
control and data paths such as OpenVSwitch.

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
make release %{?_smp_mflags}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
env CARGO_INSTALL_OPTS="--no-track" make install
install -m 0755 -d %{buildroot}%{_datadir}/retis/profiles
install -m 0644 retis/profiles/* %{buildroot}%{_datadir}/retis/profiles
rm -rf %{buildroot}/include
rm -rf %{buildroot}/pkgconfig
rm -f %{buildroot}/libbpf.a

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/retis
%{_datadir}/retis/profiles

%changelog
%autochangelog
