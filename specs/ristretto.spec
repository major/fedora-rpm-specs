# Review at https://bugzilla.redhat.com/show_bug.cgi?id=351531

%global majorversion 0.13
%global xfceversion 4.18


Name:           ristretto
Version:        0.13.4
Release:        %autorelease
Summary:        Image-viewer for the Xfce desktop environment
Summary(de):    Bildbetrachter für die Xfce Desktop-Umgebung

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/ristretto/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.xz
#VCS: git:git://git.xfce.org/apps/ristretto

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  dbus-glib-devel >= 0.34
BuildRequires:  gtk2-devel >= 2.20.0
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  libexif-devel >= 0.6.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils, gettext, intltool
BuildRequires:  libappstream-glib
Requires:       tumbler


%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop 
environment.

%description -l de
Ristretto ist ein schneller und leichtgewichtiger Bildbetrachter für die Xfce
Desktop-Umgebung.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --add-mime-type=image/x-bmp \
        --add-mime-type=image/x-png \
        --add-mime-type=image/x-pcx \
        --add-mime-type=image/x-tga \
        --add-mime-type=image/xpm \
        --delete-original \
        %{buildroot}%{_datadir}/applications/org.xfce.%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.appdata.xml

%changelog
%autochangelog
