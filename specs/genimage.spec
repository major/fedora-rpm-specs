%global fs_block_tools %(cat <<EOF
cpio \\
e2fsprogs \\
erofs-utils \\
genext2fs \\
genisoimage \\
f2fs-tools \\
btrfs-progs \\
squashfs-tools \\
dosfstools \\
mtools \\
mdadm \\
qemu-img \\
mtd-utils \\
mtd-utils-ubi \\
uboot-tools
EOF)

# Exclude some fs tools until their tests can cope with newer features
# erofs-utils https://github.com/pengutronix/genimage/issues/309
# genextfs    https://github.com/pengutronix/genimage/issues/330
%global trim_fs_block_tools %{lua:
	tr = rpm.expand('%{fs_block_tools}')
	tr = string.gsub(tr,'genext2fs', '')
	tr = string.gsub(tr ,'erofs%-utils', '')
	print(tr)
}

Name:           genimage
Version:        19

Release:        %autorelease
Summary:        Flexible filesystem and disk image generator

License:        GPL-2.0-only
URL:            https://github.com/pengutronix/genimage/
Source0:        %{url}/releases/download/v%{version}/genimage-%{version}.tar.xz

Recommends:     %{trim_fs_block_tools}

# https://bugzilla.redhat.com/show_bug.cgi?id=2374067
ExcludeArch: s390x %{ix86}

BuildRequires:  autoconf automake
BuildRequires:  gcc
BuildRequires:  libconfuse-devel
BuildRequires:  libtool

BuildRequires:  coreutils
BuildRequires:  python3-docutils
# tests
BuildRequires:  fakeroot
BuildRequires:  %{trim_fs_block_tools}

%description
genimage is a tool to generate multiple filesystem and flash/disk
images from a given root filesystem tree. genimage is intended to 
be run in a fakeroot environment. 
It also supports creating flash/disk images out of different 
file-system images and files.

%prep
%autosetup -p1
autoreconf -fi


%build
%configure
%make_build
rst2man README.rst > %{name}.1

%install
%make_install
install -D -m644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%check
make check || ! cat test-suite.log

%files
%license COPYING
%doc README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
