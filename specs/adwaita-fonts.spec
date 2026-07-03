BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  fonts-rpm-macros

Name:    adwaita-fonts
Summary: Adwaita fonts
Version: 50.0
Release: %autorelease
License: OFL-1.1
URL:     https://gitlab.gnome.org/GNOME/adwaita-fonts.git
Source0: https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz
Source1: 59-adwaita-sans-fonts.conf
Source2: 59-adwaita-mono-fonts.conf

%gnome_check_version

%global foundry         adwaita-fonts
%global fontdocs        README.md

%global common_description  %{expand:
Adwaita Fonts contains Adwaita Sans, a variation of Inter,
and Adwaita Mono, Iosevka customized to match Inter.
}

%global fontfamily1     adwaita-sans-fonts
%global fontsummary1    Adwaita Sans font family
%global fonts1          sans/*.ttf
%global fontlicenses1   LICENSE
%global fontconfs1      %{SOURCE1}
%global fontdescription1   %{expand:
%{common_description}
Adwaita Sans is a variation of the Inter font family.
}

%global fontfamily2     adwaita-mono-fonts
%global fontsummary2    Adwaita Mono font family
%global fonts2          mono/*.ttf
%global fontlicenses2   LICENSE
%global fontconfs2      %{SOURCE2}
%global fontdescription2   %{expand:
%{common_description}
Adwaita Mono is a customized version of the Iosevka font, designed to match Inter.
}


%description
%wordwrap -v common_description

%fontpkg -a
%fontmetapkg

%prep
%autosetup -n %{name}-%{gnome_tarball_version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
