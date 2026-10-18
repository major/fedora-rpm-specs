Name:           btrfs-backup-ng
Version:        0.9.12
Release:        %autorelease
Summary:        Intelligent, feature-rich backups for btrfs

License:        MIT
URL:            https://github.com/berrym/btrfs-backup-ng
Source:         %{pypi_source btrfs_backup_ng}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
# External tools the test suite invokes
BuildRequires:  btrfs-progs
BuildRequires:  dash
BuildRequires:  openssl
BuildRequires:  procps-ng

Requires:       btrfs-progs
Requires:       openssh-clients
Requires:       pv
Requires:       gzip
Requires:       bzip2
Requires:       zstd
Requires:       xz
Requires:       lz4
Requires:       lzo
Requires:       pigz
Requires:       pbzip2


%description
Complete btrfs backup solution with automated snapshots,
incremental transfers, restore functionality,
snapper integration, btrbk migration, and systemd scheduling

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
# test_source_checkout_still_resolves: looks for man/ and completions/ relative
#   to the imported module, which lives in the buildroot during %%check.
# test_ssh_commit_wraps_in_sudo_when_configured: executes `sudo -n` for real.
%{pytest} -k "not test_source_checkout_still_resolves and not test_ssh_commit_wraps_in_sudo_when_configured"


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
