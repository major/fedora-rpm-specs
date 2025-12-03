Name:           lunasvg
Version:        3.5.0
Release:        %autorelease
Summary:        Standalone SVG rendering library in C++

License:        MIT
URL:            https://github.com/sammycage/lunasvg
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  plutovg-devel >= 1.3.0

BuildRequires:  stb_image_write-devel

%description
LunaSVG is a standalone SVG rendering library in C++.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%prep
%autosetup

%build
%cmake \
  -DLUNASVG_LIBDIR="%{_libdir}" \
  -DLUNASVG_BUILD_EXAMPLES=ON \
  -DUSE_SYSTEM_PLUTOVG=ON

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

%files devel
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
