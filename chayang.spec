Name:           chayang
Version:        0.1.0

%global forgeurl https://git.sr.ht/~emersion/chayang
%global tag v%{version}
%forgemeta

Release:        %{autorelease}
Summary:        Gradually dim the screen on wlroots-based compositors

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  wayland-devel >= 1.14.91
BuildRequires:  wayland-protocols-devel >= 1.14

%description
Gradually dim the screen.
Can be used to implement a grace period before locking the session.

%prep
%forgesetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%{autochangelog}

