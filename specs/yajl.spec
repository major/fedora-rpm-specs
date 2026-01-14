%undefine __cmake_in_source_build
%global _vpath_builddir build

Name: yajl
Version: 2.1.0
Release: %autorelease
Summary: Yet Another JSON Library (YAJL)

License: ISC
URL: http://lloyd.github.com/yajl/

#
# NB, upstream does not provide pre-built tar.gz downloads. Instead
# they make you use the 'on the fly' generated tar.gz from GITHub's
# web interface
#
# The Source0 for any version is obtained by a URL
#
#   https://github.com/lloyd/yajl/releases/tag/2.1.0
#
Source0: %{name}-%{version}.tar.gz

# Patches managed at https://github.com/berrange/yajl/tree/fedora-dist-git
Patch: 0001-pkg-config-file-should-be-in-lib-dir-not-shared-data.patch
Patch: 0002-pkg-config-include-dir-should-not-have-the-yajl-suff.patch
Patch: 0003-fix-patch-to-test-files-to-take-account-of-vpath.patch
Patch: 0004-drop-bogus-_s-suffix-from-yajl-dynamic-library.patch
Patch: 0005-Fix-for-CVE-2017-16516.patch
Patch: 0006-Fix-CVE-2022-24795.patch
Patch: 0007-yajl-fix-memory-leak-problem.patch
Patch: 0008-fix-memory-leaks.patch
# Cherry-picked from: https://github.com/lloyd/yajl/pull/256.patch
Patch: 0009-Allow-cmake-4.0.patch

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: git

%package devel
Summary: Libraries, includes, etc to develop with YAJL
Requires: %{name} = %{version}-%{release}

%description
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

%description devel
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

This sub-package provides the libraries and includes
necessary for developing against the YAJL library

%prep
%autosetup -S git_am

%build
# NB, we are not using upstream's 'configure'/'make'
# wrapper, instead we use cmake directly to better
# align with Fedora standards
%cmake \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64}
   %endif

%cmake_build


%install
%cmake_install


# No static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/libyajl_s.a


%check
cd test
(cd parsing && ./run_tests.sh)
(cd api && ./run_tests.sh)

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/json_reformat
%{_bindir}/json_verify
%{_libdir}/libyajl.so.2
%{_libdir}/libyajl.so.2.*

%files devel
%dir %{_includedir}/yajl
%{_includedir}/yajl/yajl_common.h
%{_includedir}/yajl/yajl_gen.h
%{_includedir}/yajl/yajl_parse.h
%{_includedir}/yajl/yajl_tree.h
%{_includedir}/yajl/yajl_version.h
%{_libdir}/libyajl.so
%{_libdir}/pkgconfig/yajl.pc


%changelog
%autochangelog
