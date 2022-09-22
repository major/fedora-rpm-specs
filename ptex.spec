Name:           ptex
Version:        2.4.2
Release:        %autorelease
Summary:        Per-Face Texture Mapping for Production Rendering

License:        BSD
Url:            https://github.com/wdas/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  pkgconfig(zlib)

%description
Ptex is a texture mapping system developed by 
Walt Disney Animation Studios for production-quality rendering.

%package devel
Summary: Development files for the Ptex library
Requires:       %{name} = %{version}

%description devel
Development files for Walt Disney Animation Studios Ptex library.

%package doc
Summary: Documentation files for the Ptex library
BuildArch:      noarch

%description doc
Documentation files for Walt Disney Animation Studios Ptex library.

%package libs
Summary:        Libraries for Ptex

%description libs
This package contains the library needed to run programs dynamically
linked with Ptex.

%prep
%autosetup -n %{name}-%{version}


%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# Detect package version
echo %{version} > version
%cmake \
        -DPTEX_BUILD_STATIC_LIBS=OFF 
%cmake_build


%install
%cmake_install

# Create a pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/Ptex.pc << EOF
# pkg-config configuration for Ptex
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: Ptex
Description: Per-Face Texture Mapping for Production Rendering
Version: 2.4.0
Libs: -L${libdir} -llibPtex -pthread -lpthread
Libs.private: -lz
Cflags: -I${includedir} -pthread
EOF


%files
%doc src/doc/README 
%license LICENSE        
%{_bindir}/ptxinfo
%dir %{_datadir}/cmake/Ptex
%{_datadir}/cmake/Ptex/%{name}*.cmake

%files libs
%{_libdir}/libPtex.so.2.4

%files doc
%dir %{_datadir}/doc/Ptex
%doc %{_datadir}/doc/Ptex/*

%files devel
%{_includedir}/Ptex*.h
%{_libdir}/pkgconfig/Ptex.pc
%{_libdir}/libPtex.so

%changelog
%autochangelog
