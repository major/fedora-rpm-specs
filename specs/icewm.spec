# https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
%undefine __cmake_in_source_build

# Autotools/CMake
%bcond_with fallback_build_tool

%global forgeurl https://github.com/ice-wm/icewm
%global tag %{version}

%global awe_commit da8173bb6bc5a01ca4b512a5d1b7850035f710e5
%global awe_shortcommit %(c=%{awe_commit}; echo ${c:0:7})

Name:           icewm
Version:        3.9.0
%forgemeta
Release:        %autorelease
Summary:        Window manager designed for speed, usability, and consistency

License:        LGPL-2.0-or-later
URL:            https://ice-wm.org/
Source0:        %{forgesource}
Source1:        https://github.com/tim77/awesome-%{name}/archive/%{awe_commit}/awesome-%{name}.git%{awe_shortcommit}.tar.gz
Source2:        README.Fedora.md

# https://github.com/ice-wm/icewm/commit/5d530bae43e78e42d263ee742dddeee5b68348dc#diff-16f4d1fd81be9644d2565d1cde70ad40b1c73b2876e607219afae2dc755565a4L129
Patch:          cmake-locale-install.patch

%if %{with fallback_build_tool}
BuildRequires:  automake
BuildRequires:  autoconf
%else
BuildRequires:  cmake3 >= 3.5
%endif

BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  perl-Pod-Html
%endif

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

Requires:       %{name}-data = %{version}-%{release}
Requires:       xdg-utils

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-themes = %{version}-%{release}
Recommends:     abattis-cantarell-fonts
# Command line utilities for the Advanced Linux Sound
Recommends:     alsa-utils
Recommends:     desktop-backgrounds-compat
Recommends:     mutt
# Commandline utility to change output properties. Required for
# icewm-menu-xrandr.
Recommends:     xrandr
# https://github.com/bbidulock/icewm/issues/379
Recommends:     xterm

#   * Minimal session for icewm
Suggests:       %{name}-minimal-session = %{version}-%{release}
%endif

Obsoletes:      %{name}-fonts-settings < 2.3.3-3

%global _description %{expand:
IceWM is a window manager for the X Window System. The features of IceWM are
speed, simplicity, and not getting in the user's way.}

%description %{_description}


# Data package
%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data %{_description}

Data files for %{name}.


# Themes package
%package        themes
Summary:        Extra themes for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    themes %{_description}

Extra themes for %{name}.


# Minimal-session package
%package        minimal-session
Summary:        Minimal session for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    minimal-session %{_description}

Minimal, lightweight session for %{name}.


%prep
%forgeautosetup -p1
%setup -q -D -T -a1


%build
%if %{with fallback_build_tool}
# ./autogen.sh
autoreconf -fiv
%configure \
    --with-xterm=%{_bindir}/xterm \
    --sysconfdir=%{_sysconfdir}/%{name} \
    %{nil}
%else
%cmake \
    -DCFGDIR=%{_sysconfdir}/%{name} \
    -DCONFIG_LIBPNG=on \
    -DCONFIG_LIBRSVG=on \
    -DXTERMCMD=%{_bindir}/xterm \
    %{nil}
%endif

%if %{with fallback_build_tool}
%make_build
%else
%cmake_build
%endif


%install
%if %{with fallback_build_tool}
%make_install
%else
%cmake_install
%endif

# Themes
cp -a awesome-%{name}-%{awe_commit}/themes/AntiX-collection/* %{buildroot}%{_datadir}/%{name}/themes/
cp -a awesome-%{name}-%{awe_commit}/themes/IceAdwaita-* %{buildroot}%{_datadir}/%{name}/themes/
install -pm 0644 awesome-%{name}-%{awe_commit}/distro-logos/fedora/%{name}.png \
    %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Small/taskbar/%{name}.png
install -pm 0644 awesome-%{name}-%{awe_commit}/distro-logos/fedora/%{name}-24.png \
    %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Medium/taskbar/%{name}.png
install -pm 0644 awesome-%{name}-%{awe_commit}/distro-logos/fedora/%{name}-24.png \
    %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Dark-Medium-alpha/taskbar/%{name}.png
install -pm 0644 awesome-%{name}-%{awe_commit}/distro-logos/fedora/%{name}-32.png \
    %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Large/taskbar/%{name}.png
rm %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-*/taskbar/%{name}.xpm

echo "Theme=\"IceAdwaita-Medium/default.theme\"" > %{buildroot}%{_datadir}/%{name}/theme

# Install Fedora docs
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.Fedora.md

%find_lang %{name}

# Change to current Fedora default background
sed -i 's!/backgrounds/gnome/adwaita-day.jpg!/backgrounds/default.png!' \
    %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-*/default.theme


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS README.Fedora.md
%{_bindir}/%{name}
%{_bindir}/%{name}-menu-fdo
%{_bindir}/%{name}-menu-xrandr
%{_bindir}/%{name}-session
%{_bindir}/%{name}-set-gnomewm
%{_bindir}/%{name}bg
%{_bindir}/%{name}hint
%{_bindir}/icehelp
%{_bindir}/icesh
%{_bindir}/icesound
%{_datadir}/xsessions/%{name}-session.desktop
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_pkgdocdir}/*.html

%files data
%{_datadir}/%{name}/IceWM.jpg
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/keys
%{_datadir}/%{name}/ledclock/
%{_datadir}/%{name}/mailbox/
%{_datadir}/%{name}/menu
%{_datadir}/%{name}/preferences
%{_datadir}/%{name}/programs
%{_datadir}/%{name}/taskbar/
%{_datadir}/%{name}/theme
%{_datadir}/%{name}/themes/default
%{_datadir}/%{name}/themes/IceAdwaita-*/
%{_datadir}/%{name}/toolbar
%{_datadir}/%{name}/winoptions
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes/

%files themes
%{_datadir}/%{name}/themes/CrystalBlue/
%{_datadir}/%{name}/themes/Helix/
%{_datadir}/%{name}/themes/icedesert/
%{_datadir}/%{name}/themes/Infadel2/
%{_datadir}/%{name}/themes/metal2/
%{_datadir}/%{name}/themes/motif/
%{_datadir}/%{name}/themes/NanoBlue/
%{_datadir}/%{name}/themes/win95/
# AntiX-collection
%{_datadir}/%{name}/themes/Anti*-*/
%{_datadir}/%{name}/themes/blue-crystal-*/
%{_datadir}/%{name}/themes/BlueDay-*/
%{_datadir}/%{name}/themes/Breathe*/
%{_datadir}/%{name}/themes/Clearview*
%{_datadir}/%{name}/themes/eco-green-*/
%{_datadir}/%{name}/themes/FauxGlass-*/
%{_datadir}/%{name}/themes/Groove-*/
%{_datadir}/%{name}/themes/IceClearlooks-*/
%{_datadir}/%{name}/themes/icegil-remix-*/
%{_datadir}/%{name}/themes/IceGilDust-*/
%{_datadir}/%{name}/themes/icenoir-3.3-*/
%{_datadir}/%{name}/themes/Korstro-*/
%{_datadir}/%{name}/themes/KorstroDark-*/
%{_datadir}/%{name}/themes/PrettyPink-*/
%{_datadir}/%{name}/themes/quiescent-*/
%{_datadir}/%{name}/themes/Simplest_black-*/
%{_datadir}/%{name}/themes/SunnyDay-*/
%{_datadir}/%{name}/themes/Truth*/
%{_datadir}/%{name}/themes/UltraBlack-*/

%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes/

%files minimal-session
%{_datadir}/xsessions/%{name}.desktop


%changelog
%autochangelog
