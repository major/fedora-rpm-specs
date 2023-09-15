%global commit      4202ac5bdb2ce1a21f84efc0e26d75bb5aa7e248
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20230817

%global corename    prosystem

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}.%autorelease
Summary:        Port of ProSystem to the libretro API

License:        GPLv2
URL:            https://github.com/libretro/prosystem-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

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
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license License.txt
%doc README.md
%{_libdir}/libretro/


%changelog
%autochangelog
