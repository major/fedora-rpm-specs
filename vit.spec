Name:           vit
Version:        2.2.0
Release:        %autorelease
Summary:        Visual Interactive Taskwarrior full-screen terminal interface


License:        MIT
URL:            https://github.com/scottkosty/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  task
Requires:       task

%{?python_provide:%python_provide python3-vit}

%description
Features:
- Fully-customizable key bindings (default Vim-like)
- Uncluttered display
- No mouse
- Speed
- Per-column colorization
- Advanced tab completion
- Multiple/customizable themes
- Override/customize column formatters
- Intelligent sub-project indenting


%prep
%autosetup
rm -rf vit.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
find vit/ -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vit

# Install bashcompletion
install -m 0644 -p -D -t  $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/vit/ scripts/bash/%{name}.bash_completion

%check
LC_ALL=C PYTHONPATH=. %{__python3} -m unittest

%files -f %{pyproject_files}
%doc README.md CUSTOMIZE.md COLOR.md DEVELOPMENT.md UPGRADE.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
