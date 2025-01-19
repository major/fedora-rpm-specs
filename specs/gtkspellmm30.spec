%bcond mingw 1

Name:          gtkspellmm30
Version:       3.0.5
Release:       26%{?dist}
License:       GPL-2.0-or-later
Summary:       On-the-fly spell checking for GtkTextView widgets - C++ bindings
URL:           http://gtkspell.sourceforge.net/
Source0:       http://sourceforge.net/projects/gtkspell/files/gtkspellmm/gtkspellmm-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: gtkspell3-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtkmm30-doc
BuildRequires: make

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-glibmm24
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw32-gtkspell3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-glibmm24
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw64-gtkspell3
%endif


%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package       devel
Summary:       Development files for gtkspellmm30
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The gtkspellmm30-devel package provides header and documentation files for
developing C++ applications which use GtkSpell.

%package       doc
Summary:       Documentation for %{name}
BuildArch:     noarch
Requires:      gtkmm30-doc

%description   doc
This package contains the full API documentation for %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows GtkSpellmm library
Obsoletes:     mingw32-%{name}-static
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GtkSpellmm library.


%package -n mingw64-%{name}
Summary:       MinGW Windows GtkSpellmm library
Obsoletes:     mingw64-%{name}-static
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GtkSpellmm library.
%endif


%{?mingw_debug_package}


%prep
%autosetup -n gtkspellmm-%{version}


%build
# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure
%make_build
popd

%if %{with mingw}
# MinGW build
%mingw_configure --disable-documentation
%mingw_make_build
%endif


%install
%make_install -C build_native
%if %{with mingw}
%mingw_make_install
%endif

find %{buildroot} -name "*.la" -exec rm {} \;


%{?mingw_debug_install_post}


%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/libgtkspellmm-3.0.so.0*

%files devel
%{_includedir}/gtkspellmm-3.0
%{_libdir}/libgtkspellmm-3.0.so
%{_libdir}/pkgconfig/gtkspellmm-3.0.pc
%{_libdir}/gtkspellmm-3.0

%files doc
%license COPYING
%{_datadir}/devhelp/books/gtkspellmm-3.0
%{_datadir}/doc/gtkspellmm-3.0

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libgtkspellmm-3.0-0.dll
%{mingw32_includedir}/gtkspellmm-3.0/
%{mingw32_libdir}/gtkspellmm-3.0/
%{mingw32_libdir}/libgtkspellmm-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtkspellmm-3.0.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libgtkspellmm-3.0-0.dll
%{mingw64_includedir}/gtkspellmm-3.0/
%{mingw64_libdir}/gtkspellmm-3.0/
%{mingw64_libdir}/libgtkspellmm-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtkspellmm-3.0.pc
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Orion Poplawski <orion@nwra.com> - 3.0.5-21
- Change BR to mingw*-gcc-c++

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.0.5-18
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 3.0.5-17
- Make mingw subpackages noarch

* Sun Feb 20 2022 Sandro Mani <manisandro@gmail.com> - 3.0.5-16
- Add mingw subpackages

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 3.0.5-8
- Rebuild (gtkspell3)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.0.5-6
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Tue Apr 05 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-2
- Respin

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Sandro Mani <manisandro@gmail.com> - 3.0.3-4
- Rebuild for GCC5 ABI change
- Modernize spec file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri Apr 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- New upstream release (uses correct GPLv2 license headers)

* Fri Mar 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.0-1
- Initial package.
