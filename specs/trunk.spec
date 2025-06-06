# Generated by rust2rpm 25
%bcond_without check

%global cargo_install_lib 0
# Overriding defaults flags in order to:
#  * Disable the update check, which is handled my rpm/dnf in this case
#  * Switch TLS stack from rustls to openssl (native-tls)
%global _trunk_features -n -f native-tls

Name:           trunk
Version:        0.21.13
Release:        %autorelease
Summary:        Build, bundle & ship your Rust WASM application to the web

# Upstream license specification: MIT/Apache-2.0
SourceLicense:  MIT OR Apache-2.0
# START: copied from license summary
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR MPL-2.0
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSL-1.0
# CC0-1.0
# CC0-1.0 OR MIT-0 OR Apache-2.0
# ISC
# MIT
# MIT AND BSD-3-Clause
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
# END: copied from license summary
# Unicode-DFS-2016: the regex-syntax crate bundles Unicode data
License:        Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR MPL-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT) AND Unicode-DFS-2016
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/trunk-rs/trunk
Source:         https://github.com/trunk-rs/trunk/archive/refs/tags/v%{version}.tar.gz
Source:         trunk-%{version}-vendor.tar.zstd

BuildRequires:  cargo-rpm-macros >= 26
# Required by the openssl/openssl-sys crate, which is used for TLS communication
BuildRequires:  openssl-devel

ExcludeArch: %{ix86}

%global _description %{expand:
Build, bundle & ship your Rust WASM application to the web.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1 -a1
%cargo_prep -v vendor
chmod a-x vendor/bumpalo/src/lib.rs
chmod a-x vendor/zip/src/spec.rs

%build
%cargo_build %{_trunk_features}
%{cargo_license_summary %{_trunk_features}}
%{cargo_license %{_trunk_features}} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install %{_trunk_features}

%if %{with check}
%check
# the following tests don't work in the rpm build:
#  tools::tests::download_and_install_binaries:
#    tests the dowload of binaries, which isn't possible in the build system due to missing internet access
%cargo_test %{_trunk_features} -- -- --skip tools::tests::download_and_install_binaries
%endif

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/trunk

%changelog
%autochangelog
