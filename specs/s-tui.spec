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
Recommends: stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and
utilization in a graphical way from the terminal.


%prep
%autosetup
%generate_buildrequires
%pyproject_buildrequires

# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{sys_name}

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


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
