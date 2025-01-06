%global srcname virtme_ng

Name:           virtme-ng
Version:        1.32
Release:        %autorelease
Summary:        Quickly build and run kernels inside a virtualized snapshot of your live system

License:        GPL-2.0-only
URL:            https://github.com/arighi/%{name}
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  argparse-manpage

Recommends:     qemu-kvm
Recommends:     busybox
Recommends:     virtiofsd >= 1.7.0

# virtme-ng provides a mostly compatible CLI w.r.t. the original virtme,
# which is dead upstream, so obsolete it in favor of the new package.
Obsoletes:      virtme < 0.1.1-25
Provides:       virtme = %{version}-%{release}

%description
virtme-ng is a tool that allows to easily and quickly recompile and test a Linux
kernel, starting from the source code.

It allows to recompile the kernel in few minutes (rather than hours), then the
kernel is automatically started in a virtualized environment that is an exact
copy-on-write copy of your live system, which means that any changes made to the
virtualized environment do not affect the host system.

In order to do this a minimal config is produced (with the bare minimum support
to test the kernel inside qemu), then the selected kernel is automatically built
and started inside qemu, using the filesystem of the host as a copy-on-write
snapshot.

This means that you can safely destroy the entire filesystem, crash the kernel,
etc. without affecting the host.

Kernels produced with virtme-ng are lacking lots of features, in order to reduce
the build time to the minimum and still provide you a usable kernel capable of
running your tests and experiments.

virtme-ng is based on virtme, written by Andy Lutomirski <luto@kernel.org>.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove bundled binary (optional optimized init program for the VM)
rm -f virtme/guest/bin/virtme-ng-init

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Man page already installs in the right place, remove the sitelib copy
rm -rf %{buildroot}%{python3_sitelib}%{_mandir}
# These need to be moved into the right place
mv %{buildroot}%{python3_sitelib}/etc %{buildroot}%{_sysconfdir}
mv %{buildroot}%{python3_sitelib}/usr/share/* %{buildroot}%{_datadir}
rm -rf %{buildroot}%{python3_sitelib}/usr

%pyproject_save_files virtme virtme_ng

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/virtme-ng.conf
%{_bindir}/vng
%{_bindir}/virtme-ng
%{_bindir}/virtme-run
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods
%{bash_completions_dir}/{virtme-ng,vng}-prompt
%{_mandir}/man1/vng.1*

%changelog
%autochangelog
