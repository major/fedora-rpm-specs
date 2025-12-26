%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 7e9b257b8a591cb7e00f9e55371edba19db9799c
%global corename beetle-pce-fast

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.10.%autorelease
Summary:        Standalone port of Mednafen PCE Fast to libretro

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_pce_fast.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
Beetle PC Engine Fast is a port/fork of Mednafen's PC Engine Fast "pce_fast"
module to the libretro API. This libretro core contains CD-ROM2 support but
unlike Mednafen's PCE Fast module, lacks SuperGrafx support. SuperGrafx support
is available in the Beetle SuperGrafx core or the Beetle PC Engine "pce" core.


%prep
%forgeautosetup -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -m0644 -Dp %{SOURCE1} \
    %{buildroot}%{_libdir}/libretro/mednafen_pce_fast.libretro


%files
%license COPYING
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
