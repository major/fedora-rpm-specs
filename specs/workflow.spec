Summary:        C++ parallel computing and asynchronous networking engine
Name:           workflow
# Main files are available under Apache-2.0 license except
# src/util/crc32c.h available under BSD-2-Clause license
# src/util/crc32c.c available under Zlib license
# src/kernel/rbtree.c available under GPL-2.0-or-later
# src/kernel/rbtree.h available under GPL-2.0-or-later
License:        Apache-2.0 AND BSD-2-Clause AND Zlib AND GPL-2.0-or-later

Version:        0.11.7
Release:        %autorelease

URL:            https://github.com/sogou/workflow
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  gtest-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
%ifnarch %{ix86}
# Needed for redis check
BuildRequires:  redis
%endif
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

%cmake -GNinja
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
%autochangelog
