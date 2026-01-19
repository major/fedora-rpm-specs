%global debug_package %{nil}
%global middle_release 1

%bcond_without check
%bcond_with doc

ExclusiveArch: %{power64} x86_64 aarch64

%if 0%{?middle_release}
%global  commit      bb2eebb2de8a556661c00ba3c5b4c33b7c2c7a25
%global  date        .20250414git
%global  shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif

Name:      sdsl-lite
Summary:   SDSL v3 - Succinct Data Structure Library
Version:   3.0.3
Release:   7%{date}%{shortcommit}%{?dist}
License:   BSD-3-Clause
URL:       https://github.com/xxsds/%{name}
Source0:   https://github.com/xxsds/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: gcc, gcc-c++
BuildRequires: cmake
BuildRequires: cereal-devel >= 1.3.2
BuildRequires: gtest-devel >= 1.13.0
BuildRequires: texlive-endnotes

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
Obsoletes: %{name}-doc < 0:3.0.3-6

%description devel
Developer files for SDSL 3, in the form for C header files.

%if %{with doc}
%package doc
Summary: SDSL v3 HTML/Latex documentation
BuildRequires: doxygen
BuildArch: noarch

%description doc
SDSL v3 HTML/Latex documentation.
%endif

%prep
%autosetup -n sdsl-lite-%{commit} -N

%patch -P 0 -p1 -b .backup

%build
%cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_BUILD_TYPE:STRING=Release \
       -DSDSL_HEADER_TEST:BOOL=OFF -DGENERATE_DOC:BOOL=OFF -DUSE_LIBCPP:BOOL=OFF -DSDSL_CEREAL=1 \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5

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

%if %{with doc}
%files doc
%doc %__cmake_builddir/extras/docs/html
%doc %__cmake_builddir/extras/docs/latex
%endif

%files devel
%license LICENSE
%{_includedir}/sdsl/

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7.20250414gitbb2eebb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Aug 02 2025 Antonio Trande <sagitter@fedoraproject.org> - 3.0.3-6
- Bump to the commit bb2eebb
- Fix rhbz#2380805

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

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
