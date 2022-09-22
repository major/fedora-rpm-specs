%global commit      a5a10f97254d660b5e52875abd1fb0eaac396dae
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pop-icon-theme
Version:        2.1.0^2.%{shortcommit}
Release:        %autorelease
Summary:        Pop Icons
License:        CC-BY-SA
URL:            https://github.com/pop-os/icon-theme
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  meson

Requires:       gnome-icon-theme


%description
Pop_Icons is the icon theme for Pop!_OS.  It uses a semi-flat design with
raised 3D motifs to help give depth to icons.  Pop_Icons take inspiration from
the Adwaita GNOME Icons.


%prep
%autosetup -n icon-theme-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING LICENSE
%{_datadir}/icons/Pop


%changelog
%autochangelog
