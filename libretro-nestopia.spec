%global commit  a9e197f2583ef4f36e9e77d930a677e63a2c2f62
%global date    20220410
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename nestopia

Name:           libretro-%{corename}
Version:        0
Release:        0.9.%{date}git%{shortcommit}.%autorelease
Summary:        Nestopia emulator with libretro interface

License:        GPLv2
URL:            https://github.com/libretro/nestopia
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
%{summary}.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build -C libretro GIT_VERSION=%{shortcommit}


%install
%make_install         \
    -C libretro       \
    libdir=%{_libdir} \
    prefix=%{_prefix} \
    %{nil}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license COPYING
%{_libdir}/libretro/


%changelog
%autochangelog
