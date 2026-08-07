Name: cvise
Version: 2.12.0
Release: 1%{?dist}
Summary: Super-parallel Python port of the C-Reduce
License: BSD-3-Clause
URL: https://github.com/marxin/cvise
Source: https://github.com/marxin/cvise/archive/v%{version}.tar.gz

# Fix compatibility with LLVM22.
#
# Backport of upstream commits:
# https://github.com/marxin/cvise/commit/59e9058c43b12b802893bde668113c8b3b3525b7
# https://github.com/marxin/cvise/commit/68262f7d6de584b6474801827cb7dfc68011de25
# https://github.com/marxin/cvise/commit/fa1be9523d569adfe207c85a1e44f074172bc305
# https://github.com/marxin/cvise/commit/b17bbacdb279babd87dc9ef24756f3003746717c
# https://github.com/marxin/cvise/commit/c7f9642340eb61c09a05c96498fd21c9b7293770
Patch1: llvm22.patch

BuildRequires: astyle
BuildRequires: cmake
BuildRequires: flex
BuildRequires: llvm-devel
BuildRequires: unifdef
BuildRequires: clang-devel
BuildRequires: ninja-build
BuildRequires: indent
BuildRequires: gcc-c++
BuildRequires: python3-pebble
BuildRequires: python3-pytest
BuildRequires: python3-psutil
BuildRequires: python3-chardet
BuildRequires: make
BuildRequires: libffi-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-ng-devel

Requires: astyle
Requires: clang-tools-extra
Requires: unifdef
Requires: python3-pebble
Requires: python3-psutil
Requires: python3-chardet
Requires: indent
Requires: colordiff

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
%autosetup -p1

%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-error=restrict"
%cmake -DCMAKE_SKIP_RPATH=TRUE -GNinja
%cmake_build

%check
export PYTEST_ADDOPTS="\
--deselect=cvise/tests/test_test_manager.py::test_succeed_via_naive_pass \
--deselect=cvise/tests/test_test_manager.py::test_succeed_via_n_one_off_passes \
--deselect=cvise/tests/test_test_manager.py::test_succeed_after_n_invalid_results \
--deselect=cvise/tests/test_test_manager.py::test_give_up_on_stuck_pass \
--deselect=cvise/tests/test_test_manager.py::test_halt_on_unaltered \
--deselect=cvise/tests/test_test_manager.py::test_halt_on_unaltered_after_stop \
--deselect=tests/test_cvise.py::TestCvise::test_simple_reduction"
%cmake_build --target test

%install
%cmake_install

%files
%license COPYING
%{_bindir}/cvise
%{_bindir}/cvise-delta
%dir %{_libexecdir}/cvise
%{_libexecdir}/cvise/clex
%{_libexecdir}/cvise/clang_delta
%{_libexecdir}/cvise/strlex
%{_libexecdir}/cvise/topformflat
%{_datadir}/cvise

%changelog
* Fri Jul 17 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.12.0-1
- Update to v2.12.0 (rhbz#2123703), fix FTBFS (rhbz#2433972)

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Marek Polacek <polacek@redhat.com> - 2.11.0-1
- update to cvise-2.11.0 (#2123703)

* Wed Oct 2 2024 Marek Polacek <polacek@redhat.com> - 2.10.0.1-1
- update to cvise-2.10.0 (#2300616)
- require python3-chardet (#2292488)

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.0-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Marek Polacek <polacek@redhat.com> - 2.9.0-1
- update to cvise-2.9.0 (#2113164)
- require colordiff (#2252760)

* Wed Jul 26 2023 Vincent Mihalkovic <vmihalko@redhat.com> - 2.8.0-1
- update to cvise-2.8.0 (#2123703)
  various spec file improvements

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Marek Polacek <polacek@redhat.com> - 2.4.0-2
- bump Release for rebuild

* Mon Nov 01 2021 Marek Polacek <polacek@redhat.com> - 2.4.0-1
- update to cvise-2.4.0 (#2014306)
- require python3-chardet

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 09 2021 Marek Polacek <polacek@redhat.com> - 2.3.0-1
- update to cvise-2.3.0 (#1935355)

* Mon Mar 08 2021 Marek Polacek <polacek@redhat.com> - 2.2.0-1
- update to cvise-2.2.0 (#1935355)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 2.1.0-2
- Rebuild for clang-11.1.0

* Mon Jan 11 2021 Marek Polacek <polacek@redhat.com> - 2.1.0-1
- update to cvise-2.1.0 (#1914882)

* Fri Nov 20 2020 Marek Polacek <polacek@redhat.com> - 2.0.0-1
- update to cvise-2.0.0 (#1883731)

* Mon Aug 03 2020 Marek Polacek <polacek@redhat.com> - 1.4.0-4
- Use the _target_platform directory when building/installing (#1863387)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Marek Polacek <polacek@redhat.com> - 1.4.0-1
- initial version
