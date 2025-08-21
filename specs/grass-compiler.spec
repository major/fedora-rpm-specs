%bcond check 1

%global srcname grass

Name:           grass-compiler
Version:        0.13.4
Release:        %autorelease
Summary:        Sass compiler written purely in Rust

# (MIT OR Apache-2.0) AND Unicode-3.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:        (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND Unicode-3.0
# LICENSE.dependencies contains a full license breakdown
URL:            https://docs.rs/grass/
Source:         https://github.com/connorskees/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

Conflicts:      grass

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# also, str_split_big_limit fails on 32-bit due to use of a large integer
ExcludeArch:    %{ix86}

%description
A Sass compiler written purely in Rust.

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/grass

%prep
%autosetup -n %{srcname}-%{version} -p1
%cargo_prep
# warning: virtual workspace defaulting to `resolver = "1"` despite one or more
# workspace members being on edition 2021 which implies `resolver = "2"`
tomcli set Cargo.toml str workspace.resolver 2
# Remove unused (and unavailable) dependency
tomcli set crates/lib/Cargo.toml del dependencies.getrandom
# Avoid "warning: output filename collision" from the cdylib -- use default rlib only
tomcli set crates/lib/Cargo.toml del lib.crate-type

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
# %%cargo_install doesn't work with virtual workspaces, and we only want the binary
install -D -m0755 target/release/grass %{buildroot}%{_bindir}/grass

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
