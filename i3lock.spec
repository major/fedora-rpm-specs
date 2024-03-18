Name:           i3lock
Version:        2.15
Release:        %autorelease
Summary:        Simple X display locker like slock
License:        MIT
URL:            https://i3wm.org/%{name}
Source0:        %{URL}/%{name}-%{version}.tar.xz
Source1:        %{URL}/%{name}-%{version}.tar.xz.asc
# Michael Stapelberg's GPG key:
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg

BuildRequires:  gcc
BuildRequires:  meson >= 0.45
# from meson.build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.5.0
BuildRequires:  pkgconfig(cairo) >= 1.14.4
# these don't provide pkg-config files
BuildRequires:  libev-devel
BuildRequires:  pam-devel

# gpg verification
BuildRequires:  gnupg2
BuildRequires: make

%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

Many little improvements have been made to i3lock over time:

- i3lock forks, so you can combine it with an alias to suspend to RAM (run
  "i3lock && echo mem > /sys/power/state" to get a locked screen after waking up
  your computer from suspend to RAM)

- You can specify either a background color or a PNG image which will be
  displayed while your screen is locked.

- You can specify whether i3lock should bell upon a wrong password.

- i3lock uses PAM and therefore is compatible with LDAP etc. On OpenBSD i3lock
  uses the bsd_auth(3) framework.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc CHANGELOG README*
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/pam.d/%{name}
%{_mandir}/man1/i3lock.1*

%changelog
%autochangelog
