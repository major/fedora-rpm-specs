%{?mingw_package_header}
# Header-only package
%global debug_package %{nil}

%global pkgname directxmath
%global tag oct2024

Name:          mingw-%{pkgname}
Version:       3.20
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       MIT
URL:           https://github.com/microsoft/DirectXMath
Source0:       https://github.com/microsoft/DirectXMath/archive/%{tag}/%{pkgname}-%{version}.tar.gz
# Fix cmake module install dir
Patch0:        directxmath_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%prep
%autosetup -p1 -n DirectXMath-%{tag}


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_includedir}/directxmath/
%{mingw32_libdir}/pkgconfig/DirectXMath.pc
%{mingw32_datadir}/cmake/directxmath/

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_includedir}/directxmath/
%{mingw64_libdir}/pkgconfig/DirectXMath.pc
%{mingw64_datadir}/cmake/directxmath/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 17 2024 Sandro Mani <manisandro@gmail.com> - 3.20-1
- Update to 3.20

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 3.19-1
- Initial package
