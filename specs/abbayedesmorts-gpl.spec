Name:           abbayedesmorts-gpl
Version:        2.0.4
Release:        3%{?dist}
Summary:        Platform game set in 13th century

# Graphics and Sounds are licensed under
# Creative Commons 3.0 Attribution license.
License:        GPL-3.0-only AND CC-BY-3.0
# Original Windows game by locomalito
# https://locomalito.com/abbaye_des_morts.php
URL:            https://github.com/nevat/abbayedesmorts-gpl 
Source0:        https://github.com/nevat/abbayedesmorts-gpl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix building with gcc 15
Patch0:         %{name}-2.0.4-gcc15.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
In the 13th century, the Cathars, who preach about good Christian beliefs, 
were being expelled by the Catholic Church out of the Languedoc region in 
France.

One of them, called Jean Raymond, found an old church in which to hide, not 
knowing that beneath its ruins lay buried an ancient evil.

A style close to Spectrum ZX, with its dark background and bright colors, 
proper fit with the story, because it does look old and somewhat horrifying. 
Also, the gameplay is directly inspired by Manic Miner and Jet Set Willy.


%prep
%autosetup -p1

# Enable verbose build
sed -i 's/@$(CC)/$(CC)/' Makefile


%build
%set_build_flags
%make_build


%install
%make_install

# Install icons
rm %{buildroot}%{_datadir}/pixmaps/abbaye.png
cp -a abbaye.png abbaye48.png
for px in 48 64 128; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  install -p -m 644 abbaye${px}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/abbaye.png
done

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/abbaye.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/abbaye.appdata.xml


%files
%{_bindir}/abbayev2
%{_datadir}/abbayev2
%{_datadir}/appdata/abbaye.appdata.xml
%{_datadir}/applications/abbaye.desktop
%{_datadir}/icons/hicolor/*/apps/abbaye.png
%doc ReadMe.md ChangeLog.md screenshots
%license COPYING


%changelog
* Thu Jan 23 2025 Andrea Musuruane <musuruan@gmail.com> - 2.0.4-3
- Fix FTBFS (BZ #2339459)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Andrea Musuruane <musuruan@gmail.com> - 2.0.4-1
- Updated to new upstream release

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Andrea Musuruane <musuruan@gmail.com> - 2.0.2-1
- Updated to new upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20.20210509git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-19.20210509git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-18.20210509git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-17.20210509git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-16.20210509git
- Updated to new upstream post-release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-15.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13.20170709git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-7.20170709git
- Added gcc dependency
- Used new AppData directory
- Spec file clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-3.20170709git
- Fixed AppData file
- Fixed LDFLAGS usage

* Thu Jul 13 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-2.20170709git
- Updated to new upstream post-release
- Added missing BR

* Sat Jul 08 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-1
- First release

