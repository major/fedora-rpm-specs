# Review at https://bugzilla.redhat.com/show_bug.cgi?id=478659
# Successor of the xfce4-screenshooter-plugin, which was reviewed at
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=179202

%global minorversion 1.11
%global xfceversion 4.16

Name:           xfce4-screenshooter
Version:        1.11.2
Release:        %autorelease
Summary:        Screenshot utility for the Xfce desktop

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/%{name}
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  exo-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libsoup-devel >= 2.26.0
BuildRequires:  libXext-devel >= 1.0.0
BuildRequires:  libXfixes-devel >= 4.0.0
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  wayland-protocols-devel

%description
The Xfce Screenshooter utility allows you to capture the entire screen, the 
active window or a selected region. You can set the delay that elapses before 
the screenshot is taken and the action that will be done with the screenshot: 
save it to a PNG file, copy it to the clipboard, or open it using another 
application.

%package        plugin
Summary:        Screenshot utility for the Xfce panel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xfce4-panel >= %{xfceversion}

%description    plugin
The Xfce Screenshooter plugin allows you to take screenshots from the Xfce 
panel.


%prep
%autosetup

# KDE and GNOME have their own screenshot utils
echo "NotShowIn=KDE;GNOME;" >> src/xfce4-screenshooter.desktop.in.in

%build
%meson
%meson_build


%install
%meson_install

# remove la file
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS NEWS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce*screenshooter*
%{_datadir}/metainfo/xfce4-screenshooter.appdata.xml


%files plugin
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
%autochangelog
