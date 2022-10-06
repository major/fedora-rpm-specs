%global commit  db7ace387cdc87d9f2bd4f9f5211c26ce0b07867
%global date    20220915
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename mgba

Name:           libretro-%{corename}
Version:        0.1.1
Release:        0.9.%{date}git%{shortcommit}.%autorelease
Summary:        mGBA Game Boy Advance Emulator

License:        MPLv2.0
URL:            https://github.com/libretro/mgba
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and
more accurate than many existing Game Boy Advance emulators, as well as adding
features that other emulators lack. It also supports Game Boy and Game Boy Color
games.


%prep
%autosetup -n %{corename}-%{commit}


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
%license LICENSE
%doc README.md PORTING.md CONTRIBUTING.md CHANGES
%{_libdir}/libretro/


%changelog
%autochangelog
