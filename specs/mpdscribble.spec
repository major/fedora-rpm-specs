Name:           mpdscribble
Version:        0.25
Release:        %autorelease
Summary:        A mpd client which submits information about tracks being played to Last.fm
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://www.musicpd.org/clients/%{name}/
Source0:        https://www.musicpd.org/download/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}.tmpfiles.conf

BuildRequires: cmake
BuildRequires: gcc-g++
BuildRequires: git
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libmpdclient-devel >= 2.2
BuildRequires: meson
BuildRequires: systemd-devel

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
mpdscribble is a music player daemon (mpd) client which submits information
about tracks being played to Last.fm (formerly audioscrobbler)

%prep
%autosetup -S git_am

# Create a sysusers.d config file
cat >mpdscribble.sysusers.conf <<EOF
u mpdscribble - 'Mpdscribble' %{_localstatedir}/cache/%{name} -
EOF

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/run/%{name}

# Make room for logs
install -d %{buildroot}%{_localstatedir}/cache/%{name}

# Remove installed docs (this will mess with versione/unversioned docdirs)
rm -rf %{buildroot}%{_defaultdocdir}

install -m0644 -D mpdscribble.sysusers.conf %{buildroot}%{_sysusersdir}/mpdscribble.conf


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc AUTHORS NEWS README.rst
%license COPYING
%attr(0644,%{name},%{name}) %config(noreplace) %{_sysconfdir}/mpdscribble.conf
%{_bindir}/mpdscribble
%{_mandir}/man1/mpdscribble.1.gz
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%attr(0755,%{name},%{name}) %dir %{_localstatedir}/run/%{name}
%attr(0755,%{name},%{name}) %dir %{_localstatedir}/cache/%{name}
%{_sysusersdir}/mpdscribble.conf

%changelog
%autochangelog
