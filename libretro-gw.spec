%global commit  0ecff52b11c327af52b22ea94b268c90472b6732
%global date    20230528
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename gw

Name:           libretro-%{corename}
Version:        0
Release:        7.%{date}git%{shortcommit}.%autorelease
Summary:        Libretro core for Game & Watch simulators

License:        zlib
URL:            https://github.com/libretro/gw-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    retroarch

Provides:       bundled(lua) = 5.3.0

%description
gw-libretro is a libretro core that runs Game & Watch simulators.

It runs simulators converted from source code for the games available at
MADrigal. Each simulator is converted with pas2lua, which was written
specifically for this purpose, and uses bstree, which was also specifically
written to obfuscate the generated Lua source code as per MADrigal's request.


%prep
%autosetup -n %{corename}-libretro-%{commit}


%build
%set_build_flags
%make_build


%install
install -m 0755 -Dp %{corename}_libretro.so %{buildroot}%{_libdir}/libretro/%{corename}_libretro.so


%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
