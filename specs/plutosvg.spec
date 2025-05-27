Name:           plutosvg
Version:        0.0.7
Release:        %autorelease
Summary:        Tiny SVG rendering library in C
License:        MIT
URL:            https://github.com/sammycage/plutosvg

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix pluto header lookup:
Patch0:         %{name}-plutovg-header.patch
# Let meson install samples so runpath is removed:
Patch1:         %{name}-samples.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(freetype2) >= 2.12
BuildRequires:  pkgconfig(plutovg) >= 1.0.0
BuildRequires:  meson >= 0.64.0

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
%meson \
  -D examples=enabled \
  -D freetype=enabled \
  -D tests=enabled
%meson_build

%install
%meson_install

# Rename sample binaries not to conflict with other packages:
for bin in %{buildroot}%{_bindir}/*; do
   mv $bin %{buildroot}%{_bindir}/%{name}_$(basename $bin)
done

%check
%meson_test
# At the moment there are no meson tests defined and the above command is a no-op,
# so run some sample programs as a test that do not require external files:
%{_vpath_builddir}/examples/camera2png
%{_vpath_builddir}/examples/svg2png camera.svg camera.png

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files samples
%{_bindir}/%{name}_camera2png
%{_bindir}/%{name}_emoji2png
%{_bindir}/%{name}_svg2png

%changelog
%autochangelog
