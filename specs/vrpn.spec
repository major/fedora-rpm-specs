# Some of the tests randomly hang, others attempt to spin up various network
# services that don't work properly in mock
%bcond_with tests

# Python bindings fail to build with Python 3.13 (RHBZ#2247291)
%if 0%{?fedora} > 40
%bcond_with python
%else
%bcond_without python
%endif

%global common_description %{expand:
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.}

Name:           vrpn
Version:        07.35
Release:        6%{?dist}
Summary:        Virtual-Reality Peripheral Network

# According to upstream, linking to the wiiuse (GPLv3+) and gpm (GPLv2+)
# libraries makes the vrpn server (libvrpnserver.so and vrpn_server binary, as
# well as the language bindings) GPLv3+. See
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/384#note_1606303642
# for the other licenses.
License:        BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later
URL:            https://github.com/vrpn/vrpn
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vrpn.service

# Extending range of Python version search to support two-digit minor versions
Patch:          %{url}/commit/1b4676b3cf8bbaff2f75c8e41b005401b189b2e2.patch
# Fix modbus libraries detection
Patch:          vrpn-find_modbus.patch
%if %{with python}
# Fix Python modules installation
Patch:          vrpn-python_install.patch
%endif
# Add soversion to all libraries
Patch:          vrpn-soversion.patch
# Do not install binaries only used for unit tests
Patch:          vrpn-dont-install-tests.patch

%if %{with python}
BuildRequires:  chrpath
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  perl
BuildRequires:  perl-Parse-RecDescent
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  swig

BuildRequires:  glut-devel
BuildRequires:  gpm-devel
BuildRequires:  hidapi-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libGL-devel
%ifnarch s390x
BuildRequires:  libi2c-devel
%endif
BuildRequires:  libmodbus-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb1-devel
%if %{with python}
BuildRequires:  python3-devel
%else
# Drop once f40 is EOL
Provides:       python3-vrpn = %{version}-%{release}
Obsoletes:      python3-vrpn < 07.35-5
%endif
BuildRequires:  wiiuse-devel

%description    %{common_description}

The idea is to have a PC or other host at each VR station that controls the
peripherals (tracker, button device, haptic device, analog inputs, sound, etc).
VRPN provides connections between the application and all of the devices using
the appropriate class-of-service for each type of device sharing this link. The
application remains unaware of the network topology. Note that it is possible
to use VRPN with devices that are directly connected to the machine that the
application is running on, either using separate control programs or running
all as a single program.

%package devel
Summary:        Development files for the Virtual-Reality Peripheral Network
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gpm-devel
Requires:       hidapi-devel
Requires:       jsoncpp-devel
Requires:       libudev-devel
Requires:       libusb1-devel
Requires:       wiiuse-devel

%description devel %{common_description}

This package contains development files for the VRPN libraries.

%package doc
Summary:        Developer's documentation for VRPN
BuildArch:      noarch

%description doc %{common_description}

This package contains generated VRPN source code documentation.

%if %{with python}
%package -n python3-%{name}
Summary:        Python 3 bindings for the Virtual-Reality Peripheral Network

%description -n python3-%{name} %{common_description}

This package contains Python 3 bindings for the VRPN libraries.
%endif

%prep
%autosetup -p1

# Fix binaries path
sed -i 's:/usr/local/bin:%{_bindir}:g' vrpn_Connection.C

%build
%cmake \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DVRPN_GPL_SERVER=ON \
    -DBUILD_TESTING=ON \
%if %{with python}
    -DVRPN_BUILD_PYTHON_HANDCODED_3X=ON \
    -DVRPN_PYTHON_INSTALL_DIR=%{python3_sitearch} \
%endif
    %{nil}
%cmake_build
%cmake_build --target doc

%install
%cmake_install

%if %{with python}
# Install Python module and strip broken rpath
chrpath -d %{_vpath_builddir}/python/vrpn.so
install -Dpm0755 -t %{buildroot}%{python3_sitearch} %{_vpath_builddir}/python/vrpn.so
%endif

# Install systemd service
install -Dpm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Move sample config out of the way
mv %{buildroot}/%{_datadir}/%{name}-%{version}/%{name}.cfg.sample .

%if %{with tests}
%check
%ctest
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc ChangeLog %{name}.cfg.sample
%license README.Legal
%{_libdir}/lib%{name}*.so.07{,.*}
%{_libdir}/libgpsnmea.so.07{,.*}
%{_libdir}/libquat.so.07{,.*}
%{_bindir}/%{name}*
%{_bindir}/run_auxiliary_logger
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_unitdir}/%{name}.service

%files devel
%{_includedir}/latLonCoord.h
%{_includedir}/nmeaParser.h
%{_includedir}/quat.h
%{_includedir}/utmCoord.h
%{_includedir}/%{name}*
%{_libdir}/lib%{name}*.so
%{_libdir}/libgpsnmea.so
%{_libdir}/libquat.so

%files doc
%doc Format_Of_Protocol.txt
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.map
%exclude %{_docdir}/%{name}-%{version}/source-docs/html/*.md5

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/*.so
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 07.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 07.35-5
- Disable Python bindings on f41 and later; Fixes: RHBZ#2247291

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 07.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 07.35-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 07.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 07.35-1
- Unretire and update to 07.35; Fixes: RHBZ#2246766
- Rework specfile to comply with the latest packaging guidelines
- Update license tag and convert to SPDX
- Rework package descriptions
- Preserve timestamps when installing files
- Refresh patches and backport and upstream Python fix
- Drop manpage generation because it hangs the build
- Disable tests by default due to flakiness
- Drop the Java bindings, nothing uses them and they don't install properly

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 07.33-24
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 07.33-23
- Rebuild (jsoncpp)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 07.33-22
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 07.33-20
- Rebuild (jsoncpp)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 07.33-19
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 07.33-17
- Rebuild (jsoncpp)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 07.33-15
- Subpackage python2-vrpn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 07.33-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-11
- Rebuilt for jsoncpp.so.20

* Sat Sep 02 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-10
- Fix problems with finding JNI on %%arm

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 07.33-9
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 07.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 07.33-5
- Rebuild for Python 3.6

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 07.33-4
- Rebuilt for libjsoncpp.so.11

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 07.33-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 8 2016 Dmitry Mikhirev <mikhirev@gmail.com> 07.33-2
- Fix build for fc25 (#1341988)
- Fix installation of python 3 module (#1342509)

* Wed Feb 24 2016 Dmitry Mikhirev <mikhirev@gmail.com> 07.33-1
- Initial package
