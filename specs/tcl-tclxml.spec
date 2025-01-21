%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}
%define realname tclxml

Summary: XML parsing library for the Tcl scripting language
Name:    tcl-%{realname}
Version: 3.2
Release: 38%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     http://tclxml.sourceforge.net/
Source0: http://downloads.sourceforge.net/tclxml/tclxml-%{version}.tar.gz
Source1: pkgIndex.tcl.in.gui
Patch0:  tclxml-3.2-sgmlparser.patch
Patch1:  tclxml-3.2-xmlGenericError.patch
Patch2:  tcl-tclxml-libxml2-init.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  tcl-devel libxml2-devel libxslt-devel
Obsoletes:      tclxml < 3.2
Obsoletes:      tclxml-devel < 3.2
Obsoletes:      tclxml-libxml2 < 3.2
Obsoletes:      tclxml-expat < 3.2
Obsoletes:      tcldom < 3.2
Obsoletes:      tcldom-devel < 3.2
Obsoletes:      tcldom-expat < 3.2
Obsoletes:      tcldom-libxml2 < 3.2
Provides:       tclxml = %{version}-%{release}
Provides:       tcldom = %{version}-%{release}
Provides:       tclxslt = %{version}-%{release}
Requires:       tcl(abi) = 8.6 tcllib

%description
TclXML is a package that provides XML, DOM, and XSLT parsing for the
Tcl scripting language.

%package devel
Summary: Development files for the tclxml packages
Requires:       %{name} = %{version}-%{release}
Provides: tclxml-devel = %{version}-%{release}
Provides: tcldom-devel = %{version}-%{release}
%description devel
Development header files for the tclxml packages.  This includes all of the
header files for the tclxml, tcldom, and tclxslt packages

%package gui
Summary: UI widgets for manipulating a DOM tree
Requires: %{name} = %{version}-%{release} bwidget
Obsoletes: tcldom-gui = %{version}-%{release}
Provides: tcldom-gui = %{version}-%{release}
%description gui
This package provides some useful widgets for manipulating a DOM tree.

%prep
%setup -q -n %{realname}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# Fix a few spurious execute permissions
chmod -x ChangeLog doc/xsltsl/cmp.xsl *.c

# Clean up some DOS line endings
sed -i -e 's/\r//' doc/README.xml.in

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{tcl_sitearch}
mv $RPM_BUILD_ROOT%{_libdir}/Tclxml%{version} $RPM_BUILD_ROOT%{tcl_sitearch}/%{realname}-%{version}

