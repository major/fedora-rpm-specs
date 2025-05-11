%global branch 1.28

Name:          engrampa
Version:       %{branch}.2
Release:       %autorelease
Summary:       MATE Desktop file archiver
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: mate-common
BuildRequires: desktop-file-utils
BuildRequires: file-devel
BuildRequires: gtk3-devel
BuildRequires: json-glib-devel
BuildRequires: caja-devel
BuildRequires: libSM-devel
BuildRequires: PackageKit-glib-devel

%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure                 \
   --disable-schemas-compile \
   --disable-static        \
   --enable-caja-actions   \
   --enable-magic

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/engrampa.desktop

find %{buildroot} -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_mandir}/man1/*
%{_bindir}/engrampa
%{_libexecdir}/engrampa
%{_libexecdir}/engrampa-server
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so
%{_datadir}/engrampa
%{_datadir}/metainfo/engrampa.appdata.xml
%{_datadir}/applications/engrampa.desktop
%{_datadir}/caja/extensions/libcaja-engrampa.caja-extension
%{_datadir}/dbus-1/services/org.mate.Engrampa.service
%{_datadir}/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml


%changelog
%autochangelog
