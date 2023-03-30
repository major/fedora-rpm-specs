%global commit  65460e3a9ad529f6901caf669abbda11f437ab55
%global date    20230220
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename beetle-ngp

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Standalone port of Mednafen NGP to the libretro API, itself a fork of Neopop

License:        GPLv2
URL:            https://github.com/libretro/beetle-ngp-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_ngp.libretro

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
%make_install \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_ngp.libretro


%files
%license COPYING
%doc readme.md
%{_libdir}/libretro/


%changelog
%autochangelog
