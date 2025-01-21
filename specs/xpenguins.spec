Name: xpenguins
Version: 2.2
Release: 38%{?dist}
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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2-37
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Florian Weimer <fweimer@redhat.com> - 2.2-33
- C99 compatibility fixes (#2168300)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Göran Uddeborg <goeran@uddeborg.se> 2.2-23
- The current desktop-file-install does know about "Cinnamon"; add it as an
  exclude in the desktop file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Göran Uddeborg <goeran@uddeborg.se> - 2.2-21
- Add an explicit build requirement on gcc.

* Tue Feb 13 2018 Göran Uddeborg <goeran@uddeborg.se> 2.2-20
- Obsolete scriptlets removed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Göran Uddeborg <goeran@uddeborg.se> 2.2-18
- Appdata added.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun  4 2016 Göran Uddeborg <goeran@uddeborg.se> - 2.2-14
- Disable in environments where XPengiuns is known not to work. Bz #1324881.
- Also clean out some obsolete SPEC file code.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Göran Uddeborg <goeran@uddeborg.se> - 2.2-9
- Give proper error message on displays without the SHAPE extension. Bz #1071429.

* Tue Dec 03 2013 Göran Uddeborg <goeran@uddeborg.se> - 2.2-8
- Fix printf format security issue.  Bz #1037404.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Göran Uddeborg <goeran@uddeborg.se> - 2.2-2
- Create a UTF-8 version of the README file to include instead.
  Suggested by reviewer Manuel Wolfshant <wolfy@nobugconsulting.ro>.

* Thu Jul 22 2010 Göran Uddeborg <goeran@uddeborg.se> - 2.2-1
- Packaging updated using Fedora standards.

* Mon Oct  1 2001 Robin Hogan <R.J.Hogan@reading.ac.uk> - 2.1.5-1
- Removed Lemmings (now in xpenguins_themes), added Bill, Big Penguins
- Added resize-frames.scm to docs

* Wed Aug 22 2001 Robin Hogan <R.J.Hogan@reading.ac.uk> - 2.1.3-1
- Added Lemmings theme

* Sat May  5 2001 Robin Hogan <R.J.Hogan@reading.ac.uk> - 1.9.1-1
- First spec file used with autoconf

* Tue May 23 2000 Robin Hogan <R.J.Hogan@reading.ac.uk> - 1.2-1
- Use BuildRoot.
