%global branch 1.28

Summary:       Text editor for the MATE desktop
Name:          pluma
Version:       %{branch}.0
Release:       %autorelease
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

Patch1:        pluma_0001-Show-the-default-in-the-filechooser-s-Character-Enco.patch
Patch2:        pluma_0002-Do-not-use-the-window-allocation-to-save-the-window-.patch
Patch3:        pluma_0003-Fix-window-size-saving-when-maximized.patch

BuildRequires: desktop-file-utils
BuildRequires: enchant-devel
BuildRequires: libpeas1-devel
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4-devel
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: python3-gobject-base
BuildRequires: python3-devel
BuildRequires: (python3-setuptools if python3-devel >= 3.12)

Requires: %{name}-data = %{version}-%{release}
# needed to get a gsettings schema, #959607
Requires: mate-desktop-libs
# needed to get a gsettings schema, #959607
Requires: caja-schemas
# the run-command plugin uses zenity
Requires: zenity
Requires: libpeas-loader-python3

%description
pluma is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

pluma is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package data
Summary:   Data files for pluma
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description data
This package contains shared data needed for pluma.


%package devel
Summary:   Support for developing plugins for the pluma text editor
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  gtksourceview4-devel

%description devel
Development files for pluma


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;

%build
%configure \
        --disable-static          \
        --enable-gtk-doc-html     \
        --enable-gvfs-metadata    \
        --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

# clean up all the static libs for plugins
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files
%{_bindir}/pluma
%{_libdir}/pluma/
%{_libexecdir}/pluma/
%{_libdir}/girepository-1.0/Pluma-1.0.typelib
%{_datadir}/applications/pluma.desktop
%{_datadir}/metainfo/pluma.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.pythonconsole.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.spell.gschema.xml

%files data -f %{name}.lang
%doc README.md COPYING AUTHORS
%{_datadir}/pluma/
%{_mandir}/man1/pluma.1.*

%files devel
%{_includedir}/pluma/
%{_libdir}/pkgconfig/pluma.pc
%{_datadir}/gtk-doc/html/pluma/
%{_datadir}/gir-1.0/Pluma-1.0.gir


%changelog
%autochangelog
