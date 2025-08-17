%global richname QR-Code-generator
%global cmakename qrcodegen-cmake
%global cmakesuffix cmake4

Name: qr-code-generator
Version: 1.8.0
Release: %autorelease

License: MIT
Summary: High-quality QR Code generator library
URL: https://github.com/nayuki/%{richname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/EasyCoding/%{cmakename}/archive/v%{version}-%{cmakesuffix}/%{cmakename}-%{version}-%{cmakesuffix}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-devel

%description
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen
Summary: High-quality QR Code generator library (plain C version)

%description -n libqrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen-devel
Summary: Development files for libqrcodegen
Requires: libqrcodegen%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegen-devel
Development files and headers for high-quality QR Code generator library
(plain C version).

%package -n libqrcodegencpp
Summary: High-quality QR Code generator library (C++ version)

%description -n libqrcodegencpp
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegencpp-devel
Summary: Development files for libqrcodegencpp
Requires: libqrcodegencpp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegencpp-devel
Development files and headers for high-quality QR Code generator library
(C++ version).

%package -n python3-qrcodegen
Summary: High-quality QR Code generator library (Python version)
BuildArch: noarch

%description -n python3-qrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%prep
%autosetup -n %{richname}-%{version}

# Unpacking CMake build script and assets...
tar -xf %{SOURCE1} %{cmakename}-%{version}-%{cmakesuffix}/cmake %{cmakename}-%{version}-%{cmakesuffix}/CMakeLists.txt --strip=1

%generate_buildrequires
pushd python >&2
%pyproject_buildrequires

%build
# Building C and C++ versions...
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQRCODEGEN_BUILD_TESTS:BOOL=ON
%cmake_build

# Building Python version...
pushd python
%pyproject_wheel
popd

%install
# Installing C and C++ versions...
%cmake_install

# Installing Python version...
%pyproject_install
%pyproject_save_files qrcodegen

# Installing a legacy symlink for compatibility...
ln -s qrcodegen.hpp %{buildroot}%{_includedir}/qrcodegencpp/QrCode.hpp

%check
%ctest
%pyproject_check_import

%files -n libqrcodegen
%license Readme.markdown
%{_libdir}/libqrcodegen.so.1*

%files -n libqrcodegen-devel
%{_includedir}/qrcodegen/
%{_libdir}/cmake/qrcodegen/
%{_libdir}/libqrcodegen.so
%{_libdir}/pkgconfig/qrcodegen.pc

%files -n libqrcodegencpp
%license Readme.markdown
%{_libdir}/libqrcodegencpp.so.1*

%files -n libqrcodegencpp-devel
%{_includedir}/qrcodegencpp/
%{_libdir}/cmake/qrcodegencpp/
%{_libdir}/libqrcodegencpp.so
%{_libdir}/pkgconfig/qrcodegencpp.pc

%files -n python3-qrcodegen -f %{pyproject_files}
%license Readme.markdown

%changelog
%autochangelog
