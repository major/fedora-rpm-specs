
Name:           qoauth
Summary:        Qt library OAuth authorization scheme
Version:        2.0.0
Release:        22%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/ayoy/qoauth
Source0:        https://github.com/ayoy/qoauth/archive/v2.0.0.tar.gz

%if 0%{?rhel}
# rhel7/ppc64 lacks some dependencies, including qca-ossl
ExcludeArch: ppc64
%endif

## upstreamable patches
# https://ayoy.lighthouseapp.com/projects/32547-qoauth/tickets/20-qoauth-qt4qt5-parallel-installability
Patch100: qoauth-2.0.0-qt5.patch

BuildRequires: make
BuildRequires:  gcc-c++
# RHEL does not provide Qt4
%if 0%{?fedora}
# Qt4
BuildRequires:	pkgconfig(QtCore) pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	qca-ossl
Requires:	qca-ossl%{?_isa}
%endif

%description
QOAuth is a Qt-based C++ implementation of an interface to services using
OAuth authorization scheme.

%package devel
Summary:	Development files for the Qt OAuth support library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries, header files and documentations 
for developing applications that use QOAuth library. 

%if 0%{?docs}
# FIXME/TODO: common/shared -doc subpkg
%package doc
Summary:        API Documentation for %{name}
BuildRequires:  doxygen
BuildArch: noarch
%description doc
%{summary}.
%endif

%package qt5
Summary: Qt5 library OAuth authorization scheme
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  qca-qt5-ossl
Requires:       qca-qt5-ossl%{?_isa}
%description qt5
%{summary}.

%package qt5-devel
Summary:        Qt5 library OAuth authorization scheme
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}

%patch -P100 -p1 -b .qt5


%build
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
export PATH=%{_qt5_bindir}:$PATH
%{qmake_qt5} PREFIX="%{_prefix}" ..
make %{?_smp_mflags}
popd

# RHEL does not provide Qt4
%if 0%{?fedora}
mkdir %{_target_platform}-qt4
pushd %{_target_platform}-qt4
export PATH=%{_qt4_bindir}:$PATH
%{qmake_qt4} PREFIX="%{_prefix}" ..
make %{?_smp_mflags}
popd
%endif

%if 0%{?docs}
doxygen Doxyfile
# fix the time stamp
for file in doc/html/*; do
  touch -r Doxyfile $file
done
%endif


%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt5

## FIXME
sed -i \
  -e "s|^includedir=.*|includedir=%{_qt5_headerdir}/QtOAuth|" \
  -e "s|^libdir=.*|libdir=%{_qt5_libdir}|" \
  %{buildroot}%{_qt5_libdir}/pkgconfig/qoauth-qt5.pc

# RHEL does not provide Qt4
%if 0%{?fedora}
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt4

## FIXME
sed -i \
  -e "s|^includedir=.*|includedir=%{_qt4_headerdir}/QtOAuth|" \
  -e "s|^libdir=.*|libdir=%{_qt4_libdir}|" \
  %{buildroot}%{_qt4_libdir}/pkgconfig/qoauth.pc
%endif

## unpackaged files
rm -f %{buildroot}%{_qt5_libdir}/libqoauth-qt5.prl
rm -f %{buildroot}%{_qt4_libdir}/libqoauth.prl


%check
make check -C %{_target_platform}-qt5 || :
# RHEL does not provide Qt4
%if 0%{?fedora}
make check -C %{_target_platform}-qt4 || :
%endif


%ldconfig_scriptlets

# RHEL does not provide Qt4
%if 0%{?fedora}
%files
%doc README CHANGELOG
%license LICENSE
%{_qt4_libdir}/libqoauth.so.1*

%files devel
%{_qt4_libdir}/libqoauth.so
#{_qt4_libdir}/libqoauth.prl
%{_qt4_libdir}/pkgconfig/qoauth.pc
%{_qt4_prefix}/mkspecs/features/oauth.prf
%{_qt4_headerdir}/QtOAuth/
%endif

%ldconfig_scriptlets qt5

%files qt5
%doc README CHANGELOG
%license LICENSE
%{_qt5_libdir}/libqoauth-qt5.so.2*

%files qt5-devel
%{_qt5_libdir}/libqoauth-qt5.so
#{_qt5_libdir}/libqoauth-qt5.prl
%{_qt5_libdir}/pkgconfig/qoauth-qt5.pc
%{_qt5_archdatadir}/mkspecs/features/oauth.prf
%{_qt5_headerdir}/QtOAuth/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-21
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-7
- BR: gcc-c++
- use %%_qt5_archdatadir (#1606038)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-1
- qoauth-2.0.0, -qt5 support (#1415070)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Dec 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-11
- rebuild(qca)

* Mon Dec 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-10
- pkgconfig-style build deps, use %%qmake_qt4 macro, tighten %%files

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-8
- .spec cleanup, epel7: ExcludeArch: ppc64

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 08 2010 Chen Lei <supercyper@163.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jun 25 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.3.20100625git726325d
- New upstream version

* Tue Jun 22 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.2.20100622git7f69e33
- New upstream version
- Add %%check section

* Tue May 25 2010 Chen Lei <supercyper@163.com> - 1.0.1-0.1.20100525gitec7e4d5
- initial rpm build
