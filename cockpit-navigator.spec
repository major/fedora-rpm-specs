%global forgeurl https://github.com/45Drives/cockpit-navigator/
Version: 0.5.9
%forgemeta

Name: cockpit-navigator
Release: %autorelease
Summary: A File System Browser for Cockpit
License: GPLv3+
URL: %{forgeurl}
Source0:  %{forgesource}
BuildArch: noarch

Requires: cockpit-system
Requires: python3
Requires: rsync
Requires: zip

Patch0001: 0001-Fedora-remove-branding.patch

%description
Cockpit Navigator
A File System Browser for Cockpit.


%prep
%forgeautosetup -p1


%build
# empty


%install
mkdir -p %{buildroot}%{_datadir}/cockpit/
cp -rpf navigator %{buildroot}%{_datadir}/cockpit/
echo "export let NAVIGATOR_VERSION = \"%{version}\";" > %{buildroot}%{_datadir}/cockpit/navigator/version.js


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
/usr/share/cockpit/navigator/


%changelog
%autochangelog
