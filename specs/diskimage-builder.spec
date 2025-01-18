%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate sphinx openstackdocstheme yamllint pylint

Name:           diskimage-builder
Summary:        Image building tools for OpenStack
Version:        3.34.0
Release:        2%{?dist}
License:        Apache-2.0
Group:          System Environment/Base
URL:            https://launchpad.net/diskimage-builder
Source0:        https://tarballs.openstack.org/diskimage-builder/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/diskimage-builder/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

Requires: kpartx
Requires: qemu-img
Requires: curl
Requires: tar
Requires: gdisk
Requires: lvm2
Requires: git-core
Requires: /usr/bin/guestfish
Requires: /usr/sbin/mkfs.ext2
Requires: /usr/sbin/mkfs.ext3
Requires: /usr/sbin/mkfs.ext4
Requires: /usr/sbin/mkfs.xfs
Requires: /usr/sbin/mkfs.vfat
Requires: /bin/bash
Requires: /bin/sh
Requires: /usr/bin/env

%global __requires_exclude /usr/local/bin/dib-python
%global __requires_exclude %__requires_exclude|/sbin/runscript

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

%py3_shebang_fix ./diskimage_builder/elements/deploy-targetcli/extra-data.d/module/targetcli-wrapper


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/%{name}/elements

cp -vr diskimage_builder/elements/ %{buildroot}%{_datadir}/%{name}

# explicitly remove config-applier since it does a pip install
rm -rf %{buildroot}%{_datadir}/%{name}/elements/config-applier

# This file is being split out of diskimage-builder, so remove it to
# avoid conflicts with the new package.
rm -f %{buildroot}%{_bindir}/dib-run-parts


%description
Components of TripleO that are responsible for building disk images.

%files
%doc LICENSE
%{_bindir}/*
%{python3_sitelib}/diskimage_builder*
%{_datadir}/%{name}/elements

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 07 2024 Joel Capitao <jcapitao@redhat.com> 3.34.0-1
- Update to upstream version 3.34.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.32.0-3
- Rebuilt for Python 3.13

* Mon May 06 2024 Alfredo Moralejo <amoralej@redhat.com> 3.32.0-2
- Skip flake8 as runtime requirement. (rhbz#2279292)

* Mon May 06 2024 Alfredo Moralejo <amoralej@redhat.com> 3.32.0-1
- Update to upstream version 3.32.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Alfredo Moralejo <amoralej@gmail.com> 3.31.0-2
- Remove cap on flake8 (rhbz#2246609)

* Wed Oct 25 2023 Alfredo Moralejo <amoralej@gmail.com> 3.31.0-1
- Update to upstream version 3.31.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Karolina Kula <kkula@redhat.com> 3.26.0-1
- Update to upstream version 3.26.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 3.24.0-1
- Update to upstream version 3.24.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Joel Capitao <jcapitao@redhat.com> 3.20.1-1
- Update to upstream version 3.20.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 3.7.0-1
- Update to upstream version 3.7.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.3.1-2
- Update to upstream version 3.3.1

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.3.1-1
- Update to upstream version 3.3.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 2.36.0-1
- Update to upstream version 2.36.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 RDO <dev@lists.rdoproject.org> 2.27.2-1
- Update to 2.27.2

