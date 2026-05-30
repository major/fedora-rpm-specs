%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff

Name:           diskimage-builder
Summary:        Image building tools for OpenStack
Version:        3.42.0
Release:        %autorelease
License:        Apache-2.0
Group:          System Environment/Base
URL:            https://launchpad.net/diskimage-builder
Source0:        https://tarballs.openstack.org/diskimage-builder/diskimage_builder-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/diskimage-builder/diskimage_builder-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildRequires: git-core
BuildRequires: python3-devel

BuildArch: noarch


%description
Components of TripleO that are responsible for building disk images.

%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

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
%global __requires_exclude %__requires_exclude|/sbin/openrc-run


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n diskimage_builder-%{version} -S git

%py3_shebang_fix ./diskimage_builder/elements/deploy-targetcli/extra-data.d/module/targetcli-wrapper

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

%pyproject_patch_dependency flake8:ignore
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency pylint:ignore
%pyproject_patch_dependency reno:ignore


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/%{name}/elements

cp -vr diskimage_builder/elements/ %{buildroot}%{_datadir}/%{name}

# explicitly remove config-applier since it does a pip install
rm -rf %{buildroot}%{_datadir}/%{name}/elements/config-applier

%pyproject_save_files -l diskimage_builder


%check
%tox


%files -f %{pyproject_files}
%{_bindir}/dib-lint
%{_bindir}/disk-image-create
%{_bindir}/diskimage-builder
%{_bindir}/ramdisk-image-create
%{_datadir}/%{name}/elements
%doc ChangeLog README.rst


%changelog
%autochangelog
