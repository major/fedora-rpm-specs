Name:           safetyblanket
Version:        1.01
Release:        19%{?dist}
Summary:        Creepy blanket simulator

#See LICENSE.txt file in source for details
#All code is zlib excluding slam.lua and AnAL.lua, which is MIT
#All assets are CC-BY 4.0, excluding font, which is CC-BY 3.0
# Automatically converted from old format: zlib and MIT and CC-BY - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:            http://tangramgames.dk/games/safetyblanket/
Source0:        https://github.com/SimonLarsen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
#Patch for LOVE v0.10.2
#https://github.com/SimonLarsen/safetyblanket/commit/5a3387b73bb5bd85718742ab813d9df44d075cd0
Patch1:         0001-Updated-for-L-VE-11.0.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From the website (see URL above)
%description
Safety Blanket was developed in 48 hours for the Ludum Dare 29 game jam.
It’s bed time, the monsters are out to get you, and your blanket is just too
small to cover your body!
Cover your exposed limbs to fend off the approaching tentacles.
The tentacles will only go for your feet, hands and head.
If the tentacles reach you it’s game over!

%prep
%autosetup -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE.txt

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
install -p -D -m 0644 res/gfx/title_text1.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE.txt
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.01-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01-8
- Rebuilt for correct exclusive arch
- Fix some LOVE 11 issues

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01-3
- Add love 11 support

* Mon Mar 19 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01-2
- Prepare backport to all fedora branches
- Properly exclude appdata folder from binary

* Sun Mar 18 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01-1
- Initial package
