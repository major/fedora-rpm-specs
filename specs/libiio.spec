Name:          libiio
Version:       0.26
Release:       3%{?dist}
Summary:       Library for Industrial IO
License:       LGPL-2.0-or-later
URL:           https://analogdevicesinc.github.io/libiio/
Source0:       https://github.com/analogdevicesinc/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: avahi-devel
BuildRequires: bison
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libaio-devel
BuildRequires: libusb1-devel
BuildRequires: libxml2-devel
BuildRequires: man2html
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme

%description
Library for interfacing with Linux IIO devices

libiio is used to interface to Linux Industrial Input/Output (IIO) Subsystem.
The Linux IIO subsystem is intended to provide support for devices that in some 
sense are analog to digital or digital to analog converters (ADCs, DACs). This 
includes, but is not limited to ADCs, Accelerometers, Gyros, IMUs, Capacitance 
to Digital Converters (CDCs), Pressure Sensors, Color, Light and Proximity 
Sensors, Temperature Sensors, Magnetometers, DACs, DDS (Direct Digital 
Synthesis), PLLs (Phase Locked Loops), Variable/Programmable Gain Amplifiers 
(VGA, PGA), and RF transceivers.

%package utils
Summary: Utilities for Industrial IO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for accessing IIO using libiio

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package doc
Summary: Development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for development with %{name}.

%package -n python3-iio
Summary: Python 3 bindings for Industrial IO (libiio)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-iio
Python 3 bindings for Industrial IO

%prep
%autosetup -p1
sed -i 's#${LIBIIO_VERSION_MAJOR}-doc##' CMakeLists.txt
sed -i 's#DESTINATION ${CMAKE_HTML_DEST_DIR}/${CMAKE_API_DEST_DIR}#DESTINATION ${CMAKE_HTML_DEST_DIR}##' CMakeLists.txt

%build
%cmake -DPYTHON_BINDINGS=on -DWITH_DOC=on -DWITH_MAN=on \
       -DUDEV_RULES_INSTALL_DIR=%{_udevrulesdir}

%cmake_build

%install
%cmake_install

#hack: Fix man locations
mv %{buildroot}%{_mandir}/man1/man/* %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/man3/man/* %{buildroot}%{_mandir}/man3
rmdir %{buildroot}%{_mandir}/man1/man %{buildroot}%{_mandir}/man3/man
#Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%files
%license COPYING.txt
%{_libdir}/%{name}.so.*
%{_mandir}/man3/libiio*
%{_udevrulesdir}/90-libiio.rules

%files utils
%{_bindir}/iio_*
%{_bindir}/iiod
%{_mandir}/man1/iio*

%files devel
%{_includedir}/iio.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc %{_docdir}/%{name}

%files -n python3-iio
%{python3_sitelib}/__pycache__/iio*
%{python3_sitelib}/iio.py
%{python3_sitelib}/pylibiio*

%changelog
* Tue Feb 04 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 0.26-3
- Minor spec cleanups and fixes

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.26-1
- Update to 0.26

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.25-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.25-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.25-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.25-1
- Update to 0.25

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.24-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.24-1
- Update to 0.24

* Wed Jun 22 2022 Iker Pedrosa <pbrobinson@fedoraproject.org> - 0.23-6
- Package man pages

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.23-5
- Rebuilt for Python 3.11

* Thu Apr 07 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.23-4
- Drop unused libserialport

* Tue Mar 29 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.23-3
- Minor spec updates for cmake changes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.23-1
- Update to 0.23

* Sun Aug 01 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.22-1
- Update to 0.22

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.21-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.21-1
- Update to 0.21

* Sat Jun 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.20-1
- Update to 0.20

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19-2
- Rebuilt for Python 3.9

* Sat Feb 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.19-1
- Update to 0.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.18-1
- Update to 0.18

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17-1
- Update to 0.17
- Enable IIOD USB/AIO backend

* Thu Nov 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-1
- Update to 0.16

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.15-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-1
- Update to 0.15

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.14-1
- Update to 0.14

* Fri Dec 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.12-1
- Update to 0.12

* Wed Oct 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.11-1
- Update to 0.11

* Wed Aug 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-1
- Update to 0.10
- Review updates

* Wed Feb 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-1
- Initial package
