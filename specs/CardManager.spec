Name:           CardManager
Version:        3
Release:        33%{?dist}
Summary:        Java application to allows you to play any, especially collectible, card game

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://cardmanager.wz.cz/
Source0:        http://cardmanager.wz.cz/CardManager_sources%{version}.zip
Source1:        %{name}.appdata.xml
Patch0:         removeManifestEntries.patch
Patch1:         jdk8-javadoc.patch
Patch2:         bumpJdk.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Requires:       java

%description
This is free, open source multiplatform (java) application which allows you to
 play ANY card game. 
The game is designed especially to play collectible card games like Magic the
 Gathering or Doomtrooper over network.
To play those games you need to own (scanned) images of card, which are not part
 of this package.
Some can be easily downloadable from internet, but be aware of copyrights.
The default deck and background is free of copyright
Also please feel free to add your own backgrounds to 
~/CardManager/data/backgrounds and of course enhance
collection under ~/CardManager/collection

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c CardManager
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch -P0
%patch -P1
%patch -P2

%build

ant

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  CardManager.desktop
cp -p ./CardManager.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./FedoraLauncher.sh $RPM_BUILD_ROOT%{_bindir}/CardManager
#end launcher


#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r data $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r collection $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_datadir}/pixmaps/CardManager.png
%{_datadir}/applications/CardManager.desktop
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/CardManager
%{_javadir}/*
%doc license.txt
%{_datadir}/appdata/%{name}.appdata.xml

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3-30
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3-22
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3-21
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Apr 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-15
- bravely bumped to jdk8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 13 2015 Jiri Vanek <jvanek@redhat.com> - 3-6
- added patch1 jdk8-javadoc.patch

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 28 2014 Jiri Vanek <jvanek@redhat.com> - 3-5
- Added appdata.xml

* Thu Aug 08 2013 Mat Booth <fedora@matbooth.co.uk> - 3-3
- Drop BR on ant-nodeps, fixes rhbz #991930

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Jiri Vanek <jvanek@redhat.com> - 3-1
- updated to v3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Jiri Vanek <jvanek@redhat.com> - 1-1
-first release for fedora

