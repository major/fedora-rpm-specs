Name:           ibus-engine-gui-ci
Version:        1.0.0.20220118
Release:        9%{?dist}
Summary:        GUI CI for IBus engines
License:        LGPL-2.0-or-later
URL:            https://github.com/fujiwarat/ibus-engine-gui-ci
Source0:        https://github.com/fujiwarat/ibus-engine-gui-ci/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2
BuildRequires:  ibus-devel
BuildRequires:  json-glib-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gtk3-devel
Requires:       ibus
Recommends:     ibus-desktop-testing

%description
GUI CI can run with ibus-desktop-testing-runner and engines get
focus events with the window manager.

%prep
%autosetup -S git

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%doc AUTHORS README
%license COPYING
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <fujiwara@redhat.com> - 1.0.0.20220118-3
- Migrate license tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20220118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Takao Fujiwara <fujiwara@redhat.com> - 1.0.0.20220118-1
- Initial implementation
