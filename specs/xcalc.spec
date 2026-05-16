Name:           xcalc
Version:        1.1.3
Release:        %autorelease
Summary:        Scientific Calculator X11 Client

License:        MIT
URL:            https://xorg.freedesktop.org
Source0:        https://xorg.freedesktop.org/releases/individual/app/xcalc-%{version}.tar.xz
Source1:        xcalc.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros

Requires:       xorg-x11-fonts-100dpi
Requires:       xorg-x11-fonts-75dpi
Requires:       xorg-x11-fonts-misc
Requires:       xorg-x11-xbitmaps


%description
xcalc is a scientific calculator X11 client.

%prep
%autosetup
cp -p %{SOURCE1} .

%build
%configure
%make_build

%install
%make_install

install -d %{buildroot}%{_datadir}/applications
install -p -m 644 xcalc.desktop %{buildroot}%{_datadir}/applications
desktop-file-validate %{buildroot}%{_datadir}/applications/xcalc.desktop

%check
%make_build check

%files
%{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_datadir}/applications/xcalc.desktop
%{_mandir}/man1/xcalc.1.*
%doc ChangeLog README.md

%changelog
%autochangelog
