# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate bzip2-sys
%global crate_version 0.1.13+1.0.8

Name:           rust-bzip2-sys
Version:        0.1.13
Release:        %autorelease
Summary:        Bindings to libbzip2 for bzip2 exposed as Reader/Writer streams

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2-sys
Source:         %{crates_source %{crate} %{crate_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          bzip2-sys-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(bzip2)

%global _description %{expand:
Bindings to libbzip2 for bzip2 compression and decompression exposed as
Reader/Writer streams.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(bzip2)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__disabled-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__disabled-devel %{_description}

This package contains library source intended for building other packages which
use the "__disabled" feature of the "%{crate}" crate.

%files       -n %{name}+__disabled-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{crate_version} -p1
%cargo_prep
# remove bundled bzip2 sources
rm -rv bzip2-1.0.8/

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
