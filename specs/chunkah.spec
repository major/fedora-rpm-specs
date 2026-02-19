%global crate chunkah

Name:           chunkah
Version:        0.2.0
Release:        1%{?dist}
Summary:        OCI building tool for content-based container image layers

# chunkah itself is MIT OR Apache-2.0
# LICENSE.dependencies contains full breakdown of vendored crates
License:        MIT OR Apache-2.0
URL:            https://github.com/jlebon/chunkah
Source0:        %{url}/releases/download/v%{version}/%{crate}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
chunkah is an OCI building tool that takes a flat rootfs and outputs a
layered OCI image with content-based layers. It optimizes container image
layer reuse by grouping files based on their content (e.g., by RPM package)
rather than by Dockerfile instruction order.

It is a generalized successor to rpm-ostree's build-chunked-oci command.

%prep
%autosetup -n %{crate}-%{version} -p1
tar xf %{SOURCE1}
%cargo_prep -v vendor

%build
%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%check
%cargo_test

%files
%license LICENSE-MIT LICENSE-APACHE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/chunkah

%changelog
* Tue Feb 17 2026 Packit <hello@packit.dev> - 0.2.0-1
- Update to version 0.2.0

* Fri Jan 30 2026 Jonathan Lebon <jonathan@jlebon.com> - 0.1.1-1
- Update to 0.1.1
- Enable tests (vendor tarball now includes dev-dependencies)

* Wed Jan 28 2026 Jonathan Lebon <jonathan@jlebon.com> - 0.1.0-1
- Initial package
