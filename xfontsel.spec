Name:           xfontsel
Version:        1.1.0
Release:        %autorelease
Summary:        Tool to list X11 core protocol fonts

# The entire source is X11, except the following files that are not installed
# or belong to the build system and therefore do not contribute to the license
# of the binary RPMs:
#   - FSFAP: INSTALL
#   - HPND-sell-variant: Makfile.am, Makefile.in, configure.ac
#   - FSFULLR: aclocal.m4
#   - GPL-2.0-or-later: compile, depcomp, missing
#   - GPL-3.0-or-later: config.guess, config,sub
#   - FSFUL, or perhaps (FSFUL AND X11 AND HPND-sell-variant): configure
License:        X11
URL:            https://www.x.org
Source0:        %{url}/pub/individual/app/xfontsel-%{version}.tar.xz
Source1:        %{url}/pub/individual/app/xfontsel-%{version}.tar.xz.sig
# Keyring created on 2021-02-23 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint xfontsel-1.0.6.tar.bz2.sig 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkp://pool.sks-keyservers.net --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > xfontsel.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./xfontsel.gpg
# Since the SKS Keyserver Network is no longer online, you can reproduce by
# substituting:
#   --keyserver=hkps://keys.openpgp.org
Source2:        xfontsel.gpg

BuildRequires:  gnupg2

BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:      xorg-x11-apps < 7.7-31

%description
The xfontsel application provides a simple way to display the X11 core protocol
fonts known to your X server, examine samples of each, and retrieve the X
Logical Font Description (“XLFD”) full name for a font.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
autoreconf --force --install --verbose
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc ChangeLog
%doc README.md
%{_bindir}/xfontsel
%{_mandir}/man1/xfontsel.1*
%{_datadir}/X11/app-defaults/XFontSel


%changelog
%autochangelog
