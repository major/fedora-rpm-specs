Name:           btrfs-backup-ng
Version:        0.8.2
Release:        %autorelease
Summary:        Intelligent, feature-rich backups for btrfs

License:        MIT
URL:            https://github.com/berrym/btrfs-backup-ng
Source:         %{pypi_source btrfs_backup_ng}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

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

%define bash_compdir  %{_prefix}/share/bash-completions/completions
%define zsh_compdir   %{_prefix}/share/zsh/site-functions
%define fish_compdir  %{_prefix}/share/fish/vendor_completions.d

install -d %{buildroot}%{bash_compdir}
install -d %{buildroot}%{zsh_compdir}
install -d %{buildroot}%{fish_compdir}
install -m 0644 completions/btrfs-backup-ng.bash %{buildroot}%{bash_compdir}/btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.zsh  %{buildroot}%{zsh_compdir}/_btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.fish %{buildroot}%{fish_compdir}/btrfs-backup-ng.fish

%check
%{pytest}


%files -n btrfs-backup-ng -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_mandir}/man1/btrfs*.1.gz
%{_bindir}/btrfs-backup-ng
%{_prefix}/share/bash-completions/completions/btrfs-backup-ng
%{_prefix}/share/zsh/site-functions/_btrfs-backup-ng
%{_prefix}/share/fish/vendor_completions.d/btrfs-backup-ng.fish


%changelog
%autochangelog
