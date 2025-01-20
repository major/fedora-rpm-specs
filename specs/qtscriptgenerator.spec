
Name:    qtscriptgenerator
Summary: A tool to generate Qt bindings for Qt Script
Version: 0.2.0
Release: 34%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only  
URL:     http://code.google.com/p/qtscriptgenerator/	
Source0: http://qtscriptgenerator.googlecode.com/files/qtscriptgenerator-src-%{version}.tar.gz

Patch1: qtscriptgenerator-0.1.0-gcc44.patch
Patch2: qtscriptgenerator-src-0.1.0-no_phonon.patch

## upstreamable patches
Patch50: qtscriptgenerator-src-0.1.0-qmake_target.path.patch
# needs work
Patch51: qtscriptgenerator-kde_phonon443.patch
# fix arm ftbfs, kudos to mamba
Patch52: qtscriptgenerator-0.2.0-arm-ftbfs-float.patch
## debian patches
Patch60: memory_alignment_fix.diff
## fix for -Werror=format-security
Patch61: qtscriptgenerator-format_security.patch

## upstream patches

BuildRequires: make
BuildRequires: gcc-c++
# explictly BR libxslt, for xsltproc
BuildRequires: libxslt
# phonon bindings currently busted, see no_phonon patch
#BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtSql)
BuildRequires: pkgconfig(QtSvg)
BuildRequires: pkgconfig(QtUiTools)
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(QtXml)
BuildRequires: pkgconfig(QtXmlPatterns)

# not strictly required, but the expectation would be for the 
# bindings to be present
Requires: qtscriptbindings = %{version}-%{release}

%description
Qt Script Generator is a tool to generate Qt bindings for Qt Script.

%package -n qtscriptbindings 
Summary: Qt bindings for Qt Script
Provides: qtscript-qt = %{version}-%{release}
%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}
%description -n qtscriptbindings
Bindings providing access to substantial portions of the Qt API
from within Qt Script.


%prep
%setup -q -n %{name}-src-%{version}

%patch -P1 -p0 -b .gcc44
%patch -P2 -p1 -b .no_phonon

%patch -P50 -p1 -b .qmake_target.path
%patch -P51 -p1 -b .kde_phonon
# I *think* we can do this unconditionally, but I'd like to
# investigate more in-depth first
%ifarch %{arm}
%patch -P52 -p1 -b .arm_ftbfs_float
%endif

%patch -P60 -p1 -b .memory_alignment
%patch -P61 -p1 -b .format_security


%build

# workaround buildsys bogosity, see also:
# http://code.google.com/p/qtscriptgenerator/issues/detail?id=38
export INCLUDE=%{_qt4_headerdir}

pushd generator 
%{qmake_qt4}
%make_build
./generator
popd

pushd qtbindings
%{qmake_qt4}
%make_build
popd

pushd tools/qsexec/src
%{qmake_qt4}
%make_build
popd


%install
mkdir -p %{buildroot}%{_qt4_plugindir}/script/
# install doesn't do symlinks
cp -a plugins/script/libqtscript* \
  %{buildroot}%{_qt4_plugindir}/script/

cp -a tools/qsexec/README.TXT README.qsexec
install -D -p -m755 tools/qsexec/qsexec %{buildroot}%{_bindir}/qsexec

install -D -p -m755 generator/generator %{buildroot}%{_qt4_bindir}/generator


%files
%{_qt4_bindir}/generator

%files -n qtscriptbindings
%doc README
%doc README.qsexec 
%doc doc/
%doc examples/
%license LICENSE.LGPL LGPL_EXCEPTION.txt
%{_bindir}/qsexec
%{_qt4_plugindir}/script/libqtscript_core.so*
%{_qt4_plugindir}/script/libqtscript_gui.so*
%{_qt4_plugindir}/script/libqtscript_network.so*
%{_qt4_plugindir}/script/libqtscript_opengl.so*
#{_qt4_plugindir}/script/libqtscript_phonon.so*
%{_qt4_plugindir}/script/libqtscript_sql.so*
%{_qt4_plugindir}/script/libqtscript_svg.so*
%{_qt4_plugindir}/script/libqtscript_uitools.so*
%{_qt4_plugindir}/script/libqtscript_webkit.so*
%{_qt4_plugindir}/script/libqtscript_xml.so*
%{_qt4_plugindir}/script/libqtscript_xmlpatterns.so*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-33
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-19
- rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-16
- BR: gcc-c++, use %%license %%make_build
- qtscriptgenerator: FTBFS in F28 (#1556303)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-11
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-3
- pkgconfig-style deps

* Thu May 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-2
- arm_ftbfs_float patch (from mamba)

* Tue May 01 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-1
- 0.2.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-18
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-16
- fix qt-4.8 build, omit failing QFileOpenEvent code

* Wed Nov 16 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-15
- rebuild for qt48

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-13
- disable/omit phonon binding for now (#660852)

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-12
- BR: qt4-webkit-devel

* Mon Mar 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-11
- borrow memory_alignment_fix.diff from debian (should help arm/sparc)

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-10 
- rebuild (qt-4.6.0-rc1, fc13+)

* Mon Oct 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-9
- fix build (for qt-4.6.0/phonon-isms)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-7
- upstream sun_issue27 patch

* Fri Apr 10 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-6
- qtscriptbindings: Provides: qtscript-qt ...

* Tue Mar 24 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-5
- qtscriptgenerator/qtscriptbindings pkgs 
- qtscriptbindings: include docs, examples

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-4
- include qsexec

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-3
- BR: phonon-devel

* Fri Mar 20 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-2
- qt-4.5.0-7 fixed wrt phonon, drop no_phonon patch

* Fri Mar 06 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-1
- first try

