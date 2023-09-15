%global commit      8ab051edd4816f33a5631d230d54059eeed52c5f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20230220

%global corename    stella2014

Name:           libretro-%{corename}
Version:        0
Release:        0.7.%{date}git%{shortcommit}.%autorelease
Summary:        Port of Stella to libretro

License:        GPLv2
URL:            https://github.com/libretro/stella2014-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1


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
%license stella/license.txt
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
