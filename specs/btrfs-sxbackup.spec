Name:           btrfs-sxbackup
Version:        0.6.11
Release:        %autorelease
Summary:        Incremental btrfs snapshot backups with push/pull support via SSH
License:        GPL-2.0-only
URL:            https://github.com/masc3d/btrfs-sxbackup
Source0:        https://github.com/masc3d/btrfs-sxbackup/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Add a manpage. The manpage was sent upstream but rejected, because they want
# to avoid maintaining multiple documentations and generate the manpage from the
# existing documentation instead. Keep the manpage until upstream has found a
# solution. Also see https://github.com/masc3d/btrfs-sxbackup/issues/26.
Patch0:         btrfs-sxbackup-manpages.patch
# Fix missing test suite from setup.py.
Patch1:         btrfs-sxbackup-tests.patch

BuildArch:      noarch

%generate_buildrequires
%pyproject_buildrequires

%description
Btrfs snapshot backup utility with push/pull support via SSH, retention, Email
notifications, compression of transferred data, and syslog logging.


%prep
%autosetup -p 1 -n %{name}-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
install -d %{buildroot}/%{_mandir}/man1
install -p -m644 man/* %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_sysconfdir}
install -p -m644 etc/btrfs-sxbackup.conf %{buildroot}/%{_sysconfdir}


%check
%python3 -m unittest discover -v -s btrfs_sxbackup/tests -p "Test*.py"


%files
%doc README.rst
%license LICENSE
%{_bindir}/btrfs-sxbackup
%{python3_sitelib}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/btrfs-sxbackup.conf


%changelog
%autochangelog
