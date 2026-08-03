# VCS   https://gitlab.xfce.org/xfce/xfce4-session.git

%global xfceversion 4.20

Name:           xfce4-session
Version:        4.20.4
Release:        %autorelease
Summary:        Xfce session manager

License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# Add a xfce-mimeapps.list to allow setting mime handlers for Xfce apps
Source2:        xfce-mimeapps.list

# Patch startxfce4 to keep it on the same vty for logind
# https://bugzilla.redhat.com/show_bug.cgi?id=1117682
Patch1:         xfce-session-%{xfceversion}-startxfce4.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.72.0
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel >= 3.24.0
BuildRequires:  iceauth
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libwnck3-devel >= 3.10.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  libxfce4windowing-devel >= %{xfceversion}
BuildRequires:  make
BuildRequires:  polkit-devel
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  xrdb
BuildRequires:  xset

Requires:       exo
Requires:       iceauth
Requires:       systemd >= 195
Requires:       xfce-polkit >= 0.2-2
Requires:       xrdb
Requires:       xset
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
Summary:        Wayland session for Xfce
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       labwc

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

# Remove non-standard hye locale to prevent invalid-lc-messages-dir rpmlint error
rm -rf %{buildroot}%{_datadir}/locale/hye

# Make xinitrc executable as it has a shebang and is meant to be run
chmod 755 %{buildroot}%{_sysconfdir}/xdg/xfce4/xinitrc

%find_lang %{name}

# install our xfce-mimeapps.list file to set mime handlers
mkdir -p %{buildroot}%{_datadir}/applications
cp -a %{SOURCE2} %{buildroot}%{_datadir}/applications/xfce-mimeapps.list

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce-session-settings.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce4-session-logout.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%doc doc/FAQ doc/NEWS.pre-4.3 doc/README.Kiosk
%dir %{_sysconfdir}/xdg/xfce4
%config(noreplace) %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%{_sysconfdir}/xdg/xfce4/xinitrc
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%{_bindir}/startxfce4
%{_bindir}/xfce4-session
%{_bindir}/xfce4-session-logout
%{_bindir}/xfce4-session-settings
%{_bindir}/xflock4
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
%{_datadir}/xfce4/labwc/labwc-environment
%{_datadir}/xfce4/labwc/labwc-rc.xml

%changelog
%autochangelog
