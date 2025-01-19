Name:           mrrescue
Version:        1.02e
Release:        27%{?dist}
Summary:        Arcade-style fire fighting game

#See LICENSE file in source for details
#All code is zlib, excluding slam, AnAL and TSerial, which are MIT
#All assets are CC-BY-SA
# Automatically converted from old format: zlib and CC-BY-SA and MIT - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:            http://tangramgames.dk/games/mrrescue
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
#Upstream patches:
#https://github.com/SimonLarsen/mrrescue/commit/ec139833eba2781507cf32d9df30772138a76829
Patch1:         %{name}-%{version}-double-define.patch
#https://github.com/SimonLarsen/mrrescue/commit/ab23031e0c2faecb77fde1be8a41d6f8ea4e6eda
Patch2:         %{name}-%{version}-love11.patch
#https://github.com/SimonLarsen/mrrescue/commit/5a58668d9a1e661f6591bd44a76cf242b3aabf3e
Patch3:         %{name}-%{version}-Fixed-remaining-setColor-statements.patch
#https://github.com/SimonLarsen/mrrescue/commit/a5be73c60acb8d1be506f7b5e48e784492ba96ce
Patch4:         %{name}-%{version}-Updated-conf.lua-to-11.0-template.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From the website (see URL above)
%description
Mr. Rescue is an arcade styled 2d action game centered around evacuating
civilians from burning buildings. The game features fast paced fire
extinguishing action, intense boss battles, a catchy soundtrack and lots of
throwing people around in pseudo-randomly generated buildings.

%prep
%autosetup -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE -x README.md
#Generate icon (modified splash.png)
convert data/splash.png -crop 256x205+0+0 -background none -gravity center -extent 256x256! %{name}.png

%install
#Install love file
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
#Install execution script
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
#Install manpage
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
#Install appdata.xml and verify
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md
%license LICENSE
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.02e-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-15
- Rebuilt for correct exclusive arch
- LOVE 11 fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-10
- Add upstream fix for code duplication (non-functional change)

* Sun Jun 10 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-9
- Add love 11 support

* Mon Mar 19 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-8
- Remove more unnecessary files from love binary

* Sat Mar 17 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-7
- Add ppc64le build for f28+
- Add README.md to docs
- Remove docs from love binary

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-3
- More Appdata fixes

* Wed Nov 23 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-2
- Appdata fixes

* Sun Nov 20 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.02e-1
- Initial package
