# Review at https://bugzilla.redhat.com/show_bug.cgi?id=554599

%global xfceversion 4.20

%global namespc Libxfce4ui

Name:           libxfce4ui
Version:        4.20.2
Release:        %autorelease
Summary:        Commonly used Xfce widgets

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://xfce.org/
#VCS git:git://git.xfce.org/xfce/libxfce4ui
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

## Downstream patches
# add more keyboard shortcuts to make multimedia keyboards work out of the box
# Terminal changed to xfce4-terminal in the patch
Patch10:        libxfce4ui-%{xfceversion}-keyboard-shortcuts.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gobject-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:  libSM-devel
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.4
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  glade-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  make
BuildRequires:  libgtop2-devel

#
# libxfcegui4 was depreciated in the Xfce 4.8 days.
# Finally obsolete it now in 4.12
#
Obsoletes:      libxfcegui4 < 4.10.0-9

%description
Libxfce4ui is used to share commonly used Xfce widgets among the Xfce
applications.


%package -n     xfce4-about
Summary:        Xfce 4 'About' dialog

%description -n xfce4-about
This package contains the 'About Xfce' dialog with info on the desktop
environment, it's contributors, and it's licensing.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel
Requires:       libxfce4util-devel
Requires:       glade-devel
Requires:       pkgconfig
Obsoletes:      libxfcegui4-devel < 4.10.0-9

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch 10

%build
%configure --disable-static

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/libxfce4ui/.libs"

%make_build

%install
%make_install

# fix permissions for installed libraries
chmod 755 %{buildroot}%{_libdir}/*.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

# Move xfce4-about to the 'Documentation' category
desktop-file-install \
  --delete-original \
  --remove-category=X-Xfce-Toplevel \
  --add-category=Documentation \
  --add-category=System \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/xfce4-about.desktop


%ldconfig_scriptlets


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS THANKS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/%{namespc}-2.0.typelib
%{_datadir}/gir-1.0/%{namespc}-2.0.gir
%{_datadir}/vala/vapi/%{name}-2.deps
%{_datadir}/vala/vapi/%{name}-2.vapi

%files -n xfce4-about
%{_bindir}/xfce4-about
%{_datadir}/applications/xfce4-about.desktop
%{_datadir}/icons/hicolor/*/apps/*xfce*

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/
%{_libdir}/glade/modules/lib*.so
%{_datadir}/glade/catalogs/%{name}*.xml*
%{_datadir}/glade/pixmaps/hicolor/*/actions/*

%changelog
%autochangelog
