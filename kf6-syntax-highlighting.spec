%global gitdate 20230922.195427
%global cmakever 5.240.0
%global commit0 0211d718294684eb9d557e7d523b1693f03f16b9

%global framework syntax-highlighting

Name:           kf6-%{framework}
Version:        %{cmakever}^%{gitdate}.%{commit0}
Release:        135%{?dist}
Summary:        KDE Frameworks 6 Syntax highlighting engine for Kate syntax definitions
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{commit0}.tar.gz

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  extra-cmake-modules

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# Other
BuildRequires:  perl-interpreter

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=ON
%cmake_build

%install
%cmake_install
%find_lang_kf6 syntaxhighlighting6_qt

%check
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:

%files -f syntaxhighlighting6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/ksyntaxhighlighter6
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.5.240.0
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.6
%{_kf6_qmldir}/org/kde/syntaxhighlighting

%files devel
%{_kf6_archdatadir}/mkspecs/modules/qt_KSyntaxHighlighting.pri
%{_kf6_includedir}/KSyntaxHighlighting/
%{_kf6_libdir}/libKF6SyntaxHighlighting.so
%{_kf6_libdir}/cmake/KF6SyntaxHighlighting/

%changelog
* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230922.195427.0211d718294684eb9d557e7d523b1693f03f16b9-135
- Initial Package
