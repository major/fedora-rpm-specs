%global commit 88e927d2302966993724f06d57e89cc4bf6d5e35
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global tz_ver 2022g

Name:          libzonedetect
Version:       0~git%{shortcommit}
Release:       9%{?snap}%{?dist}
Summary:       Find the timezone for a given latitude and longitude

# The library is BSD-3, timezone-boundary-builder is MIT, the built database is ODbL-1.0
License:       BSD-3-Clause AND MIT AND ODbL-1.0
URL:           https://github.com/BertoldVdb/ZoneDetect
Source0:       https://github.com/BertoldVdb/ZoneDetect/archive/%{commit}/ZoneDetect-%{shortcommit}.tar.gz
Source1:       CMakeLists.txt
# For building DB
Source2:       https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries_lakes.zip
Source3:       https://github.com/evansiroky/timezone-boundary-builder/releases/download/%{tz_ver}/timezones-with-oceans.shapefile.zip
Source4:       README.data

# Don't download DB source files, use local copies
Patch1:        ZoneDetect_builddb.patch
# Improve help of sample program, fix memory leak
Patch2:        ZoneDetect_demo.patch
# Add missing cstdint include
Patch3:        ZoneDetect_cstdint.patch

BuildRequires: gcc-c++
BuildRequires: cmake
# For building DB
BuildRequires: shapelib-devel

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc


%description
Find the timezone for a given latitude and longitude.

%package devel
Summary:       Development files for %{name}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n ZoneDetect-%{commit}
cp -a %{SOURCE1} .

# Prepare for DB build
mkdir -p database/builder/{naturalearth,timezone}
cp -a %{SOURCE2} database/builder/naturalearth/ne.zip
cp -a %{SOURCE3} database/builder/timezone/tz.zip
find database/builder/


%build
# Build DB
(cd database/builder/ && ./makedb.sh)

# Native build
%cmake
%cmake_build

# MinGW build
%mingw_cmake
%mingw_make_build


%install
# Native build
%cmake_install

# MinGW build
%mingw_make_install

mkdir -p %{buildroot}%{_datadir}/ZoneDetect/
cp -a database/builder/out_v1/* %{buildroot}%{_datadir}/ZoneDetect/
cp -a %{SOURCE4} %{buildroot}%{_datadir}/ZoneDetect/


%mingw_debug_install_post


%files
%doc README.md
%license LICENSE
%{_bindir}/ZoneDetect
%{_libdir}/libzonedetect.so.0*
%{_datadir}/ZoneDetect/


%files devel
%{_libdir}/libzonedetect.so
%{_includedir}/zonedetect.h

%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/ZoneDetect.exe
%{mingw32_bindir}/libzonedetect-0.dll
%{mingw32_includedir}/zonedetect.h
%{mingw32_libdir}/libzonedetect.dll.a

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/ZoneDetect.exe
%{mingw64_bindir}/libzonedetect-0.dll
%{mingw64_includedir}/zonedetect.h
%{mingw64_libdir}/libzonedetect.dll.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git88e927d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git88e927d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git88e927d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~git88e927d-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~git88e927d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Sandro Mani <manisandro@gmail.com> - 0~git.88e927d-4
- Update to git 88e927d

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~gitc65bc88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 0~gitc65bc88-2
- Fix pkgname -> name
- List ODbL-1.0 in License

* Fri Dec 16 2022 Sandro Mani <manisandro@gmail.com> - 0~gitc65bc88-1
- Initial package
