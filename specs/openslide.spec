Name:		openslide
Version:	4.0.0
Release:	%autorelease
Summary:	C library for reading virtual slides

License:	LGPL-2.1-only
URL:		https://openslide.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libdicom)

BuildRequires:	gcc
BuildRequires:	meson

# Required for gdk-pixbuf2 to be able to load BMP images, including in tests
%if (0%{?fedora} && 0%{?fedora} < 43) || 0%{?rhel} == 10
BuildRequires:	gdk-pixbuf2-modules-extra
Requires:	gdk-pixbuf2-modules-extra%{?_isa}
%else
%if 0%{?rhel}
BuildRequires:	gdk-pixbuf2-modules
Requires:	gdk-pixbuf2-modules%{?_isa}
%endif
%endif


%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.


%package	devel
Summary:	Development files for %{name}
License:	LGPL-2.1-only AND MIT
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	bundled(js-jquery) = 3.6.0

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package   	tools
Summary:	Command line tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains command line tools for working
with virtual slides.


%prep
%autosetup


%build
# don't rebuild docs, since Doxygen configs are version-specific
%meson -Ddoc=disabled
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc README.md CHANGELOG.md
%license COPYING.LESSER
%{_libdir}/*.so.1*


%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files tools
%{_bindir}/*
%{_mandir}/man1/*


%changelog
%autochangelog
