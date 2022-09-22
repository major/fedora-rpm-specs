%global commit 71799c27da506c899f2ef04b50cd8d454374870d
%global comm %(c=%{commit}; echo ${c:0:7})
%global checkout 20171224git%{comm}
%global _docdir_fmt %{name}

Name: ctk
Version: 0.1
Release: 0.24.20190721%{?dist}
Summary: The Commmon Toolkit for biomedical imaging

License: ASL 2.0
URL: http://www.commontk.org
Source0: https://github.com/commontk/CTK/archive/2018-10-29/CTK-2018-10-29.tar.gz

Patch0:	%{name}-%{version}.%{checkout}-fix_qreal_cast.patch
Patch1: %{name}-DCMTK_3.6.4_updated_function.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: dcmtk-devel
BuildRequires: gdcm-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: qt-devel
BuildRequires: make

%description
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

This package contains the CTK Core library.


%package dicom

Summary: Library of high-level classes for querying PACS and local databases

%description dicom
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

DICOM library provides high-level classes supporting query and retrieve
operations from PACS and local databases. It includes Qt widgets to easily
set-up a server connection and to send queries and view the results.


%package plugin-framework

Summary: A dynamic component system for C++

%description plugin-framework
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

The Plugin Framework is a dynamic component system for C++, modeled after the
OSGi specifications. It enable a development model where applications are
(dynamically) composed of many different (reusable) components following a
service oriented approach.


%package widgets

Summary: A collection of Qt widgets for biomedical imaging applications

%description widgets
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

The Widgets library is a collection of Qt widgets for usage in biomedical
imaging applications.


%package devel

Summary: Development files for the Common Toolkit

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-dicom%{?_isa} = %{version}-%{release}
Requires: %{name}-plugin-framework%{?_isa} = %{version}-%{release}
Requires: %{name}-widgets%{?_isa} = %{version}-%{release}
Requires: cmake%{?_isa}
Requires: qt-devel%{?_isa}

%description devel
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

This package contains files for development of CTK applications.


%package doc

Summary: Documentation for the Common Toolkit
BuildArch: noarch

%description doc
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.

This package contains CTK developer documentation.


%prep
%autosetup -n CTK-2018-10-29 -p1
# Set up the logo
cp ctkLogo-small.png ctkLogo-small-transparent.png

%build
%cmake \
    -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/InsightToolkit \
    -DCTK_SUPERBUILD=OFF \
    -DCTK_INSTALL_LIB_DIR=%{_libdir} \
    -DCTK_INSTALL_CMAKE_DIR=%{_libdir}/cmake/%{name} \
    -DCTK_INSTALL_PLUGIN_DIR=%{_libdir}/%{name}/plugins \
    -DCTK_INSTALL_QTPLUGIN_DIR=%{_qt4_plugindir} \
    -DCTK_ENABLE_DICOM=ON \
    -DCTK_ENABLE_PluginFramework=ON \
    -DCTK_ENABLE_Widgets=ON \
    -DDOCUMENTATION_TARGET_IN_ALL=OFF \
    -DBUILD_TESTING:BOOL=OFF ..
%cmake_build

# why doesnt cmake_build doc work
pushd %{__cmake_builddir}
%make_build doc
popd



%install
%cmake_install


# No %%check section here because running tests requires working X server
# and data files that are distributed without any copyright/license info
# (see https://github.com/commontk/CTKData/issues/1).


%ldconfig_scriptlets

%ldconfig_scriptlets dicom

%ldconfig_scriptlets plugin-framework

%ldconfig_scriptlets widgets


%files
%doc README.rst
%license NOTICE LICENSE
%{_libdir}/libCTKCore.so.*

%files dicom
%{_libdir}/libCTKDICOM*.so.*

%files plugin-framework
%{_libdir}/libCTKPluginFramework.so.*

%files widgets
%{_libdir}/libCTKWidgets.so.*

%files devel
%{_includedir}/%{name}-%{version}
%{_libdir}/*.so
%{_qt4_plugindir}/designer/*.so
%{_libdir}/cmake/%{name}

%files doc
%license NOTICE LICENSE
%doc %{__cmake_builddir}/Documentation/html

%changelog
* Thu Aug 04 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1-0.24.20190721
- Rebuild for dcmtk soname bump

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Richard Shaw <hobbes1069@gmail.com> - 0.1-0.21.20190721
- Rebuild for soname bump in dcmtk.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1-0.18.20190721
- Fix build using correct cmake macros
- Remove uneeded exclude

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20190721
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.20190721
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1-0.13.20190721
- Rebuild for ITK

* Sat Mar 02 2019 Antonio Trande <sagitterATfedoraproject.org> - 0.1-0.12.20181029
- Release 2018 10 29

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20171224git71799c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20171224git71799c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20171224git71799c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.1-0.8.20171224git71799c2
- Remove BR: tcp_wrappers (#1518758)

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.1-0.7.20171224git71799c2
- Update to recent snapshot

* Wed Jan 03 2018 Björn Esser <besser82@fedoraproject.org> - 0.1-0.6.20151015gitbdc8cac
- Rebuilt for dcmtk

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.1-0.5.20151015gitbdc8cac
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20151015gitbdc8cac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.3.20151015gitbdc8cac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.20151015gitbdc8cac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 2 2016 Dmitry Mikhirev <mikhirev@gmail.com> 0.1-0.1.20151015gitbdc8cac
- Initial package
