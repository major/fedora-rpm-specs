Name:           btrfs-backup-ng
Version:        0.6.5
Release:        %autorelease
Summary:        Intelligent, feature-rich backups for btrfs

License:        MIT
URL:            https://github.com/berrym/btrfs-backup-ng
Source:         %{pypi_source btrfs_backup_ng}

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:    btrfs-progs


%description
btrfs-backup-ng supports incremental backups for *btrfs* using
*snapshots* and *send/receive* between filesystems. Think of it as a basic
version of Time Machine. Backups can be stored locally and/or remotely (e.g. via
SSH). Multi-target setups are supported as well as dealing with transmission
failures (e.g. due to network outage).


%prep
%autosetup -p1 -n btrfs_backup_ng-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l btrfs_backup_ng


%check
%pyproject_check_import


%files -n btrfs-backup-ng -f %{pyproject_files}
%doc README.md
%{_bindir}/btrfs-backup-ng

%changelog
%autochangelog
