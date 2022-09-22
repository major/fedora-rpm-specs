%global commit  517bb2d02909271836604c01c8f09a79ad605297
%global date    20220414
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename handy

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Atari Lynx emulator Handy for libretro

License:        zlib
URL:            https://github.com/libretro/libretro-handy
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
K. Wilkins' Atari Lynx emulator Handy for libretro.


%prep
%autosetup -n libretro-%{corename}-%{commit} -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install         \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license lynx/license.txt
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
