
Name:    qt-at-spi
Version: 0.3.1
Release: 26%{?dist}
Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2 

License: LGPLv2+
URL:     https://gitorious.org/qt-at-spi
%if 0%{?snap:1}
# git clone git://gitorious.org/qt-at-spi/qt-at-spi.git; cd qt-at-spi
# git archive master --prefix=qt-at-spi/ | xz > qt-at-spi-%{snap}.tar.xz
Source0: qt-at-spi-%{snap}.tar.xz
%else
# https://gitorious.org/qt-at-spi/qt-at-spi/archive-tarball/v%{version}
Source0: qt-at-spi-qt-at-spi-v%{version}.tar.gz
%endif

Source1: qt-at-spi.sh

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(QtDBus) >= 4.8.0
BuildRequires: pkgconfig(QtGui) pkgconfig(QtXml)

%{?_qt4:Requires: %{_qt4}%{?_isa} >= %{_qt4_version}}

%description
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%setup -q -n %{name}-%{name}

install -m644 -p %{SOURCE1} .


%build
%{qmake_qt4}
%make_build

# build docs
pushd doc
qdoc3 qatspi.qdocconf
popd


%install
make install INSTALL_ROOT=%{buildroot}


%files
%doc README
%doc qt-at-spi.sh
%license LICENSE
%dir %{_qt4_plugindir}/accessiblebridge/
%{_qt4_plugindir}/accessiblebridge/libqspiaccessiblebridge.so

%files doc
# install these under %{_qt4_docdir}? --rex
%doc doc/html/*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-15
- BR: gcc-c++, use %%license %%make_build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-10
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.1-3
- include sample qt-at-spi.sh shell fragment

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jaroslav Reznik <jreznik@redhat.com> 0.3.1-1
- 0.3.1, fixes accessing invalid objects

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- 0.3.0

* Tue Apr 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2-2
- License: LGPLv2+
- -doc subpkg

* Wed Mar 14 2012 Rex Dieter <rdieter@fedoraproject.org> 0.2-1
- 0.2

* Thu Jan 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.1.1-1
- 0.1.1

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1-1
- 0.1 release

* Tue Oct 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.0-0.1.20111025
- first try


