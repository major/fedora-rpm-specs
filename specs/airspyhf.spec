%global gitdate 20260107
%global commit 30e0422ab5eae0fecd429b29e89c6e8699bb5cd6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           airspyhf
Version:        1.6.8^%{gitdate}git%{shortcommit}
Release:        %autorelease
Summary:        AirSpy HF+ SDR host software for HF and VHF bands

License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            http://airspy.com/
Source0:        https://github.com/airspy/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libusbx-devel
BuildRequires:  systemd
Requires:       systemd-udev

%description
Software for AirSpy HF+, a high performance software defined
radio for the HF and VHF bands.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        BSD-3-Clause AND GPL-2.0-or-later
Summary:        Development files for %{name}

%description devel
Files needed to develop software against libairspy.

%prep
%autosetup -n %{name}-%{commit}
# Fix udev rule
sed -i -e 's/MODE="660", GROUP="plugdev"/TAG+="uaccess"/g' tools/52-airspyhf.rules
rm -rf tools/getopt

%build
%cmake -DINSTALL_UDEV_RULES=on
%cmake_build

%install
%cmake_install

# Remove static object
rm -f %{buildroot}%{_libdir}/libairspyhf.a

# Move udev rule to correct location
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspyhf.rules %{buildroot}%{_udevrulesdir}

%post
%?ldconfig
%udev_rules_update

%postun
%?ldconfig
%udev_rules_update

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{buildroot}%{_bindir}/airspyhf_lib_version

%files
%license LICENSE.BSD LICENSE.GPL-2.0
%doc README.md
%{_bindir}/airspyhf_calibrate
%{_bindir}/airspyhf_gpio
%{_bindir}/airspyhf_info
%{_bindir}/airspyhf_lib_version
%{_bindir}/airspyhf_rx
%{_libdir}/libairspyhf.so.0
%{_libdir}/libairspyhf.so.1{,.*}
%{_udevrulesdir}/52-airspyhf.rules
%{_sysconfdir}/sysusers.d/plugdev.conf

%files devel
%{_includedir}/libairspyhf
%{_libdir}/pkgconfig/libairspyhf.pc
%{_libdir}/libairspyhf.so

%changelog
%autochangelog
