%global		gitdate 20230902.184733
%global		cmakever 5.240.0
%global		commit0 74c03a0c16cf4b6cf22921231dc5be356513d7ae
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework ktexttemplate

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	Separates the structure of documents from their data
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)

%description
The goal of KTextTemplate is to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming and advanced generation of other text such as code.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_libdir}/libKF6TextTemplate.so.*
%{_kf6_plugindir}/ktexttemplate
%{_kf6_datadir}/qlogging-categories6/ktexttemplate.categories


%files devel
%{_kf6_includedir}/KTextTemplate
%{_libdir}/cmake/KF6TextTemplate
%{_libdir}/libKF6TextTemplate.so
%{_libdir}/qt6/mkspecs/modules/qt_KTextTemplate.pri

%changelog
* Thu Sep 28 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230902.184733.74c03a0-1
- Initial release
