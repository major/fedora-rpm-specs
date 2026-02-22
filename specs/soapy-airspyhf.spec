%global gitdate 20251009
%global commit 7457d6972d97ea6808a2774a9439501308e4c688
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           soapy-airspyhf
Version:        0.2.0^%{gitdate}git%{shortcommit}
Release:        %autorelease
Summary:        SoapySDR module for AirspyHF hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyAirspyHF
Source:         https://github.com/pothosware/SoapyAirspyHF/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyhf-devel

%description
SoapyAirspyHF is a plug-in module for SoapySDR adding support for
AispyHF hardware.
    
%prep
%autosetup -n SoapyAirspyHF-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules*/libairspyhfSupport.so

%changelog
%autochangelog
