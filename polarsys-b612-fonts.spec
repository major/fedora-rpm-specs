%global forgeurl https://github.com/polarsys/b612/
Version: 1.008
Release: 12%{?dist}
URL: https://projects.eclipse.org/projects/polarsys.b612

%global tag %{version}
%global foundry PolarSys

# README.md explains, "This program and the accompanying materials are
# made available under the terms of the Eclipse Public License v1.0 and
# Eclipse Distribution License v1.0 and the SIL Open Font License v1.1
# which accompanies this distribution."
%global fontlicense EPL-1.0 and BSD and OFL
%global fontlicenses edl-v10.html epl-v10.html OFL.txt
%global fontdocsex %{fontlicenses}

%global common_description %{expand:
Commissioned by Airbus and designed by Intactile Design, B612 is a
digital font intended to be used in an aeronautical context. B612 is
built with legibility as its core: every character is designed to be
highly recognizable even in critical reading conditions. B612 drawing
has been optimized for screen display, and full hinting has been added
to all sizes of alpha numeric characters.
}

%global fontfamily0 B612
%global fontsummary0 Sans-serif fonts designed for reading comfort and safety in aeroplane cockpits
%global fontpkgheader0    %{expand:
Obsoletes: polarsys-b612-fonts-common < 1.008-7
Obsoletes: polarsys-b612-sans-fonts < 1.008-7
Provides: polarsys-b612-sans-fonts = %{version}-%{release}
}
%global fonts0 fonts/ttf/B612-*.ttf
%global fontconfs0 %{SOURCE10}
%global fontappstreams0 %{SOURCE20}
%global fontdescription0  %{expand:
%{common_description}

This packages contains a sans serif font family.}

%global fontfamily1 B612 Mono
%global fontsummary1 Monospace fonts designed for reading comfort and safety in aeroplane cockpits
%global fontpkgheader1    %{expand:
Obsoletes: polarsys-b612-fonts-common < 1.008-7
}
%global fonts1 fonts/ttf/B612Mono-*.ttf
%global fontconfs1 %{SOURCE11}
%global fontappstreams1 %{SOURCE21}
%global fontdescription1  %{expand:
%{common_description}

This packages contains a monospace font family.}


%global fontname polarsys-b612
%global fontconf 64-%{fontname}


%forgemeta


Source0:        %{forgesource}
Source1:        https://www.eclipse.org/legal/epl-v10.html
Source10:       64-%{fontpkgname0}.conf
Source11:       64-%{fontpkgname1}.conf
Source20:       %{fontname}.metainfo.xml
Source21:       %{fontname}-mono.metainfo.xml


%fontpkg -a
%fontmetapkg


%package doc
Summary:        Documentation for B612
BuildArch:      noarch

%description doc
%{common_description}

This package contains a leaflet explaining the design and production of
the fonts.


%prep
%forgesetup

install -m 0644 -p %{SOURCE1} .


%build
%fontbuild -a


%install
%fontinstall -a


%check
%fontcheck -a


%fontfiles -a

%files doc
%doc docs/B612-Leaflet.pdf


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Peter Oliver <rpm@mavit.org.uk> - 1.008-7
- Update to follow new font packaging guidelines.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Peter Oliver <rpm@mavit.org.uk> - 1.008-4
- Polarsys.org was merged into Eclipse.org.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Peter Oliver <rpm@mavit.org.uk> - 1.008-1
- Update to version 1.008.
- Latest source is now at GitHub rather than PolarSys's own git repository.
- Additional licence, SIL Open Font License, Version 1.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-5.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov  8 2018 Peter Oliver <rpm@mavit.org.uk> - 1.003-4.20171129gitbd14fde
- Drop unneeded BuildRequires.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-3.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-2.20171129gitbd14fde
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec  7 2017 Peter Oliver <rpm@mavit.org.uk> - 1.003-1.20171129gitbd14fde
- Update to version 1.003.
- Split leaflet out into a separate doc subpackage.

* Fri Nov 10 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-3.20170320gitf4ce1fd
- Remove obsolete sections.

* Fri Nov  3 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-2.20170320gitf4ce1fd
- Use auto-generated source snapshot.
- Remove obsolete sections.

* Fri Nov  3 2017 Peter Oliver <rpm@mavit.org.uk> - 1.002-1.20170320gitf4ce1fd
- Initial package.
