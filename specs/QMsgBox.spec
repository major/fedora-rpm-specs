%global commit 94677dc52fe1c2ea6fe42bd5acdbddab755eeb0b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner croscato

Name:           QMsgBox
Version:        0
Release:        29.20130830git%{shortcommit}%{?dist}
Summary:        Solves a problem that prevents qt message icons from being displayed
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.qtcentre.org/wiki/index.php?title=QMsgBox_%28Solves_the_QMessageBox_icon_problem%29
Source0:        https://github.com/croscato/QMsgBox/tarball/%{commit}/%{owner}-%{name}-%{shortcommit}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel

%description
QMsgBox is a class that inherits QMessageBox to replace the static
functions:
* QMessageBox::warning
* QMessageBox::information
* QMessageBox::critical
* QMessageBox::question 

All other functions remain the same. The usage of the replaced
function also remains the same.

The objective of this class is to solve a problem that prevents the
message icon from being displayed in some platforms with some Qt
styles.


%package devel
Summary:        Development libraries for QMsgBox
Provides:       %{name}(devel) =  %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}

%description devel
This package contains the development libraries necessary
for compiling code against QMsgBox.


%package headers
Summary:        Development headers for QMsgBox
Requires:       %{name}(devel) = %{version}-%{release}
BuildArch:      noarch

%description headers
This package contains the development headers necessary
for compiling code against QMsgBox.


%package        qt5
Summary:        Qt5 version of %{name}
Requires:       qt5-qtbase%{?_isa}

%description    qt5
QMsgBox is a class that inherits QMessageBox to replace the static
functions:
* QMessageBox::warning
* QMessageBox::information
* QMessageBox::critical
* QMessageBox::question 

All other functions remain the same. The usage of the replaced
function also remains the same.

The objective of this class is to solve a problem that prevents the
message icon from being displayed in some platforms with some Qt
styles.


%package        qt5-devel
Summary:        Development files for %{name} using Qt5
Provides:       %{name}(devel) =  %{version}-%{release}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    qt5-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} and Qt5.


%prep
%setup -q -n %{owner}-%{name}-%{shortcommit}
# Plug in correct install path
sed -i "s|target.path = .*|target.path = %{buildroot}%{_libdir}|g" src/src.pro
# Fix EOL encoding
for f in LICENSE.GPL3; do
    sed 's|\r||g' $f > $f.new && \
        touch -r $f $f.new && \
        mv $f.new $f
done
# Fix file permissions
find . -type f -exec chmod 644 {} \;

# Create Qt5 dir
rm -rf ../%{owner}-%{name}-%{shortcommit}-qt5
cp -a ../%{owner}-%{name}-%{shortcommit} ../%{owner}-%{name}-%{shortcommit}-qt5
sed -i -e 's/TARGET = QMsgBox/TARGET = QMsgBox-qt5/' ../%{owner}-%{name}-%{shortcommit}-qt5/src/src.pro

%build
%{qmake_qt4}
make %{?_smp_mflags}

cd ../%{owner}-%{name}-%{shortcommit}-qt5
%{qmake_qt5}
make %{?_smp_mflags}

%install
make install
make -C ../%{owner}-%{name}-%{shortcommit}-qt5 install

# Install header file
install -D -p -m 644 src/qmsgbox.h %{buildroot}%{_includedir}/qmsgbox.h
# and symlink
ln -s %{_includedir}/qmsgbox.h %{buildroot}%{_includedir}/QMsgBox.h

%ldconfig_scriptlets

%files
%doc LICENSE.GPL3
%{_libdir}/libQMsgBox.so.*

%files devel
%{_libdir}/libQMsgBox.so

%files headers
%{_includedir}/QMsgBox.h
%{_includedir}/qmsgbox.h

%files qt5
%doc LICENSE.GPL3
%{_libdir}/libQMsgBox-qt5.so.*

%files qt5-devel
%{_libdir}/libQMsgBox-qt5.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-28.20130830git94677dc
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-13.20130830git94677dc
- Added gcc-c++ buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0-7.20130830git94677dc
- use %%qmake_qt5/%%qmake_qt4 to ensure proper build flags

* Wed Sep 16 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-6.20130830git94677dc 
- Build qt5 package.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-4.20130830git94677dc
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.20130830git94677dc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-1.20130830git94677dc
- First release.
