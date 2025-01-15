%global gdalcpp_version 1.3.0
%global protozero_version 1.6.3

%global testcommit ecfdeb0d5ffcfcb60939651d517d5d7d1bb041a3

%define debug_package %{nil}

Name:           libosmium
Version:        2.21.0
Release:        %autorelease
Summary:        Fast and flexible C++ library for working with OpenStreetMap data

License:        BSL-1.0
URL:            http://osmcode.org/libosmium/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/osmcode/osm-testdata/archive/%{testcommit}/osm-testdata-%{testcommit}.tar.gz

BuildRequires:  cmake make gcc-c++
BuildRequires:  doxygen graphviz xmlstarlet
BuildRequires:  ruby rubygems spatialite-tools

BuildRequires:  catch2-devel
BuildRequires:  boost-devel
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  gdalcpp-devel >= %{gdalcpp_version}
BuildRequires:  expat-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  lz4-devel
BuildRequires:  sparsehash-devel
BuildRequires:  gdal-devel
BuildRequires:  geos-devel

BuildRequires:  catch2-static
BuildRequires:  protozero-static
BuildRequires:  gdalcpp-static

%description
A fast and flexible C++ library for working with OpenStreetMap data.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       boost-devel
Requires:       protozero-devel >= %{protozero_version}
Requires:       gdalcpp-devel >= %{gdalcpp_version}
Requires:       expat-devel
Requires:       zlib-devel
Requires:       bzip2-devel
Requires:       lz4-devel
Requires:       sparsehash-devel
Requires:       gdal-devel
Requires:       geos-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for developing
applications that use %{name}.


%prep
%setup -q -c -T -a 0 -a 1
mv %{name}-%{version} %{name}
mv osm-testdata-%{testcommit} osm-testdata
rm -rf libosmium/include/gdalcpp.h libosmium/test/catch
ln -sf /usr/include/catch2 libosmium/test/catch
sed -i -e 's/-O3 -g//' libosmium/CMakeLists.txt


%build
cd libosmium
%cmake -DBUILD_HEADERS=ON -DBUILD_DATA_TESTS=ON
%cmake_build
%cmake_build --target doc


%install
cd libosmium
%cmake_install
rm -rf %{buildroot}%{_docdir}


%check
cd libosmium
%ctest


%files devel
%doc libosmium/README.md libosmium/CHANGELOG.md
%license libosmium/LICENSE
%{_includedir}/osmium


%files doc
%doc libosmium/%{__cmake_builddir}/doc/html/*
%license libosmium/LICENSE


%changelog
%autochangelog
