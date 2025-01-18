Summary:	C++ interface for Clutter
Name:		cluttermm
Version:	1.17.3
Release:	26%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.gtkmm.org/
Source0:	http://download.gnome.org/sources/cluttermm/1.17/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:	atkmm-devel
BuildRequires:	clutter-devel
BuildRequires:	gtkmm30-devel
BuildRequires:	pangomm-devel
BuildRequires: make

%description
Cluttermm is a C++ interface for Clutter: a software library for creating
fast, visually rich graphical user interfaces.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package	doc
Summary:	API documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains the full API documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-silent-rules

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc COPYING NEWS
%{_libdir}/libcluttermm-1.0.so.*

%files devel
%doc examples/actor.png
%doc examples/test-actors.cc
%doc examples/test-boxes.cc
%{_libdir}/libcluttermm-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/%{name}-1.0
%{_datadir}/%{name}-1.0
%{_includedir}/%{name}-1.0

%files doc
%doc %{_docdir}/cluttermm-1.0/
%doc %{_datadir}/devhelp/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.17.3-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.17.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Kalev Lember <kalevlember@gmail.com> - 1.17.3-1
- Update to 1.17.3

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 1.17.2-1
- Update to 1.17.2
- Split out a noarch -doc subpackage, similar to other *mm packages
- Tighten -devel deps
- Don't ship huge ChangeLog file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.3-1
- Update to new upstream 1.3.3 release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.6-1
- update to 0.9.6

* Thu Apr 08 2010 Debarshi Ray <rishi@fedoraproject.org> - 0.9.5-1
- Version bump to 0.9.5.
  * Use Clutter 1.0. The pkg-config file has been renamed to cluttermm-1.0.
  * Removed deprecated Actor methods.
  * http://download.gnome.org/sources/cluttermm/0.9/cluttermm-0.9.5.news
  * http://download.gnome.org/sources/cluttermm/0.9/cluttermm-0.9.5.changes
- Added 'BuildRequires: mm-common'.
- Added 'Requires: devhelp' to cluttermm-devel.
- Dropped patch to work around Automake oddity.
- Omitted unused direct shared library dependencies.
- Install the documentation in /usr/share/clutter-devel-0.9.5/reference and
  put a symlink to it in /usr/share/clutter-1.0.
- Dropped AUTHORS and README.

* Mon Sep  7 2009 Denis Leroy <denis@poolshark.org> - 0.9.4-3.git20090907
- Updated to latest git, to compile against clutter 1.0 API
- Added patch to work around automake oddity

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.9.4-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Update to upstream 0.9.4
- API update to 0.9

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Denis Leroy <denis@poolshark.org> - 0.7.5-1
- Update to upstream 0.7.5

* Thu Jan 15 2009 Denis Leroy <denis@poolshark.org> - 0.7.4-1
- Update to upstream 0.7.4

* Mon Sep 15 2008 Denis Leroy <denis@poolshark.org> - 0.7.3-2
- Fixed devel requires

* Sun Sep  7 2008 Denis Leroy <denis@poolshark.org> - 0.7.3-1
- Update to upstream 0.7.3
- Cairo and gtk parts are forked into their own tarballs

* Tue Jun  3 2008 Denis Leroy <denis@poolshark.org> - 0.5.1-2
- fixed gtkmm BR

* Mon Jun  2 2008 Denis Leroy <denis@poolshark.org> - 0.5.1-1
- Initial version, inspired by Rick Vinyard's initial work
