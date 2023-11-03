Name:           i3
Version:        4.23
Release:        %autorelease
Summary:        Improved tiling window manager
License:        BSD-3-Clause
URL:            https://i3wm.org
Source0:        %{URL}/downloads/%{name}-%{version}.tar.xz
Source1:        %{URL}/downloads/%{name}-%{version}.tar.xz.asc
# Michael Stapelberg's GPG key:
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
Source3:        %{name}-logo.svg
Source4:        fedora-i3-config
Source5:        fedora-i3-keycodes
Patch0:         0001-Correct-dex-binary-name-dex-dex-autostart.patch

# i3-gaps was merged into i3 with 4.22
Provides:       i3-gaps = %{version}-%{release}
Obsoletes:      i3-gaps < 4.22-1

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

# gpg verification
BuildRequires:  gnupg2

Requires:       xorg-x11-fonts-misc
# packages autostarted by the config
Recommends:     dex-autostart
Recommends:     xss-lock
Recommends:     network-manager-applet
Recommends:     pulseaudio-utils
Recommends:     dmenu

# for i3-save-tree
Requires:       perl(AnyEvent::I3) >= 0.12
# the config:
Requires:       (i3-config or i3-config-fedora)

Recommends:     i3status
Recommends:     i3lock
Recommends:     i3-config

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%package        config
Summary:        Upstream configuration for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Recommends:     rxvt-unicode
Conflicts:      %{name}-config-fedora

%description    config
This is the upstream/vanilla configuration file of i3.

%package        config-fedora
RemovePathPostfixes: .fedora
Summary:        Configuration of %{name} for the Fedora i3 Spin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Recommends:     xfce4-terminal
# the Fedora branded config file uses xdg-user-dirs-update indirectly via `dex-autostart --autostart`
Recommends:     xdg-user-dirs
Conflicts:      %{name}-config

%description    config-fedora
This is the configuration file of i3 used for the Fedora i3 Spin.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
Asciidoc generated documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for %{name}.

%package        devel-doc
Summary:        Documentation for the development files of %{name}
BuildRequires:  doxygen
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    devel-doc
Doxygen generated documentations for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Drop /usr/bin/env lines in those which will be installed to %%_bindir.
find . -maxdepth 1 -type f -name "i3*" -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} + -print


%build
%meson
%meson_build

doxygen pseudo-doc.doxygen
mv pseudo-doc/html pseudo-doc/doxygen

%install
%meson_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 man/*.1 \
        %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dpm0644 %{SOURCE3} \
        %{buildroot}%{_datadir}/pixmaps/

install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/config.fedora
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/config.keycodes.fedora

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
%{_bindir}/%{name}*
%dir %{_sysconfdir}/%{name}/
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/xsessions/%{name}-with-shmlog.desktop
%{_mandir}/man*/%{name}*
%{_datadir}/pixmaps/%{name}-logo.svg
%{_datadir}/applications/%{name}.desktop
%exclude %{_docdir}/%{name}/

%files config
%config(noreplace) %{_sysconfdir}/%{name}/config
%config %{_sysconfdir}/%{name}/config.keycodes

%files config-fedora
%config(noreplace) %{_sysconfdir}/%{name}/config.fedora
%config %{_sysconfdir}/%{name}/config.keycodes.fedora

%files doc
%license LICENSE
%doc docs/*.{html,png}

%files devel
%license LICENSE
%{_includedir}/%{name}/

%files devel-doc
%license LICENSE
%doc pseudo-doc/doxygen/

%changelog
%autochangelog
