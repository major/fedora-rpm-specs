%bcond_without tests

Name:       protontricks
Version:    1.13.1
Release:    %autorelease
Summary:    Simple wrapper that does winetricks things for Proton enabled games
BuildArch:  noarch

License:    GPL-3.0-or-later
URL:        https://github.com/Matoking/protontricks
# GitHub tarball won't work for setuptools-scm
Source0:    %{pypi_source %{name}}

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
%if %{with tests}
# https://github.com/Matoking/protontricks/blob/master/CHANGELOG.md#1120---2024-09-16
# BuildRequires: python3dist(vdf) >= 3.4
BuildRequires: python3dist(pytest-cov) >= 2.10
BuildRequires: python3dist(pytest) >= 6.0
%endif
Requires:   winetricks
Recommends: yad
Suggests:   zenity

%description
Run Winetricks commands for Steam Play/Proton games among other common Wine
features, such as launching external Windows executables.

This is a fork of the original project created by sirmentio. The original
repository is available at Sirmentio/protontricks.


%prep
%autosetup
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{name}
# Remove `protontricks-desktop-install`, since we already install .desktop
# files properly
# https://bugzilla.redhat.com/show_bug.cgi?id=1991684
rm %{buildroot}%{_bindir}/%{name}-desktop-install


%check
%if %{with tests}
%pyproject_check_import
%pytest
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}-launch
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop


%changelog
%autochangelog
