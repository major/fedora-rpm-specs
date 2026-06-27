%global forgeurl https://github.com/linux-msm/qdl/

Name:           qdl
Version:        2.7
Release:        %autorelease

%forgemeta

Summary:        Qualcomm EDL flash tool
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        51-qcom-usb.rules
BuildRequires:  gcc
# meson.build uses git. Fixed in upstream git, drop for 2.8 release.
BuildRequires:  git-core
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)

%description
This tool communicates with Qualcomm EDL USB devices (Vendor ID 05c6, Product
IDs 9008, 900e, 901d) to upload a flash loader and use it to flash images.


%prep
%autosetup


%conf
%meson


%build
%meson_build


%check
%meson_test


%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/51-qcom-usb.rules


%files
%license LICENSE
%doc README.md
%{_bindir}/qdl*
%config(noreplace) %{_sysconfdir}/udev/rules.d/51-qcom-usb.rules
%{_mandir}/man1/qdl*


%changelog
%autochangelog
