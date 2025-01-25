Name:           azure-vm-utils
Version:        0.4.0
Release:        %autorelease
Summary:        Core utilities and configuration for Linux VMs on Azure

License:        MIT
URL:            https://github.com/Azure/%{name}
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

# Allow the binary install to be configurable
# https://github.com/Azure/azure-vm-utils/pull/50
Patch:          0001-cmake-Allow-the-install-directory-to-be-configurable.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)

Provides:       azure-nvme-utils = %{version}-%{release}
Obsoletes:      azure-nvme-utils < 0.1.3-3

%description
This package provides a home for core utilities, udev rules and other
configuration to support Linux VMs on Azure.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DVERSION="%{version}-%{release}" -DAZURE_NVME_ID_INSTALL_DIR="%{_bindir}"
%cmake_build

%install
%cmake_install
install -D -m 0755 initramfs/dracut/modules.d/97azure-disk/module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/97azure-disk/module-setup.sh

%check
%ctest

%files
%defattr(-,root,root,-)
%{_mandir}/man8/azure-nvme-id.8.gz
%dir %{_prefix}/lib/dracut/modules.d/97azure-disk
%{_prefix}/lib/dracut/modules.d/97azure-disk/module-setup.sh
%{_bindir}/azure-nvme-id
%{_udevrulesdir}/80-azure-disk.rules

%changelog
%autochangelog
