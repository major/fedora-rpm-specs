Name:           ncmpc
Version:        0.52
Release:        %autorelease
Summary:        A curses client for the Music Player Daemon (MPD)

License:        GPL-2.0-or-later
URL:            https://www.musicpd.org/
Source0:        https://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz
Source1:        https://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz.sig

# Created with
#   $ gpg2 --receive-keys C6DB4512
#   $ gpg2 --export --export-options export-minimal 236E8A58C6DB4512
Source2:        gpgkey-236E8A58C6DB4512.gpg

BuildRequires:  cmake
BuildRequires:  gnupg2
BuildRequires:  g++
BuildRequires:  gettext
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(lirc)
BuildRequires:  python3dist(sphinx)

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc connects to
a MPD running on a machine on the local network, and controls this with an
interface inspired by cplay.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%meson \
    -Dchat_screen=true \
    -Dlyrics_screen=true \
    -Dlyrics_plugin_dir=%{_datadir}/ncmpc/lyrics
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc
install -p -m644 doc/config.sample \
    $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/config
install -p -m644 doc/keys.sample $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/keys

%find_lang ncmpc


%files -f ncmpc.lang
%doc README.rst NEWS AUTHORS COPYING doc/ncmpc.lirc doc/index.rst
%{_bindir}/ncmpc
%{_mandir}/man1/*
%dir %{_sysconfdir}/ncmpc
%config(noreplace) %{_sysconfdir}/ncmpc/config
%config(noreplace) %{_sysconfdir}/ncmpc/keys
%dir %{_datadir}/ncmpc
%dir %{_datadir}/ncmpc/lyrics
%{_datadir}/ncmpc/lyrics/*

%exclude %{_datadir}/doc/ncmpc/*
%doc %{_datadir}/doc/ncmpc/html


%changelog
%autochangelog
