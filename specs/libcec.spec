%if 0%{?fedora}
%global with_python 1
%endif

Name:          libcec
Version:       6.0.2
Release:       19%{?dist}
Summary:       Library and utilities for HDMI-CEC device control
License:       GPL-2.0-or-later
URL:           http://libcec.pulse-eight.com/
Source0:       https://github.com/Pulse-Eight/%{name}/archive/%{name}-%{version}.tar.gz
Patch1:        libcec-pythonlib.patch
# Fix FTBFS with Python 3.13
Patch2:        libcec-python13.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libXrandr-devel
BuildRequires: lockdev-devel
BuildRequires: ncurses-devel
BuildRequires: platform-devel
%if 0%{?with_python}
BuildRequires: python3-devel
%endif
BuildRequires: swig
BuildRequires: systemd-devel
BuildRequires: findutils

%description
libCEC allows you in combination with the right hardware to control your device 
with your TV remote control over your existing HDMI cabling.

libCEC is an enabling platform for the CEC bus in HDMI, it allows developers to 
interact with other HDMI devices without having to worry about the communication 
overhead, handshaking, and the various ways of send messages for each vendor.

%package       devel
Summary:       Development package for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
Files for development with %{name}.

%if 0%{?with_python}
%package -n    python3-libcec
Summary:       A Python 3 interface to libcec
Requires:      %{name}%{?_isa} = %{version}-%{release}
%py_provides   python3-cec

%description -n python3-libcec
Python 3 bindings for libcec
%endif

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Remove non linux binaries
rm -rf support
rm -rf driver

%build
%cmake \
    -DHAVE_LINUX_API=on

%cmake_build

%install
%cmake_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

# Remove versioned binaries
rm %{buildroot}/%{_bindir}/cec-client %{buildroot}/%{_bindir}/cecc-client
mv %{buildroot}/%{_bindir}/cec-client-%{version} %{buildroot}/%{_bindir}/cec-client
mv %{buildroot}/%{_bindir}/cecc-client-%{version} %{buildroot}/%{_bindir}/cecc-client

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_bindir}/cec-client
%{_bindir}/cecc-client
%{_libdir}/libcec.so.*

%files devel
%{_includedir}/libcec
%{_libdir}/pkgconfig/libcec.pc
%{_libdir}/libcec.so

%if 0%{?with_python}
%files -n python3-libcec
%{_bindir}/pyCecClient
%{python3_sitearch}/cec/
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.0.2-17
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.0.2-14
- Fix RHBZ #2245791
- Switch license tag to SPDX

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.0.2-12
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Petr Menšík <pemensik@redhat.com> - 6.0.2-10
- Provide also name matching imported python module

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.0.2-8
- Rebuilt for Python 3.11

* Fri Mar 04 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 6.0.2-7
- The cmake macro should no longer be called with a folder name

* Fri Mar 04 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 6.0.2-6
- add findutils build dep
- fix how cmake is called for newer cmake

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.0.2-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.0.2-1
- Update to 6.0.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Charalampos Stratakis <cstratak@redhat.com> - 5.0.0-3
- Improve python libs dir detection for pre-releases (#1791947)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0 release
- Enable Linux native CEC support

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.4-1
- Update to 4.0.4
- Fix issue with python3 (RHBZ 1665546)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Simone Caronni <negativo17@gmail.com> - 4.0.3-2
- Re-add updated Python libraries patch.

* Mon Nov 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.3-1
- Update to 4.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-8
- Rebuilt for Python 3.7

* Wed Mar  7 2018 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.2-7
- Add gcc BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Feb 23 2017 Iryna Shcherbina <ishcherb@redhat.com> 4.0.2-2
- Fix python3-libcec dragging in both Python 3 and Python 2 (RHBZ#1420396)

* Fri Feb  3 2017 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.2-1
- Update to 4.0.2

* Sat Jan  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-1
- Update to 4.0.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-2
- Rebuild for Python 3.6

* Sun Oct 30 2016 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.0-1
- Update to 4.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-2
- Don't build python3 bindings on EPEL

* Wed Jan 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-1
- Update to 3.1.0
- Build python3 bindings

* Mon Jan 18 2016 Ville Skyttä <ville.skytta@iki.fi> - 3.0.1-2
- Build with $RPM_OPT_FLAGS (use %%cmake macro)

* Tue Jan 12 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.1-1
- Update to 3.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.0-1
- Update to 2.2.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.4-1
- Update to 2.1.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.3-1
- Update to 2.1.3

* Mon Mar  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.5-1
- Update to 2.0.5

* Sun Nov 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.4-1
- Update to 2.0.4

* Mon Nov 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.3-1
- Update to 2.0.3

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-2
- Updates from review

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-1
- Update to 1.9.0

* Sat Jun 30 2012 Peter Robinson <pbrobinson@gmail.com> 1.7.1-1
- Initial packaging
