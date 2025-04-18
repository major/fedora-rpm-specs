# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate onig_sys

Name:           rust-onig_sys
Version:        69.8.1
Release:        %autorelease
Summary:        Rust bindings for oniguruma

License:        MIT
URL:            https://crates.io/crates/onig_sys
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump bindgen build-dependency from 0.59 to 0.69
# * remove reference to readme file that is not included in published crates
Patch:          onig_sys-fix-metadata.diff
# * unconditionally use bindgen and dynamic linking with pkg-config
Patch1:         0001-Unconditionally-use-bindgen-and-dynamic-linking-with.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(oniguruma) >= 6.8.0

%global _description %{expand:
The `onig_sys` crate contains raw rust bindings to the oniguruma
library. This crate exposes a set of unsafe functions which can then be
used by other crates to create safe wrappers around Oniguruma. You
probably don't want to link to this crate directly; instead check out
the `onig` crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(oniguruma) >= 6.8.0

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+generate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-devel %{_description}

This package contains library source intended for building other packages which
use the "generate" feature of the "%{crate}" crate.

%files       -n %{name}+generate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+posix-api-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+posix-api-devel %{_description}

This package contains library source intended for building other packages which
use the "posix-api" feature of the "%{crate}" crate.

%files       -n %{name}+posix-api-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+print-debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+print-debug-devel %{_description}

This package contains library source intended for building other packages which
use the "print-debug" feature of the "%{crate}" crate.

%files       -n %{name}+print-debug-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# remove bundled oniguruma sources
rm -r oniguruma/

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
