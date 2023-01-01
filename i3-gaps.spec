Name:           i3-gaps
Version:        4.21.1
Release:        %autorelease
Summary:        i3 with more features
License:        BSD
URL:            https://github.com/Airblader/i3
Source0:        %{URL}/releases/download/%{version}/i3-%{version}.tar.xz
Source1:        i3-logo.svg

BuildRequires:  gcc
# need at least 0.53 to build the documentation
BuildRequires:  meson >= 0.53
# from meson.build
BuildRequires:  pkg-config >= 0.25
# no pkg-config for libev
BuildRequires:  libev-devel >= 4.0
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb) >= 1.1.93
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.0
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.4.0
BuildRequires:  pkgconfig(yajl) >= 2.0.1
BuildRequires:  pkgconfig(libpcre2-8) >= 10
BuildRequires:  pkgconfig(cairo) >= 1.14.4
BuildRequires:  pkgconfig(pangocairo) >= 1.30.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
# man pages
BuildRequires:  asciidoc >= 8.3.0
BuildRequires:  xmlto >= 0.0.23

# TODO: Testsuites
BuildRequires:  desktop-file-utils
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::I3)
BuildRequires:  perl(ExtUtils::MakeMaker)
#BuildRequires:  perl(X11::XCB)
#BuildRequires:  perl(Inline)
#BuildRequires:  perl(Inline::C)
#BuildRequires:  perl(ExtUtils::PkgConfig)
#BuildRequires:  perl(Test::More)
#BuildRequires:  perl(IPC::Run)
#BuildRequires:  perl(strict)
#BuildRequires:  perl(warnings)
#BuildRequires:  perl(Pod::Usage)
#BuildRequires:  perl(Cwd)
#BuildRequires:  perl(File::Temp)
#BuildRequires:  perl(Getopt::Long)
#BuildRequires:  perl(POSIX)
#BuildRequires:  perl(TAP::Harness)
#BuildRequires:  perl(TAP::Parser)
#BuildRequires:  perl(TAP::Parser::Aggregator)
#BuildRequires:  perl(Time::HiRes)
#BuildRequires:  perl(IO::Handle)
#BuildRequires:  perl(AnyEvent::Util)
#BuildRequires:  perl(AnyEvent::Handle)
#BuildRequires:  perl(AnyEvent::I3)
#BuildRequires:  perl(X11::XCB::Connection)
#BuildRequires:  perl(Carp)

BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Simple)
%ifnarch s390 s390x
BuildRequires:  xorg-x11-drv-dummy
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       xorg-x11-fonts-misc
# packages autostarted by the config
Recommends:     dex-autostart
Recommends:     xss-lock
Recommends:     network-manager-applet
Recommends:     pulseaudio-utils
Recommends:     dmenu

# for i3-save-tree
Requires:       perl(AnyEvent::I3) >= 0.12
# require the config files from i3:
Requires:       (i3-config or i3-config-fedora)

Conflicts:      i3

Recommends:     i3status
Recommends:     i3lock
Recommends:     i3-config

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
Asciidoc generated documentation for %{name}.

%prep
%autosetup -p1 -n i3-%{version}

# Drop /usr/bin/env lines in those which will be installed to %%_bindir.
find . -maxdepth 1 -type f -name "i3*" -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} + -print


%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 man/*.1 \
        %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dpm0644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps/

# drop development files (these are provided by i3 itself)
rm -rf %{buildroot}%{_includedir}

rm -rf %{buildroot}%{_sysconfdir}/i3/config{,.keycodes}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/i3.desktop

%ifnarch s390 s390x
# TODO: with xorg dummy to test the package.
# TODO: get remaining dependencies in
# %%meson_test
%endif

%files
%doc RELEASE-NOTES-%{version}
%license LICENSE
%{_bindir}/i3*
%{_datadir}/xsessions/i3.desktop
%{_datadir}/xsessions/i3-with-shmlog.desktop
%{_mandir}/man*/i3*
%{_datadir}/pixmaps/i3-logo.svg
%{_datadir}/applications/i3.desktop
%exclude %{_docdir}/i3/

%files doc
%license LICENSE
%doc docs/*.{html,png}

%changelog
%autochangelog
