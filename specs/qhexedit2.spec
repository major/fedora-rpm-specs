%if 0%{?rhel}
%bcond_with python
%else
%bcond_without python
%endif

Name:           qhexedit2
# Remember to also update version in qhexedit2_build.patch in the setup.py hunk
Version:        0.8.9
Release:        17%{?dist}
Summary:        Binary Editor for Qt

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/Simsys/qhexedit2
Source0:        https://github.com/Simsys/qhexedit2/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        qhexedit.desktop

# Fix build issues
Patch0:         qhexedit2_build.patch
Patch1:         sip5.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-qt5-devel
BuildRequires:  %{py3_dist PyQt-builder}
BuildRequires:  %{py3_dist sip} >= 5
%endif

Requires:       %{name}-qt5-libs%{?_isa} = %{version}-%{release}

%description
QHexEdit is a hex editor widget written in C++ for the Qt framework.
It is a simple editor for binary data, just like QPlainTextEdit is for text
data.

###############################################################################

%package qt5-libs
Summary:        %{name} Qt5 library

%description qt5-libs
%{name} Qt5 library.


%package        qt5-devel
Summary:        Development files for %{name} Qt5
Requires:       %{name}-qt5-libs%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name} Qt5.

###############################################################################

%package        doc
Summary:        Documentation and examples for %{name}
Provides:       bundled(jquery)
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation and examples for %{name}.

###############################################################################

%if %{with python}
%package -n python3-%{name}-qt5
Summary:        %{name} Qt5 Python3 bindings
Requires:       %{name}-qt5-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-qt5
%{name} Qt5 Python3 bindings.


%package -n python3-%{name}-qt5-devel
Summary:        Development files for the %{name} Qt5 Python3 bindings
Requires:       python3-%{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{py3_dist sip} >= 5

%description -n python3-%{name}-qt5-devel
Development files for the %{name} Qt5 Python3 bindings
%endif


%prep
%autosetup -p1 -n %{name}-%{version}

# Prevent rpmlint W: doc-file-dependency /usr/share/doc/qhexedit2-doc/html/installdox /usr/bin/perl
rm -f doc/html/installdox


%build
%set_build_flags

# Build library, qt5
mkdir build-lib-qt5
pushd build-lib-qt5
%qmake_qt5 ../src/qhexedit.pro
%make_build
popd

%if %{with python}
# Build sip bindings, qt5, python3
sip-build --qmake=%{_qt5_qmake} --verbose --build-dir=build-python3-qt5 --no-make
%make_build -C build-python3-qt5
%endif

# Build application
mkdir build-example
pushd build-example
%qmake_qt5 ../example/qhexedit.pro
%make_build
popd


%install
# Library and headers
install -d %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_libdir}
cp -a src/*.h %{buildroot}%{_includedir}/%{name}
chmod 0755 build-lib-qt5/*.so.*.*
cp -a build-lib-qt5/*.so* %{buildroot}%{_libdir}

# pkg-config file
install -d %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}-qt5.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: %{name}-qt5
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqhexedit-qt5
EOF


%if %{with python}
# Python bindings
# Distutils does not support --build-base with install, you need to build also...
%make_install INSTALL_ROOT=%{buildroot} -C build-python3-qt5
%if 0%{?flatpak}
# prefix is not configurable with qmake
mv %{buildroot}/usr/%{_lib}/python* %{buildroot}%{_libdir}/
%endif
%endif

# Application
install -Dpm 0755 build-example/qhexedit %{buildroot}%{_bindir}/qhexedit
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}


%files
%{_bindir}/qhexedit
%{_datadir}/applications/qhexedit.desktop

%files qt5-libs
%doc doc/release.txt
%license src/license.txt
%{_libdir}/libqhexedit-qt5.so.4*

%files qt5-devel
%{_includedir}/%{name}/
%{_libdir}/libqhexedit-qt5.so
%{_libdir}/pkgconfig/%{name}-qt5.pc

%files doc
%license src/license.txt
%doc doc/html

%if %{with python}
%files -n python3-%{name}-qt5
%{python3_sitearch}/qhexedit.*.so
%{python3_sitearch}/QHexEdit-%{version}*info

%files -n python3-%{name}-qt5-devel
%{python3_sitearch}/PyQt5/bindings/qhexedit/
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.9-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.9-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Sandro Mani <manisandro@gmail.com> - 0.8.9-12
- Drop qt4 build

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.8.9-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Scott Talbert <swt@techie.net> - 0.8.9-5
- Update to build with sip 5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.9-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 05 2020 Sandro Mani <manisandro@gmail.com> - 0.8.9-1
- Update to 0.8.9

* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 0.8.8-1
- Update to 0.8.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.6-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Sandro Mani <manisandro@gmail.com> - 0.8.6-1
- Update to 0.8.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Sandro Mani <manisandro@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 0.8.4-1
- Update to 0.8.4
- Drop python2 subpackages (#1634563)
- Drop obsolete scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-7
- Rebuilt for Python 3.7

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 0.8.3-6
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Sandro Mani <manisandro@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Sandro Mani <manisandro@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Wed Aug 03 2016 Sandro Mani <manisandro@gmail.com> - 0.7.8-1
- Update to 0.7.8

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 Sandro Mani <manisandro@gmail.com> - 0.7.7-1
- Update to 0.7.7

* Sat Apr 09 2016 Sandro Mani <manisandro@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 18 2015 Sandro Mani <manisandro@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Sandro Mani <manisandro@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Wed May 20 2015 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri May 01 2015 Sandro Mani <manisandro@gmail.com> - 0.6.6-1
- Update to 0.6.6

* Wed Apr 29 2015 Sandro Mani <manisandro@gmail.com> - 0.6.5-2
- Build Qt5 library

* Thu Apr 16 2015 Sandro Mani <manisandro@gmail.com> - 0.6.5-1
- Update to 0.6.5

* Tue Dec 16 2014 Sandro Mani <manisandro@gmail.com> - 0.6.3-3.20141212svnr41
- Fix incorrect Requires

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.6.3-2.20141212svnr41
- Update source file name to include svn revision
- Fix license LGPLv2+ -> LGPLv2
- Added -Wl,--as-needed to fix unused-direct-shlib-dependency

* Sun Aug 10 2014 Sandro Mani <manisandro@gmail.com> - 0.6.3-1
- Initial package
