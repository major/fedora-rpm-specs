%bcond_without check

Name:           bootc
Version:        0.1.2
Release:        %{autorelease}
Summary:        Bootable container system

# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://github.com/containers/bootc
Source0:        %{url}/releases/download/v%{version}/bootc-%{version}.tar.zst
Source1:        %{url}/releases/download/v%{version}/bootc-%{version}-vendor.tar.zst

BuildRequires: make
BuildRequires: ostree-devel
BuildRequires: openssl-devel
%if 0%{?rhel} && !0%{?eln}
BuildRequires: rust-toolset
%else
BuildRequires: cargo-rpm-macros >= 25
%endif
BuildRequires: systemd

# For OS updates
Requires: skopeo

%description
%{summary}

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%cargo_vendor_manifest
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%make_install INSTALL="install -p -c"

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE-MIT
%license LICENSE-APACHE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/bootc
%{_prefix}/lib/bootc/
%{_mandir}/man8/bootc*

%changelog
%autochangelog

