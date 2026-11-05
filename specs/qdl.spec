%global forgeurl https://github.com/linux-msm/qdl/

Name:           qdl
Version:        2.9
Release:        %autorelease

%forgemeta

Summary:        Qualcomm EDL flash tool
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}
# https://github.com/linux-msm/qdl/pull/351
Patch0:         351.patch
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(nbdkit)
BuildRequires:	systemd-rpm-macros

%description
This tool communicates with Qualcomm EDL USB devices (Vendor ID 05c6, Product
IDs 9008, 900e, 901d) to upload a flash loader and use it to flash images.

%package -n nbdkit-qdl-plugin
Summary:	Qdl plugin for nbdkit
Requires:	nbdkit-server

%description -n nbdkit-qdl-plugin
This package is the Qdl plugin for nbdkit.


%prep
%autosetup -p1


%if 0%{?rhel} && 0%{?rhel} < 10
%build
%meson
%else
%conf
%meson
%build
%endif
%meson_build


%check
%meson_test


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/qdl*
%{_udevrulesdir}/70-qdl.rules
%{_mandir}/man1/qdl*


%files -n nbdkit-qdl-plugin
%license LICENSE
%{_libdir}/nbdkit/plugins/nbdkit-qdl-plugin.so


%changelog
%autochangelog
