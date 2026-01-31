%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 8f837ebc077afdd6652efb2827fd8308a07113ca
%global corename beetle-vb

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.10.%autorelease
Summary:        Standalone port of Mednafen VB to libretro

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_vb.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
%{summary}.


%prep
%forgeautosetup -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install         \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_vb.libretro


%files
%license COPYING
%{_libdir}/libretro/


%changelog
%autochangelog
