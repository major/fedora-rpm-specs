# Note: compton fork renamed to 'picom' since version 7.5

%global oldname compton-ng
%global tarball_version %%(echo %{version} | tr '~' '-')

Name:           picom
Version:        10.2
Release:        %autorelease
Summary:        Lightweight compositor for X11

License:        MPLv2.0 and MIT
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# FR: Please port pcre dependency to pcre2. Pcre has been deprecated.
# https://fedoraproject.org/wiki/PcreDeprecation
# https://github.com/yshui/picom/issues/895
Patch0:         https://github.com/yshui/picom/pull/937.patch#/c2:-replace-pcre-with-pcre2.patch

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  uthash-devel

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
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
%{_bindir}/%{name}*
%{_bindir}/compton*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_mandir}/man1/*.1*
%{_sysconfdir}/xdg/autostart/%{name}.desktop


%changelog
%autochangelog
