#https://bugzilla.redhat.com/show_bug.cgi?id=455071

%global _hardened_build 1
%global minorversion 0.5
%global xfceversion 4.16

Name:           xfce4-mpc-plugin
Version:        0.5.3
Release:        %autorelease
Summary:        MPD client for the Xfce panel

License:        ISC
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-mpc-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  libmpd-devel >= 0.12
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
A simple client plugin for MPD, the Music Player Daemon.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# FIXME: make sure debuginfo is generated properly (#795107)
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
%autochangelog