chmod a-x $RPM_BUILD_ROOT%{tcl_sitearch}/%{realname}-%{version}/*.a

# Install the examples in a -gui subpackage
install -d $RPM_BUILD_ROOT%{tcl_sitelib}/%{realname}-gui%{version}
sed -e 's/@VERSION@/%{version}/' < %{SOURCE1} > $RPM_BUILD_ROOT/%{tcl_sitelib}/%{realname}-gui%{version}/pkgIndex.tcl
install -p -m 0644 examples/tcldom/domtree.tcl \
        examples/tcldom/domtree-treectrl.tcl \
        examples/tcldom/domtext.tcl \
        examples/tcldom/cgi2dom.tcl \
        $RPM_BUILD_ROOT%{tcl_sitelib}/%{realname}-gui%{version}/

%check
# The test suite fails to run properly from the build directory.
#make test

%files
%dir %{tcl_sitearch}/%{realname}-%{version}
%{tcl_sitearch}/%{realname}-%{version}/*.so
%{tcl_sitearch}/%{realname}-%{version}/*.tcl
%doc LICENSE ANNOUNCE ChangeLog README.html
%doc doc/*.html

%files devel
%{_includedir}/tclxml
%{_libdir}/TclxmlConfig.sh
%{tcl_sitearch}/%{realname}-%{version}/*.a

%files gui
%dir %{tcl_sitelib}/%{realname}-gui%{version}
%{tcl_sitelib}/%{realname}-gui%{version}/*.tcl

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2-37
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 3.2-32
- Avoid call to undeclared Tcldom_libxml2_Init function

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 3.2-22
- Fix FTBFS: tclxml-3.2-xmlGenericError.patch added.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2-13
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Wart <wart at kobold.org> - 3.2-4
- Add additional Provides: and Obsoletes: to properly replace the old
  tclxml/tcldom packages

* Sun Dec 21 2008 Wart <wart at kobold.org> - 3.2-3
- Don't use a macro for the version in Obsoletes:

* Thu Dec 18 2008 Wart <wart at kobold.org> - 3.2-2
- Remove execute permission from stub library

* Wed Dec 17 2008 Wart <wart at kobold.org> - 3.2-1
- Update to 3.2
- Rename package to conform with Fedora Tcl packaging guidelines

* Wed Dec 17 2008 Wart <wart at kobold.org> - 3.1-14
- Fix parsing of stylesheet entity (BZ #474766)
- Remove package name from Summary

* Sat Feb 8 2008 Wart <wart at kobold.org> - 3.1-13
- Better download URL
- rebuild for gcc 4.3

* Thu Jan 3 2008 Wart <wart at kobold.org> - 3.1-12
- Rebuild for Tcl 8.5

* Sun Feb 4 2007 Wart <wart at kobold.org> - 3.1-11
- Move package directory back to %%{_libdir} until %%{tcl_sitearch}
  is part of the default package search path in Tcl.

* Fri Feb 2 2007 Wart <wart at kobold.org> - 3.1-10
- Fix sgmlparser version mismatch
- Move package directories to tcl-specific directories

* Mon Aug 28 2006 Wart <wart at kobold.org> - 3.1-9
- Rebuild for Fedora Extras

* Thu Jun 1 2006 Wart <wart at kobold.org> - 3.1-8
- Fixed Requires: for subpackages

* Tue Feb 21 2006 Wart <wart at kobold.org> - 3.1-7
- Rebuild for FC5

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.1-6
- Remove broken parts of patch
- Clean up build root before installing.

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.1-5
- Added missing ChangeLog entries.

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.1-4
- Retag to fix tag problem.

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.1-3
- Updated patch to fix quoting bug with bash >= 3.1

* Sun Jan 8 2006 Wart <wart at kobold.org> - 3.1-2
- Package now owns the directories that it creates.

* Sat Nov 26 2005 Wart <wart at kobold.org> - 3.1-1
- Update to new upstream sources.

* Sat Nov 26 2005 Wart <wart at kobold.org> - 3.0-3
- Remove dependency on dos2unix with clever sed command.

* Fri Nov 25 2005 Wart <wart at kobold.org> - 3.0-2
- Fix file permissions to clean up rpmlint warnings.
- Add BR: dos2unix to remove DOS line endings on a documentation file.
- Other minor fixes to clean up rpmlint warnings.

* Fri Jun 17 2005 Wart <wart at kobold.org> - 3.0-1
- Updated spec file to conform to Fedora Core 4 standards.
- Move autoreconf from the build to the prep stage.

* Tue Jan 18 2005 Wart <wart at kobold.org> - 3.0-0.fdr.5
- Fix typo in version string for subpackage dependencies.
- Don't include the .a library in the base package.

* Fri Nov 5 2004 Wart <wart at kobold.org> - 3.0-0.fdr.4
- Add epoch to version dependencies in spec file.
- Added additional doc files.

* Thu Nov 4 2004 Wart <wart at kobold.org> - 3.0-0.fdr.3
- enable building on x86_64

* Thu Nov 4 2004 Wart <wart at kobold.org> - 3.0-0.fdr.2
- Clean up rpmlint warnings.

* Thu Nov 4 2004 Wart <wart at kobold.org> - 3.0-0.fdr.1
- Added Fedora-style spec file.
- Allow building generic RPMs from the Makefile.
- Fix VPATH problems with newer versions of autoconf tools.
