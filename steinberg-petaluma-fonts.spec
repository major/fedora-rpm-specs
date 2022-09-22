# The Scripts font has a different version from the other two
%global petalumaver       1.065
%global petalumascriptver 1.10

Version:        %{petalumaver}
URL:            https://www.smufl.org/fonts/

%global tag              petaluma-%{version}
%global date             20210127
%global forgeurl         https://github.com/steinbergmedia/petaluma

%forgemeta

# If both %%petalumaver and %%petalumascriptver were increased,
# release should be reset to 1. Otherwise, keep increasing it so that
# name-version-release keeps growing for both subpackages.
Release:        5%{?dist}

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL
%global fontlicenses     redist/OFL*.txt
%global fontdocs         README.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:
Petaluma is a Unicode typeface designed by Steinberg for its Dorico music
notation and scoring application.  It is compliant with version 1.3 of
the Standard Music Font Layout (SMuFL), a community-driven standard for
how music symbols should be laid out in the Unicode Private Use Area
(PUA) in the Basic Multilingual Plane (BMP) for compatibility between
different scoring applications.}

%global fontfamily0      Petaluma
%global fontsummary0     Petaluma music font
%global fonts0           redist/otf/Petaluma.otf
%global fontconfs0       %{SOURCE1}
%global fontdescription0 %{expand:%{common_description}

This package contains the Petaluma font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily1      PetalumaText
%global fontsummary1     Petaluma text font
%global fonts1           redist/otf/PetalumaText.otf
%global fontconfs1       %{SOURCE2}
%global fontdescription1 %{expand:%{common_description}

This package contains the Petaluma Text font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

%global fontfamily2      PetalumaScript
%global fontsummary2     Petaluma script font
%global fonts2           redist/otf/PetalumaScript.otf
%global fontconfs2       %{SOURCE3}
%global fontdescription2 %{expand:%{common_description}
%global fontpkgheader2   %{expand:
Version:        %{petalumascriptver}
}

This package contains the Petaluma Script font.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.}

Source0:        %{forgesource}
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf
Source3:        65-%{fontpkgname2}.conf

BuildRequires:  appstream

%fontpkg -a

# We cannot use %%fontmetapkg, because it doesn't know how to deal with a
# different version number for the Scripts font.
%package        all
Summary:        All the font packages generated from %{name}
Version:        %{petalumaver}
Requires:       %{name} = %{petalumaver}-%{release}
Requires:       steinberg-petalumatext-fonts = %{petalumaver}-%{release}
Requires:       steinberg-petalumascript-fonts = %{petalumascriptver}-%{release}

%description    all
This meta-package installs all the font packages generated from the
%{name} source package.

%prep
%forgesetup

%build
%fontbuild -a

%install
%fontinstall -a
metainfo="%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.steinberg-petalumascript-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.steinberg-petalumatext-fonts.metainfo.xml"

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,OFL,OFL-1.1-RFN,' \
    -e 's,updatecontact,update_contact,g' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

# Install the SMuFL metadata
install -m 0644 -p redist/petaluma_metadata.json \
        %{buildroot}%{_fontdir}/metadata.json

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck -a
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles -z 0
%{_fontdir}/metadata.json

%fontfiles -z 1

%fontfiles -z 2

%files          all

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.065-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 27 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.065-4
- Bump release so that petalumascript-fonts is "newer" than in f35

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.065-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Jerry James <loganjerry@gmail.com> - 1.065-1
- Version 1.065
- Add font organization
- Small fixes to the metainfo
- Validate metainfo with appstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.055-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jerry James <loganjerry@gmail.com> - 1.055-1.20190129gitc7a3e8e
- Initial RPM
