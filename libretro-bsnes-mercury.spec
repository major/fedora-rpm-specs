%global commit      4a382621da58ae6da850f1bb003ace8b5f67968c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190817

%global corename    bsnes-mercury

Name:           libretro-%{corename}
Version:        0
Release:        0.12.%{date}git%{shortcommit}.%autorelease
Summary:        Fork of bsnes with various performance improvements

License:        GPLv3+
URL:            https://github.com/libretro/bsnes-mercury
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/bsnes_mercury_balanced.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
bsnes-mercury is a fork of higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.


%prep
%autosetup -n %{corename}-%{commit}


%build
%set_build_flags
%make_build \
    core_installdir=%{_libdir}/libretro \
    profile=balanced


%install
%make_install \
    core_installdir=%{_libdir}/libretro \
    profile=balanced
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}_balanced.libretro


%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
