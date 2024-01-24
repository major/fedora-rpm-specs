%bcond tests 1

Name:           ansible-builder
Version:        3.0.0
Release:        3%{?dist}
Summary:        A tool for building Ansible Execution Environments

License:        Apache-2.0
URL:            https://ansible.readthedocs.io/projects/builder/en/stable/
Source:         %{pypi_source ansible-builder}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli+tomlkit
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytest-xdist}
%endif

%description
Using Ansible content that depends on non-default dependencies can be tricky.
Packages must be installed on each node, play nicely with other software
installed on the host system, and be kept in sync.

To help simplify this process, we have introduced the concept of Execution
Environments, which you can create with Ansible Builder.


%prep
%autosetup -p1
# Remove setuptools version pins. They're not needed in Fedora.
grep -q setuptools pyproject.toml
tomcli-set pyproject.toml list build-system.requires setuptools setuptools_scm


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ansible_builder


%check
%if %{with tests}
%pytest -n auto test/unit
%endif


%files -f %{pyproject_files}
# Note(gotmax23): Yes, pyproject_save_files and setuptools already handle
# this automatically, but I refuse to rely on it, as it makes it too easy to
# miss licenses when upstream changes their build system or something else.
%license LICENSE.md
%doc README.md
%doc docs/*.rst
%{_bindir}/ansible-builder


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Maxwell G <maxwell@gtmx.me> - 3.0.0-1
- Initial package. Closes rhbz#2247156.
