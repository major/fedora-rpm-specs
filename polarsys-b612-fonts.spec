%global forgeurl https://github.com/polarsys/b612/
Version: 1.008
Release: %autorelease
URL: https://projects.eclipse.org/projects/polarsys.b612

%global tag %{version}
%global foundry PolarSys

# README.md explains, "This program and the accompanying materials are
# made available under the terms of the Eclipse Public License v1.0 and
# Eclipse Distribution License v1.0 and the SIL Open Font License v1.1
# which accompanies this distribution."
# EDL v1.0 at https://www.eclipse.org/org/documents/edl-v10.php says
# to use BSD-3-Clause as SPD-X identifier.
%global fontlicense EPL-1.0 AND BSD-3-Clause AND OFL-1.1
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
%autochangelog
