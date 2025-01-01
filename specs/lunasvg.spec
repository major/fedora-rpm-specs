Name:           lunasvg
Version:        3.1.0
Release:        %autorelease
Summary:        Standalone SVG rendering library in C++

License:        MIT
URL:            https://github.com/sammycage/lunasvg
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        plutovg-0.0.10.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  stb_image_write-devel

# License: MIT
Provides:       bundled(plutovg) = 0.0.10

# use local plutovg, not git clone
Patch:          plutovg.patch

%description
LunaSVG is a standalone SVG rendering library in C++.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%prep
%setup -q -T -D -b0
%setup -q -T -D -b1
%autopatch -p1

%build
# move plutovg into place
mv ../plutovg-0.0.10 plutovg

%cmake \
  -DLUNASVG_LIBDIR="%{_libdir}" \
  -DLUNASVG_BUILD_EXAMPLES=ON \

%cmake_build

%install
%cmake_install

chrpath -d %{_vpath_builddir}/examples/svg2png
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/examples/svg2png

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/svg2png
%{_libdir}/lib%{name}.so.3{,.*}
%{_libdir}/libplutovg.so.0{,.*}

%files devel
%{_includedir}/%{name}/%{name}.h
%{_includedir}/plutovg/plutovg.h
%{_libdir}/lib%{name}.so
%{_libdir}/libplutovg.so
%{_libdir}/cmake/%{name}
%{_libdir}/cmake/plutovg

%changelog
%autochangelog
