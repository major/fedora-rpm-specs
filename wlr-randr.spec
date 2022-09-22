%global commit 5ff601a584b661e4bad9036026ce9e4f23fcbc4f
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
Name:           wlr-randr
Version:        0
Release:        9.20200408git%{shortcommit}%{?dist}
Summary:        An xrandr clone for wlroots compositors
License:        MIT
URL:            https://github.com/emersion/wlr-randr
Source0:        https://github.com/emersion/wlr-randr/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(wayland-client)

%description
wlr-randr is an xrandr clone for wlroots compositors

%prep
%autosetup -n wlr-randr-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wlr-randr

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 28 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-4.20200408git5ff601a
- Remove unnecessary BuildRequires

* Mon Apr 27 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-3.20200408git5ff601a
- Remove unnecessary explicit requires

* Sat Apr 25 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-2.20200408git5ff601a
- Use recommended source URL

* Mon Dec 02 2019 Morian Sonnet <MorianSonnet@googlemail.com> - 0-1.20190321gitc4066aa
- Initial build

