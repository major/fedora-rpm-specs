Name:           binwalk
Version:        3.1.0
Release:        1%{?dist}
Summary:        Firmware analysis tool

License:        MIT
URL:            https://github.com/ReFirmLabs/binwalk
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.xz

# Currently supported only on 64-bit systems
ExcludeArch:    %{ix86} %{arm}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  fontconfig-devel

%description
Binwalk is a tool for searching a given binary image for embedded files and
executable code. Specifically, it is designed for identifying files and code
embedded inside of firmware images.

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%install
%cargo_install
# Binwalk is packaged as a CLI application, not as a Rust library crate.
# Remove the crate source files installed by cargo to prevent "unpackaged files" errors.
rm -rf %{buildroot}/usr/share/cargo/registry

%check
# Skip 'analyze' and 'extract' doctests. 
# These tests rely on hardcoded file paths that are incompatible with the isolated mock build environment.
%cargo_test -- -- --skip analyze --skip extract

%files
%doc README.md
%license LICENSE
%{_bindir}/binwalk

%changelog
%autochangelog
