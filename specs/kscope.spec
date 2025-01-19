%global commit 98db2b43124e7d0873270675bc05f4f9f90f88e5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20170716

Name:		kscope
Summary: 	QT front-end to Cscope
Version:	1.9.4
Release:	44.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
# Source0:	http://download.sourceforge.net/kscope/%{name}-%{version}.tar.gz
Source0:	https://github.com/chaoys/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:	kscope.desktop
Patch0:		kscope-strings-conflict.patch
URL:		https://github.com/chaoys/kscope
BuildRequires:	desktop-file-utils, qt5-qtbase-devel, gettext, qscintilla-qt5-devel
BuildRequires:	glib2-devel
BuildRequires: make
Requires:	cscope, ctags, graphviz

%description
KScope is a QT5 front-end to Cscope. It provides a source-editing 
environment for large C projects, such as the Linux kernel.

KScope is by no means intended to be a replacement to any of the leading 
Linux/KDE IDEs, such as KDevelop. First of all, it is not an Integrated 
Development Environment: it does not provide the usual write/compile/debug 
cycle supported by most IDE's. Instead, KScope is focused on source 
editing and analysis. 

%package devel
Summary:	Development files for kscope
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for kscope.

%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .conflicts
sed -i 's|/usr/local|%{buildroot}%{_prefix}|g' config
for i in app/app.pro core/core.pro cscope/cscope.pro editor/editor.pro; do
	sed -i 's|/lib|/%{_lib}|g' $i
done

%build
%{qmake_qt5}
# not smp-safe
make

%install
make INSTALL_ROOT=%{buildroot}%{_prefix} install
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p app/images/kscope.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%ldconfig_scriptlets

%files
%doc COPYING
%{_bindir}/kscopeapp
%{_libdir}/libkscope_core.so.*
%{_libdir}/libkscope_cscope.so.*
%{_libdir}/libkscope_editor.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/kscope.png

%files devel
%{_libdir}/libkscope_core.so
%{_libdir}/libkscope_cscope.so
%{_libdir}/libkscope_editor.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-44.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.4-43.20170716git98db2b4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-42.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-41.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-40.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-39.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-38.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-37.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-36.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-35.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-34.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-33.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-32.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-31.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.9.4-30.20170716git98db2b4
- rebuild (qscintilla)

* Sat Feb 16 2019 Björn Esser <besser82@fedoraproject.org> - 1.9.4-29.20170716git98db2b4
- rebuilt (qscintilla)

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 1.9.4-28.20170716git98db2b4
- rebuilt (qscintilla)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-27.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-26.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-25.20170716git98db2b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1.9.4-24.20170716git98db2b4
- fix FTBFS caused by use of "strings.h"

* Mon Aug  7 2017 Tom Callaway <spot@fedoraproject.org> - 1.9.4-23.20170716git98db2b4
- move to qt5 fork (upstream is gone)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.9.4-20
- rebuild (qscintilla)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.9.4-17
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-15
- rebuild (qscintilla)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-12
- rebuild (qscintilla)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-9
- rebuild (qscintilla)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-6
- rebuild (qscintilla)

* Sat May 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1.9.4-5
- rebuild (qscintilla)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9.4-3
- fix implicit DSO linking issue with libqscintilla2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9.4-1
- update to 1.9.4

* Fri Feb 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9.2-3
- add missing BR: glib2-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.9.2-1
- update to 1.9.2

* Tue Jan 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.9.1-1
- Update to 1.9.1

* Mon Jan 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.9.0-1
- update to 1.9.0, no longer depends on kde
- license change to GPLv2+

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.2-1
- update to 1.6.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.1-4
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.1-3
- drop vendor

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.1-2
- cleanups from review 

* Fri Jan 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.1-1
- Initial package for Fedora
