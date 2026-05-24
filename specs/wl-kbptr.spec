Name:          wl-kbptr
Version:       0.4.1
Release:       %autorelease
Summary:       Control the mouse pointer with the keyboard on Wayland

# The wl-kbptr is released under the GPL-3.0-only license. Other licenses:
# protocol/wlr-layer-shell-unstable-v1.xml: NTP
# protocol/fractional-scale-v1.xml: NTP
# protocol/wlr-screencopy-unstable-v1.xml: NTP
# protocol/wlr-virtual-pointer-unstable-v1.xml: NTP
License:       GPL-3.0-only AND NTP
URL:           https://github.com/moverest/wl-kbptr
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       wl-kbptr.metainfo.xml
Patch:         https://github.com/moverest/wl-kbptr/pull/92.patch

BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: desktop-file-utils
BuildRequires: jq
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(opencv)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)

Recommends:    jq

%description
%{summary}

%prep
%autosetup 

%conf
%meson -Dopencv=enabled

%build
%meson_build

%install
%meson_install
install -Dp LICENSE{,-NTP} -t %{buildroot}%{_defaultlicensedir}/%{name}
install -Dp {README.md,config.example} -t %{buildroot}%{_docdir}/%{name}
install -Dp %{SOURCE1} -t %{buildroot}%{_metainfodir}
install -p helpers/wl-kbptr-sway-active-win -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -o %{buildroot}%{_mandir}/man1/%{name}.1

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%{buildroot}%{_bindir}/%{name} --help

%files
%license LICENSE LICENSE-NTP
%doc README.md config.example
%{_bindir}/%{name}
%{_bindir}/wl-kbptr-sway-active-win
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
