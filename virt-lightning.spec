%global srcname virt-lightning
%global libname virt_lightning

%global common_description %{expand:
A CLI to start local Cloud image on libvirt!

Virt-Lightning can quickly deploy a bunch of new VM. It also prepares the
Ansible inventory file!

This is handy to quickly validate a new Ansible playbook, or a role on a large
number of environments.}

Name:           %{srcname}
Version:        2.2.0
Release:        %autorelease
Summary:        A pure-Python implementation of the HTTP/2 priority tree

License:        Apache-2.0
URL:            https://virt-lightning.org
VCS:            https://github.com/virt-lightning/virt-lightning
Source0:        %{pypi_source virt-lightning}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Requires:       libvirt-daemon

%description %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE-2.0.txt
%doc DEBUGGING.md README.md changelog.md conf/example.ini
%{_bindir}/virt-lightning
%{_bindir}/vl

%changelog
%autochangelog
