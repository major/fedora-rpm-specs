%global forgeurl https://gitlab.freedesktop.org/wlroots/wlr-protocols
%global date 20250816
%global commit a741f0ac5d655338a5100fc34bc8cec87d237346
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wlr-protocols
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Wayland protocols designed for use in wlroots (and other compositors)
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.bz2

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  /usr/bin/wayland-scanner

%description
Wayland protocols designed for use in wlroots (and other compositors).

%package        devel
Summary:        Wayland protocols designed for use in wlroots (and other compositors)

%description    devel
Wayland protocols designed for use in wlroots (and other compositors).

%prep
%autosetup -p1 -C

%build
%make_build

%install
%make_install

%files devel
%{_datadir}/pkgconfig/wlr-protocols.pc
%{_datadir}/wlr-protocols/

%changelog
%autochangelog
