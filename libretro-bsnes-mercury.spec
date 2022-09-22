%global commit      4a382621da58ae6da850f1bb003ace8b5f67968c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190817

%global corename    bsnes-mercury

Name:           libretro-%{corename}
Version:        0
Release:        0.12.%{date}git%{shortcommit}%{?dist}
Summary:        Fork of bsnes with various performance improvements

License:        GPLv3+
URL:            https://github.com/libretro/bsnes-mercury
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/bsnes_mercury_balanced.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Suggests:       gnome-games
Suggests:       retroarch

%description
bsnes-mercury is a fork of higan, aiming to restore some useful features that
have been removed, as well as improving performance a bit. Maximum accuracy is
still uncompromisable; anything that affects accuracy is optional and off by
default.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build core_installdir=%{_libdir}/libretro


%install
%make_install core_installdir=%{_libdir}/libretro
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}_accuracy.libretro
sed -i 's!Balanced!accuracy!' %{buildroot}%{_libdir}/libretro/%{corename}_accuracy.libretro
sed -i 's!balanced!accuracy!' %{buildroot}%{_libdir}/libretro/%{corename}_accuracy.libretro


%files
%license LICENSE
%doc README.md
%{_libdir}/libretro/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20190817git4a38262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.11.20190817git4a38262
- build(fix previous commit): Downgrade to '20190817git4a38262' due upstream
  failure and wait for proper fix

* Thu Feb 10 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.10.20201013gitd01138b
- rebuilt

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20210318gitd232c6e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.8.20210318gitd232c6e
- chore(update): Latest git snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20190817git4a38262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20190817git4a38262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190817git4a38262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190817git4a38262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.3.20190817git4a38262
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190817git4a38262
- Initial package
