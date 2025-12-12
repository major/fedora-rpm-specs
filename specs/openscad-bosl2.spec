%global forgeurl https://github.com/BelfrySCAD/BOSL2
%global commit 961ed6d8ff70da10861d873b06df628554fa1e8f
%global date 20251210
%global version 0

%forgemeta

Name:    openscad-bosl2
Version: %forgeversion
Release: %{autorelease}
Summary: BOSL2 library for OpenSCAD

License: BSD-2-Clause
URL:     %{forgeurl}
Source:  %{forgesource}

BuildArch:     noarch

# For running the tests
BuildRequires: openscad
BuildRequires: sed

Requires: openscad


%description
A library for OpenSCAD, filled with useful tools, shapes, masks, math and
manipulators, designed to make OpenSCAD easier to use.

BOSL2 is beta code. The code is still being reorganized.

%prep
%forgesetup

%build
#no build, only scad scripts

%install
install -dD -m755 %{buildroot}%{_datadir}/openscad/libraries/BOSL2

for FILE in *.scad; do
  install -p "$FILE" -m644 "%{buildroot}%{_datadir}/openscad/libraries/BOSL2/$FILE"
done


%check
./scripts/run_tests.sh


%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING.md
%doc tutorials
%doc examples
%{_datadir}/openscad/libraries/BOSL2


%changelog
%autochangelog
