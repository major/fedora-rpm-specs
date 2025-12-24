Name:           mpdscribble
Version:        0.25
Release:        %autorelease
Summary:        A mpd client which submits information about tracks being played to Last.fm
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://www.musicpd.org/clients/%{name}/
Source0:        https://www.musicpd.org/download/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.musicpd.org/download/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
# Find which key was used for signing the release:
#
# $ LANG=C gpg --verify mpdscribble-0.25.tar.xz.sig mpdscribble-0.25.tar.xz

# gpg: Signature made Mon Dec 11 18:22:41 2023 CET
# gpg:                using RSA key 0392335A78083894A4301C43236E8A58C6DB4512
# gpg: Can't check signature: No public key
#
# Now export the key required as follows:
#
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key 0392335A78083894A4301C43236E8A58C6DB4512
# gpg --no-default-keyring --keyring ./keyring.gpg  --output 0392335A78083894A4301C43236E8A58C6DB4512.gpg --export --armour
Source2:        0392335A78083894A4301C43236E8A58C6DB4512.gpg
Source3:        %{name}.tmpfiles.conf

BuildRequires: cmake
BuildRequires: gcc-g++
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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

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

install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
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
