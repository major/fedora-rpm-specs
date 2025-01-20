%global sover 20

Name:           quarter
Version:        1.2.2
Release:        2%{?dist}
Summary:        Lightweight glue library between Coin and Qt

License:        BSD-3-Clause 
URL:            https://grey.colorado.edu/quarter/
Source0:        https://github.com/coin3d/%{name}/releases/download/v%{version}/%{name}-%{version}-src.tar.gz

BuildRequires:  cmake gcc gcc-c++ doxygen
BuildRequires:  mesa-libGL-devel
BuildRequires:  Coin4-devel
BuildRequires:  qt5-qtbase-devel
# Needed for Cmake UI Config
BuildRequires:  qt5-qttools-static
BuildRequires:  libspnav-devel

%description
Quarter is a light-weight glue library that provides seamless integration
between Systems in Motions's Coin high-level 3D visualization library and
Trolltech's Qt 2D user interface library.

Qt and Coin is a perfect match since they are both open source, widely portable
and easy to use. Quarter has evolved from Systems in Motion's own experiences
using Coin and Qt together in our applications.

The functionality in Quarter revolves around QuarterWidget, a subclass of
QGLWidget. This widget provides functionality for rendering of Coin scenegraphs
and translation of QEvents into SoEvents. Using this widget is as easy as using
any other QWidget.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -p1 -n %{name}


%build
%cmake -DQUARTER_BUILD_DOCUMENTATION=ON

%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_libdir}/*.so.%{sover}*
%{_libdir}/qt5/plugins/designer/*

%files devel
%{_includedir}/Quarter/
%{_libdir}/*.so
%{_libdir}/cmake/Quarter-%{version}/
%{_libdir}/pkgconfig/Quarter.pc

%files doc
%{_docdir}/Quarter/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 19 2024 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Richard Shaw <hobbes1069@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-10
- Rebuild for Coin4.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-2
- Update per reviewer feedback.

* Tue Dec 17 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Initial packaging
