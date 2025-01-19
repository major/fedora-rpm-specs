
%define apidocs 1

Name:    grantlee-qt5
Summary: Qt5 string template engine based on the Django template system
Version: 5.3.1
Release: 7%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/steveire/grantlee
Source0: http://downloads.grantlee.org/grantlee-%{version}%{?pre:-%{pre}}.tar.gz

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Source1: macros.grantlee5
%global grantlee5_plugins 5.3
%global grantlee5_plugindir %{_libdir}/grantlee/%{grantlee5_plugins}/
Provides: %{name}(%{grantlee5_plugins}) = %{version}-%{release}

## upstreamable patches
# Install headers into a versioned directory to be parallel-installable
# based on:
# https://github.com/steveire/grantlee/pull/1
#Patch1: grantlee-5.2.0-install_headers_into_versioned_directory.patch

BuildRequires: cmake >= 2.8.12
BuildRequires: gcc-c++
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Test)
%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
%endif
## for %%check
BuildRequires: xorg-x11-server-Xvfb

%description
Grantlee is a plug-in based String Template system written
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system,
and the design of Django is reused in Grantlee.

Part of the design of both is that application developers can extend
the syntax by implementing their own tags and filters. For details of
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details of
how to write templates, see the documentation.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# without versioning patch above, conflicts with older kde4 grantlee-devel
# no biggie, only one pkg in distro depends on kde4 grantlee -- rex
Conflicts: grantlee-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package apidocs
Summary: Grantlee API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Grantlee API documentation in HTML
format for easy browsing.


%prep
%autosetup -n grantlee-%{version} -p1

%build
%cmake \
  -DBUILD_TESTS:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=release

%cmake_build

%if 0%{?apidocs}
make docs -C %{__cmake_builddir}
%endif


%install
%cmake_install

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_docdir}/HTML/en/Grantlee5/
cp -prf %{__cmake_builddir}/apidox/* %{buildroot}%{_docdir}/HTML/en/Grantlee5/
%endif

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.grantlee5
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  -e "s|@@GRANTLEE5_PLUGINS@@|%{grantlee5_plugins}|g" \
  -e "s|@@GRANTLEE5_PLUGINDIR@@|%{grantlee5_plugindir}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.grantlee5


%check
#export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a make test -C %{__cmake_builddir} ||:


%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libGrantlee_Templates.so.5*
%{_libdir}/libGrantlee_TextDocument.so.5*
%dir %{_libdir}/grantlee/
%{grantlee5_plugindir}/

%files devel
%{_includedir}/grantlee/
%{_includedir}/grantlee_templates.h
%{_includedir}/grantlee_textdocument.h
%{_libdir}/libGrantlee_Templates.so
%{_libdir}/libGrantlee_TextDocument.so
%{_libdir}/cmake/Grantlee5/
%{rpm_macros_dir}/macros.grantlee5

%if 0%{?apidocs}
%files apidocs
%{_docdir}/HTML/en/Grantlee5/
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.3.1-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-10
- disable autotests, fixes FTBFS (#1923556)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 5.2.0-9
- use cmake macro

* Tue Aug 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-8
- FTBFS, define %__cmake_in_source_build until we have time to port to new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-5
- BR: Qt5Qml, use cmake-style Qt5 deps

* Mon Feb 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-4
- drop problematic versioned includes patch

* Fri Feb 14 2020 Troy Dawson <tdawson@redhat.com> - 5.2.0-3
- Fix templates multiversion include directory

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Troy Dawson <tdawson@redhat.com> - 5.2.0-1
- Update to 5.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-9
- use %%make_build %%ldconfig_scriptlets

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-8
- BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 5.1.0-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-2
- macros.grantlee5: notably, %%{grantlee5_plugindir} %%{grantlee5_requires}

* Tue Apr 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.1.0-1
- grantlee-5.1.0

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-4
- grantlee-qt5: FTBFS in rawhide (#1307592)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 08 2015 Rex Dieter <rdieter@fedoraproject.org>  5.0.0-2
- update URL

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org>  5.0.0-1
- grantlee-5.0.0
