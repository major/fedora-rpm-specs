%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           diskimage-builder
Summary:        Image building tools for OpenStack
Version:        3.24.0
Release:        2%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://launchpad.net/diskimage-builder
Source0:        https://tarballs.openstack.org/diskimage-builder/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/diskimage-builder/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
AutoReqProv: no

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires: kpartx
Requires: qemu-img
Requires: curl
Requires: tar
Requires: gdisk
Requires: lvm2
Requires: git-core
Requires: dib-utils
Requires: /usr/sbin/mkfs.ext2
Requires: /usr/sbin/mkfs.ext3
Requires: /usr/sbin/mkfs.ext4
Requires: /usr/sbin/mkfs.xfs
Requires: /usr/sbin/mkfs.vfat
Requires: /bin/bash
Requires: /bin/sh
Requires: /usr/bin/env
Requires: python3
Requires: python3-flake8 >= 3.6.0
Requires: python3-pbr >= 2.0.0
Requires: python3-stevedore >= 1.20.0
Requires: python3-networkx >= 2.3.0
Requires: python3-yaml >= 3.12

%global __requires_exclude /usr/local/bin/dib-python
%global __requires_exclude %__requires_exclude|/sbin/runscript

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# Remove bundled egg-info
rm -r diskimage_builder.egg-info

%build
%{py3_build}

%install
%{py3_install}

mkdir -p %{buildroot}%{_datadir}/%{name}/elements

cp -vr diskimage_builder/elements/ %{buildroot}%{_datadir}/%{name}

# explicitly remove config-applier since it does a pip install
rm -rf %{buildroot}%{_datadir}/%{name}/elements/config-applier

# This file is being split out of diskimage-builder, so remove it to
# avoid conflicts with the new package.
rm -f %{buildroot}%{_bindir}/dib-run-parts

# Fix shebangs for Python 3-only distros
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/elements/pypi/pre-install.d/04-configure-pypi-mirror
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/elements/deploy-targetcli/extra-data.d/module/targetcli-wrapper
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/elements/package-installs/bin/package-installs-squash
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/elements/svc-map/extra-data.d/10-merge-svc-map-files
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}/elements/svc-map/bin/svc-map
%py3_shebang_fix %{buildroot}%{python3_sitelib}/diskimage_builder/elements/pypi/pre-install.d/04-configure-pypi-mirror
%py3_shebang_fix %{buildroot}%{python3_sitelib}/diskimage_builder/elements/deploy-targetcli/extra-data.d/module/targetcli-wrapper
%py3_shebang_fix %{buildroot}%{python3_sitelib}/diskimage_builder/elements/package-installs/bin/package-installs-squash
%py3_shebang_fix %{buildroot}%{python3_sitelib}/diskimage_builder/elements/svc-map/extra-data.d/10-merge-svc-map-files
%py3_shebang_fix %{buildroot}%{python3_sitelib}/diskimage_builder/elements/svc-map/bin/svc-map

%description
Components of TripleO that are responsible for building disk images.

%files
%doc LICENSE
%{_bindir}/*
%{python3_sitelib}/diskimage_builder*
%{_datadir}/%{name}/elements

%changelog
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

