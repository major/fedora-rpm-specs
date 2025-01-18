Name:           coldet
Version:        1.2
Release:        37%{?dist}
Summary:        3D Collision Detection Library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://coldet.sourceforge.net/
Source0:        http://downloads.sourceforge.net/coldet/coldet12.zip
Patch0:         coldet-1.1-fixes.patch
Patch1:         coldet-1.2-gcc46.patch

BuildRequires:  gcc-c++
BuildRequires: make
%description
This library is an effort to provide a free collision detection library for
generic polyhedra. Its purpose is mainly for 3D games where accurate detection
is needed between two non-simple objects.

Features:
    * Works on any model, even polygon soups.
    * Uses bounding box hierarchies for fast detection.
    * Uses additional triangle intersection tests for 100% accuracy.
    * Provides (upon request) exact point of collision, plus the pair of
      triangles that collided.
    * Supports timeout setting, to limit detection time.
    * Model-Model collision test.
    * Ray-Model collision test.
    * Segment-Model collision test.
    * Sphere-Model collision test.
    * Ray-Sphere and Sphere-Sphere primitive collision tests.


%package devel
Summary: Development libraries and headers for coldet
Requires: %{name} = %{version}-%{release}

%description devel
The developmental files that must be installed in order to compile
applications which use coldet.


%prep
%setup -q -n %{name}
%patch -P0 -p1 -z .fixes
%patch -P1 -p1
# for %doc
sed -i 's/\r//' readme.txt COPYING doc/quickstart.html doc/html/{*.html,*.css}
mv doc/quickstart.html doc/html


%build
pushd src
make %{?_smp_mflags} -f makefile.g++ OPT="$RPM_OPT_FLAGS"
popd


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 755 src/lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 src/coldet.h src/math3d.h $RPM_BUILD_ROOT%{_includedir}/%{name}



%ldconfig_scriptlets


%files
%doc COPYING readme.txt
%{_libdir}/lib%{name}.so.0

%files devel
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Feb 13 2011 Hans de Goede <hdegoede@redhat.com> - 1.2-8
- Fix building with gcc-4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-3
- Fix Source0 URL

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-2
- Update License tag for new Licensing Guidelines compliance

* Sun May 20 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2-1
- New upstream release 1.2
- Fix URL field (bz 240645)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-4
- FE6 Rebuild

* Fri Jul  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-3
- Make -devel package Requires on the main package fully versioned.

* Mon Jun 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-2
- Put headers under /usr/include/coldet instead of straight under /usr/include.

* Mon Jun 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-1
- Initial Fedora Extras package
