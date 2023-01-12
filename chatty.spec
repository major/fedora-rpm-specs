%global _build_id_links none
%global __requires_exclude ^libjabber\\.so.*$
%global libgd_commit c7c7ff4e05d3fe82854219091cf116cce6b19de0
%global libcmatrix_commit d532b70591b67ac3ad4861390fbb906b323c906f

Name: chatty
Version: 0.7.0~rc5
Release: 0%{?dist}
Summary: A libpurple messaging client

License: GPLv3+
URL: https://source.puri.sm/Librem5/chatty
Source0: https://source.puri.sm/Librem5/%{name}/-/archive/v0.7.0_rc5/%{name}-v0.7.0_rc5.tar.gz
Source1: https://gitlab.gnome.org/GNOME/libgd/-/archive/%{libgd_commit}/libgd-%{libgd_commit}.tar.gz
Source2: https://source.puri.sm/Librem5/libcmatrix/-/archive/%{libcmatrix_commit}/libcmatrix-%{libcmatrix_commit}.tar.gz

# Chatty links against a libpurple private library (libjabber).
# Obviously, Fedora build tooling doesn't support that, so we have to use
# some kind of workaround. This seemed simplest.
# We do not want to provide a private library, which is from another
# project, to be used in other packages.
Patch0:  0001-hacky-hack.patch

# Temporary. Test failure on ppc64le
ExcludeArch:	ppc64le
ExcludeArch:	i686

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	itstool
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libebook-1.2) >= 3.42.0
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(sqlite3) >= 3.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(mm-glib) >= 1.12.0
BuildRequires:	gspell-devel
BuildRequires:  libolm-devel
BuildRequires:	openssl1.1-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
BuildRequires:  libsecret-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth

Requires: hicolor-icon-theme

# Those packages may be dynamically loaded, but they depend on libsoup-2.4
# libsoup-2.4 and libsoup-3.0 can't exist in the same process
# Better to create a conflict, so user doesn't get a hard to debug error
Conflicts: purple-chime <= 1.4.1
Conflicts: purple-sipe <= 1.25.0

%description
Chatty is a libpurple based messaging client for mobile phones,
works best with the phosh mobile DE.

%prep

# Copy private libjabber library in so we can build against it
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 /tmp/libjabber.so

%setup -a1 -a2 -n %{name}-v0.7.0_rc5
%patch0 -p1

rm -rf subprojects/libcmatrix
mv libcmatrix-%{libcmatrix_commit} subprojects/libcmatrix

rmdir subprojects/libgd
mv libgd-%{libgd_commit} subprojects/libgd

%build
%meson
%meson_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/sm.puri.Chatty.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Chatty.desktop

# the upstream meson tests already validate the desktop file
# and the appstream file

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test -t 2
SH

%install
%meson_install

# Adding libjabber to link against
mkdir -p %{buildroot}%{_libdir}
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 %{buildroot}%{_libdir}

# Adding ld.so.conf.d in order to use the libjabber at runtime
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/chatty" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/chatty.conf

%find_lang purism-chatty

# The mesa vulkan bug breaks tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1911130

%files -f purism-chatty.lang
%{_bindir}/chatty
%{_sysconfdir}/xdg/autostart/sm.puri.Chatty-daemon.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.Chatty.gschema.xml
%{_datadir}/applications/sm.puri.Chatty.desktop
%{_datadir}/icons/hicolor/*/apps/sm.puri.Chatty*.svg
%{_metainfodir}/sm.puri.Chatty.metainfo.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/chatty
%{_datadir}/help/C/chatty/index.page
%{_libdir}/libjabber.so.0
%{_sysconfdir}/ld.so.conf.d/chatty.conf
%doc README.md
%license COPYING

%changelog
%autochangelog
