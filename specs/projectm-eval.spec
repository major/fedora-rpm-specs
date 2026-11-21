%ifnarch %{ix86}
%bcond ctest 1
%endif

Name:       projectm-eval
Version:    1.0.8
Release:    1%{?dist}
Summary:    Expression parser for use in Milkdrop, projectM and other applications
License:    MIT
URL:        https://github.com/projectM-visualizer/projectm-eval
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake-rpm-macros

%ifnarch %{ix86}
# Test dep
BuildRequires:  gtest-devel
BuildOption:    -DBUILD_TESTING=ON
%endif

%description
Cross-platform and cross-architecture reimplementation of
Milkdrop's pendant, the NullSoft Expression
Evaluation Library 2, or short "ns-eel2" for use in
Milkdrop, projectM and other applications.

This library aims at being as portable as possible, sacrificing some
performance over portability. The original ns-eel2 library directly
assembles machine code from compiled assembler fragments.
While this is super performant, the assembler code needs
to be rewritten manually for every target platform and
CPU architecture and is really hard to read or edit.

%package        devel
Summary:        Development files for %{name}
Provides:       projectm-eval-static = %{version}-%{release}
%description    devel
Development library files for %{name}.

%files devel
%doc ReadMe.md
%license LICENSE.md
%{_includedir}/projectm-eval/
%{_libdir}/cmake/projectM-Eval/
%{_libdir}/libprojectM_eval.a
%{_libdir}/pkgconfig/projectm-eval.pc

%changelog
* Sat Oct 24 2026 Owen Zimmerman <owen@fyralabs.com> - 1.0.8-1
- Initial package release
