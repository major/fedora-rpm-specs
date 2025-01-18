%global uuid    org.gnome.HexGL

%global commit f47a351055a235730795341dcd6b2397cc4bfa0c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200724

Name:           gnome-hexgl
Version:        0.2.0
Release:        17.%{date}git%{shortcommit}%{?dist}
Summary:        Gthree port of HexGL

# The entire source code is GPLv3+ except sounds which is CC-BY
# Automatically converted from old format: MIT and CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:            https://github.com/alexlarsson/gnome-hexgl
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

# https://github.com/alexlarsson/gthree/issues/66
ExcludeArch:    i686

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gthree-1.0) >= 0.9.0
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
%{summary}.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING sounds/LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-16.20200724gitf47a351
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7.20200724gitf47a351
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 20:38:05 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-6.20200724gitf47a351
- build(update): commit f47a351 | rh#1863680
- build: no longer exclude 'armv7hl' arch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-2
- Update to 0.2.0

* Fri Mar 29 2019 Artem Polishchuk <ego.cordatus@gmail.com>
- Initial package
