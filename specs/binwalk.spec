Name:           binwalk
Version:        3.1.0
Release:        2%{?dist}
Summary:        Firmware analysis tool

License:        %{shrink:
    (0BSD OR MIT OR Apache-2.0)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND BSL-1.0
    AND ISC
    AND MIT
    AND (MIT OR Apache-2.0)
    AND (MIT OR Zlib OR Apache-2.0)
    AND (MPL-2.0)
    AND (Unlicense OR MIT)
    AND (Zlib OR Apache-2.0 OR MIT)
    }
# LICENSE.dependencies contains a full license breakdown

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
%cargo_vendor_manifest

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

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
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_bindir}/binwalk

%changelog
%autochangelog
