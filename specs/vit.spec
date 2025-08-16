Name:           vit
%global forgeurl https://github.com/scottkosty/%{name}
Version:        2.3.3
Release:        %autorelease
Summary:        Visual Interactive Taskwarrior full-screen terminal interface

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man

# use the newest task release
BuildRequires:  (task >= 3 or task2)
# either of these will do, depends on the user
Requires:       (task >= 3 or task2)

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
install -m 0644 -p -D -T scripts/bash/%{name}.bash_completion $RPM_BUILD_ROOT/%{bash_completions_dir}/vit

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

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
%pretrans -p <lua>

path = "%{bash_completions_dir}/vit"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%files -f %{pyproject_files}
%doc README.md CUSTOMIZE.md COLOR.md DEVELOPMENT.md UPGRADE.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{_mandir}/man1/vit*
%ghost %{bash_completions_dir}/%{name}.rpmmoved

%changelog
%autochangelog
