Name:           alfont
Version:        2.0.9
Release:        30%{?dist}
Summary:        Font rendering library for the Allegro game library
License:        FTL
URL:            http://chernsha.sitesled.com/
# this is http://chernsha.sitesled.com/AlFont209.rar repackaged in .tgz format
Source0:        %{name}-%{version}.tar.gz
Patch0:         alfont-2.0.9-linux.patch
Patch1:         alfont-2.0.9-remove-alfont_get_string.patch
Patch2:         alfont-2.0.9-build-fixes.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel freetype-devel

%description
alfont also known as AllegroFont or AlFont is a wrapper around the freetype2
library for use with the Allegro game library. Thus allowing the display of
text using freetype fonts on Allegro bitmaps.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       allegro-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
for i in include/alfont*.h freetype/docs/FTL.TXT; do
    sed -i.orig s'/\r//g' $i
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.utf8
    mv $i.utf8 $i
    touch -r $i.orig $i
done


%build
# Upstreams makefile uses its own private copy of freetype, since all
# we want is the wrapper and since the wrapper is only one file we
# do a manual compile here
gcc -fPIC -DPIC $RPM_OPT_FLAGS -Iinclude `freetype-config --cflags` \
  -o src/alfont.o -c src/alfont.c
gcc -shared -Wl,-soname,lib%{name}.so.2 -o lib%{name}.so.%{version} \
  $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  src/alfont.o $(freetype-config --libs) $(allegro-config --libs)


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.2
ln -s lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 include/%{name}*.h $RPM_BUILD_ROOT%{_includedir}


%ldconfig_scriptlets


%files
%doc CHANGES.txt README.txt
%license freetype/docs/FTL.TXT
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Hans de Goede <hdegoede@redhat.com> - 2.0.9-28
- Fix FTBFS (rhbz#2260975)
- Use distro LD_FLAGS when linking

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Hans de Goede <hdegoede@redhat.com> - 2.0.9-3
- Fix undefined reference to _msize

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Hans de Goede <hdegoede@redhat.com> - 2.0.9-1
- New upstream release 2.0.9

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 2.0.6-8
- Rebuild for new allegro-4.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.6-4
- Autorebuild for GCC 4.3

* Wed Sep  5 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.6-3
- Update license tag

* Sun Dec  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.6-2
- Link the .so file with allegro (bz 217998)
- Add "Requires: allegro-devel" to the -devel subpackage

* Thu Nov 30 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 2.0.6-1
- Initial FE package
