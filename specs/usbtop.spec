Name:           usbtop
Version:        1.0
Release:        %autorelease
Summary:        Utility to show USB bandwidth
License:        BSD-3-Clause
URL:            https://github.com/aguinet/usbtop
Source0:        %{url}/archive/release-%{version}/usbtop-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  boost-devel >= 1.48.0


%description
usbtop is a top-like utility that shows an estimated instantaneous bandwidth on
USB buses and devices.


%prep
%autosetup -n usbtop-release-%{version}
rm -rf third-party


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install
install -d %{buildroot}%{_modulesloaddir}
echo usbmon > %{buildroot}%{_modulesloaddir}/usbtop.conf

# The CMake config hardcodes the directory name
%if "%{_sbindir}" == "%{_bindir}"
mv -v %{buildroot}/usr/sbin %{buildroot}%{_bindir}
%endif

%post
modprobe usbmon &> /dev/null || :


%files
%license LICENSE
%doc README.md CHANGELOG
%{_sbindir}/usbtop
%{_modulesloaddir}/usbtop.conf


%changelog
%autochangelog
