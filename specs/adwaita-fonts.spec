%global tarball_version %%(echo %{version} | tr '~' '.')

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  fonts-rpm-macros
BuildRequires:  fonts-rpm-templates

Version: 49.0
Release: 2%{?dist}
License: OFL-1.1
URL:     https://gitlab.gnome.org/GNOME/adwaita-fonts.git

%global foundry         adwaita-fonts
%global fontdocs        README.md

%global	common_description	%{expand:
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


Source0:	https://download.gnome.org/sources/adwaita-fonts/49/adwaita-fonts-%{tarball_version}.tar.xz
Source1:    59-adwaita-sans-fonts.conf
Source2:    59-adwaita-mono-fonts.conf

Name:       adwaita-fonts
Summary:    Adwaita fonts
%description
%wordwrap -v common_description

%fontpkg -a
%fontmetapkg

%prep
%autosetup -n %{name}-%{tarball_version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 49.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
