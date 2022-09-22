# Note: compton fork renamed to 'picom' since version 7.5

%global oldname compton-ng

Name:           picom
Version:        9.1
Release:        2%{?dist}
Summary:        Lightweight compositor for X11 (previously a compton fork)

License:        MPLv2.0 and MIT
URL:            https://github.com/yshui/picom
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  uthash-devel

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)

Requires:       hicolor-icon-theme

Conflicts:      compton%{?_isa}

Provides:       %{oldname}%{?_isa} = %{version}-%{release}

Obsoletes:      %{oldname} =< 7.5-1

%description
This is forked from the original Compton because that seems to have become
unmaintained.

The current battle plan of this fork is to refactor it to make the code
possible to maintain, so potential contributors won't be scared away when they
take a look at the code.

We also try to fix bugs.


%prep
%autosetup -p1


%build
%meson               \
    -Dwith_docs=true \
    %{nil}
%meson_build


%install
%meson_install


%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING LICENSES/MPL-2.0 LICENSES/MIT
%doc README.md CONTRIBUTORS picom.sample.conf
%{_bindir}/%{name}*
%{_bindir}/compton*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_mandir}/man1/*.1*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 9.1-1
- chore(update): 9.1

* Sun Jan 30 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 8.2-6
- fix: FTBFS 36 and building with docs

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 8.2-4
- Rebuild(uthash)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 8.2-1
- build(update): 8.2

* Tue Sep  8 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 8.1-1
- Update to 8.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 8-1
- Update to 8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.5-2
- Renamed to 'picom'

* Mon Nov 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.5-1
- Update to 7.5

* Sat Sep 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.4-1
- Update to 7.4
- Drop git submodule, now vendored with release tarball

* Tue Aug 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.2-2
- Update to 7.2
- Packaging fixes
- Disable LTO

* Tue Aug 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 7.1-5
- Initial package
