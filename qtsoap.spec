Name:           qtsoap
Version:        2.7
Release:        29%{?dist}
Summary:        The Simple Object Access Protocol Qt4-based client side library

License:        LGPLv2 with exceptions or GPLv3
URL:            http://qt.gitorious.org/qt-solutions/qt-solutions/trees/master/qtsoap
Source0:        http://get.qt.nokia.com/qt/solutions/lgpl/qtsoap-%{version}_1-opensource.tar.gz
Patch0:         qtsoap-2.7_1-opensource-install-pub-headers.patch
Patch1:		qtsoap-2.7_1-qt5-cleanups.patch
BuildRequires: make
BuildRequires:  qt5-qtbase-devel qt4-devel

%description
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.
This package is built against Qt4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package -n qtsoap5
Summary:	The Simple Object Access Protocol Qt5-based client side library

%description -n qtsoap5
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.
This package is built against Qt5.

%package -n qtsoap5-devel
Summary:        Development files for qtsoap5
Requires:	qtsoap5%{?_isa} = %{version}-%{release}

%description -n qtsoap5-devel
Development files for qtsoap5.

%prep
%setup -q -c -n %{name}
# headers are not installed for shared library
%patch0 -p0 -b .install-pub-headers
# Fix build for qt5
%patch1 -p0 -b .qt5

sed -i 's:$$DESTDIR:%{_libdir}:g' qtsoap-%{version}_1-opensource/buildlib/buildlib.pro

cp -a qtsoap-%{version}_1-opensource qtsoap5-%{version}_1-opensource

%build
pushd qtsoap-%{version}_1-opensource
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri
echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%{version}" >> common.pri

%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags} CXXFLAGS="%{optflags} -fPIC"
popd

pushd qtsoap5-%{version}_1-opensource
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri
echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap5)" >> common.pri
echo "VERSION=%{version}" >> common.pri

%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags} CXXFLAGS="%{optflags} -fPIC -DQT_DISABLE_DEPRECATED_BEFORE=0x000000"
popd

%install
pushd qtsoap-%{version}_1-opensource
make INSTALL_ROOT=%{buildroot} install
popd

pushd qtsoap5-%{version}_1-opensource
make INSTALL_ROOT=%{buildroot} install
popd

%ldconfig_scriptlets

%ldconfig_scriptlets -n %{name}5

%files
%doc qtsoap-%{version}_1-opensource/README.TXT 
%license qtsoap-%{version}_1-opensource/LGPL_EXCEPTION.txt 
%license qtsoap-%{version}_1-opensource/LICENSE.GPL3 
%license qtsoap-%{version}_1-opensource/LICENSE.LGPL
%{_qt4_libdir}/libqtsoap.so.2*

%files devel
%{_qt4_libdir}/libqtsoap.so
%{_qt4_headerdir}/QtSoap/

%files -n %{name}5
%doc qtsoap5-%{version}_1-opensource/README.TXT 
%license qtsoap5-%{version}_1-opensource/LGPL_EXCEPTION.txt 
%license qtsoap5-%{version}_1-opensource/LICENSE.GPL3 
%license qtsoap5-%{version}_1-opensource/LICENSE.LGPL
%{_qt5_libdir}/libqtsoap5.so.2*

%files -n %{name}5-devel
%{_qt5_libdir}/libqtsoap5.so
%{_qt5_headerdir}/QtSoap/


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Tom Callaway <spot@fedoraproject.org> - 2.7-15
- build qt5 variant

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.7-12
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.7-7
- qtsoap: URL in spec file is outdated (#955258)
- devel: use arch'd dep
- track soname

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Jaroslav Reznik <jreznik@redhat.com> - 2.7-2
- libqtsoap library name

* Thu May 19 2011 Jaroslav Reznik <jreznik@redhat.com> - 2.7-1
- fix version

* Tue Oct 26 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.7-1
- Initial spec file
