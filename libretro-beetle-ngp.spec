%global commit  facf8e1f5440c5d289258ee3c483710f3bf916fb
%global date    20220409
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global corename beetle-ngp

Name:           libretro-%{corename}
Version:        0
Release:        0.10.%{date}git%{shortcommit}%{?dist}
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
%autosetup -n %{corename}-libretro-%{commit} -p1


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20220409gitfacf8e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.9.20220409gitfacf8e1
- chore(update): Latest git snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20211001git2c54de7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.7.20211001git2c54de7
- build(update): Latest git snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210324git6599a2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 01 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.5.20210324git6599a2b
- build(update): Latest git snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20200518git3d31f4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20200518git3d31f4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20200518git3d31f4a
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191121gitd839c35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191121gitd839c35
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependencie

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190911git6130e40
- Initial package
