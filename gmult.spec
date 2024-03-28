%global app_id  app.drey.MultiplicationPuzzle

Name:           gmult
Version:        14.0
Release:        %autorelease
Summary:        Multiplication Puzzle
# CC0-1.0 applies only to build system files
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/mterry/gmult
Source:         %{url}/-/archive/%{version}/gmult-%{version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gtk4) >= 4.14
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  vala

Requires:       hicolor-icon-theme

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Multiplication Puzzle is a simple game inspired by the multiplication game 
inside the popular editor emacs. You are presented with a long multiplication 
problem where a 3-digit number is multiplied by a 2-digit number, yielding two 
intermediate 4-digit number and a final 5-digit answer.  However, all the 
digits are replaced by letters.  Your job is to discover which letters are 
which digits.

%prep
%autosetup -p1
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
# Gtk.CssProvider.load_from_data deprecated and replaced in 4.12
sed -i -e 's/VALA_0_58/VALA_0_56/;s/load_from_data/load_from_string/' gmult/main.vala
%endif


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/CC-BY-SA-4.0.md LICENSES/GPL-3.0-or-later.md
%doc MAINTAINERS.md NEWS.md README.md
%{_bindir}/gmult
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.metainfo.xml


%changelog
%autochangelog
