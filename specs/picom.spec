# Note: compton fork renamed to 'picom' since version 7.5

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global oldname compton-ng
%global tarball_version %%(echo %{version} | tr '~' '-')

Name:           picom
Version:        13
Release:        %autorelease
Summary:        Lightweight compositor for X11

License:        MPL-2.0 AND MIT
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  rubygem-asciidoctor
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)

Requires:       hicolor-icon-theme

Conflicts:      compton%{?_isa}

Provides:       %{oldname}%{?_isa} = %{version}-%{release}

Obsoletes:      %{oldname} =< 7.5-1

%description
picom is a compositor for X, and a fork of Compton.

This is a development branch, bugs to be expected

You can leave your feedback or thoughts in the discussion tab.


%package        devel
Summary:        Devel files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    devel
Devel files for %{name}.


%prep
%autosetup -p1


%build
%meson               \
    -Dwith_docs=true \
    %{nil}
%meson_build


%install
%meson_install


%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING LICENSES/MPL-2.0 LICENSES/MIT
%doc README.md CONTRIBUTORS %{name}.sample.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-inspect
%{_bindir}/%{name}-trans
%{_bindir}/compton
%{_bindir}/compton-trans
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_mandir}/man1/*.1*
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-api.pc


%changelog
%autochangelog
