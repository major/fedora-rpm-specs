Name: xpenguins
Version: 3.2.3
Release: %autorelease
Summary: Cute little penguins that walk along the tops of your windows
Summary(sv): Söta små pingviner som vandrar längs överkanterna på dina fönster

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

License: GPL-2.0-or-later
URL: https://ratrabbit.nl/ratrabbit/software/xpenguins/

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %name.appdata.xml

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: pkgconf-pkg-config

%global desktopdir %_datadir/applications
%global icondir %_datadir/pixmaps

%description
XPenguins animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, levitate, skateboard, and do
other similarly exciting things.  XPenguins is now themeable so if
you are bored of penguins, try something else.  The themes that come
with this package are "Penguins", "Classic Penguins", "Big Penguins",
"Turtles" and "Bill".

The penguins are able to walk on X11 windows, but are ignorant of
Wayland windows. Some of the effect is lost by this.

%description -l sv
XPengiuns animerar en vänlig familj av pingviner i ditt rotfönster.
De trillar ner från toppen av skärmen, går längs överkanten av dina
fönster, upp längs sidorna på dina fönster, svävar, åker skateboard,
och gör andra liknande spännande saker.  XPenguins kan nu använda
teman, så om du har tröttnat på pingviner, pröva något annat.  De
teman som följer med detta paket är "Penguins" (pingviner), "Classic
Penguins" (klassiska pingviner), "Big Penguins" (stora pingviner),
"Turtles" (sköldpaddor) och "Bill" (Bill).

Pingvinerna kan gå på X11-fönster, men vet inte om Wayland-fönster.
Detta gör att lite av effekten går förlorad.


%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags} 

%install
make install DESTDIR=%buildroot
desktop-file-install --dir=%buildroot%desktopdir src/%name.desktop
install -D --target-directory=%buildroot%icondir src/%name.xpm
install -D --target-directory=%buildroot%_datadir/metainfo %SOURCE1

%check
appstream-util validate-relax --nonet \
	       %buildroot%_datadir/metainfo/%name.appdata.xml

%files
%doc README AUTHORS ChangeLog lay-out-frames.scm resize-frames.scm
%license COPYING
%_bindir/%name
%_mandir/man1/*
%_datadir/%name
%desktopdir/%name.desktop
%icondir/%name.xpm
%_datadir/metainfo/%name.appdata.xml

%changelog
%autochangelog
