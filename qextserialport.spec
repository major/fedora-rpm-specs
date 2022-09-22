Name:      qextserialport
Version:   1.2
Release:   0.24.beta2%{?dist}
Summary:   Qt interface class for old fashioned serial ports
License:   MIT
URL:       http://code.google.com/p/qextserialport/
Source0:   http://qextserialport.googlecode.com/files/%{name}-%{version}beta2.tar.gz
Source1:   %{name}-config.pri

BuildRequires: make
BuildRequires:  qt4-devel
BuildRequires:  libudev-devel

%description
QextSerialPort provides an interface to old fashioned
serial ports for Qt-based applications.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt4-devel

%description devel
This package contains the files necessary
to develop applications using Qextserialport.


%prep
%setup -qn %{name}-%{version}beta2
cp -a %{SOURCE1} config.pri


%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}


%ldconfig_scriptlets


%files 
%doc ChangeLog LICENSE
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/QtExtSerialPort/
%{_libdir}/lib%{name}*.so
%{_qt4_datadir}/mkspecs/features/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.24.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.23.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.22.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.21.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.20.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.19.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.18.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.17.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.16.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.15.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.14.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.13.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.12.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.11.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.2-0.10.beta2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.9.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-0.8.beta2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Dave Johansen <davejohansen@gmail.com> 1.2-0.7.beta2
- Rebuild for gcc 5.0 C++ ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.6.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.5.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Volker Fröhlich <volker27@gmx.at> 1.2-0.2.beta2
- Correct Source location
- Require qt4-devel for devel sub-package

* Fri Nov  2 2012 Volker Fröhlich <volker27@gmx.at> 1.2-0.1.beta2
- Initial packaging for Fedora
