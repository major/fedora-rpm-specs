Name:           btrfs-assistant
Version:        1.6.3
Release:        1%{?dist}
Summary:        GUI management tool to make managing a Btrfs filesystem easier

License:        GPLv3+
URL:            https://gitlab.com/%{name}/%{name}
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       hicolor-icon-theme
Requires:       polkit

BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  btrfs-progs-devel
BuildRequires:  libbtrfsutil
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  libappstream-glib

Recommends:     btrfsmaintenance
Recommends:     snapper


%description
Btrfs Assistant is a GUI management tool to make managing a Btrfs filesystem
easier.

The primary features it offers are:

* An easy to read overview of Btrfs metadata
* A simple view of subvolumes with or without Snapper/Timeshift snapshots
* Run and monitor scrub and balance operations
* A pushbutton method for removing subvolumes
* A management front-end for Snapper with enhanced restore functionality
    * View, create and delete snapshots
    * Restore snapshots in a variety of situations
        * When the filesystem is mounted in a different distro
        * When booted off a snapshot
        * From a live ISO
    * View, create, edit, remove Snapper configurations
    * Browse snapshots and restore individual files
    * Browse diffs of a single file across snapshot versions
    * Manage Snapper systemd units
* A front-end for Btrfs Maintenance
    * Manage systemd units
    * Easily manage configuration for defrag, balance and srub settings


%prep
%autosetup -p1

# Fix config path for btrfsmaintenance
sed -i 's|^bm_config =.*|bm_config = %{_sysconfdir}/sysconfig/btrfsmaintenance|' src/btrfs-assistant.conf

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-bin
%{_bindir}/%{name}-launcher
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/org.%{name}.pkexec.policy
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Thu Aug 25 2022 Arthur Bols <arthur@bols.dev> - 1.6.3-1
- Update to 1.6.3 (#2120071)

* Wed Aug 24 2022 Arthur Bols <arthur@bols.dev> - 1.6.2-1
- Update to 1.6.2 (#2120071)
- Add metainfo
- Fix summary

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 04 2022 Arthur Bols <arthur@bols.dev> - 1.6.1-1
- Initial package
