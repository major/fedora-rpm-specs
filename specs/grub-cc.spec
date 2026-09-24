%global _enable_debug_packages 0

#
# Arch variables
#
%ifarch aarch64
%global efiarch aa64
%global grub_target_name arm64-efi
%global package_arch efi-aa64
%endif

%ifarch x86_64
%global efiarch x64
%global grub_target_name x86_64-efi
%global package_arch efi-x64
%endif

#
# Get version/release from GRUB's efi package required for sbat generation
#
%global grub_version %{expand:%%(\\\
	if rpm -q grub2-%{package_arch} >/dev/null 2>&1; then \\\
		rpm -q grub2-%{package_arch} | rpmsort | tail -1 \\\
		| xargs rpm -q --qf '%{version}'; \\\
	else \\\
		echo 0; \\\
	fi)}
%global grub_release %{expand:%%(\\\
	if rpm -q grub2-%{package_arch} >/dev/null 2>&1; then \\\
		rpm -q grub2-%{package_arch} | rpmsort | tail -1 \\\
		| xargs rpm -q --qf '%{release}'; \\\
	else \\\
		echo 0; \\\
	fi)}

#
# Set the directory wher the image would be installed
# e.g. grub_dir = /usr/lib/efi/grub-cc/1:2.12-74.fc45/EFI/fedora
# it is a long path but it is consistent with GRUB package
#

#
# For each subfolder, define a variable so %%install & %%files can properly definine them
# Final path would look like /usr/lib/efi/grub-cc/1:2.12-74.fc45/EFI/fedora
#
%global _libdir %{_exec_prefix}/lib
%global grub_efi_dir %{_libdir}/efi
%global grub_name_dir %{grub_efi_dir}/%{name}
%global grub_evr_dir %{grub_name_dir}/%{epoch}:%{version}-%{release}
%global grub_uppercase_efi_dir %{grub_evr_dir}/EFI
%global grub_dir %{grub_uppercase_efi_dir}/%{efi_vendor}

%global grub_modules  " \\\
	all_video \\\
	blscfg \\\
	blsuki	\\\
	boot \\\
	btrfs \\\
	configfile \\\
	echo \\\
	ext2 \\\
	f2fs \\\
	fat \\\
	gfxmenu \\\
	gfxterm \\\
	hfsplus \\\
	http \\\
	increment \\\
	iso9660	\\\
	jpeg \\\
	linux \\\
	mdraid09 \\\
	mdraid1x \\\
	memdisk \\\
	net \\\
	normal \\\
	part_apple \\\
	part_gpt \\\
	part_msdos \\\
	pgp \\\
	serial \\\
	sleep \\\
	squash4 \\\
	test \\\
	tftp \\\
	version \\\
	video \\\
	xfs "

%global efi_modules " efifwsetup  bli "

%ifarch x86_64
%global platform_modules " chain tpm usb usbserial_common usbserial_pl2303 usbserial_ftdi usbserial_usbdebug keylayouts at_keyboard "
%endif

%ifarch aarch64
%global platform_modules " "
%endif

Name:		grub-cc

# Epoch should match the one for standard grub2 package so in case the latter changes
# this must be bumped and keep it synced all time
Epoch:		1

Version:	1
Release:	%autorelease
Summary:	Grub image for use in confidential computing

# As in the Epoch, the License must match the grub2's one
License:	GPL-3.0-or-later

URL:		http://www.gnu.org/software/grub/

ExclusiveArch:	aarch64 x86_64

BuildRequires:	coreutils
BuildRequires:	efi-srpm-macros
BuildRequires:	findutils
BuildRequires:	git
BuildRequires:	grub2-efi-%{efiarch}
BuildRequires:	grub2-efi-%{efiarch}-modules
BuildRequires:	grub2-tools
BuildRequires:	pesign
BuildRequires:	rpm
BuildRequires:	sed
BuildRequires:	squashfs-tools

Source0:	sbat.csv.in
Source1:	grub_prefix_embedded.cfg
Source2:	grub.cfg


%description
GRUB image intended for Confidential Computing Environments.

%prep
%autosetup -S git -T -c

%build

sed -e 's,@@VERSION@@,%{grub_version},g' \
    -e 's,@@VERSION_RELEASE@@,%{grub_version}-%{grub_release},g' \
    < '%{SOURCE0}' > sbat.csv

mkdir -p memdisk/fonts memdisk/grub2
cp /usr/share/grub/unicode.pf2 memdisk/fonts
cp %{SOURCE2} memdisk/grub2/grub.cfg
mksquashfs memdisk memdisk.squashfs -comp lzo

GRUB_MODULES+=%{grub_modules}
GRUB_MODULES+=%{efi_modules}
GRUB_MODULES+=%{platform_modules}

grub2-mkimage \
	-O %{grub_target_name} \
	-o grub%{efiarch}.efi.orig \
	-d /usr/lib/grub/%{grub_target_name} \
	--disable-tpm-string-pcr \
	--package-string "GRUB CC %{grub_version}-%{grub_release}" \
	--sbat sbat.csv \
	-m memdisk.squashfs \
	-c '%{SOURCE1}' \
	-p /EFI/%{efi_vendor} \
	${GRUB_MODULES}

%pesign -s -i grub%{efiarch}.efi.orig -o grub%{efiarch}.efi

%install
set -e
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_efi_dir}/
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_name_dir}/
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_evr_dir}/
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_uppercase_efi_dir}/
install -d -m 0700 ${RPM_BUILD_ROOT}%{grub_dir}/
install -m 700 grub%{efiarch}.efi ${RPM_BUILD_ROOT}%{grub_dir}/grub%{efiarch}.efi

%files
%dir %attr(0755,root,root) %{grub_efi_dir}
%dir %attr(0755,root,root) %{grub_name_dir}
%dir %attr(0755,root,root) %{grub_evr_dir}
%dir %attr(0755,root,root) %{grub_uppercase_efi_dir}
%dir %attr(0700,root,root) %{grub_dir}
%attr(0700,root,root) %{grub_dir}/grub%{efiarch}.efi

%changelog
%autochangelog
