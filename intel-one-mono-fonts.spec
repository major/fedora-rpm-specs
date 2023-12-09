Version: 1.3.0
Release: %autorelease
URL:     https://github.com/intel/intel-one-mono

%global fontlicense       OFL-1.1-RFN

%global fontlicenses      license
%global fontdocs          README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Intel One Mono
%global fontsummary       An expressive monospaced font family

%global fonts             fonts/otf/*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Introducing Intel One Mono, an expressive monospaced font family that's built
with clarity, legibility, and the needs of developers in mind.

It's easier to read, and available for free, with an open-source font license.

Identifying the typographically underserved low-vision developer audience,
Frere-Jones Type designed the Intel One Mono typeface in partnership with the
Intel Brand Team and VMLY&R, for maximum legibility to address developers' 
fatigue and eyestrain and reduce coding errors.
A panel of low-vision and legally blind developers provided feedback at each
stage of design.

Intel One Mono also covers a wide range of over 200 languages using the Latin
script. The Intel One Mono fonts are provided in four weights — Light, Regular,
Medium, and Bold — with matching italics, and we are happy to share both an
official release of fonts ready to use as well as editable sources.
}

Source0:  %{url}/archive/V%{version}/%{name}-V%{version}.tar.gz
Source10: 59-%{fontpkgname}.conf

# Font family name changed from "IntelOne Mono" to "Intel One Mono"
Provides: intelone-mono-fonts = 1.3.0
Obsoletes: intelone-mono-fonts < 1.3.0

%fontpkg

%prep
%autosetup -n intel-one-mono-%{version}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
