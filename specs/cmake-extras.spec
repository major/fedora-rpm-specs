%global debug_package %{nil}
%bcond check 1

Name:           cmake-extras
Version:        1.9
Release:        %autorelease
Summary:        A collection of add-ons for the CMake build tool
License:        LGPL-3.0-or-later AND BSD-2-Clause
URL:            https://gitlab.com/ubports/development/core/cmake-extras
Source0:        %{url}/-/archive/%{version}/cmake-extras-%{version}.tar.bz2
Patch0:         cmake-extras-fix-find-qmlplugindump.patch
Patch1:         https://salsa.debian.org/debian-ayatana-team/cmake-extras/-/raw/master/debian/patches/1004_switch-to-python3.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

%if %{with check}
BuildRequires:  licensecheck
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  python3-clang
%endif

Requires:       licensecheck
Requires:       lcov
Requires:       doxygen
Requires:       astyle
Requires:       gettext
Requires:       intltool
Requires:       vala
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)

%description
A collection of add-ons for the CMake build tool.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%if %{with check}
%check
pushd examples/copyrighttest-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/CopyrightTest
%cmake_build
%ctest -E 'must_fail_1|must_fail_4'
popd

pushd examples/gsettings-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/GSettings
%cmake_build
%ctest
popd

pushd examples/includechecker-demo
%cmake -DCMAKE_PREFIX_PATH=%{_builddir}/%{name}-%{version}/src/IncludeChecker
%cmake_build
%ctest
popd
%endif

%files
%license LICENSE
%doc README.md
%{_datadir}/cmake/CopyrightTest/
%{_datadir}/cmake/CoverageReport/
%{_datadir}/cmake/DoxygenBuilder/
%{_datadir}/cmake/FormatCode/
%{_datadir}/cmake/GDbus/
%{_datadir}/cmake/GMock/
%{_datadir}/cmake/GObjectIntrospection/
%{_datadir}/cmake/GSettings/
%{_datadir}/cmake/GdbusCodegen/
%{_datadir}/cmake/IncludeChecker/
%{_datadir}/cmake/Intltool/
%{_datadir}/cmake/Lcov/
%{_datadir}/cmake/QmlPlugins/
%{_datadir}/cmake/Vala/
%{_datadir}/cmake/gcovr/

%changelog
%autochangelog
