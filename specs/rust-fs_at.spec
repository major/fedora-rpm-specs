# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate fs_at

Name:           rust-fs_at
Version:        0.2.1
Release:        %autorelease
Summary:        Implementation of 'at' functions for various platforms

License:        Apache-2.0
URL:            https://crates.io/crates/fs_at
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          fs_at-fix-metadata-auto.diff
# * upstream PR to add missing Apache-2.0 license text:
#   https://github.com/rbtcollins/fs_at/pull/121
Patch:          https://github.com/rbtcollins/fs_at/pull/121.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Implementation of 'at' functions for various platforms.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+workaround-procmon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+workaround-procmon-devel %{_description}

This package contains library source intended for building other packages which
use the "workaround-procmon" feature of the "%{crate}" crate.

%files       -n %{name}+workaround-procmon-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

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
