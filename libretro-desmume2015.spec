%global commit  af397ff3d1f208c27f3922cc8f2b8e08884ba893
%global date    20220406
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename desmume2015

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Port of Desmume to libretro
ExclusiveArch:  i686 x86_64

License:        GPLv2
URL:            https://github.com/libretro/desmume2015
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
Port of Desmume to libretro based on Desmume SVN circa 2015.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build                    \
    -C desmume                 \
    GIT_VERSION=%{shortcommit} \
    %{nil}


%install
%make_install         \
    -C desmume        \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    %{nil}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license desmume/COPYING
%doc desmume/dsm.txt
%{_libdir}/libretro/


%changelog
%autochangelog
