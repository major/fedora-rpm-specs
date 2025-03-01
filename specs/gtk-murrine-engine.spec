Summary: Murrine GTK2 engine
Name: gtk-murrine-engine
Version: 0.98.2
Release: %autorelease
# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL: http://www.cimitan.com/murrine/
Source0: https://download.gnome.org/sources/murrine/0.98/murrine-%{version}.tar.xz
Source10: http://cimi.netsons.org/media/download_gallery/MurrinaFancyCandy.tar.bz2
Source11: http://cimi.netsons.org/media/download_gallery/MurrinaVerdeOlivo.tar.bz2
Source12: http://cimi.netsons.org/media/download_gallery/MurrinaAquaIsh.tar.bz2
Source13: http://cimi.netsons.org/media/download_gallery/MurrinaGilouche.tar.bz2
Source14: http://cimi.netsons.org/media/download_gallery/MurrinaLoveGray.tar.bz2
Source15: http://cimi.netsons.org/media/download_gallery/MurrineThemePack.tar.bz2

#rhbz 130313
Patch0: %{name}_possible-wnck-applet-crash.patch
Patch1: gtk-murrine-engine-c99.patch

BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: make

%description
Murrine Engine is a Gtk2 theme engine, using the Cairo vector graphics
library. It comes by default with a modern glassy look, inspired by
Venetian glass artworks, and is extremely customizable.


%prep
%setup -q -n murrine-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --enable-animation --enable-animationrtl
%make_build

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
(cd $RPM_BUILD_ROOT%{_datadir}/themes;
bzcat %{SOURCE10} | tar -xvf -;
bzcat %{SOURCE11} | tar -xvf -;
bzcat %{SOURCE12} | tar -xvf -;
bzcat %{SOURCE13} | tar -xvf -;
bzcat %{SOURCE14} | tar -xvf -;
bzcat %{SOURCE15} | tar -xvf -;
)
%{__sed} -i s/scrollbar_color/#\\0/ $RPM_BUILD_ROOT%{_datadir}/themes/Murrina*/gtk-2.0/gtkrc

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true
#fix permission
find $RPM_BUILD_ROOT%{_datadir}/themes -type f | xargs chmod 0644 || true

%files
%license COPYING COPYING.2.1
%doc AUTHORS ChangeLog NEWS
%{_libdir}/gtk-2.0/*/engines/*
%{_datadir}/gtk-engines
%{_datadir}/themes/*

%changelog
%autochangelog
