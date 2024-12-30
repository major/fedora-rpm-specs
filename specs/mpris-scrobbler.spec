%global forgeurl    https://github.com/mariusor/mpris-scrobbler
%global commit c1144a57b4536329cfdef2f514aa2cabfe81fdfa

Name:           mpris-scrobbler
Version:        0.5.5
Release:        %autorelease
Summary:        User daemon to submit currently playing song to LastFM, LibreFM, ListenBrainz
License:        MIT

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.rpmlintrc

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  /usr/bin/m4

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif

%if 0%{?fedora}
BuildRequires:  /usr/bin/scdoc
%endif

Requires:       /usr/bin/xdg-open


%description
mpris-scrobbler is a minimalist user daemon that submits the currently playing
song to LastFM, LibreFM, ListenBrainz, and compatible services. To retrieve
song information, it uses the MPRIS DBus interface, so it works with any media
player that exposes this interface.


%prep
%forgesetup
%autosetup -p1 -n %{archivename}

%build
%meson --buildtype=release -Dc_args="-g -fPIE -Wno-address -Wno-stringop-truncation -Wno-unused-parameter -Wno-free-nonheap-object -Wno-format-truncation"
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-signon
%{_userunitdir}/%{name}.service

%if 0%{?fedora}
%{_mandir}/man1/mpris-scrobbler{,-signon}.1*
%{_mandir}/man5/mpris-scrobbler-{config,credentials}.5*
%endif


%changelog
%autochangelog
