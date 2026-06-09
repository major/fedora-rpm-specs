%bcond tests 1

Name:           ansible-builder
Version:        3.1.1
Release:        %autorelease
Summary:        A tool for building Ansible Execution Environments

License:        Apache-2.0
URL:            https://ansible.readthedocs.io/projects/builder/en/stable/
Source:         %{pypi_source ansible_builder}

Patch:          0001-Fix-incorrect-pytest-mark-fixture-usage.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli+tomlkit
%if %{with tests}
BuildRequires:  %{py3_dist filelock}
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
%autosetup -p1 -n ansible_builder-%{version}
# Remove setuptools version upper version pins.
# They're not needed in Fedora.
grep -q setuptools pyproject.toml
tomcli-set pyproject.toml lists replace build-system.requires \
    '(setuptools.*), <=.+' '\1'


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
%autochangelog
