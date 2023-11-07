Name:           vit
%global forgeurl https://github.com/scottkosty/%{name}
Version:        2.3.2
Release:        %autorelease
Summary:        Visual Interactive Taskwarrior full-screen terminal interface

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man
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
%forgesetup
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

# generate man pages
for binary in "vit"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done
%check
LC_ALL=C PYTHONPATH=. %{__python3} -m unittest

%files -f %{pyproject_files}
%doc README.md CUSTOMIZE.md COLOR.md DEVELOPMENT.md UPGRADE.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/vit*

%changelog
%autochangelog
