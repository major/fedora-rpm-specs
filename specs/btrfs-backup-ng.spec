Name:           btrfs-backup-ng
Version:        0.9.18
Release:        %autorelease
Summary:        Btrfs backups with snapshots, incremental transfers and restore

License:        MIT
URL:            https://github.com/berrym/btrfs-backup-ng
Source:         %{pypi_source btrfs_backup_ng}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
# External tools the test suite invokes
BuildRequires:  btrfs-progs
BuildRequires:  bzip2
BuildRequires:  dash
BuildRequires:  fish
BuildRequires:  gzip
BuildRequires:  lz4
BuildRequires:  lzop
BuildRequires:  openssl
BuildRequires:  pbzip2
BuildRequires:  pigz
BuildRequires:  procps-ng
BuildRequires:  xz
BuildRequires:  zsh
BuildRequires:  zstd

Requires:       btrfs-progs
Requires:       openssh-clients
Requires:       pv
Requires:       gzip
Requires:       bzip2
Requires:       zstd
Requires:       xz
Requires:       lz4
Requires:       lzop
Requires:       pigz
Requires:       pbzip2


%description
btrfs-backup-ng creates, transfers, prunes and restores btrfs snapshots: to
local disks, to other machines over SSH, or as raw send-stream files on any
filesystem (NFS, SMB, cloud storage). It is configured with TOML and driven by
subcommands such as run, snapshot, transfer, prune, restore and verify, with an
interactive wizard to write the first configuration.

Features:
- Incremental transfers, with the parent matched by btrfs UUID so a re-created
  snapshot is never used as the wrong parent
- Time-based retention: hourly, daily, weekly, monthly and yearly
- Restore from local, SSH and raw targets, as full or incremental chains
- Stream compression with zstd, gzip, lz4, xz, bzip2, lzop, pigz and pbzip2
- Raw backups with GPG or OpenSSL encryption and a checksummed metadata
  sidecar that raw verify can check
- SSH host-key verification, bandwidth limits and sudo support on the remote
- Locks kept on the remote target, so a prune running elsewhere cannot delete
  a snapshot that a restore is reading
- Snapper integration, including restoring snapshots with their metadata
- Import of btrbk configuration, snapshots and systemd timers
- systemd timer installation, email and webhook notifications, and a doctor
  command that diagnoses and repairs common problems

Man pages and bash, zsh and fish completions are included.

%prep
%autosetup -p1 -n btrfs_backup_ng-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l btrfs_backup_ng

install -d %{buildroot}%{_mandir}/man1
install -m 0644 man/man1/btrfs*.1* %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -m 0644 completions/btrfs-backup-ng.bash %{buildroot}%{bash_completions_dir}/btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.zsh  %{buildroot}%{zsh_completions_dir}/_btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.fish %{buildroot}%{fish_completions_dir}/btrfs-backup-ng.fish

%check
# Tests that run an external program skip when it is missing; listing a tool
# here turns its skips into failures, so a dropped BuildRequires fails the build.
export BBNG_TEST_REQUIRE_TOOLS=awk,btrfs,bzip2,dash,fish,gzip,lz4,lzop,openssl,pbzip2,pigz,ps,xz,zsh,zstd
%{pytest}


%files -n btrfs-backup-ng -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_mandir}/man1/btrfs*.1.gz
%{_bindir}/btrfs-backup-ng
%{_datadir}/%{name}/
%{bash_completions_dir}/btrfs-backup-ng
%{zsh_completions_dir}/_btrfs-backup-ng
%{fish_completions_dir}/btrfs-backup-ng.fish


%changelog
%autochangelog
