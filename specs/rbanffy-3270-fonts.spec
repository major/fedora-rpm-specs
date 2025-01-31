%global srcname           3270font
%global foundry           rbanffy
%global fontlicense       BSD-3-Clause AND OFL-1.1-RFN
%global fontlicenses      LICENSE.txt
%global fontdocs          README.md CHANGELOG.md

%global fontfamily        3270
%global fontsummary       Monospaced font based on IBM 3270 terminals
%global fonts             build/*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
This font is derived from the x3270 font, which, in turn, was translated from
the one in Georgia Tech's 3270tool, which was itself hand-copied from a 3270
terminal.}

Version:                  3.0.1
Release:                  %autorelease
URL:                      https://github.com/rbanffy/3270font
Source0:                  %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source10:                 65-%{fontpkgname}.conf
BuildRequires:            fontforge
BuildRequires:            make

%fontpkg

%prep
%autosetup -n %{srcname}-%{version}

%build
%{__make} font
%fontbuild

%install
%fontinstall

%check
for f in %{fonts}; do
  # https://github.com/rbanffy/3270font/issues/110
  fontlint -i 98 -i 2 -i 5 -i 3 $f
done
%fontcheck

%fontfiles

%changelog
%autochangelog
