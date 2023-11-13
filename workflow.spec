Summary:        C++ parallel computing and asynchronous networking engine
Name:           workflow
# Main files are available under Apache-2.0 license except
# src/util/crc32c.h available under BSD-2-Clause license
# src/util/crc32c.c available under Zlib license
# src/kernel/rbtree.c available under GPL-2.0-or-later
# src/kernel/rbtree.h available under GPL-2.0-or-later
License:        Apache-2.0 AND BSD-2-Clause AND Zlib AND GPL-2.0-or-later

Version:        0.11.1
Release:        1%{?dist}

URL:            https://github.com/sogou/workflow
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# Needed for redis check
BuildRequires:  redis
BuildRequires:  sed
# Needed for memory check
BuildRequires:  valgrind

%global _description %{expand:
As Sogou`s C++ server engine, Sogou C++ Workflow supports almost all back-end
C++ online services of Sogou, including all search services, cloud input
method, online advertisements, etc., handling more than 10 billion requests
every day. This is an enterprise-level programming engine in light and elegant
design which can satisfy most C++ back-end development requirements. }

%description
%_description

%package devel
Summary:        C++ parallel computing and asynchronous networking engine
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%_description

%package docs
Summary:       C++ parallel computing and asynchronous networking engine
BuildArch:     noarch

%description docs
%_description

%prep
%autosetup
# Rename files to make installation of documentation easier
pushd docs
pushd en
rename .md .en.md *.md
mv *.* ..
popd
popd

%build

%cmake
%cmake_build
# remove copies of header files to minimize
# size of debugsource package, these files are
# copied into a _include directory
rm -r _include
mkdir -p _include/workflow
ln -s src/algorithm/*.h   _include/workflow/
ln -s src/algorithm/*.inl _include/workflow/
ln -s src/client/*.h      _include/workflow/
ln -s src/kernel/*.h      _include/workflow/
ln -s src/factory/*.h     _include/workflow/
ln -s src/factory/*.inl   _include/workflow/
ln -s src/manager/*.h     _include/workflow/
ln -s src/manager/*.inl   _include/workflow/
ln -s src/nameservice/*.h _include/workflow/
ln -s src/protocol/*.h    _include/workflow/
ln -s src/protocol/*.inl  _include/workflow/
ln -s src/server/*.h      _include/workflow/
ln -s src/util/*.h        _include/workflow/

%install
%cmake_install

# Package Readmes separately
rm %{buildroot}/%{_docdir}/%{name}-%{version}/README.md
# Do not package static library
rm %{buildroot}/%{_libdir}/libworkflow.a

%check
# Run tests
make check

%files
%license LICENSE LICENSE_GPLV2
%doc README.md
%doc README_cn.md
%{_libdir}/libworkflow.so.0.*
%{_libdir}/libworkflow.so.0

%files devel
%{_libdir}/libworkflow.so
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%dir %{_includedir}/workflow
%{_includedir}/workflow/*.h
%{_includedir}/workflow/*.inl

%files docs
%license LICENSE
%doc docs/*.md
%doc tutorial/


%changelog
* Sat Nov 11 2023 Benson Muite <benson_muite@emailplus.org> - 0.11.1-1
- Update to new release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun  6 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.7-1
- Update to new release

* Sat Feb 25 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.6-1
- Update to new release

* Thu Feb 23 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.5-4
- Get tests to work
- Add redis and valgrind
- Use GTest with c++14

* Wed Feb 22 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.5-3
- Remove static library rather than use exclude macro
- Use tutorial instead of tests

* Fri Jan 13 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.5-2
- Ensure tests run

* Wed Jan 11 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.5-1
- Version update
- Add copy of GPL license

* Mon Jan 02 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.4-2
- Do not include static library
- Update license information

* Sun Jan 01 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.4-1
- Initial packaging
