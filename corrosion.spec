Name:           corrosion
Version:        0.4.5
Release:        %autorelease
Summary:        Easy Rust and C/C++ Integration
#SourceLicense:  MIT

# Apache-2.0 OR BSL-1.0
# MIT
# MIT OR Apache-2.0
License:        MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/corrosion-rs/corrosion
Source:         %{url}/archive/v%{version}/corrosion-%{version}.tar.gz

# drop support for building with older versions of Rust
Patch:          0001-drop-build-rules-that-depend-on-Cargo.lock-files-bei.patch

BuildRequires:  cmake
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  rust

Requires:       cmake

%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating Rust
into an existing CMake project. Corrosion can automatically import
executables, static libraries, and dynamic libraries from a workspace or
package manifest (Cargo.toml file).

%prep
%autosetup -p1
%cargo_prep
find -name "Cargo.lock" -print -delete
rm generator/Compat.Cargo.*

%generate_buildrequires
cd generator
%cargo_generate_buildrequires
cd ..

%build
export RUSTFLAGS="%build_rustflags"
%cmake -DCORROSION_NATIVE_TOOLING:BOOL=ON
%cmake_build
cd generator
%cargo_license_summary
%{cargo_license} > ../LICENSE.dependencies
cd ..

%install
%cmake_install

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc RELEASES.md

%{_libexecdir}/corrosion-generator
%{_libdir}/cmake/Corrosion/
%{_datadir}/cmake/{Corrosion,CorrosionGenerator,FindRust}.cmake

%changelog
%autochangelog
