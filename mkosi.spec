Name:           mkosi
Version:        15.1
Release:        %autorelease
Summary:        Create bespoke OS images

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  binutils
BuildRequires:  python3dist(pexpect)
BuildRequires:  pandoc
# for tests
BuildRequires:  systemd

%global recoreq %{?el7:Requires}%{!?el7:Recommends}

%bcond tests 1

# mkosi wants the uncompressed man page to show via 'mkosi documentation'
%global __brp_compress true

Requires:       bubblewrap
Requires:       systemd-repart

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
Recommends:     (dnf5 or dnf)
%else
Recommends:     dnf
%endif

%description
A fancy wrapper around "dnf --installroot", "debootstrap", "pacman", "zypper",
"emerge", and "swupd-extract" that may generate disk images with a number of
bells and whistles.

Generated images are tailored to the purpose. This means GPT disk labels are
used and only systemd-based images may be generated.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
tools/make-man-page.sh

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mkosi

mkdir -p %{buildroot}%{_mandir}/man1
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/mkosi.1

%files -f %pyproject_files
%license LICENSE
%doc README.md
%_bindir/mkosi
%_mandir/man1/mkosi.1*

%check
%if %{with tests}
%pytest tests/ -v

# just a smoke test for syntax or import errors
%py3_test_envvars %{buildroot}%{_bindir}/mkosi --help >/dev/null
%endif

%changelog
%autochangelog
