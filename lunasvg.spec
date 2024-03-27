Name:           lunasvg
Version:        2.3.9
Release:        %autorelease
Summary:        Standalone SVG rendering library in C++

License:        MIT AND FTL
URL:            https://github.com/sammycage/lunasvg
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Add soversion
Patch:          %{url}/pull/92.patch

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed

BuildRequires:  stb_image_write-devel

# Vendored copy under 3rdparty/plutovg
# License: FTL
Provides:       bundled(plutovg)

%description
LunaSVG is a standalone SVG rendering library in C++.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%prep
%autosetup -p1

# Replace bundled libraries with the system ones
ln -sf %{_includedir}/stb/stb_image_write.h 3rdparty/stb/

# Do not hardcode libdir
sed -i '/set(LUNASVG_LIBDIR/d' CMakeLists.txt

%build
%cmake \
  -DLUNASVG_LIBDIR="%{_libdir}" \
  -DLUNASVG_BUILD_EXAMPLES=ON \

%cmake_build

%install
%cmake_install

chrpath -d %{_vpath_builddir}/svg2png
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/svg2png

%check
%ctest

%files
%license LICENSE 3rdparty/plutovg/FTL.TXT
%doc README.md
%{_bindir}/svg2png
%{_libdir}/lib%{name}.so.2{,.*}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
