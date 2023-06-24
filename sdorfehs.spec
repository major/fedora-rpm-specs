Name:           sdorfehs
Version:        1.5
Release:        %autorelease
Summary:        A tiling window manager

License:        GPL-2.0-or-later
URL:            https://github.com/jcs/sdorfehs
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXres-devel
BuildRequires:  libXtst-devel

%description
sdorfehs (pronounced "starfish") is a tiling window manager descended from
ratpoison (which itself is modeled after GNU Screen).

sdorfehs divides the screen into one or more frames, each only displaying one
window at a time but can cycle through all available windows (those which are
not being shown in another frame).

Like Screen, sdorfehs primarily uses prefixed/modal key bindings for most
actions. sdorfehs's command mode is entered with a configurable keystroke which
then allows a number of bindings accessible with just a single keystroke or any
other combination.

%prep
%autosetup
# Do not strip binaries on install so we can get debuginfo
sed -e 's/install -s/install -p/' -i Makefile

%build
%set_build_flags
%make_build

%install
export PREFIX="%{_prefix}"
%make_install MANDIR="%{buildroot}%{_mandir}/man1"

%files
%license COPYING
%doc README.md
%{_bindir}/sdorfehs
%{_mandir}/man1/sdorfehs.1*

%changelog
%autochangelog
