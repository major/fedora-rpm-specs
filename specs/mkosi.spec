Name:           mkosi
Version:        25.2
Release:        %autorelease
Summary:        Create bespoke OS images

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  pandoc

%bcond tests 1

# mkosi wants the uncompressed man page to show via 'mkosi documentation'
%global __brp_compress true

Requires:       python3
Requires:       coreutils

# for various image building tools (systemd-hwdb, systemd-sysusers, ...)
Recommends:     systemd

# for systemd-nspawn
Recommends:     systemd-container >= 254

# for bootable images (systemd-udev ships bootctl)
Recommends:     systemd-udev >= 254
Recommends:     systemd-ukify >= 254

# for disk images
Recommends:     systemd-repart >= 254

# for signing
Recommends:     openssl
Recommends:     sbsigntools
Recommends:     gnupg

# for building specific distributions
Recommends:     (dnf5 or dnf)
Recommends:     apt
Recommends:     debian-keyring
Recommends:     pacman
Recommends:     archlinux-keyring
Recommends:     zypper

# for various filesystems
Recommends:     btrfs-progs
Recommends:     e2fsprogs
Recommends:     dosfstools
Recommends:     mtools
Recommends:     erofs-utils
Recommends:     xfsprogs
Recommends:     squashfs-tools

# for various output formats
Recommends:     cpio
Recommends:     tar

# for mkosi qemu
Recommends:     qemu-kvm-core
Recommends:     edk2-ovmf
Recommends:     swtpm

# for mkosi ssh
Recommends:     openssh-clients
Recommends:     socat

# for output compression
Recommends:     zstd
Recommends:     xz

%description
A fancy wrapper around "dnf --installroot", "apt", "pacman", and "zypper" that
generates disk images with a number of bells and whistles.

Generated images are tailored to the purpose: GPT partitions,
systemd-boot or grub2, images for containers, VMs, initrd, and extensions.

Mkosi can boot an image via QEMU or systemd-nspawn, or simply start a shell in
chroot, burn the image to a device, connect to a running VM via ssh, extract
logs and coredumps, serve an image over HTTP and more.

See https://mkosi.systemd.io/ for documentation.

%package initrd
Summary:       Build initrds locally using mkosi
Requires:      %{name} = %{version}-%{release}
Requires:      (dnf5 or dnf)

%description initrd
This package provides the CLI and the plugin for kernel-install to build
initrds with mkosi locally.

After the package is installed, the plugin can be enabled by writing
'initrd_generator=mkosi-initrd' to '/etc/kernel/install.conf'.

%package addon
Summary:       Build PE addons locally using mkosi
Requires:      %{name} = %{version}-%{release}

%description addon
This package provides the CLI and the plugin for kernel-install to build
PE addons for distribution-signed unified kernel images with mkosi locally.

After the package is installed, the plugin can be enabled by adding
configuration for the addon to `/etc/mkosi-addon` or `/run/mkosi-addon`.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
tools/make-man-page.sh

%pyproject_wheel

bin/mkosi completion bash >mkosi.bash
bin/mkosi completion fish >mkosi.fish
bin/mkosi completion zsh >mkosi.zsh

%install
%pyproject_install
%pyproject_save_files mkosi

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.1
ln -s -t %{buildroot}%{_mandir}/man7/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.news.7
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-sandbox.1
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-initrd.1
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-addon.1

# Install the kernel-install plugins

install -Dt %{buildroot}%{_prefix}/lib/kernel/install.d/ \
         kernel-install/50-mkosi.install
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-initrd
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-initrd

install -Dt %{buildroot}%{_prefix}/lib/kernel/install.d/ \
         kernel-install/51-mkosi-addon.install
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-addon
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-addon

# Install shell completions
install -m0644 -D mkosi.bash %{buildroot}%{bash_completions_dir}/mkosi
install -m0644 -D mkosi.fish %{buildroot}%{fish_completions_dir}/mkosi.fish
install -m0644 -D mkosi.zsh %{buildroot}%{zsh_completions_dir}/_mkosi

%files -f %pyproject_files
%license LICENSES/GPL-2.0-only.txt
%license LICENSES/LGPL-2.1-or-later.txt
%license LICENSES/OFL-1.1.txt
%license LICENSES/PSF-2.0.txt
%doc README.md
%_bindir/mkosi
%_bindir/mkosi-sandbox
%_mandir/man1/mkosi.1*
%_mandir/man7/mkosi.news.7*
%_mandir/man1/mkosi-sandbox.1*
%{bash_completions_dir}/mkosi
%{fish_completions_dir}/mkosi.fish
%{zsh_completions_dir}/_mkosi

%files initrd
%_bindir/mkosi-initrd
%_mandir/man1/mkosi-initrd.1*
%_prefix/lib/kernel/install.d/50-mkosi.install
%ghost %dir %{_prefix}/lib/mkosi-initrd
%ghost %dir %{_sysconfdir}/mkosi-initrd

%files addon
%_bindir/mkosi-addon
%_mandir/man1/mkosi-addon.1*
%_prefix/lib/kernel/install.d/51-mkosi-addon.install
%ghost %dir %{_prefix}/lib/mkosi-addon
%ghost %dir %{_sysconfdir}/mkosi-addon

%check
%if %{with tests}
%pytest tests/ -v

# just a smoke test for syntax or import errors
%py3_test_envvars %{buildroot}%{_bindir}/mkosi --help >/dev/null
%endif

%changelog
%autochangelog
