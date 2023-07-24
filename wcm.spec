%undefine __cmake_in_source_build

Name:		wcm
Version:	0.20.0
Release:	22%{?dist}
Summary:	WCM Commander
License:	MIT
Url:		https://github.com/corporateshark/WalCommander
Source0:	https://github.com/corporateshark/WalCommander/archive/release-%{version}.tar.gz
# https://github.com/corporateshark/WCMCommander/issues/505
Source1:	%{name}.appdata.xml
# https://github.com/corporateshark/WCMCommander/issues/504
Source3:	wcm.1
# https://github.com/corporateshark/WCMCommander/issues/508
Patch0:		%{name}-0.19.0.1.patch
# https://github.com/corporateshark/WCMCommander/issues/503
Source2:	FindUtf8proc.cmake
Patch1:		wcm-utf8proc.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	utf8proc-devel
# https://github.com/corporateshark/WCMCommander/issues/507
Patch2:		wcm-changelog.patch
BuildRequires:	cmake >= 2.8
BuildRequires:	desktop-file-utils
# libsmbclient-devel
BuildRequires:	pkgconfig(smbclient)
# libssh2-devel
BuildRequires:	pkgconfig(libssh2)
# freetype-devel
BuildRequires:	pkgconfig(freetype2)
# libX11-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	ImageMagick
BuildRequires:	libappstream-glib
Requires:	hicolor-icon-theme


%description
File manager mimicking the look-n-feel of Far Manager.


%prep
%setup0 -q -n WCMCommander-release-%{version}
%patch0 -p 0
%patch1 -p 0
cp %{SOURCE2} cmake/
rm -rf src/utf8proc
%patch2 -p 0
# https://github.com/corporateshark/WCMCommander/issues/490
rm -rf install-files/share/wcm/fonts
rm -rf libssh2
# https://github.com/corporateshark/WCMCommander/issues/506
rm -f install-files/share/wcm/styles/solarize*
rm -f tools/*


%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
# appdata
install -Dm 0644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/wcm.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/wcm.appdata.xml
# additional icons
# https://github.com/corporateshark/WCMCommander/issues/371
for i in 16x16 22x22 24x24 32x32 48x48 64x64 72x72 96x96 128x128
do
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/$i/apps
    convert install-files/share/pixmaps/wcm.png -resize $i %{buildroot}/%{_datadir}/icons/hicolor/$i/apps/wcm.png;
done
install -Dm 0644 %{SOURCE3} %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG.txt Contributors.txt README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.20.0-6
- Bump release for ABI break in utf8proc

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 TI_Eugene <ti.eugene@gmail.com> 0.20.0-4
- hicolor-icon-theme added as Requires
- fixed source tarball name
- post, postun and posttrans fixes
- some unwanted files removed
- generic man added

* Thu Aug 13 2015 TI_Eugene <ti.eugene@gmail.com> 0.20.0-3
- system utf8proc

* Wed Aug 12 2015 TI_Eugene <ti.eugene@gmail.com> 0.20.0-2
- wcm.appdata.xml added
- additional icons added

* Tue May 05 2015 TI_Eugene <ti.eugene@gmail.com> 0.20.0-1
- Version bump

* Mon Dec 15 2014 TI_Eugene <ti.eugene@gmail.com> 0.18.0-1
- Version bump
- Minor spec fixes.

* Wed Oct 08 2014 TI_Eugene <ti.eugene@gmail.com> 0.17.0-1
- initial packaging
