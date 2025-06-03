# Review: https://bugzilla.redhat.com/show_bug.cgi?id=238349

%global _hardened_build 1
%global minorversion 1.9
%global xfceversion 4.20

Name:           xfce4-places-plugin
Version:        1.9.0
Release:        %autorelease
Summary:        Places menu for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-places-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
A menu with quick access to folders, documents, and removable media. The 
Places plugin brings much of the functionality of GNOME’s Places menu to 
Xfce. It puts a simple button on the panel. Clicking on this button opens up 
a menu with 4 sections:
1) System-defined directories (home folder, trash, desktop, file system)
2) Removable media
3) User-defined bookmarks (reads ~/.gtk-bookmarks)
4) Recent documents submenu (requires GTK v2.10 or greater) 


%prep
%autosetup -p1

%build
%meson
%meson_build


%install
%meson_install


# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md TODO
%license COPYING
%{_bindir}/xfce4-popup-places
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
