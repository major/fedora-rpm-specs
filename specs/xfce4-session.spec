%global xfceversion 4.20

Name:           xfce4-session
Version:        4.20.0
Release:        %autorelease
Summary:        Xfce session manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-session
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# Add a xfce-mimeapps.list to allow setting mime handlers for Xfce apps

Source2:        xfce-mimeapps.list
# Patch startxfce4 to keep it on the same vty for logind
# https://bugzilla.redhat.com/show_bug.cgi?id=1117682
Patch1:         xfce-session-%{xfceversion}-startxfce4.patch

BuildRequires:  make
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:  dbus-glib-devel >= 0.84
BuildRequires:  glib2-devel >= 2.24.0
BuildRequires:  libSM-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  startup-notification-devel
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  iceauth xrdb xset
# Build tools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  libxslt
#BuildRequires:  libxml2
BuildRequires:  systemd-devel >= 195
BuildRequires:  polkit-devel
BuildRequires:  libtool
BuildRequires:  libxfce4windowing-devel

Requires:       iceauth xrdb xset
Requires:       xfce-polkit >= 0.2-2
Requires:       systemd >= 195
# Needed for exo desktop preferred applications
Requires:       exo
# Need this to pull in the right imsettings in groupinstalls
# See https://bugzilla.redhat.com/show_bug.cgi?id=1349743
Suggests:       imsettings-xfce
Suggests:       xfce4-screensaver

Obsoletes:      xfce-utils < 4.8.3-7.fc18

# splash screens no longer exists
Obsoletes:      xfce4-session-engines <= 4.13.1
Obsoletes:      xfce4-session-devel <= 4.13.3

%description
xfce4-session is the session manager for the Xfce desktop environment.

%package wayland-session
Summary:       Wayland session for Xfce
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      labwc
%description wayland-session
Wayland session for Xfce. Currently requires labwc.
Available for testing/advanced users.
See https://wiki.xfce.org/releng/wayland_roadmap#testing

%prep
%autosetup -p1

%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install

# remove xscreensaver autostart file
rm -fr %{buildroot}%{_sysconfdir}/xdg/autostart/xscreensaver.desktop

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}

# install our xfce-mimeapps.list file to set mime handlers
mkdir -p %{buildroot}%{_datadir}/applications
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/xfce-mimeapps.list

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%doc doc/FAQ doc/NEWS.pre-4.3 doc/README.Kiosk
%{_sysconfdir}/xdg/xfce4
%{_bindir}/*
%dir %{_libdir}/xfce4/session/
%{_libdir}/xfce4/session/xfsm-shutdown-helper
%{_datadir}/xdg-desktop-portal/xfce-portals.conf
%{_datadir}/applications/*.desktop
%{_datadir}/applications/xfce-mimeapps.list
%{_datadir}/xsessions/xfce.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.xfce.session.policy
%{_mandir}/man1/*

%files wayland-session
%{_datadir}/wayland-sessions/xfce-wayland.desktop

%changelog
%autochangelog
