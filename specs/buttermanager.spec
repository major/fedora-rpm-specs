Name:           buttermanager
Version:        2.5.2
Release:        %autorelease
Summary:        Tool for managing Btrfs snapshots, balancing filesystems and more

License:        GPL-3.0-only
URL:            https://github.com/egara/buttermanager
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Requires:       btrfs-progs
Requires:       python3-tkinter
# Recommends:     grub2-btrfs

%description
ButterManager is a BTRFS tool for managing snapshots, balancing filesystems
and upgrading the system safely.

%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l buttermanager

install -Dpm644 packaging/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Fix the desktop file
sed \
  -e "s/Icon=.*/Icon=%{name}/" \
  -i packaging/%{name}.desktop

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  packaging/%{name}.desktop


%files -f %{pyproject_files}
%doc README.md doc
%{_bindir}/buttermanager
%{python3_sitelib}/buttermanager*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
%autochangelog
