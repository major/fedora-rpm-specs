# Created by pyp2rpm-3.3.6
%global pypi_name virt-lightning

Name:           %{pypi_name}
Version:        2.1.0
Release:        5%{?dist}
Summary:        Deploy your testing VM in a couple of seconds

License:        ASL 2.0
URL:            https://virt-lightning.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(libvirt-python)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(urwid)
Requires:       libvirt-daemon

%description
A CLI to start local Cloud image on libvirt!

Virt-Lightning can quickly deploy a bunch of new VM. It also prepares the
Ansible inventory file!

This is handy to quickly validate a new Ansible playbook, or a role on a large
number of environments.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove shebang from Python libraries
for lib in virt_lightning/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py3_build

%install
%py3_install

%check
%pytest

%files
%license LICENSE-2.0.txt
%doc DEBUGGING.md README.md changelog.md conf/example.ini
%{_bindir}/virt-lightning
%{_bindir}/vl
%{python3_sitelib}/virt_lightning
%{python3_sitelib}/virt_lightning-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 19:46:23 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- Initial package.
- Close: rhbz#1965791
