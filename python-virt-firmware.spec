%global pypi_version 23.5

Name:           python-virt-firmware
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Tools for virtual machine firmware volumes

License:        GPLv2
URL:            https://pypi.org/project/virt-firmware/
Source0:        virt-firmware-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(setuptools)
BuildRequires:  make help2man

%description
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n     python3-virt-firmware
Summary:        %{summary}
%{?python_provide:%python_provide python3-virt-firmware}
Provides:       virt-firmware
Requires:       python3dist(cryptography)
Requires:       python3dist(setuptools)
%description -n python3-virt-firmware
Tools for ovmf / armvirt firmware volumes This is a small collection of tools
for edk2 firmware images. They support decoding and printing the content of
firmware volumes. Variable stores (OVMF_VARS.fd) can be modified, for example
to enroll secure boot certificates.

%package -n     python3-virt-firmware-peutils
Summary:        %{summary} - peutils
Requires:       python3dist(pefile)
Conflicts:      python3-virt-firmware < 1.6
%description -n python3-virt-firmware-peutils
Some utilities to inspect efi (pe) binaries.

%package -n     python3-virt-firmware-tests
Summary:        %{summary} - test cases
Requires:       python3-virt-firmware
Requires:       python3dist(pytest)
Requires:       edk2-ovmf
%description -n python3-virt-firmware-tests
test cases

%prep
%autosetup -n virt-firmware-%{pypi_version}

%build
%py3_build

%install
%py3_install
# manpages
install -m 755 -d      %{buildroot}%{_mandir}/man1
install -m 644 man/*.1 %{buildroot}%{_mandir}/man1
# tests
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -ar tests %{buildroot}%{_datadir}/%{name}

%files -n python3-virt-firmware
%license LICENSE
%doc README.md experimental
%{_bindir}/host-efi-vars
%{_bindir}/virt-fw-dump
%{_bindir}/virt-fw-vars
%{_bindir}/virt-fw-sigdb
%{_bindir}/migrate-vars
%{_mandir}/man1/virt-*.1*
%{python3_sitelib}/virt/firmware
%{python3_sitelib}/virt_firmware-%{pypi_version}-py%{python3_version}.egg-info

%files -n python3-virt-firmware-peutils
%{python3_sitelib}/virt/peutils
%{_bindir}/pe-dumpinfo
%{_bindir}/pe-listsigs
%{_bindir}/pe-addsigs

%files -n python3-virt-firmware-tests
%{_datadir}/%{name}/tests

%changelog
%autochangelog
