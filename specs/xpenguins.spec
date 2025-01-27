Name: xpenguins
Version: 2.2
Release: %autorelease
Summary: Cute little penguins that walk along the tops of your windows
Summary(sv): Söta små pingviner som vandrar längs överkanterna på dina fönster

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://xpenguins.seul.org/

Source0: http://xpenguins.seul.org/%name-%version.tar.gz
Source1: %name.appdata.xml
# Mailed upstreams developer with this patch, but it is unclear if
# there ever will be a new release.  This is a rather inactive
# project.
Patch0: xpenguins-2.2-format-security.patch
# If run on a display without the SHAPE extension, xpenguins will
# crash.  This patch causes it to exit more gracefully.  Sent
# upstreams, in case there ever will be a new release.
Patch1: xpenguins-2.2-no-SHAPE.patch
Patch2: xpenguins-configure-c99.patch
Patch3: xpenguins-c99.patch
Patch4: xpenguins-c23.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: libappstream-glib
BuildRequires: libXpm-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel

%global desktopdir %_datadir/applications
%global icondir %_datadir/icons/hicolor/48x48/apps

%description
XPenguins animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, levitate, skateboard, and do
other similarly exciting things.  XPenguins is now themeable so if
you are bored of penguins, try something else.  The themes that come
with this package are "Penguins", "Classic Penguins", "Big Penguins",
"Turtles" and "Bill".

XPenguins works by drawing on the X root window.  This might not have
the desired effect in modern desktop environments like Gnome where the
root window is not visible.

%description -l sv
XPengiuns animerar en vänlig familj av pingviner i ditt rotfönster.
De trillar ner från toppen av skärmen, går längs överkanten av dina
fönster, upp längs sidorna på dina fönster, svävar, åker skateboard,
och gör andra liknande spännande saker.  XPenguins kan nu använda
teman, så om du har tröttnat på pingviner, pröva något annat.  De
teman som följer med detta paket är "Penguins" (pingviner), "Classic
Penguins" (klassiska pingviner), "Big Penguins" (stora pingviner),
"Turtles" (sköldpaddor) och "Bill" (Bill).

XPenguins fungerar genom att rita på X rotfönster.  Detta fungerar
kanske inte som önskat i moderna skrivbordsmiljöer som Gnome där
rotfönstret inte är synligt.


%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags} 
cat << EOF > %name.desktop
[Desktop Entry]
Name=XPenguins
GenericName=Animated penguins
GenericName[sv]=Animerade pingviner
Comment=Cute little penguins that walk along the tops of your windows
Comment[sv]=Söta små pingviner som vandrar längs överkanterna på dina fönster
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Amusement;
# Try to exclude desktops where the the X root window, and thus the penguins,
# are hidden.
#
# Sugar is not defined in
# https://standards.freedesktop.org/menu-spec/latest/apb.html
# I'm guessing at X-Sugar.
#
# Suggestions for improvements/corrections are welcome:
# https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=xpenguins
NotShowIn=Cinnamon;GNOME;KDE;LXDE;MATE;X-Sugar;
EOF
iconv -f ISO-8859-1 -t UTF-8 -o README.utf8 README

%install
make install DESTDIR=%buildroot
desktop-file-install --dir=%buildroot%desktopdir %name.desktop
mkdir -p %buildroot%icondir
convert themes/Big_Penguins/walker.xpm -crop 45x45+0+45 -gravity center -compose src -extent 48x48 %buildroot%icondir/%name.png
install -d %buildroot%_datadir/metainfo
cp -p %SOURCE1 %buildroot%_datadir/metainfo

%check
appstream-util validate-relax --nonet \
	       %buildroot%_datadir/metainfo/%name.appdata.xml

%files
%doc README.utf8 AUTHORS COPYING ChangeLog lay-out-frames.scm resize-frames.scm
%_bindir/%name
%_mandir/man1/*
%_datadir/%name
%desktopdir/%name.desktop
%icondir/%name.png
%_datadir/metainfo/%name.appdata.xml

%changelog
%autochangelog
