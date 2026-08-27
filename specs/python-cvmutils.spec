Name:           python-cvmutils
Version:        0.3.2
Release:        %autorelease
Summary:        Toolkit for preparing Linux OS images for confidential virtual machines

License:        LGPL-2.1-or-later
URL:            https://gitlab.com/vkuznets/cvmutils
Source:         https://gitlab.com/vkuznets/cvmutils/-/archive/%version/cvmutils-%version.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel systemd-rpm-macros

%description
A toolkit for preparing Linux OS images to run in confidential virtual machine
(CVM) environments. It enables pre-encryption of root volumes with TPM-sealed
keys and supports creating integrity-protected images.

%package -n     python3-cvmutils
Summary:        %{summary}

%description -n python3-cvmutils
Common Python libraries and utilities for confidential virtual machine (CVM)
tools.

%package -n     cvm-encrypt-image
Summary:        %{summary}
Requires:       python3-cvmutils = %{version}-%{release}
Requires:       systemd-udev util-linux cryptsetup e2fsprogs openssl
Recommends:     qemu-img

%description -n cvm-encrypt-image
Pre-encrypts root volumes and seals encryption keys to a target vTPM using
predicted PCR values. Converts root partitions to LUKS2 encryption, predicts
PCR values by analyzing boot chains and Secure Boot configurations, and seals
keys to TPM with predicted PCR policies.

%package -n     cvm-reseal
Summary:        %{summary}
Requires:       python3-cvmutils = %{version}-%{release}
Requires:       systemd-udev util-linux cryptsetup openssl

%description -n cvm-reseal
Re-seals LUKS volume keys on a running system when PCR measurements change
(e.g., after kernel or UKI updates). Reads current Secure Boot state, discovers
boot chains, compares predicted PCR policies against existing LUKS tokens, and
manages token lifecycle.

%prep
%autosetup -p1 -n cvmutils-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -k unit_tests

%files -n python3-cvmutils
%doc README.md
%license COPYING
%{python3_sitelib}/cvmutils
%{python3_sitelib}/cvmutils-%{version}.dist-info
%{_datarootdir}/cvmutils

%files -n cvm-encrypt-image
%{_bindir}/cvm-encrypt-image
%{_mandir}/man1/cvm-encrypt-image.1*

%files -n cvm-reseal
%{_bindir}/cvm-reseal
%{_mandir}/man1/cvm-reseal.1*

%changelog
%autochangelog
