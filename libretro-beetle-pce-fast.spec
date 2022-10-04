%global commit  cc248db4d2f47d0f255fbc1a3c651df4beb3d835
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20220828

%global corename beetle-pce-fast

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Standalone port of Mednafen PCE Fast to libretro

License:        GPLv2
URL:            https://github.com/libretro/beetle-pce-fast-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_pce_fast.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1


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
