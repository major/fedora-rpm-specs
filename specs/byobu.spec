%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# define icons directories...
%define _iconstheme    hicolor
%define _iconsbasedir  %{_datadir}/icons/%{_iconstheme}
%define _iconsscaldir  %{_iconsbasedir}/scalable/apps

Name:		byobu
Version:	6.15
Release:	%autorelease
Summary:	Light-weight, configurable window manager built upon GNU screen

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/dustinkirkland/byobu
Source0:	https://github.com/dustinkirkland/byobu/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Default windows examples
Source1:	fedoracommon

# prefer dnf when installed
# sent upstream: https://code.launchpad.net/~sanjay-ankur/byobu/byobu/+merge/415959
Patch:		0002-byobu-use-dnf.patch

# for F41+ where we have dnf5
Patch:		0002-byobu-use-dnf5.patch
Patch:		0001-byobu-autostart-with-fish-shell.patch

BuildArch:	noarch
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	make
BuildRequires:	%{_bindir}/msgfmt
BuildRequires:	python3
Requires:	gettext-runtime
Requires:	newt
Requires:	python3-newt
Requires:	screen
Requires:	tmux

%Description
Byobu is a Japanese term for decorative, multi-panel screens that serve 
as folding room dividers. As an open source project, Byobu is an 
elegant enhancement of the otherwise functional, plain, 
practical GNU Screen. Byobu includes an enhanced profile 
and configuration utilities for the GNU screen window manager, 
such as toggle-able system status notifications.

%prep
%autosetup -N
%if 0%{?fedora} >= 41
%autopatch -p0 1
%else
%autopatch -p0 0
%endif

# remove swap file
if [ -e "usr/bin/.byobu-status-print.swp" ]; then rm usr/bin/.byobu-status-print.swp
fi

# fix path for lib directory in scripts
for i in `find . -type f -exec grep -l {BYOBU_PREFIX}/lib/ {} \;`; do
sed -i "s#{BYOBU_PREFIX}/lib/#{BYOBU_PREFIX}/libexec/#g" $i;
done

# fix path for lib directory #2
for i in `find . -type f -exec grep -l BYOBU_PREFIX/lib {} \;`; do
sed -i "s#BYOBU_PREFIX/lib/#BYOBU_PREFIX/libexec/#g" $i;
done

# fix path for correct directory in /usr/share
sed -i "s#DOC = BYOBU_PREFIX + '/share/doc/' + PKG#DOC='%{_pkgdocdir}'#g" usr/lib/byobu/include/config.py.in

# set default fedora windows
cp -p %{SOURCE1} usr/share/byobu/windows/common

# fix path from lib to libexec by modified Makefile.am and in
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/Makefile.am
sed -i "s#/lib/#/libexec/#g" usr/lib/byobu/include/Makefile.am


%build
export BYOBU_PYTHON=%{__python3}
sh ./autogen.sh
%configure
%make_build


%install
%make_install
rm -rf %{buildroot}%{_sysconfdir}/profile.d

# remove apport which is not available in fedora
rm %{buildroot}/%{_libexecdir}/%{name}/apport

sed -i 's#status\[\"apport\"\]=0##g' %{buildroot}%{_bindir}/byobu-config
cp -p COPYING %{buildroot}%{_pkgdocdir}

for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/%{name}.mo
done

#use the old xterm .desktop style for while
cp -a usr/share/%{name}/desktop/%{name}.desktop.old usr/share/%{name}/desktop/%{name}.desktop
desktop-file-install usr/share/%{name}/desktop/%{name}.desktop --dir %{buildroot}%{_datadir}/applications

# remove vigpg
rm %{buildroot}/usr/bin/vigpg
rm %{buildroot}/usr/share/man/man1/vigpg.1

# add icon into /usr/share/icons/hicolor/scalable/apps/ from /usr/share/byobu/pixmaps/byobu.svg
mkdir -p %{buildroot}%{_iconsscaldir}
cp -p usr/share/byobu/pixmaps/byobu.svg %{buildroot}%{_iconsscaldir}


%find_lang %{name}
%files -f %{name}.lang

%dir %{_datadir}/%{name}
%dir %{_libexecdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_pkgdocdir}
%{_iconsscaldir}/%{name}.svg
%{_pkgdocdir}/*
%{_bindir}/%{name}*
%{_bindir}/col1
%{_bindir}/ctail
%{_bindir}/manifest
%{_bindir}/purge-old-kernels
%{_bindir}/wifi-status
%{_datadir}/applications/%{name}.desktop
%{_datadir}/sounds/%{name}/%{name}.ogg
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/us.kirkland.terminals.byobu.service
%{_mandir}/man1/%{name}*.1.gz
%{_mandir}/man1/col1.1.gz
%{_mandir}/man1/ctail.1.gz
%{_mandir}/man1/manifest.1.gz
%{_mandir}/man1/purge-old-kernels.1.gz
%{_mandir}/man1/wifi-status.1.gz
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
%autochangelog

