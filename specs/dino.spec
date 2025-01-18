Name:       dino
Version:    0.4.4
Release:    4%{?dist}

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
BuildRequires: libsignal-protocol-c-devel
BuildRequires: libsoup-devel
BuildRequires: libsrtp-devel
BuildRequires: make
BuildRequires: ninja-build
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

# Remove the bundled library
rm .gitmodules
rm -r plugins/signal-protocol/libsignal-protocol-c


%build
# Build in C89 mode due to Vala compiler problem:
# C99 compatibility of internal setters
# <https://discourse.gnome.org/t/c99-compatibility-of-internal-setters/13360>
# valac does not respect internal header/vapi setting
# <https://gitlab.gnome.org/GNOME/vala/-/issues/358>
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
# Use the system version of libsignal-protocol-c instead of the bundled one.
export SHARED_SIGNAL_PROTOCOL=true
%configure
%make_build


%install
%make_install
%find_lang %{name}
%find_lang %{name}-omemo
%find_lang %{name}-openpgp


%check
make test
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
%{_datadir}/vala/vapi/qlite.*
%{_datadir}/vala/vapi/xmpp-vala.*
%{_includedir}/crypto-vala.h
%{_includedir}/dino.h
%{_includedir}/dino_i18n.h
%{_includedir}/qlite.h
%{_includedir}/xmpp-vala.h
%{_libdir}/libcrypto-vala.so
%{_libdir}/libdino.so
%{_libdir}/libqlite.so
%{_libdir}/libxmpp-vala.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 0.4.4-3
- Rebuild for ICU 76

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.4-2
- convert license to SPDX

* Sun Jul 21 2024 Jeremy Cline <jeremy@jcline.org> - 0.4.4-1
- Update to v0.4.4

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.4.3-6
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 0.4.3-3
- Set build_type_safety_c to 0 (#2173174)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3 (#2221577).

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.4.2-2
- Rebuilt for ICU 73.2

* Thu Mar 02 2023 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.4.1-1
- Update to dino 0.4.1.

* Fri Feb 24 2023 Florian Weimer <fweimer@redhat.com> - 0.4.0-2
- Build in C89 mode due to Vala limiation (#2173174)

* Sat Feb 18 2023 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.4.0-1
- Update to dino 0.4.0 (#2168027).

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.3.1-2
- Rebuild for ICU 72

* Fri Nov 04 2022 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1 (#2140081).

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.0-4
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 19 2022 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.0-2
- Add a missing dependency on gstreamer1-plugins-good, needed for vp8+9.

* Tue Feb 15 2022 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 (#2053977).
- https://github.com/dino/dino/releases/tag/v0.3.0
- https://dino.im/blog/2022/02/dino-0.3-release/

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2 (#2007073).
- https://github.com/dino/dino/releases/tag/v0.2.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.1-1
- CVE-2021-33896: Update to 0.2.1 (#1968753).

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 0.2.0-4
- Rebuild for ICU 69

* Wed Feb 17 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.0-3
- Add a dependency on webp-pixbuf-loader (#1929149).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0 (#1897438).
- https://github.com/dino/dino/releases/tag/v0.2.0
- https://dino.im/blog/2020/11/dino-0.2-release/

* Mon Nov 16 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1 (#1897438).
- https://github.com/dino/dino/releases/tag/v0.1.1

* Sat Aug 15 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.0-2
- Fix FTBFS.

* Fri Jan 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.0-1
- Update to the first Dino release.
- https://dino.im/blog/2020/01/dino-0.1-release/
- https://github.com/dino/dino/compare/11c18cdf...v0.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.18.20191216.git.11c18cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
