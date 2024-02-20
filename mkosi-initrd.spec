%global commit 6ba68f17cbf075a48fbf4008555baf4b261eeafc
%global shortcommit %(c=%commit; echo ${c:0:7})
%global commitdate 20230506

Name:           mkosi-initrd
Version:        0~%{commitdate}g%{shortcommit}
Release:        %autorelease
Summary:        Generator for initrd images using distro packages

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi-initrd
Source0:        %{url}/archive/%{commit}/mkosi-initrd-%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       mkosi
Requires:       rpm
Requires:       dnf5 or dnf
Requires:       dnf5-command(download) or dnf-command(download)
Requires:       cpio
Requires:       python3dist(pyxattr)

%description
This is a generator for initrd images (cpio archives compressed with zstd).
The initrd is created by downloading rpms and installing them into a temporary
location. This is different than the usual approach, where files from the host
are used. In the initrd, only systemd is used, and no special runtime is used.
This means that only things which are supported by normal packages will work.

The package provides a kernel-install plugin that will automatically create an
initrd during kernel package installation. This initrd will then be picked up by
kernel-install and used in the Boot Loader Specification entry.

Initrds created in this way support some common machine types, but no more:
- plain partitions
- LVM2
- LUKS

%prep
%autosetup -n %{name}-%{commit}

%global pkgroot %{_prefix}/lib/mkosi-initrd

%install
install -Dt %{buildroot}%{pkgroot} mkosi.finalize
install -Dt %{buildroot}%{pkgroot} -m 0644 fedora.mkosi
install -Dt %{buildroot}%{_prefix}/lib/kernel/install.d/ kernel-install/50-mkosi-initrd.install

%files
%license LICENSE.LGPL2.1
%doc README.md
%doc docs/fedora.md
%pkgroot/mkosi.finalize
%pkgroot/fedora.mkosi
/usr/lib/kernel/install.d/50-mkosi-initrd.install

%changelog
%autochangelog
