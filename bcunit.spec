# Use old cmake macro behaviour.
%define __cmake_in_source_build 1

# 0 for release build and 1 for test builds that enable examples for smoke testing.
%define testing_build 0

Name: bcunit
Version: 5.2.0
Release: 1%{?dist}
Summary: Provide C programmers basic testing functionality
License: LGPL-2.0-or-later
URL: https://gitlab.linphone.org/BC/public/bcunit/

Source: https://gitlab.linphone.org/BC/public/bcunit/-/archive/%{version}/%{name}-%{version}.tar.gz

# Patches.
Patch00: 0001_bcunit_set_current_version.patch
Patch01: 0002_bcunit_sover.patch
%if 0%{?testing_build}
Patch02: 0003_bcunit_examples_include_folder.patch
%endif
Patch03: 0004_bcunit_change_cmake_files_default_install_location.patch
Patch04: 0005_bcunit_ncurses_fix_error_format_security.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: pkgconfig(ncurses)

%description
BCUnit is a unit testing framework for C, derived from CUnit.
(B)CUnit provides various interfaces to the framework, some of which
are platform dependent (e.g. curses on *nix). The framework complies
with the conventional structure of test cases bundled into suites
which are registered with the framework for running.

%package devel
Summary: BCUnit development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
BCUnit is a unit testing framework for C.
This package installs the BCUnit development files.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_CURSES=ON \
  -DENABLE_DOC=ON \
  -DENABLE_TEST=OFF \
%if 0%{?testing_build}
  -DENABLE_EXAMPLES=ON
%endif
%cmake_build

%install
%cmake_install

%files
%license COPYING
# NOTE: soname number must be '1' as project 'PROPERTIES VERSION' is '1.0.1'. 
%{_libdir}/libbcunit.so.1*

%files devel
%doc AUTHORS ChangeLog NEWS README.md TODO
%license COPYING
%{_includedir}/BCUnit/
%{_libdir}/libbcunit.so
# Note: cmake files location. We have moved location, see Patch03.
%{_libdir}/cmake/BCunit/
%{_libdir}/pkgconfig/bcunit.pc
%{_datadir}/BCUnit/
%{_docdir}/BCUnit/
%{_mandir}/man3/BCUnit.3*

%changelog
* Thu Mar 09 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.2.0-1
- Initial package.
