Name:           ptex
Version:        2.5.1
Release:        %autorelease
Summary:        Per-Face Texture Mapping for Production Rendering

License:        BSD-3-Clause
Url:            https://github.com/wdas/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(libdeflate)

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
        -DCMAKE_CXX_STANDARD=17 \
        -DPTEX_BUILD_STATIC_LIBS=OFF 
%cmake_build

%install
%cmake_install

# Relocate .pc file
mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}

# Generate and install man pages.
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

%check
%ifarch s390x
%ctest -- -R "halftest"
%else
%ctest
%endif

%files
%doc src/doc/README 
%license LICENSE        
%{_bindir}/ptxinfo
%{_mandir}/man1/ptxinfo.1.gz

%files libs
%{_libdir}/libPtex.so.2.5

%files doc
%doc %{_datadir}/doc/Ptex

%files devel
%doc src/doc/README
%{_includedir}/Ptex*.h
%{_libdir}/cmake/Ptex
%{_libdir}/libPtex.so
%{_libdir}/pkgconfig/ptex.pc

%changelog
%autochangelog
