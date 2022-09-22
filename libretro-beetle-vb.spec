%global commit  246555f8ed7e0b9e5748b2ee2ed6743187c61393
%global date    20220409
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename beetle-vb

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}%{?dist}
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
%autosetup -n %{corename}-libretro-%{commit} -p1


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20220409git246555f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.9.20220409git246555f
- chore(update): Latest git snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20211025gitaeb8e07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.7.20211025gitaeb8e07
- chore(update): Latest git snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210405git06f9017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 01 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.5.20210405git06f9017
- build(update): Latest git snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20191115gitee8e580
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191115gitee8e580
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191115gitee8e580
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191115gitee8e580
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190912git9066cda
- Initial package
