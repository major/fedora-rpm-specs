%global forgeurl https://github.com/45Drives/cockpit-file-sharing/
Version: 2.4.5
%forgemeta

Name: cockpit-file-sharing
Release: %autorelease
Summary: Cockpit user interface for managing SMB and NFS file sharing.
License: GPLv3+
URL: %{forgeurl}
Source0:  %{forgesource}
BuildArch: noarch

BuildRequires: make

Requires: cockpit-ws
Requires: python3
Recommends: nfs-utils
Recommends: samba

Provides: bundled(patternfly) = 3

# Strip out the 45Drives branding since this isn't part of their product
Patch0001: 0001-Fedora-remove-branding.patch

%description
A Cockpit component for managing SMB exports and NFS shares.  This package uses Samba and nfs-utils.


%prep
%forgeautosetup -p1


%build
# no build required


%install
%make_install


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_datadir}/cockpit/file-sharing/


%changelog
%autochangelog
