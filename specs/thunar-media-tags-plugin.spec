# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=238349

%global minor_version 0.6
%global thunar_version 4.18
%global xfceversion 4.18

Name:           thunar-media-tags-plugin
Version:        0.6.0
Release:        %autorelease
Summary:        Media Tags plugin for the Thunar file manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz
#VCS:           git:git://git.xfce.org/thunar-plugins/thunar-media-tags-plugin

BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  exo >= 0.12.0
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  taglib-devel >= 1.4

Requires:       Thunar >= %{thunar_version}

%description
This plugin adds special features for media files to the Thunar file manager.
It includes a special media file page for the file properties dialog, a tag 
editor for ID3 or OGG/Vorbis tags and a so-called bulk renamer, which allows 
users to rename multiple audio files at once, based on their tags.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_libdir}/thunarx-*/%{name}.so


%changelog
%autochangelog
