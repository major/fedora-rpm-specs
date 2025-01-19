Name:           orthorobot
Version:        1.1.1
Release:        23%{?dist}
Summary:        A perspective based puzzle game

License:        WTFPL
URL:            http://stabyourself.net/orthorobot/
Source0:        https://github.com/Stabyourself/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source1 is a copy of the license, which was added after v1.1.1:
#https://github.com/Stabyourself/orthorobot/commit/48f07423950b29a94b04aefe268f2f951f55b62e
Source1:        https://raw.githubusercontent.com/Stabyourself/%{name}/48f07423950b29a94b04aefe268f2f951f55b62e/LICENSE.txt
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
#Love 11 patch (backwards compatible):
#https://github.com/Stabyourself/orthorobot/pull/3
Patch1:         %{name}-%{version}-love11.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From the website (see URL above)
%description
Literally bridging the gap between 2D and 3D games, Ortho Robot is a
perspective based puzzle game, where you flatten the view to move
across gaps. This game is made with LOVE.

%prep
%autosetup -p1
#Copy LICENSE, fixed after v1.1.1
cp -f %{SOURCE1} ./LICENSE.txt
#Change version in appdata
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources
zip -r %{name}.love . -x appdata/* -x appdata/ -x README.md -x LICENSE.txt

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
install -p -D -m 0644 helpplayer.png \
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1.1-12
- Rebuilt for correct exclusive arch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1.1-7
- Add love 11 support

* Mon Mar 19 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1.1-6
- Remove some unnecessary files from love binary

* Thu Mar 15 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1.1-5
- Add ppc64le for f28+

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1.1-1
- Fix LICENSE issues
- Update to 1.1.1
- Appdata fixes

* Sat Nov 19 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-6
- love 0.10.* fixes (a bit late, just noticed this issue)

* Wed Nov 16 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-5
- Remove exclusive arch for noarch, see bug#1298668

* Wed Nov 09 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-4
- Exclusive arches to what love builds on

* Mon Feb 22 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-3
- Adding appdata and basic manpage via patch
- Moving desktop and script to appdata patch

* Fri Feb 19 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-2
- Adding license file
- Fixing source0
- Generate desktop file similar to the execution script
- Forgot to exclude zipping the execution script
- Removed duplicate package file

* Mon Nov 30 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 1.1-1
- Initial package
