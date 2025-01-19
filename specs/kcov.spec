%undefine _auto_set_build_flags

%bcond_with tests
%bcond_with tools

%if %{with tests}
# The test suite expects a VPATH/out-of-source build with the following
# directories: build, build-tests and build-tools.
%global _vpath_builddir build
%endif

%ifnarch x86_64
# Same heuristic as upstream CI.
%global kcov_test_args --no-ptrace
%endif

Name:           kcov
Version:        43
Release:        2%{?dist}
Summary:        Code coverage tool without special compilation options

# Licenses of kcov itself and its bundled js libraries (see below)
License:        GPL-2.0-only AND MIT AND (GPL-2.0-only OR MIT)
URL:            https://simonkagstrom.github.io/%{name}
Source:         https://github.com/SimonKagstrom/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/SimonKagstrom/kcov/blob/v43/src/solib-parser/lib.c#L87-L104
ExcludeArch:    s390 s390x

BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3

%if %{with tests}
BuildRequires:  gawk
BuildRequires:  procps
%endif

# NB: Last I tried to unbundle those dependencies I hit a first roadblock in
# the sense that all three were available in Fedora but packaged differently
# and none of the versions matched:
#
# - js-jquery.noarch (compat package js-jquery2.noarch too)
# - nodejs-handlebars.noarch
# - xstatic-jquery-tablesorter-common.noarch
#
# All three packages drop files in different locations, following different
# patterns. NodeJS modules in particular look a bit more involved.
#
# Since those dependencies are merely used to slightly improve static HTML
# reports, I'd rather not spend mindless efforts unbundling things that are
# not ultimately exposed by the package. They are embedded in the kcov(1)
# program and written by `html-writer.cc` as static strings.
#
# It would make more sense to unbundle those if they were used as libraries
# instead of just assets. Here it seems overkill. I'm registering them as
# bundled provides even though they don't appear as individual files to at
# least keep awareness of what I consider a non-issue.
#
# -- dridi
Provides:       bundled(handlebars) = 2.0.0
Provides:       bundled(jquery) = 2.1.1
Provides:       bundled(jquery-tablesorter) = 2.17.1


%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.


%prep
%autosetup -p1


%build
# NB: the test suite is not built using the %%cmake macro, on purpose.
%if %{with tests}
cmake -S tests -B build-tests -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%make_build -C build-tests
%endif

%if %{with tools}
cmake -S tools -B build-tools -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
%make_build -C build-tools
%endif

%cmake
%cmake_build


%install
%cmake_install


%check
%if %{with tests}
export PYTHONPATH=tests/tools
%python3 -m libkcov build/src/kcov tmp/ build-tests/ . -v %{?kcov_test_args}
%endif


%files
%license COPYING*
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%{_pkgdocdir}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 17 2024 Dridi Boukelmoune <dridi@fedoraproject.org> - 43-1
- Bumped version to 43
- Updated license using SPDX
- Better upstream test suite support

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Dridi Boukelmoune <dridi@fedoraproject.org> - 42-1
- Bump to version 42

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 24 2023 Dridi Boukelmoune <dridi@fedoraproject.org> - 41-1
- Bump to version 41
- Remove upstream patch for GCC 13

* Fri Jan 20 2023 Dridi Boukelmoune <dridi@fedoraproject.org> - 39-6
- Upstream patch for GCC 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Dridi Boukelmoune <dridi@fedoraproject.org> - 39-3
- Conditionally build the extra tools

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 39-1
- Bump to version 39
- New libssl dependency

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 38-1
- Bump to version 38

* Tue Oct 01 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 37-1
- Bump to version 37
- Remove python2 workaround

* Fri Aug 09 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 36-2
- Temporarily move python shebangs to python2
- Build the test suite on x86_64 and run it conditionally
- Build tools/line2addr (but don't install it)

* Wed Aug 07 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 36-1
- Bump to version 36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 35-1
- Initial spec
