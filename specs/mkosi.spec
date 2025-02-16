Name:           mkosi
Version:        25.3
Release:        %autorelease
Summary:        Create bespoke OS images

License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi
Source:         https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%bcond tests 1

# Build with OBS-specific quirks
%bcond obs 0

# mkosi wants the uncompressed man page to show via 'mkosi documentation'
%global __brp_compress true

BuildRequires:  pandoc
%if %{undefined suse_version}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest
Requires:       python3
Requires:       coreutils
%else
%define pythons python3
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3 >= 3.9
%endif

%if %{with obs}
Requires:       %{name}-system-deps = %{version}-%{release}
%endif

%if %{defined suse_version}
%global bash_completions_dir %{_datadir}/bash-completion/completions
%global fish_completions_dir %{_datadir}/fish/completions
%global zsh_completions_dir %{_datadir}/zsh/site-functions
%endif

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

# TODO: once all supported SUSE builds can use RPM 4.20 drop this and rely
# on the specpart logic
%if %{defined suse_version}
%package system-deps
Summary:       Pull in additional dependencies needed to build images
Requires:      %{name} = %{version}-%{release}
Requires:      python3-pefile
Requires:      tar
Requires:      xz
Requires:      zstd
Requires:      cpio
Requires:      kmod
Requires:      dosfstools
Requires:      mtools
Requires:      e2fsprogs
Requires:      erofs-utils
Requires:      pesign
Requires:      mozilla-nss-tools
Requires:      openssl
Requires:      jq
Requires:      createrepo
Requires:      distribution-gpg-keys
Requires:      squashfs
Requires:      systemd-experimental
Requires:      btrfsprogs
Requires:      zypper

%description system-deps
This package pulls in all the dependencies needed to build images with various
filesystem types, contents and signing with mkosi. It is separate to allow the
main package to be leaner.
%endif

%prep
%autosetup -p1 -n %{name}-%{version}

%if %{undefined suse_version}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
tools/make-man-page.sh

%pyproject_wheel

bin/mkosi completion bash >mkosi.bash
bin/mkosi completion fish >mkosi.fish
bin/mkosi completion zsh >mkosi.zsh

%install
%pyproject_install

%if %{undefined suse_version}
%pyproject_save_files mkosi
{
  bin/mkosi dependencies | sed -e 's/^/Recommends: /'
  echo "%package system-deps"
  echo "Summary:       Pull in additional dependencies needed to build images"
  bin/mkosi dependencies | sed -e 's/^/Requires: /'
  echo "Requires:      pesign"
  echo "%description system-deps"
  echo "This package pulls in all the dependencies needed to build images"
  echo "%files system-deps"
} >%{specpartsdir}/mkosi.specpart
%else
# See comment about __brp_compress above
export NO_BRP_STALE_LINK_ERROR=yes
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/mkosi
%endif

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-sandbox.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-initrd.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-addon.1
ln -s -t %{buildroot}%{_mandir}/man7/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.news.7

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

%if %{undefined suse_version}
%files -f %pyproject_files
%else
%files
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-*.dist-info
%endif
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
%if %{defined suse_version}
%dir %{fish_completions_dir}
%dir %{fish_completions_dir}/..
%dir %{zsh_completions_dir}
%dir %{zsh_completions_dir}/..
%endif

%files initrd
%_bindir/mkosi-initrd
%_mandir/man1/mkosi-initrd.1*
%_prefix/lib/kernel/install.d/50-mkosi.install
%ghost %dir %{_prefix}/lib/mkosi-initrd
%ghost %dir %{_sysconfdir}/mkosi-initrd
%if %{defined suse_version}
%dir %_prefix/lib/kernel
%dir %_prefix/lib/kernel/install.d
%endif

%files addon
%_bindir/mkosi-addon
%_mandir/man1/mkosi-addon.1*
%_prefix/lib/kernel/install.d/51-mkosi-addon.install
%ghost %dir %{_prefix}/lib/mkosi-addon
%ghost %dir %{_sysconfdir}/mkosi-addon
%if %{defined suse_version}
%dir %_prefix/lib/kernel
%dir %_prefix/lib/kernel/install.d
%endif

%if %{defined suse_version}
%files system-deps
%endif

%check
%if %{with tests}
%pytest tests/ -v

%if %{undefined suse_version}
# just a smoke test for syntax or import errors
%py3_test_envvars %{buildroot}%{_bindir}/mkosi --help >/dev/null
%endif
%endif

%changelog
%if %{without obs}
%autochangelog
%endif
