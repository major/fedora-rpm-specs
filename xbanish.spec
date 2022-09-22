Name:           xbanish
Version:        1.8
Release:        %autorelease
Summary:        Banish the mouse cursor when typing, show it again when the mouse moves

License:        BSD
URL:            https://github.com/jcs/xbanish
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libXt-devel

%description
xbanish hides the mouse cursor when you start typing, and shows it again when
the mouse cursor moves or a mouse button is pressed. This is similar to xterm's
pointerMode setting, but xbanish works globally in the X11 session.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
export PREFIX='%{_prefix}'
export MANDIR='%{_mandir}/man1'
export INSTALL_PROGRAM='install -p'
%make_install

%files
%doc README.md
%{_bindir}/xbanish
%{_mandir}/man1/xbanish.1*

%changelog
%autochangelog
