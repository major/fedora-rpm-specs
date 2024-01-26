%global appname include-what-you-use
%global toolchain clang
%global llvmver 16.0.0

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2215937
# https://github.com/include-what-you-use/include-what-you-use/issues/1264
%undefine _include_frame_pointers

Name: iwyu
Version: 0.20
Release: 5%{?dist}

License: NCSA
Summary: C/C++ source files #include analyzer based on clang
URL: https://github.com/%{appname}/%{appname}
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz

BuildRequires: clang >= %{llvmver}
BuildRequires: clang-devel >= %{llvmver}
BuildRequires: libcxx-devel >= %{llvmver}
BuildRequires: llvm-devel >= %{llvmver}
BuildRequires: llvm-static >= %{llvmver}

BuildRequires: ncurses-devel
BuildRequires: python3-devel
BuildRequires: zlib-devel

BuildRequires: cmake
BuildRequires: ninja-build

Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
"Include what you use" means this: for every symbol (type, function, variable,
or macro) that you use in foo.cc (or foo.cpp), either foo.cc or foo.h should
include a .h file that exports the declaration of that symbol. (Similarly, for
foo_test.cc, either foo_test.cc or foo.h should do the including.) Obviously
symbols defined in foo.cc itself are excluded from this requirement.

This puts us in a state where every file includes the headers it needs to
declare the symbols that it uses. When every file includes what it uses,
then it is possible to edit any file and remove unused headers, without fear
of accidentally breaking the upwards dependencies of that file. It also
becomes easy to automatically track and update dependencies in the source
code.

%prep
%autosetup -n %{appname}-%{version} -p1
sed -e s@lib/@lib\${LLVM_LIBDIR_SUFFIX}/@g -i CMakeLists.txt
%py3_shebang_fix *.py

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DIWYU_LLVM_ROOT_PATH=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest --exclude-regex "cxx.test_(badinc|ms_inline_asm)"

%files
%doc docs/* README.md
%license LICENSE.TXT
%{_bindir}/%{appname}
%{_bindir}/fix_includes.py
%{_bindir}/iwyu_tool.py
%{_datadir}/%{appname}/
%{_mandir}/man1/%{appname}.1*

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.20-2
- Disabled frame pointers to fix crashes on F38+.

* Mon Apr 03 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.20-1
- Updated to version 0.20.

* Sun Mar 19 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.19-1
- Resurrected package.
- Updated to version 0.19.
- Performed major SPEC cleanup.
- Fixed issues with tests.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.5.20171001git576e80f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.4.20171001git576e80f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.3.20171001git576e80f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.2.20171001git576e80f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Tom Stellard <tstellar@redhat.com> - 0.9-0.1.20171001git576e80f
- Update to git snapshot that works with LLVM 5

* Wed Aug 02 2017 Dave Johansen <davejohansen@gmail.com> - 0.8-4
- Official 0.8/LLVM 4.0 release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Dave Johansen <davejohansen@gmail.com> - 0.8-1
- Use 0.8 to work with LLVM 4.0

* Thu Mar 30 2017 Tom Stellard <tstellar@redhat.com> - 0.7-3.20130330git.23253ec
- Update to git snapshot that works with LLVM4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Dave Johansen <davejohansen@gmail.com> - 0.7-1
- Upstream release

* Thu May 12 2016 Dave Johansen <davejohansen@gmail.com> - 0.6-1
- Upstream release

* Wed Feb 24 2016 Dave Johansen <davejohansen@gmail.com> - 0.6-0.2
- Remove use of rand() in badinc test

* Wed Feb 24 2016 Dave Johansen <davejohansen@gmail.com> - 0.6-0.1
- Test build against 3.8

* Thu Feb 04 2016 Dave Johansen <davejohansen@gmail.com> - 0.5-3
- Changes for new llvm cmake build system

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Dave Johansen <davejohansen@gmail.com> - 0.5-1
- Upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Dave Johansen <davejohansen@gmail.com> - 0.4-2
- Added iwyu_tool

* Mon Jun 01 2015 Dave Johansen <davejohansen@gmail.com> - 0.4-1
- Update to 0.4 based on clang 3.6.0

* Tue Jan 27 2015 Dave Johansen <davejohansen@gmail.com> - 0.3-1
- Update to 0.3 based on clang 3.5.0

* Fri Apr 25 2014 Dave Johansen <davejohansen@gmail.com> - 0.2-1
- Initial RPM release
