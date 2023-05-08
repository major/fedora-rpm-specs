%bcond_with tests

Name:       protontricks
Version:    1.10.3
Release:    %autorelease
Summary:    Simple wrapper that does winetricks things for Proton enabled games
BuildArch:  noarch

License:    GPLv3+
URL:        https://github.com/Matoking/protontricks

# GitHub tarball won't work for setuptools-scm
Source0:    %{pypi_source %{name}}

BuildRequires: desktop-file-utils
BuildRequires: python3-devel > 3.6
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(vdf) >= 3.4
%if %{with tests}
BuildRequires: python3dist(pytest-cov) >= 2.10
BuildRequires: python3dist(pytest) >= 6.0
%endif

Requires:   winetricks

Recommends: yad

Suggests:   zenity


%description
A simple wrapper that does winetricks things for Proton enabled games,
requires Winetricks.

This is a fork of the original project created by sirmentio. The original
repository is available at Sirmentio/protontricks.


%prep
%autosetup


%build
%py3_build


%install
%py3_install

# Remove `protontricks-desktop-install`, since we already install .desktop
# files properly
# https://bugzilla.redhat.com/show_bug.cgi?id=1991684
rm %{buildroot}%{_bindir}/%{name}-desktop-install


%if %{with tests}
%check
%{python3} -m pytest -v
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}-launch
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*.egg-info


%changelog
%autochangelog
