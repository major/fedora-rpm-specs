%global commit 06c88433662a4004cf56a6e471b523a0a8880be0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20210303
%global tname capitaine-cursors

Name:           la-capitaine-cursor-theme
Version:        4
Release:        10%{?commit:.%{date}git%{shortcommit}}%{?dist}
Summary:        X-cursor theme inspired by macOS and based on KDE Breeze

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/keeferrourke/capitaine-cursors
%if 0%{?commit:1}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
%else
Source0:        %{url}/archive/r%{version}/%{name}-%{version}.tar.gz
%endif
BuildArch:      noarch

BuildRequires:  bc
BuildRequires:  inkscape
BuildRequires:  xcursorgen

Suggests:       la-capitaine-icon-theme

%description
This is an x-cursor theme inspired by macOS and based on KDE Breeze. The source
files were made in Inkscape, and the theme was designed to pair well with my
icon pack, La Capitaine.


%prep
%if 0%{?commit:1}
%autosetup -n %{tname}-%{commit}
%else
%autosetup -n %{tname}-r%{version}
%endif


%build
./build.sh --max-dpi xxxhd --type dark
./build.sh --max-dpi xxxhd --type light


%install
mkdir -p           %{buildroot}/%{_datadir}/icons/
cp -rfa dist/dark  %{buildroot}/%{_datadir}/icons/%{tname}
cp -rfa dist/light %{buildroot}/%{_datadir}/icons/%{tname}-light
find %{buildroot} -size 0 -delete


%post
/bin/touch --no-create %{_datadir}/icons/%{tname}{,-light} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{tname}{,-light} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{tname}{,-light} &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{tname}{,-light} &>/dev/null || :


%files
%license COPYING
%doc README.md
%{_datadir}/icons/%{tname}{,-light}
%ghost %{_datadir}/icons/%{tname}{,-light}/icon-theme.cache


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4-10.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4-9.20210303git06c8843
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4-8.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4-7.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4-6.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4-5.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4-4.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4-3.20210303git06c8843
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 07 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 4-2.20210303git06c8843
- fix: Hotfix for rh#2061265
- build: User upstream recommended name for end dir

* Tue Mar 01 2022 Cedric Staniewski <cedric@gmx.ca> - 4-1.git06c8843
- Update to r4
- Include fix to allow building with inkscape >= 1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 3-9
- Reduce BuildRequires to xcursorgen, it's the the only tool from
  xorg-x11-apps that we need.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3-5
- Update to r3
- Packaging fixes

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 2-1
- Initial package
