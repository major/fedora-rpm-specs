Name:           AllegroOGG
Version:        1.0.3
Release:        37%{?dist}
Summary:        Ogg library for use with the Allegro game library
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.allegro.cc/resource/Libraries/Audio/alogg
Source0:        http://www.hero6.com/filereviver/alogg.zip
Source1:        AllegroOGG.pc.in
BuildRequires:  gcc
BuildRequires:  allegro-devel libvorbis-devel

%description
%{name} is an Allegro wrapper for the Ogg Vorbis decoder from the Xiph.org
foundation. This lib lets you play OGGs and convert OGGs to Allegro SAMPLEs
amongst a lot of other capabilites.


%package devel
Summary:        Developmental libraries and include files for AllegroOgg
Requires:       %{name} = %{version}-%{release}
Requires:       allegro-devel

%description devel
Development libraries and include files for developing applications using
the %{name} library.


%prep
%setup -q -c
%{__sed} -i 's/\r//' docs/A*.txt
%{__sed} -e "s#@prefix@#%{_prefix}#g" -e "s#@libdir@#%{_libdir}#g" \
  -e "s#@includedir@#%{_includedir}#g" -e "s#@version@#%{version}#g" \
  -e "s#@name@#%{name}#" %{SOURCE1} > %{name}.pc

%build
# makefile doesn't support creating an .so, and wants to use its own version
# of libogg and libvorbis and there is only one source file so lets DIY
gcc $RPM_OPT_FLAGS -fPIC -DPIC -Iinclude -c src/alogg.c -o src/alogg.o
gcc -g -shared -Wl,-soname=lib%{name}.so.0 -o lib%{name}.so.0 \
  src/alogg.o -logg -lvorbis -lvorbisfile $(allegro-config --libs)


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -m 755 lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig

mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 644 include/* $RPM_BUILD_ROOT%{_includedir}/%{name}


%ldconfig_scriptlets


%files
%doc docs/*.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Hans de Goede <hdegoede@redhat.com> - 1.0.3-8
- Rebuilt for new allegro-4.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-4
- Autorebuild for GCC 4.3

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-3
- FE6 Rebuild

* Sat Apr 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-2
- Rename .so file from liballog.so(.0) to libAllegroOGG.so(.0) and put the
  headers in /usr/include/AllegroOGG to avoid any future conflicts with the
  (unpackaged) alogg library which unsurprisingly installs libalogg.so too.
- Add a pkgconfig file to allow apps to get the proper CFLAGS and LIBS for
  this change. (bz 188625)

* Tue Apr 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.3-1
- Initial spec file
