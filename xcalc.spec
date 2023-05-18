Name:           xcalc
Version:        1.1.2
Release:        %autorelease
Summary:        Scientific Calculator X11 Client

License:        MIT
URL:            http://xorg.freedesktop.org
Source0:        http://xorg.freedesktop.org/releases/individual/app/xcalc-%{version}.tar.xz
Source1:        xcalc.desktop

BuildRequires:  gcc make
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXaw-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xorg-x11-util-macros
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel

Requires:       xorg-x11-xbitmaps
Requires:       xorg-x11-fonts-75dpi
Requires:       xorg-x11-fonts-100dpi


%description
xcalc is a scientific calculator X11 client.

%prep
%setup -q
cp -p %{SOURCE1} .

%build
%configure
make V=1 %{?_smp_mflags}

%install
%make_install

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications
install -p -m 644 xcalc.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/xcalc.desktop

%files
%{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_datadir}/applications/xcalc.desktop
%{_mandir}/man1/xcalc.1.*
%doc ChangeLog README.md

%changelog
%autochangelog
