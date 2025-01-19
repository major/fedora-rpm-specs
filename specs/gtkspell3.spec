Name:           gtkspell3
Version:        3.0.10
Release:        22%{?dist}
Summary:        On-the-fly spell checking for GtkTextView widgets

License:        GPL-2.0-or-later
URL:            https://gtkspell.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gtkspell/gtkspell3-%{version}.tar.xz

BuildRequires:  enchant2-devel
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  make
BuildRequires:  vala

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-gettext
BuildRequires: mingw32-gtk3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-gettext
BuildRequires: mingw64-gtk3

Requires:       iso-codes

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use GtkSpell API version 3.0.


%package -n mingw32-%{name}
Summary:       MinGW Windows GtkSpell3 library
Obsoletes:     mingw32-%{name}-static
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GtkSpell3 library.


%package -n mingw64-%{name}
Summary:       MinGW Windows GtkSpell3 library
Obsoletes:     mingw64-%{name}-static
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GtkSpell3 library.


%{?mingw_debug_package}


%prep
%autosetup -p1


%build
# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static --enable-vala --enable-gtk-doc
%make_build V=1
popd

# MinGW build
%mingw_configure --disable-static
%mingw_make_build


%install
%make_install -C build_native
%mingw_make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang gtkspell3
cat gtkspell3.lang | grep -v mingw32 > gtkspell3_native.lang
%mingw_find_lang %{name}


%mingw_debug_install_post


%files -f gtkspell3_native.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib
%{_libdir}/libgtkspell3-3.so.*

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/gtkspell-3.0/
%{_libdir}/libgtkspell3-3.so
%{_libdir}/pkgconfig/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%{_datadir}/vala/vapi/gtkspell3-3.0.deps

%files -n mingw32-%{name} -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/libgtkspell3-3-0.dll
%{mingw32_includedir}/gtkspell-3.0/
%{mingw32_libdir}/libgtkspell3-3.dll.a
%{mingw32_libdir}/pkgconfig/gtkspell3-3.0.pc

%files -n mingw64-%{name} -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/libgtkspell3-3-0.dll
%{mingw64_includedir}/gtkspell-3.0/
%{mingw64_libdir}/libgtkspell3-3.dll.a
%{mingw64_libdir}/pkgconfig/gtkspell3-3.0.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 3.0.10-20
- Rebuild (enchant2)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Sandro Mani <manisandro@gmail.com> - 3.0.10-15
- Exclude mingw lang files from native package

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.0.10-13
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 3.0.10-12
- Make mingw subpackages noarch

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 3.0.10-11
- Add mingw subpackages

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.0.10-3
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Sandro Mani <manisandro@gmail.com> - 3.0.10-1
- Update to 3.0.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.9-1
- Update to 3.0.9

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.8-1
- Update to 3.0.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Sandro Mani <manisandro@gmail.com> - 3.0.7-1
- Update to 3.0.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.6-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Sandro Mani <manisandro@gmail.com> - 3.0.6-1
- Update to 3.0.6

* Sat Apr 19 2014 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Thu Sep 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.3-2
- Add iso-codes requires and iso-codes-devel BR

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Thu Mar 07 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-2
- Merge -vala into -devel package

* Wed Mar 06 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2
- Adds vala bindings

* Sat Feb 09 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Thu Nov 15 2012 Kalev Lember <kalevlember@gmail.com> - 3.0.0-1
- Initial gtkspell3 packaging, based on Fedora's gtkspell package
