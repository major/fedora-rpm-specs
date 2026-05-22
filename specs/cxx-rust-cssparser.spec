Name:           cxx-rust-cssparser
Version:        1.0.0
Release:        1%{?dist}
Summary:        Library for parsing CSS using the Rust cssparser crate

# Rust Crates Licensing:
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib

License:        BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (Apache-2.0 OR MIT) and MIT AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib

URL:            https://invent.kde.org/libraries/cxx-rust-cssparser
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

# Hard modify a crate version
Patch0:         crate-fix.patch

# Fixes the build
# https://invent.kde.org/libraries/cxx-rust-cssparser/-/merge_requests/18
Patch1:         testpatch.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Corrosion)
BuildRequires:  rust-packaging
BuildRequires:  cxxbridge

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
%cargo_prep
find -name "Cargo.lock" -print -delete

%generate_buildrequires
cd rust
%cargo_generate_buildrequires
cd ..

%conf
%cmake_kf6
cd rust
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ..


%build
%cmake_build

%install
%cmake_install


%files
%license LICENSES/*
%license rust/LICENSE.dependencies
%{_kf6_bindir}/cxx-rust-cssparser-parse
%{_kf6_libdir}/lib%{name}.so.1
%{_kf6_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_kf6_libdir}/cmake/%{name}/
%{_kf6_libdir}/lib%{name}.so

%changelog
* Tue May 12 2026 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
