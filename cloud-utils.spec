Summary:	Cloud image management utilities
Name:		cloud-utils
Version:	0.33
Release:	%autorelease
License:	GPL-3.0-only
URL:		https://github.com/canonical/%{name}

Source:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	%{name}-growpart
Requires:	python3
Requires:	util-linux
# cloud-localds
Recommends:	tar
Recommends:	dosfstools
Recommends:	mtools
Recommends:	genisoimage
# cloud-localds & mount-image-callback
Recommends:	qemu-img
# resize-part-image
Requires:	file
Requires:	gzip
Requires:	e2fsprogs
# resize-part-image & mount-image-callback
Requires:	gawk
# vcs-run
Recommends:	breezy
Recommends:	git-core
Recommends:	mercurial
Recommends:	wget

%description
This package provides a useful set of utilities for managing cloud images.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.


%package growpart
Summary:	Script for growing a partition

Requires:	gawk
Requires:	util-linux
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
Recommends:	gdisk
Recommends:	lvm2


%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.


%prep
%setup -q

%build

%install

# Create the target directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

# Install binaries and manpages
install -pm 0755 bin/* %{buildroot}%{_bindir}/
install -pm 0644 man/* %{buildroot}%{_mandir}/man1/

# Exclude Ubuntu-specific tools
rm %{buildroot}%{_bindir}/*ubuntu*

# Exclude the cloud-run-instances manpage
rm -f %{buildroot}%{_mandir}/man1/cloud-run-instances.*

# Exclude euca2ools wrappers and manpages
rm -f %{buildroot}%{_bindir}/cloud-publish-*
rm -f %{buildroot}%{_mandir}/man1/cloud-publish-*


# Files for the main package
%files
%doc ChangeLog
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


# Files for the growpart subpackage
%files growpart
%doc ChangeLog
%license LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*


%changelog
%autochangelog
