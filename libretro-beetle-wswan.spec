%global commit  16d96f64a32cbe1fa89c40b142298dbd007f2f4d
%global date    20220618
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename beetle-wswan

Name:           libretro-%{corename}
Version:        0
Release:        0.8.%{date}git%{shortcommit}.%autorelease
Summary:        Standalone port of Mednafen WonderSwan to libretro, itself a fork of Cygne

License:        GPLv2
URL:            https://github.com/libretro/beetle-wswan-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_wswan.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit}


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install         \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_wswan.libretro


%files
%license COPYING
%{_libdir}/libretro/


%changelog
%autochangelog
