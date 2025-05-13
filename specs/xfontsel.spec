Name:           xfontsel
Version:        1.1.1
Release:        %autorelease
Summary:        Tool to list X11 core protocol fonts

# The entire source is X11, except the following files that are not installed
# or belong to the build system and therefore do not contribute to the license
# of the binary RPMs…
License:        X11
# FSFAP-no-warranty-disclaimer
#   - INSTALL
# FSFUL AND HPND-sell-variant:
# (HPND-sell-variant is because it is derived from configure.ac)
#   - configure
# FSFULLR:
#   - aclocal.m4
# FSFULLR AND HPND-sell-variant:
#   - Makefile.in
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
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP-no-warranty-disclaimer AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                HPND-sell-variant
                }
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

BuildRequires:  gettext

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The xfontsel application provides a simple way to display the X11 core protocol
fonts known to your X server, examine samples of each, and retrieve the X
Logical Font Description (“XLFD”) full name for a font.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%conf
autoreconf --force --install --verbose
%configure


%build
%make_build


%install
%make_install


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
