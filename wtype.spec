Name:           wtype
Version:        0.4
Release:        %autorelease
Summary:        xdotool type for Wayland
License:        MIT

%global         forgeurl    https://github.com/atx/%{name}
%global         tag         v%{version}
%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/wtype
%{_mandir}/man1/wtype.1*


%changelog
%autochangelog
