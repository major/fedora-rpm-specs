Version:        1.392
URL:            https://www.smufl.org/fonts/

%global tag         bravura-%{version}
%global date        20210209
%global forgeurl    https://github.com/steinbergmedia/bravura

%forgemeta

Release:        4%{?dist}

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL-1.1-RFN
%global fontlicenses     LICENSE.txt
%global fontdocs         README.md redist/bravura-text.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:
Bravura is an OpenType music font developed for Steinberg's Dorico music
notation and composition software.  It is also the reference font for
Standard Music Font Layout (SMuFL), which provides a standard way of
mapping the thousands of musical symbols required by conventional music
notation into the Private Use Area in Unicode's Basic Multilingual Plane
for a single (format-independent) font.}

%global fontfamily0      Bravura
%global fontsummary0     Bravura music font
%global fonts0           redist/otf/Bravura.otf
%global fontconfs0       %{SOURCE1}
%global fontdescription0 %{expand:%{common_description}

This package contains the Bravura font family.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.
}

# This can be removed when F36 reaches EOL
%global fontpkgheader0 %{expand:
Obsoletes:      steinberg-bravura-fonts-common < 1.360
Provides:       steinberg-bravura-fonts-common = %{version}-%{release}
}

%global fontfamily1      BravuraText
%global fontsummary1     Bravura text font
%global fonts1           redist/otf/BravuraText.otf
%global fontconfs1       %{SOURCE2}
%global fontdescription1 %{expand:%{common_description}

This package contains the Bravura Text font family.  It is a Unicode
typeface designed by Steinberg for its music notation and scoring
application.
}

# This can be removed when F36 reaches EOL
%global fontpkgheader1 %{expand:
Obsoletes:      steinberg-bravura-text-fonts < 1.360
Provides:       steinberg-bravura-text-fonts = %{version}-%{release}
}

Source0:        %{forgesource}
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf

BuildRequires:  appstream

%fontpkg -a
%fontmetapkg

%prep
%forgesetup
 
%build
%fontbuild -a

%install
%fontinstall -a
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -i 's,updatecontact,update_contact,g' $metainfo

appstreamcli validate --no-net $metainfo

# Install the SMuFL metadata
install -m 0644 -p redist/bravura_metadata.json \
        %{buildroot}%{_fontdir}/metadata.json

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck -a
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles -z 0
%{_fontdir}/metadata.json

%fontfiles -z 1

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.392-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 1.392-3
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.392-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.392-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Jerry James <loganjerry@gmail.com> - 1.392-1
- Version 1.392
- Add font organization
- Small fixes to the metainfo
- Validate metainfo with appstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.390-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.390-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Jerry James <loganjerry@gmail.com> - 1.390-4
- Install the SMuFL metadata where MuseScore expects it

* Wed Oct 21 2020 Jerry James <loganjerry@gmail.com> - 1.390-3
- Fix installation locations of fontconfig and appstream files

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.390-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Jerry James <loganjerry@gmail.com> - 1.390-1
- Version 1.390

* Tue Apr  7 2020 Jerry James <loganjerry@gmail.com> - 1.360-2.20200401git788874a
- Fix Obsoletes (bz 1821488)

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 1.360-1.20200401git788874a
- Version 1.360
- Comply with the new font guidelines

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.320-2.20191209.6aa3a10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jerry James <loganjerry@gmail.com> - 1.320-1.20191209.6aa3a10
- Version 1.320

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 1.277-1.20190423.ccc90dd
- Initial RPM
