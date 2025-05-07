Name:       dino
Version:    0.5.0
Release:    %autorelease

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
Summary:    Modern XMPP ("Jabber") Chat Client using GTK+/Vala
URL:        https://github.com/dino/dino
Source0:    %{url}/releases/download/v%{version}/dino-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/dino-%{version}.tar.gz.asc
# dino.im has a published Web Key Directory[0], which is the URL used here. However, I also verified
# that the key matched what was available via public key servers. I also verified that the key was
# indeed the key that generated the signature for the release tarball for dino-0.1.0, ensuring that
# both the signature and tarball were retrieved from GitHub over TLS. Lastly, a couple users
# in the official Dino MUC chat room, chat@dino.im, verified the full release key ID, and my
# connection to that chat room used CA verified TLS. I believe the WKD verification is strong
# enough, but I feel more confident given my secondary (though admittedly weaker)
# verifications.
#
# [0] https://wiki.gnupg.org/WKD
Source2:    https://dino.im/.well-known/openpgpkey/hu/kf5ictsogs7pr4rbewa9ie1he85r9ghc

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: gnupg2
BuildRequires: gpgme-devel
BuildRequires: gspell-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgee-devel
BuildRequires: libnice-devel
BuildRequires: libnotify-devel
BuildRequires: libomemo-c-devel
BuildRequires: libsignal-protocol-c-devel
BuildRequires: libsoup-devel
BuildRequires: libsrtp-devel
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: protobuf-c-devel
BuildRequires: qrencode-devel
BuildRequires: sqlite-devel
BuildRequires: vala
BuildRequires: pkgconfig(webrtc-audio-processing) >= 0.3

Recommends: webp-pixbuf-loader
Requires:   filesystem
Requires:   gstreamer1-plugins-good
Requires:   hicolor-icon-theme


%description
A modern XMPP ("Jabber") chat client using GTK+/Vala.


%package devel
Summary:    Development files for dino

Requires:   dino%{?_isa} == %{version}-%{release}


%description devel
Development files for dino.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}


%build
# Build in C89 mode due to Vala compiler problem:
# C99 compatibility of internal setters
# <https://discourse.gnome.org/t/c99-compatibility-of-internal-setters/13360>
# valac does not respect internal header/vapi setting
# <https://gitlab.gnome.org/GNOME/vala/-/issues/358>
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%find_lang %{name}-omemo
%find_lang %{name}-openpgp

%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/im.dino.Dino.desktop


%files -f %{name}.lang -f %{name}-omemo.lang -f %{name}-openpgp.lang
%license LICENSE
%doc README.md
%{_bindir}/dino
%{_datadir}/applications/im.dino.Dino.desktop
%{_datadir}/dbus-1/services/im.dino.Dino.service
%{_datadir}/icons/hicolor/scalable/apps/im.dino.Dino.svg
%{_datadir}/icons/hicolor/symbolic/apps/im.dino.Dino-symbolic.svg
%{_datadir}/metainfo/im.dino.Dino.appdata.xml
%{_libdir}/dino
%{_libdir}/libcrypto-vala.so.0*
%{_libdir}/libdino.so.0*
%{_libdir}/libqlite.so.0*
%{_libdir}/libxmpp-vala.so.0*


%files devel
%{_datadir}/vala/vapi/crypto-vala.*
%{_datadir}/vala/vapi/dino.*
%{_datadir}/vala/vapi/libdino.vapi
%{_datadir}/vala/vapi/qlite.*
%{_datadir}/vala/vapi/xmpp-vala.*
%{_includedir}/crypto-vala.h
%{_includedir}/libdino.h
%{_includedir}/dino_i18n.h
%{_includedir}/qlite.h
%{_includedir}/xmpp-vala.h
%{_libdir}/libcrypto-vala.so
%{_libdir}/libdino.so
%{_libdir}/libqlite.so
%{_libdir}/libxmpp-vala.so


%changelog
%autochangelog
