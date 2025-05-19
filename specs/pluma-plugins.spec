%global branch 1.28

# provides are in a private subdirectory of %%{_libdir}
%global __provides_exclude_from ^%{_libdir}/pluma/plugins

Summary:       Modules for the pluma text editor
Name:          pluma-plugins
Version:       %{branch}.0
Release:       %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://mate-desktop.org
Source0:       https://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4-devel
BuildRequires: libpeas-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: pluma-devel
BuildRequires: python3-dbus
BuildRequires: python3-devel
BuildRequires: vte291-devel
BuildRequires: yelp-tools

Requires:      %{name}-data = %{version}-%{release}
Requires:      pluma
Requires:      python3-dbus
Requires:      libpeas-loader-python3

%description
Modules for the pluma text editor

%package data
Summary:   Data files for pluma-plugins
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description data
This package contains shared data needed for pluma-plugins.


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --enable-verify-all   \
        --enable-python       \
        --enable-deprecations

# fix unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build V=1

%install
%{make_install}

# clean up all the static libs for plugins
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files
%{_libdir}/pluma/plugins/*
%{_datadir}/metainfo/pluma-bookmarks.metainfo.xml
%{_datadir}/metainfo/pluma-codecomment.metainfo.xml
%{_datadir}/metainfo/pluma-quickhighlight.metainfo.xml
%{_datadir}/metainfo/pluma-synctex.metainfo.xml
%{_datadir}/metainfo/pluma-terminal.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.sourcecodebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.wordcompletion.gschema.xml

%files data -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_datadir}/pluma/plugins/sourcecodebrowser/


%changelog
%autochangelog
