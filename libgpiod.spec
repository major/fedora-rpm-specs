#global candidate rc3

Name:          libgpiod
Version:       2.0
Release:       1%{?candidate:.%{candidate}}%{?dist}
Summary:       C library and tools for interacting with linux GPIO char device

License:       LGPLv2+
URL:           https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:       https://mirrors.edge.kernel.org/pub/software/libs/%{name}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.xz

BuildRequires: automake autoconf autoconf-archive libtool
BuildRequires: doxygen
BuildRequires: gcc gcc-c++
BuildRequires: help2man
BuildRequires: kernel-headers
BuildRequires: kmod-devel
BuildRequires: libstdc++-devel
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-devel

%description
libgpiod is a C library and tools for interacting with the linux GPIO character 
device (gpiod stands for GPIO device) The new character device interface 
guarantees all allocated resources are freed after closing the device file 
descriptor and adds several new features that are not present in the obsolete 
sysfs interface (like event polling, setting/reading multiple values at once or 
open-source and open-drain GPIOs).

%package utils
Summary: Utilities for GPIO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for interacting with GPIO character devices.

%package c++
Summary: C++ bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description c++
C++ bindings for use with %{name}.

%package -n python3-%{name}
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 bindings for development with %{name}.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-c++ = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --enable-tools=yes --disable-static \
           --enable-bindings-cxx --enable-bindings-python

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.*

%files utils
%{_bindir}/gpio*
%{_mandir}/man*/gpio*

%files c++
%{_libdir}/libgpiodcxx.so.*

%files -n python3-%{name}
%{python3_sitearch}/gpiod-*/

%files devel
%{_includedir}/gpiod.*
%{_includedir}/gpiodcxx/
%{_libdir}/pkgconfig/libgpiod*.pc
%{_libdir}/%{name}*.so

%changelog
* Thu Mar 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0-1
- Update to 2.0

* Mon Feb 27 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0-0.4.rc3
- libgpiod 2.0 RC3

* Thu Feb 16 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0-0.3.rc2
- libgpiod 2.0 RC2

* Mon Feb 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0-0.2.rc1
- Add deps for man pages build

* Mon Feb 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0-0.1.rc1
- Update to libgpiod 2.0 RC1

* Wed Feb 08 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.4-1
- Update to 1.6.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.3-7
- Update devel dependencies

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.3-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.3-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Mon Nov  2 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Thu Oct 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6-1
- Update to 1.6

* Sat Sep 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Wed Aug 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Tue Jan 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-1
- Update to 1.5

* Wed Jan 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.2-RC2
- Update to 1.5 RC2

* Tue Jan  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-0.1-RC1
- Update to 1.5 RC1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.8

* Fri Aug  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.1-1
- Update to 1.4.1 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-1
- Update to 1.4 release

* Tue Mar 26 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-1
- Update to 1.3 release

* Sat Feb 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.1-1
- Update to 1.2.1 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2-1
- Update to 1.2 release

* Thu Jul 26 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- Update to 1.1.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1-1
- Update to 1.1 release
- New C++ and Python 3 bindings

* Sun Apr 15 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Thu Feb  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-1
- Update to 1.0.0 with stable API

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.2-1
- Update to 0.3.2

* Tue Aug 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-2
- Minor review updates

* Sat Jul  1 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-1
- Initial package
