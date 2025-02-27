%global _x11fontdir %{_datadir}/X11/fonts
%global legacydir %{_x11fontdir}/dockapp

Name:           libdockapp
Version:        0.7.3
Release:        %autorelease
Summary:        DockApp Development Standard Library

License:        MIT
URL:            https://www.dockapps.net/libdockapp
Source0:        https://www.dockapps.net/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libXpm-devel libXext-devel libX11-devel

%description
LibDockApp is a library that provides a framework for developing dockapps. 
It provides functions and structures to define and display command-line 
options, create a dockable icon, handle events, etc.

The goal of the library is to provide a simple, yet clean interface and 
standardize the ways in which dockapps are developed. A dockapp developed 
using libDockApp will automatically behave well under most window 
managers, and especially well under Window Maker.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libXpm-devel
Requires:       libX11-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        fonts
Summary:        Fonts provided with %{name}
Requires:       mkfontdir
BuildRequires:  xorg-x11-font-utils mkfontdir
BuildRequires:  fontconfig
BuildRequires: make

%description fonts
Bitmap X fonts provided with libdockapp.


%prep
%autosetup
find . -depth -type d -name CVS -exec rm -rf {} ';'

%build
%configure --disable-static --without-examples --disable-rpath
%make_build


%install
%make_install XFONTDIR=%{builddir}%{_x11fontdir}
rm %{buildroot}%{_libdir}/libdockapp.la

rm -rf __examples_dist
cp -a examples __examples_dist
rm __examples_dist/Makefile*

install -m 0755 -d %{buildroot}%{_sysconfdir}/X11/fontpath.d
install -m 0755 -d %{buildroot}%{legacydir}
ln -sf %{legacydir} %{buildroot}%{_sysconfdir}/X11/fontpath.d

%files
%doc AUTHORS BUGS COPYING NEWS README
%{_libdir}/libdockapp.so.3
%{_libdir}/libdockapp.so.3.*

%files devel
%doc __examples_dist/*
%{_includedir}/libdockapp
%{_libdir}/libdockapp.so
%{_libdir}/pkgconfig/dockapp.pc

%files fonts
%{legacydir}
%{_sysconfdir}/X11/fontpath.d/dockapp
%{_x11fontdir}/misc/fonts.dir
%{_x11fontdir}/misc/luxel-ascii-06x09.pcf.gz
%{_x11fontdir}/misc/seg7-ascii-05x07.pcf.gz

%changelog
%autochangelog
