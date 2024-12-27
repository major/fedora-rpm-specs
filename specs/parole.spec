%global fullname org.xfce.Parole
%global minorversion 4.18

Name:           parole
Version:        4.18.2
Release:        %autorelease
Summary:        Media player for the Xfce desktop

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/parole
#VCS: git:git://git.xfce.org/apps/parole
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel >= 3.2.0
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  clutter-devel >= 1.16.4
BuildRequires:  clutter-gtk-devel >= 1.4.4
BuildRequires:  gstreamer1-plugins-base-devel >= 0.10.11
BuildRequires:  dbus-devel >= 0.60
BuildRequires:  dbus-glib-devel >= 0.70
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  xfconf-devel
BuildRequires:  libnotify-devel >= 0.4.1
BuildRequires:  libappstream-glib
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext 
BuildRequires:  gtk-doc

# If you checkout from git rather than using a release tarball, uncomment these
# so that ./autogen.sh runs.
# BuildRequires:  xfce4-dev-tools
# BuildRequires:  libtool

Requires:       gstreamer1-plugins-good
# Obsolete the dead mozilla plugin
Obsoletes:      %{name}-mozplugin <= 2.0.2-7

%description
Parole is a modern simple media player based on the GStreamer framework and 
written to fit well in the Xfce desktop. Parole features playback of local 
media files, DVD/CD and live streams. Parole is extensible via plugins.

The project still in its early developments stage, but already contains the 
following features:
* Audio playback
* Video playback with optional subtitle
* Playback of live sources


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing plugins for 
%{name}.


%prep
%setup -q

%build
# If you checkout from git rather than using a release tarball, uncomment this.
# The tarballs contain ./configure & friends INSTEAD of ./autogen.sh
# ./autogen.sh

%configure --disable-static --enable-gtk-doc --enable-clutter
%{make_build}

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

desktop-file-install                                    \
  --delete-original                                     \
  --remove-mime-type=video/x-totem-stream               \
  --dir=%{buildroot}%{_datadir}/applications            \
  %{buildroot}/%{_datadir}/applications/%{fullname}.desktop

# clean up appdata file
sed -i 's/<\/em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
sed -i 's/<em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS TODO THANKS README.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}-0/
%{_libdir}/%{name}-0/*.so
%{_datadir}/applications/%{fullname}.desktop
%{_datadir}/icons/hicolor/*/apps/*parole*
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/%{name}/


%changelog
%autochangelog
