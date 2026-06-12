%global test_data_version bbcacec05d60f923869545c5eab33d94c390d50e

Name:           libE57Format
Version:        3.3.0
Release:        %autorelease
Summary:        Library for reading & writing the E57 file format

License:        BSL-1.0
URL:            https://asmaloney.github.io/libE57Format-docs/
Source0:        https://github.com/asmaloney/libE57Format/archive/v%{version}/libE57Format-v%{version}.tar.gz
Source1:        https://github.com/asmaloney/libE57Format-test-data/archive/%{test_data_version}/libE57Format-test-data-%{test_data_version}.tar.gz
Patch0:         https://github.com/asmaloney/libE57Format/commit/ad54a32b22d4df96f569f667610f4a883c8f51ff.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/asmaloney/libE57Format/pull/346.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(XercesC)
BuildRequires:  crcpp-static
BuildRequires:  cmake(GTest)
BuildRequires:  libasan
BuildRequires:  libubsan

# libE57Format only supports little-endian
ExcludeArch:    s390x

%description
libE57Format is a C++ library which provides read & write support for the
ASTM-standard E57 file format on Linux, macOS, and Windows. E57 files store
3D point cloud data (produced by 3D imaging systems such as laser scanners),
attributes associated with 3D point data (color & intensity), and 2D images
(photos taken using a 3D imaging system).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -b1 -p1
rm -r extern/CRCpp
mv ../libE57Format-test-data-%{test_data_version} ../libE57Format-test-data

%build
%cmake -DE57_USE_EXTERNAL_CRCPP=ON -DE57_USE_EXTERNAL_GTEST=ON -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%{_vpath_builddir}/testE57

%files
%license LICENSE.md
%doc README.md
%doc CHANGELOG.md
%{_libdir}/libE57Format.so.3
%{_libdir}/libE57Format.so.3.*

%files devel
%{_includedir}/E57Format/
%{_libdir}/libE57Format.so
%{_libdir}/cmake/E57Format/

%changelog
%autochangelog
