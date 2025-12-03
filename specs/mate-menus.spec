Name:          mate-menus
Version:       1.28.0
Release:       %autorelease
Summary:       Displays menus for MATE Desktop
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# >= f43 , see rhbz (#2411809)
%if 0%{?fedora} && 0%{?fedora} >= 43
Patch1:        mate-menus_glib2-2.86.patch
%endif

BuildRequires: make
BuildRequires: gobject-introspection-devel
BuildRequires: mate-common

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description
Displays menus for MATE Desktop

%package libs
Summary: Shared libraries for mate-menus
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description libs
Shared libraries for mate-menus

%package preferences-category-menu
Summary: Categories for the preferences menu
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}

%description preferences-category-menu
Categories for the preferences menu

%package devel
Summary: Development files for mate-menus
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-menus

%prep
%autosetup -p1

# fedora specific
# fix for usage of multimedia-menus, games-menu and wine-menu packages
sed -i -e '/<!-- End Other -->/ a\  <MergeFile>applications-merged/multimedia-categories.menu</MergeFile>' layout/mate-applications.menu
sed -i -e '/<MergeFile>applications-merged\/multimedia-categories.menu<\/MergeFile>/ a\  <MergeFile>applications-merged/games-categories.menu</MergeFile>' layout/mate-applications.menu
sed -i -e '/<MergeFile>applications-merged\/games-categories.menu<\/MergeFile>/ a\  <MergeFile>applications-merged/wine.menu</MergeFile>' layout/mate-applications.menu

#Patch1
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
    --disable-static \
    --enable-introspection=yes \
    --disable-collection

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/xdg/menus/mate-applications.menu
%config %{_sysconfdir}/xdg/menus/mate-settings.menu
%{_datadir}/mate-menus
%{_datadir}/mate/desktop-directories

%files preferences-category-menu
%config %{_sysconfdir}/xdg/menus/mate-preferences-categories.menu

%files libs
%{_libdir}/girepository-1.0/MateMenu-2.0.typelib
%{_libdir}/libmate-menu.so.2
%{_libdir}/libmate-menu.so.2.4.9

%files devel
%{_datadir}/gir-1.0/MateMenu-2.0.gir
%{_libdir}/libmate-menu.so
%{_includedir}/mate-menus
%{_libdir}/pkgconfig/libmate-menu.pc


%changelog
%autochangelog
