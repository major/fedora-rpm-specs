%global branch 1.28

Summary:       Terminal emulator for MATE
Name:          mate-terminal
Version:       %{branch}.1
Release:       %autorelease
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

#Default to black bg white fg, unlimited scrollback, turn off use theme default
Patch1:        mate-terminal_better_defaults-1.26.0.patch

BuildRequires: dconf-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: vte291-devel

# needed to get a gsettings schema, rhbz #908105
Requires:      mate-desktop-libs
Requires:      gsettings-desktop-schemas

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static                \
           --disable-schemas-compile       

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-terminal.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/mate-terminal
%{_bindir}/mate-terminal.wrapper
%{_datadir}/applications/mate-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%{_datadir}/metainfo/mate-terminal.appdata.xml
%{_mandir}/man1/*


%changelog
%autochangelog
