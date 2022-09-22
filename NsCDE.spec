# NsCDE desktop files don't validate, but they are also only used by NsCDE
#
# + desktop-file-validate /builddir/build/BUILDROOT/NsCDE-2.1-1.fc36.x86_64/usr/share/applications/NsCDE-AppMgr.desktop
# /builddir/build/BUILDROOT/NsCDE-2.1-1.fc36.x86_64/usr/share/applications/NsCDE-AppMgr.desktop: error: value "nscde_fvwmclnt 'Exec exec $[info
# store.appmgr]'" for key "Exec" in group "Desktop Entry" contains a reserved character ''' outside of a quote
# /builddir/build/BUILDROOT/NsCDE-2.1-1.fc36.x86_64/usr/share/applications/NsCDE-AppMgr.desktop: error: value "nscde_fvwmclnt 'Exec exec $[info
# store.appmgr]'" for key "Exec" in group "Desktop Entry" contains a reserved character '$' outside of a quote
# /builddir/build/BUILDROOT/NsCDE-2.1-1.fc36.x86_64/usr/share/applications/NsCDE-AppMgr.desktop: error: value "nscde_fvwmclnt 'Exec exec $[info
# store.appmgr]'" for key "Exec" in group "Desktop Entry" contains a reserved character ''' outside of a quote
# /builddir/build/BUILDROOT/NsCDE-2.1-1.fc36.x86_64/usr/share/applications/NsCDE-AppMgr.desktop: error: value "NsCDE;" for key "OnlyShowIn" in
# group "Desktop Entry" contains an unregistered value "NsCDE"; values extending the format should start with "X-"
%bcond_with check

Name:           NsCDE
Version:        2.1
Release:        %autorelease
Summary:        Modern and functional CDE desktop based on FVWM

License:        GPLv3
URL:            https://github.com/NsCDE/NsCDE
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

# For the installer
BuildRequires:  cpp
BuildRequires:  dunst
BuildRequires:  fvwm
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  ksh
BuildRequires:  python3-psutil
BuildRequires:  python3-qt5
BuildRequires:  python3-yaml
BuildRequires:  redhat-menus
BuildRequires:  rofi
BuildRequires:  sed
BuildRequires:  stalonetray
BuildRequires:  xclip
BuildRequires:  xdotool
BuildRequires:  xdpyinfo
BuildRequires:  xprop
BuildRequires:  xrandr
BuildRequires:  xrdb
BuildRequires:  xrefresh
BuildRequires:  xscreensaver
BuildRequires:  xset
BuildRequires:  xsettingsd

# For rebuilding the bundled precompiled binaries
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libxcb-devel

# Test dependencies
%if %{with check}
BuildRequires:  desktop-file-utils
%endif

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}

Requires:       cpp
Requires:       dex-autostart
Requires:       fvwm
Requires:       gettext
Requires:       ImageMagick
Requires:       ksh
Requires:       python3-psutil
Requires:       python3-pyxdg
Requires:       python3-qt5
Requires:       python3-yaml
Requires:       qt5-qtstyleplugins
Requires:       redhat-menus
Requires:       xdotool
Requires:       xdpyinfo
Requires:       xprop
Requires:       xrandr
Requires:       xrdb
Requires:       xrefresh
Requires:       xset
Requires:       xterm

# Highly recommended
Recommends:     dunst
Recommends:     stalonetray
Recommends:     xscreensaver
Recommends:     xsettingsd

# Recommended
Suggests:       gkrellm
Suggests:       rofi
Suggests:       xclip


# These are an integral part of NsCDE and have been specifically modified
Provides:       bundled(colorpicker) = 0
Provides:       bundled(pclock) = 0.13.1
Provides:       bundled(XOverrideFontCursor) = 20190901

%description
NsCDE is a retro but powerful UNIX desktop environment which resembles CDE look
(and partially feel) but with a more powerful and flexible framework
beneath-the-surface, more suited for 21st century UNIX-like and Linux systems
and user requirements than original CDE.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
%description    data
This package contains data files for %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc
This package contains documentation for %{name}.

%prep
%autosetup -p1

%build
%set_build_flags
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
%find_lang NsCDE --all-name

# Doc cleanups
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
# this is the same as COPYING
rm %{buildroot}%{_docdir}/%{name}/LICENSE
for d in examples html NsCDE.{pdf,txt}; do
  mv %{buildroot}%{_docdir}/%{name}/${d} %{buildroot}%{_docdir}/%{name}-doc/
done

%if %{with check}
%check
# Desktop file validation
for f in %{buildroot}%{_datadir}/applications/*.desktop; do
  desktop-file-validate ${f}
done
%endif

%files -f NsCDE.lang
%license COPYING
%doc %{_docdir}/%{name}/*
%{_bindir}/nscde
%{_bindir}/nscde_fvwmclnt
%{_datadir}/applications/NsCDE-*.desktop
%{_libdir}/%{name}
%{_libexecdir}/%{name}
%config(noreplace) %{_sysconfdir}/xdg/menus/nscde-applications.menu

%files data
%license COPYING
%{_datadir}/desktop-directories/nscde-*.directory
%{_datadir}/xsessions/nscde.desktop
%{_datadir}/icons/NsCDE
%{_datadir}/%{name}

%files doc
%license COPYING
%doc %{_docdir}/%{name}-doc/*

%changelog
%autochangelog
