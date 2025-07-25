Name:           plutosvg
Version:        0.0.7
Release:        %autorelease
Summary:        Tiny SVG rendering library in C
License:        MIT
URL:            https://github.com/sammycage/plutosvg

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix pluto header lookup:
Patch0:         %{name}-plutovg-header.patch
Patch1:         %{name}-soversion-cmake.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(freetype2) >= 2.12
BuildRequires:  pkgconfig(plutovg) >= 1.0.0
BuildRequires:  cmake

%description
PlutoSVG is a compact and efficient SVG rendering library written in C. It is
specifically designed for parsing and rendering SVG documents embedded in
OpenType fonts, providing an optimal balance between speed and minimal memory
usage. It is also suitable for rendering scalable icons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       plutovg-devel%{?_isa}       

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        samples
Summary:        Sample programs for %{name}

%description    samples
Sample programs that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DPLUTOSVG_BUILD_EXAMPLES=ON \
    -DPLUTOSVG_ENABLE_FREETYPE=ON
%cmake_build

%install
%cmake_install
# Rename sample binaries so they don't conflict with other packages:
install -p -m 0755 -D %{_vpath_builddir}/examples/camera2png %{buildroot}%{_bindir}/%{name}_camera2png
install -p -m 0755 -D %{_vpath_builddir}/examples/emoji2png %{buildroot}%{_bindir}/%{name}_emoji2png
install -p -m 0755 -D %{_vpath_builddir}/examples/svg2png %{buildroot}%{_bindir}/%{name}_svg2png

%check
%ctest
# At the moment there are no meson tests defined and the above command is a no-op,
# so run some sample programs as a test that do not require external files:
export LD_LIBRARY_PATH=%{_vpath_builddir}
%{_vpath_builddir}/examples/camera2png
%{_vpath_builddir}/examples/svg2png camera.svg camera.png

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files samples
%{_bindir}/%{name}_camera2png
%{_bindir}/%{name}_emoji2png
%{_bindir}/%{name}_svg2png

%changelog
%autochangelog
