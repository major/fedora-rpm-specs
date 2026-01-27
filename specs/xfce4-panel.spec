%global xfceversion 4.20

%global namespc Libxfce4panel

%global __provides_exclude_from ^%{_libdir}/xfce4/panel/plugins/.*\\.so$
# vapigen failed with vala 0.47:
# https://bugzilla.xfce.org/show_bug.cgi?id=16426
# It is safe to disable vapigen by now, since no package in Fedora requires the
# vapi
%global _with_vala 0

Name:           xfce4-panel
Version:        4.20.6
Release:        %autorelease
Summary:        Next generation panel for Xfce

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-panel
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

# clock icon taken from system-config-date, license is GPLv2+
Source1:        xfce4-clock.png
Source2:        xfce4-clock.svg

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  garcon-devel >= 0.6.0
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  startup-notification-devel
BuildRequires:  exo-devel >= 0.3.93
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  libxfce4windowing-devel

%if 0%{?fedora}
BuildRequires:  libdbusmenu-gtk3-devel
%endif

%if %{_with_vala}
BuildRequires:  vala
%endif


# obsolete old plugins
Obsoletes:      orage < 4.12.1-17.fc34
Obsoletes:      xfce4-embed-plugin < 1.6.0-13.fc34
Obsoletes:      xfce4-cellmodem-plugin < 0.0.5-29.fc34
Obsoletes:      xfce4-kbdleds-plugins < 0.0.6-20.fc34
Obsoletes:      xfce4-hardware-monitor-plugin < 1.6.0-11

%description
This package includes the panel for the Xfce desktop environment.

%package devel
Summary:        Development headers for xfce4-panel
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libxfce4util-devel >= %{xfceversion}
Requires:       libxfce4ui-devel >= %{xfceversion}

%description devel
This package includes the header files you will need to build
plugins for xfce4-panel.


%prep
%autosetup -p1

# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=office-calendar|Icon=xfce4-clock|g' plugins/clock/clock.desktop.in.in


%build
%configure --enable-gtk-doc --disable-static 

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# The LD_LIBRARY_PATH hack is needed for --enable-gtk-doc
# because lt-libxfce4panel-scan is linked against libxfce4panel
export LD_LIBRARY_PATH="`pwd`/libxfce4panel/.libs"

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-desktop-handler.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-preferences.desktop

# install additional icons
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%{_bindir}/*
%{_libdir}/libxfce4panel-*.so.*
%{_libdir}/xfce4/panel/
%{_libdir}/girepository-1.0/%{namespc}-2.0.typelib
%{_datadir}/gir-1.0/%{namespc}-2.0.gir
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/
%{_datadir}/applications/*.desktop
%if %{_with_vala}
%{_datadir}/vala/vapi/libxfce4panel-2.0.deps
%{_datadir}/vala/vapi/libxfce4panel-2.0.vapi
%endif

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/libxfce4panel-*.so
%doc %{_datadir}/gtk-doc/html/libxfce4panel-*/
%{_includedir}/xfce4/libxfce4panel-*/

%changelog
%autochangelog
