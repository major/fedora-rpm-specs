%global commit 7ad58fac017622b6c696aa65bc97a8cd73766a50
%global gittag %{commit}
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global commitdate 20210516

# qt6-qtbase-devel is not available in Fedora 36+ s390x
%if 0%{?fedora} > 35
%ifarch s390x
%bcond_with qt6
Obsoletes:  	libmml-qt6 < 0:2.4-14
%else
%bcond_without qt6
%endif
%endif

Name:           libmml
Version:        2.4
Release:        22.%{commitdate}git%{shortcommit}%{?dist}
Summary:        MML Widget
License:        GPL-3.0-only OR LGPL-2.1-only WITH Qt-LGPL-exception-1.1
URL:            https://github.com/copasi/copasi-dependencies/tree/master/src/mml
Source0:        https://gitlab.com/anto.trande/mml/-/archive/%{commit}/mml-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)

%description
The QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

############### QT6 ######################
%if %{with qt6}
%package        qt6
Summary:        Qt6/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Qwt6)
Buildrequires:  qt6-rpm-macros
Requires:       pkgconfig(Qt6)
Provides:       libqtmmlwidget-qt6%{?_isa} = %{version}-%{release}

%description    qt6
The Qt5 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}

%description    qt6-devel
The %{name}-qt6-devel package contains Qt6 libraries and header files for
developing applications that use %{name}.
%endif

############### QT5 ######################
%package        qt5
Summary:        Qt5/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qwt6)
Buildrequires:  qt5-rpm-macros, qt5-qtbase-devel
Requires:       pkgconfig(Qt5Core)
Provides:       libqtmmlwidget%{?_isa} = %{version}-%{release}

%description    qt5
The Qt5 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains Qt5 libraries and header files for
developing applications that use %{name}.

############### QT4 ######################
%package        qt4
Summary:        Qt4/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt)
BuildRequires:  pkgconfig(qwt5-qt4)
Requires:       pkgconfig(QtCore)
Provides:       libqtmmlwidget-qt4%{?_isa} = %{version}-%{release}

%description    qt4
The Qt4 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt4-devel
Summary:        Development files for %{name}-qt4
Requires:       %{name}-qt4%{?_isa} = %{version}-%{release}

%description    qt4-devel
The %{name}-qt4-devel package contains Qt4 libraries and header files for
developing applications that use %{name}.

%prep
%setup -qc -n mml-%{commit}

mv mml-%{commit} qt5; cp -a qt5 qt4
%if %{with qt6}
cp -a qt5 qt6
%endif

%build
############### QT6 ######################
%if %{with qt6}
pushd qt6
mkdir -p build
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev -S ./ -B build \
 -DSELECT_QT=Qt6 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt6 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt) \
 -DQWT_LIBRARY:FILEPATH=%{_qt6_libdir}/libqwt.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt6_headerdir}/qwt \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt6_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt6_headerdir}/%{name}-qt6
make -C build
popd
%endif

############### QT5 ######################
pushd qt5
mkdir -p build
# -Werror=format-security/ flag prevents compilation
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev -S ./ -B build \
 -DSELECT_QT=Qt5 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt5 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt) \
 -DQWT_LIBRARY:FILEPATH=%{_qt5_libdir}/libqwt-qt5.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt5_headerdir}/qwt \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt5_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt5_headerdir}/%{name}-qt5
%make_build -C build
popd

############### QT4 ######################
pushd qt4
mkdir -p build
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev -S ./ -B build \
 -DSELECT_QT=Qt4 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt4 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt5-qt4) \
 -DQWT_LIBRARY:FILEPATH=%{_qt4_libdir}/libqwt5-qt4.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt4_headerdir}/qwt5-qt4 \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt4_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt4_headerdir}/%{name}-qt4
%make_build -C build
popd

%install
############### QT6 ######################
%if %{with qt6}
%make_install -C qt6/build
%endif

############### QT5 ######################
%make_install -C qt5/build

############### QT4 ######################
%make_install -C qt4/build

############### QT6 ######################
%if %{with qt6}
%files qt6
%license qt6/LGPL_EXCEPTION.txt qt6/LICENSE.LGPL
%{_qt6_libdir}/%{name}-qt6.so.*

%files qt6-devel
%{_qt6_headerdir}/%{name}-qt6/
%{_qt6_libdir}/%{name}-qt6.so
%endif

############### QT5 ######################
%files qt5
%license qt5/LGPL_EXCEPTION.txt qt5/LICENSE.LGPL
%{_qt5_libdir}/%{name}.so.*

%files qt5-devel
%dir %{_qt5_headerdir}
%{_qt5_headerdir}/%{name}-qt5/
%{_qt5_libdir}/%{name}.so

############### QT4 ######################
%files qt4
%license qt4/LGPL_EXCEPTION.txt qt4/LICENSE.LGPL
%{_qt4_libdir}/%{name}-qt4.so.*

%files qt4-devel
%{_qt4_headerdir}/%{name}-qt4/
%{_qt4_libdir}/%{name}-qt4.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-22.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-21.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-20.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-19.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-18.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-17.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-16.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4-15.20210516git7ad58fac
- Disable Qt6 MML in Fedora 36+ s390x only

* Sun Jan 30 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.4-14.20210516git7ad58fac
- Disable Qt6 MML in Fedora 36+ s390x

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-12.20210516git7ad58fac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.4-11.20210516git7ad58fac
- Introduce Qt6 MML
- Commit #7ad58fac

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10.20200509gitcedd544
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9.20200509gitcedd544
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8.20200509gitcedd544
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.4-7.20200509gitcedd544
- Move code to GitLab repository
- Rebuild new commit

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-2.20180425git07159b0
- Co-own /usr/lib*/qt5 directory
- Include GPLv3 as used license for files of a Qt Solutions component

* Sat May 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-1.20180425git07159b0
- First rpm
- Use CMake method
