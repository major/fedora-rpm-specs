Summary:        A fast, feature rich Window Manager
Name:           WindowMaker
Version:        0.96.0
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            http://www.windowmaker.org 
Source0:        https://github.com/window-maker/wmaker/releases/download/wmaker-%{version}/%{name}-%{version}.tar.gz

Source3:        WindowMaker-WMRootMenu-fedora

# X BR
BuildRequires: make
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrender-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
# graphic BR
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
BuildRequires:  ImageMagick-devel
# other
BuildRequires:  zlib-devel
BuildRequires:  gettext-devel
BuildRequires:  fontconfig-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  chrpath
BuildRequires:  pango-devel
BuildRequires:	git-core

Requires:       WINGs-libs = %{version}-%{release}
Requires:       desktop-backgrounds-compat

%description
Window Maker is an X11 window manager designed to give additional
integration support to the GNUstep Desktop Environment. In every way
possible, it reproduces the elegant look and feel of the NEXTSTEP GUI.
It is fast, feature rich, easy to configure, and easy to use. In
addition, Window Maker works with GNOME and KDE, making it one of the
most useful and universal window managers available.

%package devel
Summary:        Development files for WindowMaker
Requires:       WindowMaker = %{version}-%{release}
Requires:       WINGs-devel = %{version}-%{release}

%description devel
Development files for WindowMaker.

%package -n WINGs-libs
Summary:        Widgets and image libraries needed for WindowMaker

%description -n WINGs-libs
Widgets and image libraries needed for WindowMaker.

%package -n WINGs-devel
Summary:        Development files for the WINGs library
Requires:       WINGs-libs = %{version}-%{release}
Requires:       libX11-devel
Requires:       xorg-x11-proto-devel
Requires:       libXinerama-devel
Requires:       libXrandr-devel
Requires:       libXext-devel
Requires:       libtiff-devel
Requires:       zlib-devel
Requires:       libXpm-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       giflib-devel
Requires:       libXft-devel
Requires:       fontconfig-devel

%description -n WINGs-devel
Development files for the WINGs library.

%package extra
Summary:        Extra themes and Icons for WindowMaker
Requires:       WindowMaker = %{version}-%{release}
BuildArch:      noarch

%description extra
This is the extra data package for Window Maker. For now it only contains some
icons and a few themes.

%prep
%autosetup -S git

