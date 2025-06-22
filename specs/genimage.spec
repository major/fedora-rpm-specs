%global commit 3bfee1fe3f69e15b38969bcf087d394f6d1ae9fe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global fs_block_tools %(cat <<EOF
e2fsprogs \\
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
erofs-utils \\
uboot-tools \\
erofs-utils
EOF)

Name:           genimage
Version:        18^20250620.g%{shortcommit}

Release:        %autorelease
Summary:        Flexible filesystem and disk image generator

License:        GPL-2.0-only
URL:            https://github.com/pengutronix/genimage/
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

Recommends:     %{fs_block_tools}

# https://bugzilla.redhat.com/show_bug.cgi?id=2374067
ExcludeArch: s390x

BuildRequires:  autoconf automake
BuildRequires:  gcc
BuildRequires:  libconfuse-devel
BuildRequires:  libtool

BuildRequires:  coreutils
BuildRequires:  python3-docutils
# tests
BuildRequires:  fakeroot
BuildRequires:  %{fs_block_tools}

%description
genimage is a tool to generate multiple filesystem and flash/disk
images from a given root filesystem tree. genimage is intended to 
be run in a fakeroot environment. 
It also supports creating flash/disk images out of different 
file-system images and files.

%prep
%autosetup -n %{name}-%{commit} -p1
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
