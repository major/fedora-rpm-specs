# Review at https://bugzilla.redhat.com/show_bug.cgi?id=554603

%global xfceversion 4.18

%global namespc Garcon

Name:           garcon
Version:        4.18.2
Release:        %autorelease
Summary:        Implementation of the freedesktop.org menu specification

# garcon's source code is licensed under the LGPLv2+,
# while its documentation is licensed under the GFDL 1.1
License:        LGPLv2+ and GFDL
URL:            http://xfce.org/
#VCS git:git://git.xfce.org/xfce/garcon
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Source1:        Documentation.directory
Patch0:         garcon-%{xfceversion}-fedora-menus.patch

BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  make

Obsoletes:      libxfce4menu < 4.6.3
# because of %%{_datadir}/desktop-directories/xfce-*
Conflicts:      xfdesktop <= 4.6.2

%description
Garcon is an implementation of the freedesktop.org menu specification replacing
the former Xfce menu library libxfce4menu. It is based on GLib/GIO only and 
aims at covering the entire specification except for legacy menus.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       pkgconfig
Obsoletes:      libxfce4menu-devel < 4.6.2

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -P 0 -p1 -b.fedora-menus


%build
%configure --disable-static --enable-gtk-doc

%make_build


%install
%make_install

# fix permissions for libraries
chmod 755 %{buildroot}/%{_libdir}/*.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/desktop-directories

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/menus/xfce-applications.menu
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/%{namespc}*
%{_datadir}/icons/hicolor/*/apps/org.xfce.garcon.png
%{_datadir}/gir-1.0/%{namespc}*
%{_datadir}/desktop-directories/*.directory

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
