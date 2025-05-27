Name:           plutovg
Version:        1.1.0
Release:        %autorelease
Summary:        Tiny 2D vector graphics library in C
License:        MIT AND FTL
URL:            https://github.com/sammycage/plutovg

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-samples.patch
Patch1:         %{name}-system-stb.patch

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_truetype-devel

%description
PlutoVG is a standalone 2D vector graphics library in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        samples
Summary:        Sample programs for %{name}

%description    samples
Sample programs that use %{name}.

%prep
%autosetup -p1
# Remove bundled stb:
rm -fv source/%{name}-stb-*.h

%build
%meson \
  -D examples=enabled \
  -D tests=enabled
%meson_build

%install
%meson_install

%check
%meson_test
# At the moment there are no meson tests defined and the above command is a no-op,
# so run the sample program as a test:
%{_vpath_builddir}/examples/smiley

%files
%license LICENSE source/FTL.TXT
%doc README.md
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files samples
%{_bindir}/smiley

%changelog
%autochangelog
