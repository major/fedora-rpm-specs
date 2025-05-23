# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate exr

Name:           rust-exr
Version:        1.73.0
Release:        %autorelease
Summary:        Read and write OpenEXR files without any unsafe code

License:        BSD-3-Clause
URL:            https://crates.io/crates/exr
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  dos2unix
BuildRequires:  tomcli

%global _description %{expand:
Read and write OpenEXR files without any unsafe code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%doc %{crate_instdir}/CONTRIBUTORS.md
%doc %{crate_instdir}/GUIDE.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/releasing.md
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
# fix CRLF line endings in source files: https://github.com/johannesvollmer/exrs/issues/239
find . -type f \( -name '*.md' -o -name '*.rs' \) -execdir dos2unix --keepdate '{}' '+'
# Do not depend on bencher; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.bencher
# Avoid a circular dependency on image.
tomcli set Cargo.toml del dev-dependencies.image
# These are the tests and examples that would have required the image crate.
rm tests/across_compression.rs
rm examples/6_extract_mip_map_pngs.rs
rm examples/1b_convert_exr_to_png.rs
rm examples/7_crop_alpha_rgba.rs
rm examples/7_crop_alpha_any_image.rs
rm examples/5b_extract_exr_layers_as_pngs.rs

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%ifarch s390x
# * skip tests which require test data that is not included in published crates
# * skip a test that is an expected failure on big-endian architectures
%cargo_test -- -- --skip compression::b44::test::border_on_multiview --skip image::validate_results::test_value_result::test_error --skip compare_compression_contents_ --skip compare_png_to_ --skip damaged --skip fuzzed --skip roundtrip_all_files_in_repository_x4 --skip pxr24_expect_error_on_big_endian
%else 
# * skip tests which require test data that is not included in published crates
%cargo_test -- -- --skip compression::b44::test::border_on_multiview --skip image::validate_results::test_value_result::test_error --skip compare_compression_contents_ --skip compare_png_to_ --skip damaged --skip fuzzed --skip roundtrip_all_files_in_repository_x4
%endif
%endif

%changelog
%autochangelog