# cleanup menu entries
for i in WindowMaker/*menu*; do
echo $i
sed -i.old -e 's:/usr/local/:%{_prefix}/:g' \
  -e 's:/home/mawa:$(HOME):g' \
  -e 's:GNUstep/Applications/WPrefs.app:bin:g' $i
done

for i in util/wmgenmenu.c WindowMaker/Defaults/WindowMaker.in WPrefs.app/Paths.c; do
echo $i
sed -i.old -e  's:/usr/local/:%{_prefix}/:g'  $i
done

# fix utf8 issues
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

for i in doc/cs/geticonset.1 doc/cs/seticons.1 doc/cs/wdwrite.1 doc/cs/wmaker.1 \
 doc/cs/wmsetbg.1 doc doc/cs/wxcopy.1 doc/cs/wxpaste.1 doc/sk/geticonset.1 \
 doc/sk/seticons.1 doc/sk/wdwrite.1 doc/sk/wmaker.1 doc/sk/wmsetbg.1 \
 doc/sk/wxcopy.1 doc/sk/wxpaste.1; do
echo $i
iconv -f iso8859-1 -t utf-8 $i > $i.conv && mv -f $i.conv $i
done

autoreconf -vfi -I m4

%build
CFLAGS="$RPM_OPT_FLAGS -DNEWAPPICON"
LINGUAS=`(cd po ; echo *.po | sed 's/.po//g')`
NLSDIR="%{_datadir}/locale"

export CFLAGS LINGUAS NLSDIR

%configure \
 --disable-static \
 --enable-modelock \
 --enable-randr \
 --enable-xinerama \
 --enable-usermenu \
 --enable-pango \
 --enable-wmreplace \
 --x-includes=%{_includedir} \
 --x-libraries=%{_libdir}

%make_build

%install
%make_install NLSDIR=%{_datadir}/locale

%find_lang '\(WPrefs\|WindowMaker\|WINGs\|wmgenmenu\|WRaster\)'

# make first login fedora specific
install -D -m0644 -p %{SOURCE3} \
%{buildroot}%{_sysconfdir}/WindowMaker/WMRootMenu
sed -i \
  -e 's:WorkspaceBack = (solid:WorkspaceBack = (mpixmap, "/usr/share/backgrounds/default.png":' \
  %{buildroot}%{_sysconfdir}/WindowMaker/WindowMaker

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

chmod 755 %{buildroot}%{_datadir}/WindowMaker/{autostart.sh,exitscript.sh}
chmod 644 util/wmiv.{c,h}

# remove rpath
for f in wmaker wdwrite wdread getstyle setstyle convertfonts seticons \
    geticonset wmsetbg wmagnify wmgenmenu wmmenugen WPrefs \
    wmiv wxcopy wxpaste ; do
  chrpath --delete %{buildroot}%{_bindir}/$f
done

chrpath --delete %{buildroot}%{_libdir}/libWINGs.so.3.2.0
chrpath --delete %{buildroot}%{_libdir}/libwraster.so.6.1.0
chrpath --delete %{buildroot}%{_libdir}/libWMaker.so.1.0.1

%ldconfig_scriptlets

%ldconfig_scriptlets -n WINGs-libs

%files -f '\(WPrefs\|WindowMaker\|WINGs\|wmgenmenu\|WRaster\)'.lang
%doc AUTHORS ChangeLog NEWS FAQ* README* COPYING*
%dir %{_sysconfdir}/WindowMaker
%config(noreplace) %{_sysconfdir}/WindowMaker/*
%{_bindir}/wmaker
%{_bindir}/wdwrite
%{_bindir}/wdread
%{_bindir}/getstyle
%{_bindir}/setstyle
%{_bindir}/convertfonts
%{_bindir}/seticons
%{_bindir}/geticonset
%{_bindir}/wmsetbg
%{_bindir}/wmagnify
%{_bindir}/wmgenmenu
%{_bindir}/wmmenugen
%{_bindir}/WPrefs
%{_bindir}/wkdemenu.pl
%{_bindir}/wm-oldmenu2new
%{_bindir}/wmaker.inst
%{_bindir}/wxcopy
%{_bindir}/wxpaste
%{_bindir}/wmiv
%{_libdir}/libWMaker.so.*
%{_datadir}/xsessions/wmaker.desktop
%{_datadir}/applications/WPrefs.desktop
%dir %{_datadir}/WindowMaker
%{_datadir}/WindowMaker/appearance.menu
%{_datadir}/WindowMaker/appearance.menu.*
%{_datadir}/WindowMaker/autostart.sh
%{_datadir}/WindowMaker/background.menu
%{_datadir}/WindowMaker/background.menu.*
%{_datadir}/WindowMaker/exitscript.sh
%{_datadir}/WindowMaker/menu*
%{_datadir}/WindowMaker/plmenu*
%{_datadir}/WindowMaker/README*
%{_datadir}/WindowMaker/wmmacros
%{_datadir}/WindowMaker/Backgrounds/
%{_datadir}/WindowMaker/IconSets/
%{_datadir}/WindowMaker/Pixmaps/
%{_datadir}/WindowMaker/Styles/
# these are shared with -extra
%dir %{_datadir}/WindowMaker/Icons
%{_datadir}/WindowMaker/Icons/BitchX.*
%{_datadir}/WindowMaker/Icons/clip.*
%{_datadir}/WindowMaker/Icons/defaultAppIcon.*
%{_datadir}/WindowMaker/Icons/defaultterm.*
%{_datadir}/WindowMaker/Icons/draw.*
%{_datadir}/WindowMaker/Icons/Drawer.*
%{_datadir}/WindowMaker/Icons/Ear.png
%{_datadir}/WindowMaker/Icons/Ftp.png
%{_datadir}/WindowMaker/Icons/GNUstep3D.*
%{_datadir}/WindowMaker/Icons/GNUstepGlow.*
%{_datadir}/WindowMaker/Icons/GNUstep.*
%{_datadir}/WindowMaker/Icons/GNUterm.*
%{_datadir}/WindowMaker/Icons/GreenWilber.png
%{_datadir}/WindowMaker/Icons/ICQ.png
%{_datadir}/WindowMaker/Icons/Jabber.png
%{_datadir}/WindowMaker/Icons/linuxterm.*
%{_datadir}/WindowMaker/Icons/Magnify.*
%{_datadir}/WindowMaker/Icons/mixer.*
%{_datadir}/WindowMaker/Icons/Mouth.png
%{_datadir}/WindowMaker/Icons/Mozilla.png
%{_datadir}/WindowMaker/Icons/notepad.*
%{_datadir}/WindowMaker/Icons/pdf.*
%{_datadir}/WindowMaker/Icons/Pencil.png
%{_datadir}/WindowMaker/Icons/Pen.png
%{_datadir}/WindowMaker/Icons/ps.*
%{_datadir}/WindowMaker/Icons/README
%{_datadir}/WindowMaker/Icons/Real.png
%{_datadir}/WindowMaker/Icons/real.*
%{_datadir}/WindowMaker/Icons/sgiterm.*
%{_datadir}/WindowMaker/Icons/Shell.png
%{_datadir}/WindowMaker/Icons/Speaker.png
%{_datadir}/WindowMaker/Icons/staroffice2.*
%{_datadir}/WindowMaker/Icons/TerminalGNUstep.*
%{_datadir}/WindowMaker/Icons/TerminalLinux.*
%{_datadir}/WindowMaker/Icons/Terminal.*
%{_datadir}/WindowMaker/Icons/timer.*
%{_datadir}/WindowMaker/Icons/wilber.*
%{_datadir}/WindowMaker/Icons/Wine.png
%{_datadir}/WindowMaker/Icons/write.*
%{_datadir}/WindowMaker/Icons/XChat.png
%{_datadir}/WindowMaker/Icons/xdvi.*
%{_datadir}/WindowMaker/Icons/xv.*
%dir %{_datadir}/WindowMaker/Themes
%{_datadir}/WindowMaker/Themes/Blau.style
%{_datadir}/WindowMaker/Themes/Default.style
%{_datadir}/WindowMaker/Themes/OpenStep.style
%{_datadir}/WindowMaker/Themes/Pastel.style
%{_datadir}/WindowMaker/Themes/SteelBlueSilk.style
%{_datadir}/WPrefs/
%{_mandir}/man1/*.1*
%lang(cs) %{_mandir}/cs/man1/*.1*
%lang(sk) %{_mandir}/sk/man1/*.1*
%lang(ru) %{_mandir}/ru/man1/*.1*

%files devel
%{_libdir}/libWMaker.so
%{_libdir}/pkgconfig/wmlib.pc
%{_includedir}/WMaker.h

%files -n WINGs-libs
%doc WINGs/BUGS WINGs/ChangeLog WINGs/NEWS WINGs/README WINGs/TODO
%{_libdir}/libWINGs.so.*
%{_libdir}/libwraster.so.*
%{_libdir}/libWUtil.so.*
%{_datadir}/WINGs/

%files -n WINGs-devel
%{_libdir}/libWINGs.so
%{_libdir}/libWUtil.so
%{_libdir}/libwraster.so
%{_libdir}/pkgconfig/WINGs.pc
%{_libdir}/pkgconfig/WUtil.pc
%{_libdir}/pkgconfig/wrlib.pc
%{_includedir}/WINGs/
%{_includedir}/wraster.h

%changelog
%autochangelog
