%global uuid    com.github.spheras.%{name}

Name:           desktopfolder
Version:        1.1.3
Release:        %autorelease
Summary:        Bring your desktop back to life

License:        GPLv3+
URL:            https://github.com/spheras/desktopfolder
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix FTBFS
# Remove deprecated positional arguments for translation merges
# https://github.com/spheras/desktopfolder/pull/335/files
Patch0:         %{url}/pull/335.patch#/Remove-deprecated-positional-arguments-for-translation-merges.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libwnck-3.0)

Requires:       hicolor-icon-theme

%description
Organize your desktop with panels that hold your things.

- Access files, folders and apps from your desktop
- Drop files, folders, links and .desktop launchers inside panels
- Resize, position and color panels
- Display photos and keep notes on your desktop
- Reveal the desktop with ⌘-D

Open it like any other app after installing. Desktop Folder will launch
automatically when you next log in.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%doc README.md AUTHORS.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{_sysconfdir}/xdg/autostart/%{uuid}-autostart.desktop


%changelog
%autochangelog
