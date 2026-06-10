Name:		openslide
Version:	4.0.1
Release:	%autorelease
Summary:	C library for reading virtual slides

License:	LGPL-2.1-only
URL:		https://openslide.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdicom) >= 1.3.0
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)

BuildRequires:	gcc
BuildRequires:	meson


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
%autosetup -p1


%build
# don't rebuild docs, since Doxygen configs are version-specific
%meson -Ddoc=disabled -Dtest=disabled
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc README.md CHANGELOG.md
%license COPYING.LESSER
%{_libdir}/lib%{name}.so.1*


%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files tools
%{_bindir}/%{name}-*
%{_bindir}/slidetool
%{_mandir}/man1/%{name}-*
%{_mandir}/man1/slidetool.*


%changelog
%autochangelog
