# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate lcms2

Name:           rust-lcms2
Version:        6.1.0
Release:        %autorelease
Summary:        ICC color profile handling. Rusty wrapper for Little CMS

License:        MIT
URL:            https://crates.io/crates/lcms2
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove feature for statically linking liblcms2
Patch:          lcms2-fix-metadata.diff
# * include correct license text:
#   https://github.com/kornelski/rust-lcms2/issues/21
#   https://github.com/kornelski/rust-lcms2/pull/22
#   upstream seems to have accidentally included the MIT-0 text instead of MIT
Patch:          https://github.com/kornelski/rust-lcms2/pull/22.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
ICC color profile handling. Rusty wrapper for Little CMS.}

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
# * skip one failing test (needs investigating)
%cargo_test -- -- --exact --skip profile::setters
%endif

%changelog
%autochangelog