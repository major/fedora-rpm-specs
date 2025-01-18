Name:           90-Second-Portraits
Version:        1.01b
Release:        24%{?dist}
Summary:        Frantic street painting game

# Zlib: Main package
# CC-BY-SA-4.0: assets by Tangram Games
# CC-BY-3.0: data/music/monkeys.ogg
# OFL-1.1: data/fonts/neuton.ttf
# MIT: middleclass/
# X11: slam.lua and hump/
License:        Zlib AND CC-BY-SA-4.0 AND CC-BY-3.0 AND OFL-1.1 AND MIT AND X11
URL:            http://tangramgames.dk/games/90secondportraits/
Source0:        https://github.com/SimonLarsen/%{name}/releases/download/%{version}/90secondportraits-%{version}.love#/%{name}-%{version}.zip
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
%if 0%{?fedora} > 28
#https://github.com/SimonLarsen/90-Second-Portraits/pull/6
Patch2:         %{name}-%{version}-love11.patch
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le riscv64

#From the website (see URL above)
%description
90 Second Portraits is a silly speed painting game developed for Ludum Dare 31
Jam competition. Time is money and you have neither! In 90 SECOND PORTRAITS
you’re paying the bills by speed painting portraits of bypassing customers!
You have 90 seconds to paint the customer and his/her preferred background!
Your work day ends after 5 customers!

%prep
%autosetup -c -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6
#Remove non-free font and replace with existing font:
rm data/fonts/yb.ttf
sed -i "s/yb.ttf/neuton.ttf/" *.lua

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x *.txt -x *.md

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
install -p -D -m 0644 data/images/title_background.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md CREDITS.txt
%license LICENSE.txt middleclass/MIT-LICENSE.txt
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1.01b-22
- Add riscv64 support

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-17
- Migrate to SPDX license
- Fix license breakdown
- Add MIT license file to license macro
- Remove non-free font

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-9
- Rebuilt for correct exclusive arch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-4
- Add love 11 support

* Sat Mar 17 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-3
- Prepare backport to all fedora branches
- Properly exclude appdata folder from binary

* Fri Mar 16 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-2
- Fix license and use license macro
- Move some documentation to correct location

* Fri Mar 16 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.01b-1
- Initial package
