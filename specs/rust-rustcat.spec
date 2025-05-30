# Generated by rust2rpm 25
%bcond_without check

%global crate rustcat

Name:           rust-rustcat
Version:        1.3.0
Release:        %autorelease
Summary:        Rustcat - The Modern Port Listener & Reverse Shell

License:        MIT
URL:            https://crates.io/crates/rustcat
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump rustyline dependency from 9.0 to 13.0
Patch:          rustcat-fix-metadata.diff
Patch:          0001-port-to-rustyline-v12.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rustcat - The Modern Port Listener & Reverse Shell.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
License:        MIT AND MPL-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc README.md
%doc contributing.md
%{_bindir}/rcat

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# remove executable bits from source files
find . -type f -executable -print -exec chmod -x {} + ;

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
# rename binary from rc to rcat to avoid conflict with rc package
mv %{buildroot}%{_bindir}/rc %{buildroot}%{_bindir}/rcat

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
