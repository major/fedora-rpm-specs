Name:           mkosi14
Version:        14
Release:        %autorelease
Summary:        Create bespoke OS images

License:        LGPLv2+
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}/mkosi-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  binutils
BuildRequires:  python3dist(pexpect)

%global recoreq %{?el7:Requires}%{!?el7:Recommends}

%{recoreq}:     dnf
%{recoreq}:     gnupg
%{recoreq}:     xz
%{recoreq}:     tar
%{recoreq}:     e2fsprogs
%{recoreq}:     squashfs-tools
%{recoreq}:     veritysetup
%{recoreq}:     binutils
%if 0%{?el7} == 0
Recommends:     debootstrap
Recommends:     arch-install-scripts
Recommends:     edk2-ovmf
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     cpio
Recommends:     zstd
Recommends:     python3dist(argcomplete)
Recommends:     python3dist(cryptography)
Recommends:     python3dist(pexpect)
%endif

%description
A fancy wrapper around "dnf --installroot", "debootstrap", "pacman", "zypper",
"emerge", and "swupd-extract" that may generate disk images with a number of
bells and whistles.

Generated images are tailored to the purose. This means GPT disk labels are used
by default, though MBR disk labels are supported, and only systemd based images
may be generated.

%prep
%autosetup -p1 -n mkosi-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%_bindir/mkosi
%{python3_sitelib}/mkosi/
%{python3_sitelib}/mkosi-%{version}-py*.egg-info/
%_mandir/man1/mkosi.1*

%check
%pytest tests/ -v \
  --ignore=tests/test_config_parser.py \
  -k 'not test_copy_file'

# just a smoke test for syntax or import errors
%buildroot/usr/bin/mkosi --help >/dev/null

%changelog
%autochangelog
