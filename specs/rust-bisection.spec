# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate bisection

Name:           rust-bisection
Version:        0.1.0
Release:        %autorelease
Summary:        Rust implementation of the Python bisect module

License:        MIT
URL:            https://crates.io/crates/bisection
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Use proptest 1: https://github.com/SteadBytes/bisection/pull/6
Patch:          bisection-fix-metadata.diff
# * Add a LICENSE file (fix #3)
# * Fixes: “Please add a license file”
#   https://github.com/SteadBytes/bisection/issues/3
# * Text and copyright statement based on
#   https://github.com/SteadBytes/samplr/blob/add-license-1/LICENSE; date
#   adjusted to 2020 based on the last commit to this repository.
# * Given that the LICENSE file is based on another repository from the same
#   author, and there is little ambiguity in the text that can be meant by SPDX
#   “MIT”, we are sufficiently confident that there is no significant deviation
#   from the intended license text. See
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/#_license_text.
Patch10:        https://github.com/SteadBytes/bisection/pull/4.patch
# * Fix bisect::… instead of bisection::… in the examples
# * We would certainly send a PR upstream, except that this was never wrong in
#   git. It is unclear how the error was introduced to the released crate only.
Patch11:        bisection-0.1.0-fix-use-bisect-examples.patch
# * Fix integer overflow in midpoint calculation:
#   https://github.com/SteadBytes/bisection/pull/5
# * Fixes: let mid = (lo + hi) / 2; Overflows:
#   https://github.com/SteadBytes/bisection/issues/2
Patch12:        https://github.com/SteadBytes/bisection/pull/5.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust implementation of the Python bisect module.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
