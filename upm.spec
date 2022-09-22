# Nodejs >= 12 is not supported by current versions of SWIG.
%bcond_with nodejs_pkg

%if %{with nodejs_pkg}
%global BUILD_NODEJS ON
%else
%global BUILD_NODEJS OFF
%endif

Name:    upm
Version: 2.0.0
Release: 14%{?dist}
Summary: A high level library for sensors and actuators
License: MIT
URL:     https://projects.eclipse.org/projects/iot.upm/

Source0: https://github.com/intel-iot-devkit/upm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# To quote "Only x86, arm and mock platforms currently supported"
ExcludeArch:   %{power64} s390x

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: libjpeg-turbo-devel
BuildRequires: mraa-devel
%if %{with nodejs_pkg}
BuildRequires: nodejs-devel nodejs-packaging nodejs-mraa
%endif
BuildRequires: python3-devel python3-setuptools python3-mraa
BuildRequires: swig
BuildRequires: doxygen graphviz sphinx

%if %{without nodejs_pkg}
Obsoletes: nodejs-upm < %{version}-%{release}
%endif

%description
UPM is a high level repository that provides software drivers for a wide variety 
of commonly used sensors and actuators. These software drivers interact with the 
underlying hardware platform through calls to MRAA APIs.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libjpeg-turbo-devel
Requires: mraa-devel

%description devel
Files for development with %{name}.

%package -n python3-upm
Summary: Python3 bindings for sensors and actuators
License: GPLv2+
%{?python_provide:%python_provide python3-upm}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3-mraa

%description -n python3-upm
Python3 bindings for sensors and actuators

%if %{with nodejs_pkg}
%package -n nodejs-upm
Summary: NodeJS package for sensors and actuators
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: nodejs-mraa

%description -n nodejs-upm
NodeJS bindings for sensors and actuators
%endif

%prep
%autosetup -p1

find . -name \*.cxx -exec chmod -x {} \;

%build
%cmake -DBUILDSWIGNODE=%{BUILD_NODEJS} -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_SKIP_RPATH=ON -DUSE_LIB64:BOOL=%["%{?_isa_bits}" == "64" ? "ON" : "OFF"] -DVERSION:STRING=%{version} -DWERROR=OFF
%cmake_build

%install
%cmake_install

rm -f %{buildroot}/%{_includedir}/upm/upm_utilities.hpp
sed -i '/Requires: jpeg/d' %{buildroot}/%{_libdir}/pkgconfig/upm-vcap.pc

%if %{with nodejs_pkg}
# Symlink nodejs dependencies
%nodejs_symlink_deps
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/upm/
%{_datadir}/upm/
%{_libdir}/pkgconfig/%{name}*.pc
%{_libdir}/lib%{name}*.so

%files -n python3-upm
%{python3_sitearch}/upm/

%if %{with nodejs_pkg}
%files -n nodejs-upm
%{nodejs_sitelib}/jsupm_*/
%endif

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-13
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.9

* Wed May 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.0-6
- Fix incorrect jpeg devel requires

* Thu Apr 16 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Make the package installable again
- Disable Nodejs package, as SWIG does not support Nodejs >= 12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-1
- New upstream 2.0.0 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.1-1
- New upstream 1.7.1 release
- Minor cleanups

* Mon Sep 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.0-2
- Add nodejs-mraa dep for nodejs-upm sub package

* Sun Sep  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.0-1
- New upstream 1.7.0 release

* Thu Oct 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.0-1
- New upstream 1.5.0 release

* Tue May 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.0-1
- Initial package
