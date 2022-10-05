%global commit  162918f06d9a705330b2ba128e0d3b65fd1a1bcc
%global date    20220828
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename beetle-vb

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Standalone port of Mednafen VB to libretro

License:        GPLv2
URL:            https://github.com/libretro/beetle-vb-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_vb.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit}


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
