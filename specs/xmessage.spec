Name:           xmessage
Version:        1.0.7
Release:        %autorelease
Summary:        Display a message in a window

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
Source0:        %{url}/pub/individual/app/%{name}-%{version}.tar.xz
Source1:        %{url}/pub/individual/app/%{name}-%{version}.tar.xz.sig
# Keyring created on 2023-02-10 with:
#   workdir="$(mktemp --directory)"
#   gpg2 --with-fingerprint xmessage-1.0.5.tar.bz2.sig 2>&1 |
#     awk '$2 == "using" { print "0x" $NF }' |
#     xargs gpg2 --homedir="${workdir}" \
#         --keyserver=hkps://keys.openpgp.org --recv-keys
#   gpg2 --homedir="${workdir}" --export --export-options export-minimal \
#       > xmessage.gpg
#   rm -rf "${workdir}"
# Inspect keys using:
#   gpg2 --list-keys --no-default-keyring --keyring ./xmessage.gpg
# The fingerprint matches the key in the keyring in the xfontsel package, which
# was obtained on 2021-02-23.
Source2:        %{name}.gpg

BuildRequires:  gnupg2

BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)

%description
xmessage displays a message or query in a window. The user can click on an
“okay” button to dismiss it or can select one of several buttons to answer a
question. xmessage can also exit after a specified time.


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


# Upstream does not provide any tests.


%files
%license COPYING

%doc ChangeLog
%doc README

%{_bindir}/xmessage
%{_mandir}/man1/xmessage.1*

%{_datadir}/X11/app-defaults/Xmessage
%{_datadir}/X11/app-defaults/Xmessage-color


%changelog
%autochangelog
