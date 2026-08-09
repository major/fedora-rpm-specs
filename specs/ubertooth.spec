%global POSTYEAR 2020
%global POSTMONTH 12
%global POSTNUM 1

%global _description %{expand:
Project Ubertooth is an open source wireless development platform suitable
for Bluetooth experimentation. Ubertooth ships with a capable BLE (Bluetooth
Smart) sniffer and can sniff some data from Basic Rate (BR) Bluetooth Classic
connections.}

Name:           ubertooth
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        %autorelease
Summary:        Bluetooth wireless development platform for experimentation
# This package is only includes host part of the Ubertooth project, which is licensed under GPLv2.
# But parts of the firmware, which is running on the board, licensed under BSD (3 clause): lpcusb,
# and GPL v2 or later.
License:        GPL-2.0-only
URL:            https://github.com/greatscottgadgets/ubertooth
Source:         %{url}/releases/download/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}/%{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.xz
Patch:          ubertooth-0001-remove-shebang-from-library-script.patch

BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbtbb-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  systemd-rpm-macros

Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-specan-ui = %{version}-%{release}

%description    %_description

%package        -n lib%{name}
Summary:        Shared library for Bluetooth experimentation
Requires:       systemd-udev

%description    -n lib%{name} %_description

This package provides the the ubertooth shared library.

%package        devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        specan-ui
Summary:        Graphical spectrum analyzer for %{name}
Requires:       python3-QtPy
Requires:       python3-numpy%{?_isa}
Requires:       python3-pyside6%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    specan-ui
The %{name}-specan-ui is a basic spectrum analysis tool for the Ubertooth.


%prep
%autosetup -p1 -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}

# Fix udev rules
sed -i -e 's/GROUP="@UBERTOOTH_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' \
  host/misc/udev/40-ubertooth.rules.in

# Use the correct version
sed -i "s/version\s*=.*/version = '%{version}',/" \
  host/python/specan_ui/setup.py.in \
  host/python/specan_ui/setup.py

%generate_buildrequires
cd host/python/specan_ui >/dev/null
%pyproject_buildrequires
cd - >/dev/null

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DINSTALL_UDEV_RULES=on \
    -DUDEV_RULES_GROUP=plugdev \
    -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
    -S host

%cmake_build

(
  cd host/python/specan_ui
  %pyproject_wheel
)


%install
%cmake_install
(
  cd host/python/specan_ui
  %pyproject_install
%pyproject_save_files specan
  install -Dp -m755 ubertooth-specan-ui %{buildroot}%{_bindir}
)

%check
%pyproject_check_import

%files
%license COPYING TRADEMARK
%doc README.md
%{_bindir}/%{name}*
%exclude %{_bindir}/%{name}-specan-ui
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man7/%{name}.7*

%files -n lib%{name}
%license COPYING TRADEMARK
%doc README.md
%{_libdir}/lib%{name}.so.*
%{_udevrulesdir}/40-ubertooth.rules

%files devel
%{_includedir}/ubertooth.h
%{_includedir}/ubertooth_*.h
%{_libdir}/lib%{name}.so

%files specan-ui -f %{pyproject_files}
%doc host/python/specan_ui/README
%{_bindir}/%{name}-specan-ui


%changelog
%autochangelog
