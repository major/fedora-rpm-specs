Name:           soapy-airspyhf
Version:        0.2.1
Release:        %autorelease
Summary:        SoapySDR module for AirspyHF hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyAirspyHF
Source:         https://github.com/pothosware/SoapyAirspyHF/archive/refs/tags/soapy-airspyhf-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyhf-devel

%description
SoapyAirspyHF is a plug-in module for SoapySDR adding support for
AispyHF hardware.
    
%prep
%autosetup -n SoapyAirspyHF-soapy-airspyhf-%{version}

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
