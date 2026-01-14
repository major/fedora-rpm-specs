%global sys_name s_tui

Name:       s-tui
Version:    1.3.0
Release:    %autorelease
Summary:    Terminal-based CPU stress and monitoring utility
BuildArch:  noarch

License:    GPL-2.0-or-later
URL:        https://github.com/amanusk/s-tui
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)

Recommends: stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and
utilization in a graphical way from the terminal.


%prep
%autosetup

# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,sources,sturwid}/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{sys_name}/


%changelog
%autochangelog
