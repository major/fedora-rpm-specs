%global debug_package %{nil}
%global middle_release 0

%bcond_without check

ExclusiveArch: %{power64} x86_64 aarch64

%if 0%{?middle_release}
%global  commit      4604f1b2db7131ea10b9d9ff56bf5a93e8c66847
%global  date        .20210809git
%global  shortcommit %(c=%{commit}; echo ${c:0:8})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

Name:      sdsl-lite
Summary:   SDSL v3 - Succinct Data Structure Library
Version:   3.0.3
Release:   4%{date}%{shortcommit}%{?dist}
License:   BSD-3-Clause
URL:       https://github.com/xxsds/%{name}
Source0:   https://github.com/xxsds/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc, gcc-c++
BuildRequires: cmake
BuildRequires: cereal-devel >= 1.3.2
BuildRequires: gtest-devel >= 1.13.0

Patch0: %{name}-unbundle_libraries.patch

%description
The Succinct Data Structure Library (SDSL) is a powerful and flexible C++11
library implementing succinct data structures.
In total, the library contains the highlights of 40 research publications.
Succinct data structures can represent an object (such as a bitvector or a tree)
in space close to the information-theoretic lower bound of the object while
supporting operations of the original object efficiently.
The theoretical time complexity of an operation performed on the classical
data structure and the equivalent succinct data structure are
(most of the time) identical.


%package devel
Summary: SDSL v3 - Succinct Data Structure Library
Requires: cmake >= 3.13
Requires: cereal-devel%{?_isa} >= 1.3.2

%description devel
Developer files for SDSL 3, in the form for C header files.


%package doc
Summary: SDSL v3 HTML/Latex documentation
BuildRequires: doxygen
BuildArch: noarch

%description doc
SDSL v3 HTML/Latex documentation.

%prep
%autosetup -n sdsl-lite-%{version} -N

%patch -P 0 -p1 -b .backup

%build
%cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_BUILD_TYPE:STRING=Release \
       -DSDSL_HEADER_TEST:BOOL=OFF -DGENERATE_DOC:BOOL=ON -DUSE_LIBCPP:BOOL=OFF -DSDSL_CEREAL=1
%cmake_build

%install
mkdir -p %{buildroot}%{_prefix}
cp -a include %{buildroot}%{_prefix}/

rm -f %{buildroot}%{_includedir}/sdsl/.gitignore

%if %{with check}
%check
# Test excluded by upstream
%ctest -- -E 'k2-treap-test_k2-0.1.0.0'
%endif

%files doc
%doc %__cmake_builddir/extras/docs/html
%doc %__cmake_builddir/extras/docs/latex

%files devel
%license LICENSE
%{_includedir}/sdsl/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.0.3-1
- Release 3.0.3

* Wed Jul 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-1
- Release 3.0.2

* Tue Jan 24 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-5
- Fix for GCC-13

* Mon Jan 23 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-4
- Remove pkgconfig file

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Release 3.0.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-1
- First package
