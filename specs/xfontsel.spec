Name:           xfontsel
Version:        1.1.2
Release:        %autorelease
Summary:        Tool to list X11 core protocol fonts

# The upstream COPYING file (and meson.build) show that the license is (X11 AND
# SMLNJ AND MIT). The exact breakdown of which licenses apply to which sources
# is only clear for those sources that contain copyright notices:
#
# X11:
#   - app-defaults/XFontSel (produces %%{_datadir}/X11/app-defaults/XFontSel)
#   - man/xfontsel.man (produces %%{_mandir}/man1/xfontsel.1*)
# X11 AND SMLNJ:
#   - ULabel.c, ULabel.h, ULabelP.h
# X11 AND MIT:
#   - xfontsel.c
# Additionally, a number of files belong to the build system and therefore do
# not contribute to the license of the binary RPM. These are documented below.
License:        X11 AND SMLNJ AND MIT
# FSFAP:
#   - INSTALL
# FSFUL AND HPND-sell-variant:
# (HPND-sell-variant is because it is derived from configure.ac)
#   - configure
# FSFULLR AND FSFULLRWD AND GPL-2.0-or-later WITH Autoconf-exception-generic
# AND MIT AND GPL-3.0-or-later WITH Autoconf-exception-generic AND X11:
#   - aclocal.m4
# FSFULLRWD AND HPND-sell-variant:
#   - Makefile.in
# FSFULLRWD:
#   - man/Makefile.in
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - compile
#   - depcomp
#   - missing
# GPL-3.0-or-later WITH Autoconf-exception-generic:
#   - config.guess
#   - config.sub
# HPND-sell-variant:
#   - Makefile.am
#   - configure.ac
# MIT:
#   - meson.build
# X11 AND LicenseRef-LicenseRef-Fedora-Public-Domain:
#   - install-sh
SourceLicense:  %{shrink:
    %{license} AND
    FSFAP AND
    FSFUL AND
    FSFULLR AND
    FSFULLRWD AND
    GPL-2.0-or-later WITH Autoconf-exception-generic AND
    GPL-3.0-or-later WITH Autoconf-exception-generic AND
    HPND-sell-variant
    }
URL:            https://www.x.org
Source0:        %{url}/pub/individual/app/xfontsel-%{version}.tar.xz
Source1:        %{url}/pub/individual/app/xfontsel-%{version}.tar.xz.sig
# Keyring re-created on 2026-07-01 for the 1.1.2 release with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint xfontsel-1.1.2.tar.xz.sig 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkps://keys.openpgp.org --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > xfontsel.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --show-keys xfontsel.gpg
# The old signing keys had expired 2023-04-21 and included at least one weak
# algorithm (dsa1024), so having to recreate the keychain is expected. The new
# key expires 2026-10-24, and upstream releases every few years, so this kind
# of trust-on-first-use verification isn’t very useful.
Source2:        xfontsel.gpg

BuildRequires:  gpgverify
BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  gettext
# meson.build: dependency(…)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)

%description
The xfontsel application provides a simple way to display the X11 core protocol
fonts known to your X server, examine samples of each, and retrieve the X
Logical Font Description (“XLFD”) full name for a font.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%conf
%meson


%build
%meson_build


%install
%meson_install


# Upstream provides no tests.


%files
%license COPYING

%doc ChangeLog
%doc README.md

%{_bindir}/xfontsel
%{_mandir}/man1/xfontsel.1*
%{_datadir}/X11/app-defaults/XFontSel


%changelog
%autochangelog
