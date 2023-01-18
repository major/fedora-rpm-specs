Name:           autotrace
Version:        0.31.9
Release:        %autorelease
Summary:        Utility for converting bitmaps to vector graphics
License:        GPLv2+ and LGPLv2+
URL:            http://autotrace.sourceforge.net/
Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/autotrace/autotrace/pull/105
Patch0:	autotrace-0.31.9-pr105-ImageMagick7.patch
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel > 2:1.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	procps-ng
BuildRequires:	pstoedit-devel


%description
AutoTrace is a program for converting bitmaps to vector graphics.

Supported input formats include BMP, TGA, PNM, PPM, and any format
supported by ImageMagick, whereas output can be produced in
Postscript, SVG, xfig, SWF, and others.


%package devel
Summary:        Header files for autotrace
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       ImageMagick-devel
Requires:       pstoedit-devel


%description devel
This package contains header files and development libraries for autotrace.


%prep
%autosetup -p1


%build
autoreconf -ivf
%configure --enable-magick-readers --disable-static
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}


%check
make check


%ldconfig_scriptlets


%files -f %{name}.lang
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog FAQ NEWS README.md THANKS TODO
%{_bindir}/autotrace
%{_libdir}/*.so.*
%{_mandir}/man[^3]/*


%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/autotrace.pc
%{_includedir}/autotrace/


%changelog
%autochangelog
