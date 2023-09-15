%global commit      fb9a41fe9bc230a07c4506cad3cbf21d3fa635b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20220807

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
    DEBUG=1


%install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro
sed -i 's!Balanced!performance!' %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro
sed -i 's!balanced!performance!' %{buildroot}%{_libdir}/libretro/%{corename}_performance.libretro

install -D -p -m 0755 bsnes_mercury_performance_libretro.so -t %{buildroot}%{_libdir}/libretro


%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
