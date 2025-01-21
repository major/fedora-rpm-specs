%global         _hardened_build 1

%define underscore_version 2_6_2

Name:           tinyxml
Version:        2.6.2
Release:        31%{?dist}
Summary:        A simple, small, C++ XML parser
License:        zlib
URL:            http://www.grinninglizard.com/tinyxml/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{underscore_version}.tar.gz
Source1:        tinyxml.pc.in
Patch0:         tinyxml-2.5.3-stl.patch
# https://sourceforge.net/p/tinyxml/patches/_discuss/thread/fa2235db/f16d/attachment/entity.patch
Patch1:         tinyxml-issue51.patch
Patch2:         https://sources.debian.org/data/main/t/tinyxml/2.6.2-6.1/debian/patches/CVE-2021-42260.patch
Patch3:         https://sources.debian.org/data/main/t/tinyxml/2.6.2-6.1/debian/patches/CVE-2023-34194.patch

BuildRequires:  gcc-c++

%description
TinyXML is a simple, small, C++ XML parser that can be easily integrating
into other programs. Have you ever found yourself writing a text file parser
every time you needed to save human readable data or serialize objects?
TinyXML solves the text I/O file once and for all.
(Or, as a friend said, ends the Just Another Text File Parser problem.)


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}


%build
%{set_build_flags}
mv changes.txt changes.txt-orig
iconv -f ISO-8859-1 -t UTF-8 changes.txt-orig > changes.txt
rm -f changes.txt-orig
# Not really designed to be build as lib, DYI
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
  ${CXX} $RPM_OPT_FLAGS -fPIC -o $i.o -c $i
done
${CXX} $RPM_LD_FLAGS -shared -o lib%{name}.so.0.%{version} \
   -Wl,-soname,lib%{name}.so.0 *.cpp.o


%install
rm -rf $RPM_BUILD_ROOT
# Not really designed to be build as lib, DYI
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -p -m 644 %{name}.h $RPM_BUILD_ROOT%{_includedir}

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
 -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
 -e 's![@]libdir[@]!%{_libdir}!g' \
 -e 's![@]includedir[@]!%{_includedir}!g' \
 -e 's![@]version[@]!%{version}!g' \
 %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc


%check
%{set_build_flags}
${CXX} $RPM_OPT_FLAGS -DTIXML_USE_STL -fPIE -ltinyxml -L%{buildroot}%{_libdir} -o xmltest xmltest.cpp
chmod +x xmltest
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./xmltest


%files
%doc changes.txt readme.txt
%{_libdir}/*.so.*

%files devel
%doc docs/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Dominik Mierzejewski <dominik@greysector.net> - 2.6.2-28
- apply Debian patch to fix CVE-2021-42260 (rhbz#2253716, rhbz#2253718)
- apply Debian patch to fix CVE-2023-34194 and its duplicate, CVE-2023-40462
  (rhbz#2254376, rhbz#2254381)
- fix incorrect text element encoding (upstream isssue #51)
- compile and run tests

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 2.6.2-16
- Use LDFLAGS from redhat-rpm-config

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.2-9
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.2-8
- Rebuilt for GCC 5 ABI change

* Fri Jan 09 2015 François Cami <fcami@fedoraproject.org> - 2.6.2-7
- Use PIC.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Scott K Logan <logans@cottsay.net> - 2.6.2-4
- Fix wrong pkgconfig path

* Sat Mar 01 2014 Scott K Logan <logans@cottsay.net> - 2.6.2-3
- Add basic pkgconfig

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 17 2013 François Cami <fcami@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2
- Fix changes.txt encoding

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.6.1-1
- Updated to 2.6.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.3-3
- Autorebuild for GCC 4.3

* Fri Dec 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.5.3-2
- Various improvements from review (bz 407571)

* Fri Nov 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.5.3-1
- Initial Fedora Package
