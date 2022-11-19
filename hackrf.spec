Name:           hackrf
Version:        2022.09.1
Release:        1%{?dist}
Summary:        HackRF Utilities

License:        GPL-2.0
URL:            https://greatscottgadgets.com/hackrf/
Source0:        https://github.com/mossmann/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  systemd

%description
Hardware designs and software for HackRF, a project to produce a low cost, open
source software radio platform.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libusbx-devel

%description devel
Files needed to develop software against libhackrf.


%package doc
Summary:        Supplemental documentation for HackRF
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Supplemental documentation for HackRF. For more information, visit the wiki at
https://github.com/mossmann/hackrf/wiki


%package static
Summary:        Static libraries for libhackrf
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for libhackrf.


%prep
%autosetup -p1

# Fix "plugdev" nonsense
%if 0%{?fedora} >= 20
sed -i -e 's/GROUP="@HACKRF_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules.in
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules
%else
sed -i -e 's/GROUP="@HACKRF_GROUP@"/TAG+="uaccess"/g' host/libhackrf/53-hackrf.rules.in
sed -i -e 's/GROUP="plugdev"/TAG+="uaccess"/g' host/libhackrf/53-hackrf.rules
%endif


%build
%cmake \
  -DINSTALL_UDEV_RULES=on \
  -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
  -DUDEV_RULES_GROUP=plugdev \
  host

%cmake_build


%install
%cmake_install


%post
%{?ldconfig}
%udev_rules_update

%postun
%{?ldconfig}
%udev_rules_update


%files
%license COPYING TRADEMARK
%doc Readme.md
%{_bindir}/hackrf_*
%{_libdir}/libhackrf.so.*
%{_udevrulesdir}/53-hackrf.rules

%files devel
%{_includedir}/libhackrf/hackrf.h
%{_libdir}/pkgconfig/libhackrf.pc
%{_libdir}/libhackrf.so

%files static
%{_libdir}/libhackrf.a

%files doc
%doc docs/*


%changelog
* Thu Nov 17 2022 Richard Shaw <hobbes1069@gmail.com> - 2022.09.1-1
- Update to 2022.09.1.
- Update license tag to SPDX format.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Scott K Logan <logans@cottsay.net> - 2018.01.1-8
- Resolve build issues due to CMake out-of-source build changes
- Re-arranged spec to better align to modern patterns
- Fix %%{_isa} in static subpackage dependency

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2018.01.1-1
- Update package to 2018.01.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Scott K Logan <logans@cottsay.net> - 2017.02.1-2
- Fix noarch dependency in doc package

* Thu Dec 14 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2017.02.1-1
- Update package to 2017.02.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Scott K Logan <logans@cottsay.net> - 2015.07.2-1
- Update to 2015.07.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.08.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 23 2014 Scott K Logan <logans@cottsay.net> - 2014.08.1-1
- Initial package
