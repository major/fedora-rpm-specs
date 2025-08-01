Name:           python-virt-firmware
Version:        25.7.3
Release:        %autorelease
Summary:        Tools for virtual machine firmware volumes

License:        GPL-2.0-only
URL:            https://pypi.org/project/virt-firmware/
Source0:        virt_firmware-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  make help2man
BuildRequires:  systemd systemd-rpm-macros

%generate_buildrequires
%pyproject_buildrequires

%description
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n     python3-virt-firmware
Summary:        %{summary}
%{?python_provide:%python_provide python3-virt-firmware}
Provides:       virt-firmware
Conflicts:      python3-virt-firmware-peutils < 23.9
Obsoletes:      python3-virt-firmware-peutils < 23.9
Requires:       virt-sb-certs
Recommends:     qemu-img
Recommends:     dialog
%description -n python3-virt-firmware
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n     python3-virt-firmware-tests
Summary:        %{summary} - test cases
Requires:       python3-virt-firmware
Requires:       python3dist(pytest)
Requires:       edk2-ovmf
%description -n python3-virt-firmware-tests
test cases

%package -n     uki-direct
Provides:       ukidirect
Summary:        %{summary} - manage UKI kernels.
Requires:       python3-virt-firmware
Conflicts:      systemd < 254
%description -n uki-direct
kernel-install plugin and systemd unit to manage automatic
UKI (unified kernel image) updates.

%package -n     virt-sb-certs
Summary:        secure boot certificate database
%description -n virt-sb-certs
secure boot certificates used by microsoft and linux distributions, to
be used for a more finegrained secure boot configuration for virtual
machines.

%prep
%autosetup -n virt_firmware-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# manpages
install -m 755 -d      %{buildroot}%{_mandir}/man1
install -m 644 man/*.1 %{buildroot}%{_mandir}/man1
# tests
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -ar tests %{buildroot}%{_datadir}/%{name}
# uki-direct
install -m 755 -d  %{buildroot}%{_unitdir}
install -m 755 -d  %{buildroot}%{_prefix}/lib/kernel/install.d
install -m 644 systemd/kernel-bootcfg-boot-successful.service %{buildroot}%{_unitdir}
install -m 755 systemd/99-uki-uefi-setup.install %{buildroot}%{_prefix}/lib/kernel/install.d
# virt-sb-certs
install -m 755 -d %{buildroot}%{_datadir}/virt-sb-certs
dirs=$(cd %{buildroot}%{python3_sitelib}/virt/firmware/certs; echo *)
mv -v %{buildroot}%{python3_sitelib}/virt/firmware/certs/* \
   %{buildroot}%{_datadir}/virt-sb-certs
for dir in $dirs; do
    ln -vs ../../../../../../..%{_datadir}/virt-sb-certs/$dir \
       %{buildroot}%{python3_sitelib}/virt/firmware/certs/$dir
done

%post -n uki-direct
%systemd_post kernel-bootcfg-boot-successful.service

%preun -n uki-direct
%systemd_preun kernel-bootcfg-boot-successful.service

%postun -n uki-direct
%systemd_postun kernel-bootcfg-boot-successful.service

%files -n python3-virt-firmware
%license LICENSE
%doc README.md experimental
%{_bindir}/host-efi-vars
%{_bindir}/virt-fw-dump
%{_bindir}/virt-fw-vars
%{_bindir}/virt-fw-sigdb
%{_bindir}/kernel-bootcfg
%{_bindir}/uefi-boot-menu
%{_bindir}/migrate-vars
%{_bindir}/pe-dumpinfo
%{_bindir}/pe-listsigs
%{_bindir}/pe-addsigs
%{_bindir}/pe-inspect
%{_mandir}/man1/virt-*.1*
%{_mandir}/man1/kernel-bootcfg.1*
%{_mandir}/man1/uefi-boot-menu.1*
%{_mandir}/man1/pe-*.1*
%dir %{python3_sitelib}/virt
%{python3_sitelib}/virt/firmware
%{python3_sitelib}/virt/peutils
%{python3_sitelib}/virt_firmware-%{version}.dist-info

%files -n python3-virt-firmware-tests
%{_datadir}/%{name}/tests

%files -n uki-direct
%{_unitdir}/kernel-bootcfg-boot-successful.service
%{_prefix}/lib/kernel/install.d/99-uki-uefi-setup.install

%files -n virt-sb-certs
%{_datadir}/virt-sb-certs

%changelog
%autochangelog
