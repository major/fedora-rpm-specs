Summary:	Cloud image management utilities
Name:		cloud-utils
Version:	0.31
Release:	11%{?dist}
License:	GPLv3
URL:		https://launchpad.net/cloud-utils/

Source0:	https://launchpad.net/%{name}/trunk/0.31/+download/%{name}-%{version}.tar.gz

# Don't build the cloud-utils main package on EPEL architectures that don't
# have qemu-img. Which means we need to make it a no-noarch package for EPEL
# for this to work properly.
%define BuildMainPackage 1
%if 0%{?rhel}
# don't build debuginfo packages
%global	debug_package %{nil}
%ifarch	i686 ppc64
%define	BuildMainPackage 0
%endif
%else
BuildArch:	noarch
%endif

Requires:	cloud-utils-growpart
Requires:	gawk
Requires:	e2fsprogs
Requires:	file
Requires:	python3
Requires:	qemu-img
Requires:	util-linux

%description
This package provides a useful set of utilities for managing cloud images.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.


%package growpart
Summary:	Script for growing a partition

Requires:	gawk
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk
Requires:	util-linux


%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.


%prep
%setup -q

%build

%install

# Create the target directories
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

%if %{BuildMainPackage}
# Install binaries and manpages
cp bin/* $RPM_BUILD_ROOT/%{_bindir}/
cp man/* $RPM_BUILD_ROOT/%{_mandir}/man1/

# Exclude Ubuntu-specific tools
rm $RPM_BUILD_ROOT/%{_bindir}/*ubuntu*

# Exclude the cloud-run-instances manpage
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/cloud-run-instances.*

# Exclude euca2ools wrappers and manpages
rm -f $RPM_BUILD_ROOT/%{_bindir}/cloud-publish-*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/cloud-publish-*
%endif

# Install the growpart binary and man page
cp bin/growpart $RPM_BUILD_ROOT/%{_bindir}/
cp man/growpart.* $RPM_BUILD_ROOT/%{_mandir}/man1/


# Files for the main package
%if %{BuildMainPackage}
%files
%doc ChangeLog
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/cloud-localds
%{_bindir}/write-mime-multipart
%{_bindir}/ec2metadata
%{_bindir}/resize-part-image
%{_bindir}/mount-image-callback
%{_bindir}/vcs-run
%doc %{_mandir}/man1/resize-part-image.*
%doc %{_mandir}/man1/write-mime-multipart.*
%doc %{_mandir}/man1/cloud-localds.*
%endif


# Files for the growpart subpackage
%files growpart
%doc ChangeLog
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Juerg Haefliger <juergh@gmail.com> - 0.31-5
- Bump the release number to differentiate from the previous version which didn't build.

* Thu Oct 24 2019 Juerg Haefliger <juergh@gmail.com> - 0.31-4
- Drop euca2ools dependency (retired package) and wrapper scripts [bz#1762325].

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Juerg Haefliger <juergh@gmail.com> - 0.31-2
- Add new cloud-utils-0.31.tar.gz sources.

* Mon Mar 18 2019 Juerg Haefliger <juergh@gmail.com> - 0.31-1
- Requires python3 instead of python2 [bz#1530224].
- Drop python2-paramiko dependency (no longer required).
- Drop cloud-run-instances manpage (script no longer included).
- Rebase to upstream release 0.31
- mount-image-callback: mount with -o 'rw' or -o 'ro' (LP: #1663722)
- mount-image-callback: run blockdev and udevadm settle on nbd devices. (LP: #1741096, 1741300)
- mount-image-callback: Drop support for mounting lxd containers. (LP: #1715994)
- growpart: fix bug that stopped GPT disks from being grown past 2TB. (LP: #1762748)
- mount-image-callback: mention --help and -C/--cd-mountpoint in Usage
- growpart: fix bug when resizing a middle partition with sgdisk (LP: #1706751) [Fred De Backer]
- growpart: Resolve symbolic links before operating. [Kevin Locke] (LP: #1744406)
- growpart: fix bug occurring if start sector and size were the same. [Lars Kellogg-Stedman] (LP: #1807171)
- debian/control: drop Suggests on lxc1
- debian/tests/control: add test growpart-start-matches-size.
- White space cleanup.  Remove trailing space and tabs.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.30-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 0.30-1
- Rebase to upstream release 0.30
- Resolves RHBZ#1515835 - growpart fails to resize partition on aarch64
- Remove patches in spec file because they are already available in 0.30
- Fix rpmlint issues on spec file
- Remove LICENSE file, already shipped with 0.30 source tar
- cloud-run-instances binary has been dropped in 0.28
- mount-image-callback and vcs-run binaries has been introduced in 0.28

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Adam Williamson <awilliam@redhat.com> - 0.27-16
- backport fix for RHBZ #1327337 (growpart fail with newer util-linux-ng)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Juerg Haefliger <juergh@gmail.com> - 0.27-13
- [1197894] sfdisk dropped --show-pt-geometry option

* Fri Jul 11 2014 Tom Callaway <spot@fedoraproject.org> - 0.27-12
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-10
- [966574] growpart spits out a non-fatal error

* Fri Aug 16 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-9
- Prevent building of debuginfo packages.
- Fix 32-bit arch type.

* Fri Aug 16 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-8
- Make the package a no-noarch package on EPEL so that the build of the main
  package can be prevented for the arches that don't support it [bz#986809].

* Tue Aug 06 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-7
- Build the growpart subpackage on all EPEL architectures [bz#986809].

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-5
- Don't make gdisk a hard requirement for cloud-utils-growpart to save some
  space on systems that don't use GPT partitions.

* Mon Jun 17 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-4
- Break out the growpart script into its own subpackage to prevent pulling a
  boatload of unnecessary dependencies into a cloud image.

* Mon Apr  8 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-3
- 3rd attempt to fix the spec file to only build on x86_64 for EPEL.

* Fri Apr  5 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-2
- Yet another spec file fix to only build on x86_64 for EPEL.

* Tue Apr  2 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-1
- Update to upstream release 0.27.
- Fix spec file to only build on x86_64 for EPEL.

* Tue Feb 12 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-0.2.bzr216
- Add GPL-3 license.
- Exclude Ubuntu-specific tools.
- Fix some spec file issues per reviewers comments.

* Tue Feb  5 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-0.1.bzr216
- Initial build based on upstream revision bzr216.
