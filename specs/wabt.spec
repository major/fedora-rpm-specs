%undefine __cmake_in_source_build
%bcond_without check
%global commit 3e826ecde1adfba5f88d10d361131405637e65a3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ts_commit f3f048661dc1686d556a27d522df901cb747ab4a
%global ts_shortcommit %(c=%{ts_commit}; echo ${c:0:7})
%global wc_commit b6dd1fb658a282c64b029867845bc50ae59e1497
%global wc_shortcommit %(c=%{wc_commit}; echo ${c:0:7})

Summary: The WebAssembly Binary Toolkit
Name: wabt
Version: 1.0.36
Release: 2%{?dist}
URL: https://github.com/WebAssembly/wabt
Source0: https://github.com/WebAssembly/wabt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/WebAssembly/testsuite/archive/%{ts_commit}/%{name}-testsuite-%{ts_shortcommit}.tar.gz
Source2: https://github.com/WebAssembly/wasm-c-api/archive/%{wc_commit}/%{name}-wasm-c-api-%{wc_shortcommit}.tar.gz
License: Apache-2.0
BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: openssl-devel
%if %{with check}
BuildRequires: gtest-devel
BuildRequires: python%{python3_pkgversion}-ply
BuildRequires: simde-devel >= 0.8.2
%endif
# wasm.h from https://github.com/WebAssembly/wasm-c-api/ is used for build
Provides: bundled(wasm-c-api) = %{wc_commit}

%description
WABT (we pronounce it "wabbit") is a suite of tools for WebAssembly. These tools
are intended for use in (or for development of) toolchains or other systems that
want to manipulate WebAssembly files. Unlike the WebAssembly spec interpreter
(which is written to be as simple, declarative and "speccy" as possible), they
are written in C/C++ and designed for easier integration into other systems.
Unlike Binaryen these tools do not aim to provide an optimization platform or a
higher-level compiler target; instead they aim for full fidelity and compliance
with the spec (e.g. 1:1 round-trips with no changes to instructions).

%prep
%setup -q
rmdir third_party/wasm-c-api
tar xzf %{S:2} -C third_party
mv third_party/wasm-c-api{-%{wc_commit},}
%if %{with check}
rmdir third_party/testsuite
tar xzf %{S:1} -C third_party
mv third_party/testsuite{-%{ts_commit},}
pushd test
# https://github.com/WebAssembly/wabt/issues/1044
%ifarch i686
rm regress/empty-quoted-module.txt
rm spec/float_exprs.txt
rm spec/float_misc.txt
rm spec/local_tee.txt
rm spec/simd_f32x4_arith.txt
rm spec/simd_f32x4_pmin_pmax.txt
rm spec/simd_f64x2_arith.txt
rm spec/simd_f64x2_pmin_pmax.txt
rm wasm2c/spec/conversions.txt
rm wasm2c/spec/float_memory.txt
rm wasm2c/spec/float_misc.txt
rm wasm2c/spec/float_exprs.txt
rm wasm2c/spec/local_tee.txt
rm wasm2c/spec/memory64/float_memory64.txt
rm wasm2c/spec/multi-memory/float_memory0.txt
rm wasm2c/spec/select.txt
%endif
# https://github.com/WebAssembly/wabt/issues/1045
# https://github.com/WebAssembly/wabt/issues/2240
%ifarch ppc64le
rm spec/conversions.txt
rm spec/simd_conversions.txt
rm wasm2c/spec/simd_address.txt
rm wasm2c/spec/simd_f32x4_arith.txt
rm wasm2c/spec/simd_f32x4_pmin_pmax.txt
rm wasm2c/spec/simd_splat.txt
%endif
# https://github.com/WebAssembly/wabt/issues/2070
# https://github.com/WebAssembly/wabt/issues/2240
%ifarch s390x
rm wasm2c/spec/address.txt
rm wasm2c/spec/endianness.txt
rm wasm2c/spec/exception-handling/imports.txt
rm wasm2c/spec/float_exprs.txt
rm wasm2c/spec/float_memory.txt
rm wasm2c/spec/imports.txt
rm wasm2c/spec/left-to-right.txt
rm wasm2c/spec/memory.txt
rm wasm2c/spec/memory_redundancy.txt
rm wasm2c/spec/memory_trap.txt
rm wasm2c/spec/memory64/address.txt
rm wasm2c/spec/memory64/address64.txt
rm wasm2c/spec/memory64/endianness64.txt
rm wasm2c/spec/memory64/float_memory64.txt
rm wasm2c/spec/memory64/memory.txt
rm wasm2c/spec/memory64/memory_redundancy64.txt
rm wasm2c/spec/memory64/memory_trap64.txt
rm wasm2c/spec/memory64/memory64.txt
rm wasm2c/spec/memory64/simd_address.txt
rm wasm2c/spec/multi-memory/address0.txt
rm wasm2c/spec/multi-memory/address1.txt
rm wasm2c/spec/multi-memory/float_exprs1.txt
rm wasm2c/spec/multi-memory/float_memory0.txt
rm wasm2c/spec/multi-memory/imports.txt
rm wasm2c/spec/multi-memory/imports1.txt
rm wasm2c/spec/multi-memory/imports2.txt
rm wasm2c/spec/multi-memory/load.txt
rm wasm2c/spec/multi-memory/load0.txt
rm wasm2c/spec/multi-memory/memory.txt
rm wasm2c/spec/multi-memory/memory-multi.txt
rm wasm2c/spec/multi-memory/memory_trap1.txt
rm wasm2c/spec/simd_address.txt
rm wasm2c/spec/simd_align.txt
rm wasm2c/spec/simd_const.txt
rm wasm2c/spec/simd_f32x4.txt
rm wasm2c/spec/simd_f32x4_arith.txt
rm wasm2c/spec/simd_f64x2.txt
rm wasm2c/spec/simd_f64x2_arith.txt
rm wasm2c/spec/simd_i16x8_arith.txt
rm wasm2c/spec/simd_i16x8_arith2.txt
rm wasm2c/spec/simd_i16x8_cmp.txt
rm wasm2c/spec/simd_i16x8_sat_arith.txt
rm wasm2c/spec/simd_i32x4_arith.txt
rm wasm2c/spec/simd_i32x4_arith2.txt
rm wasm2c/spec/simd_i32x4_cmp.txt
rm wasm2c/spec/simd_i64x2_arith.txt
rm wasm2c/spec/simd_i64x2_arith2.txt
rm wasm2c/spec/simd_i8x16_arith.txt
rm wasm2c/spec/simd_i8x16_cmp.txt
rm wasm2c/spec/simd_i8x16_sat_arith.txt
rm wasm2c/spec/simd_lane.txt
rm wasm2c/spec/simd_load.txt
rm wasm2c/spec/simd_load16_lane.txt
rm wasm2c/spec/simd_load32_lane.txt
rm wasm2c/spec/simd_load64_lane.txt
rm wasm2c/spec/simd_load_extend.txt
rm wasm2c/spec/simd_load_splat.txt
rm wasm2c/spec/simd_load_zero.txt
rm wasm2c/spec/simd_store.txt
rm wasm2c/spec/simd_store16_lane.txt
rm wasm2c/spec/simd_store32_lane.txt
rm wasm2c/spec/simd_store64_lane.txt
rm wasm2c/spec/simd_store8_lane.txt
rm wasm2c/spec/threads/atomic.txt
%endif
popd
%endif

%build
%cmake3 -DUSE_SYSTEM_GTEST=ON
%cmake3_build

%install
%cmake3_install

%if %{with check}
%check
%ifarch i686
export WASM2C_CFLAGS="-msse2 -mfpmath=sse"
%endif
test/run-tests.py -v --bindir %{_vpath_builddir} --timeout=1200 %{?_smp_mflags}
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/spectest-interp
%{_bindir}/wasm-decompile
%{_bindir}/wasm-interp
%{_bindir}/wasm-objdump
%{_bindir}/wasm-stats
%{_bindir}/wasm-strip
%{_bindir}/wasm-validate
%{_bindir}/wasm2c
%{_bindir}/wasm2wat
%{_bindir}/wast2json
%{_bindir}/wat-desugar
%{_bindir}/wat2wasm
%{_datadir}/wabt
%{_includedir}/wabt
%{_includedir}/wasm-rt.h
%{_includedir}/wasm-rt-exceptions.h
%{_libdir}/cmake/wabt
%{_libdir}/libwabt.a
%{_libdir}/libwasm-rt-impl.a
%{_mandir}/man1/spectest-interp.1*
%{_mandir}/man1/wasm-decompile.1*
%{_mandir}/man1/wasm-interp.1*
%{_mandir}/man1/wasm-objdump.1*
%{_mandir}/man1/wasm-stats.1*
%{_mandir}/man1/wasm-strip.1*
%{_mandir}/man1/wasm-validate.1*
%{_mandir}/man1/wasm2c.1*
%{_mandir}/man1/wasm2wat.1*
%{_mandir}/man1/wast2json.1*
%{_mandir}/man1/wat-desugar.1*
%{_mandir}/man1/wat2wasm.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Dominik Mierzejewski <dominik@greysector.net> 1.0.36-1
- update to 1.0.36 (#2246227)
- drop obsolete patches
- fix some tests in i686
- simde-0.8.2 is now required
- run all tests on aarch64, all issues resolved
- review skipped tests on i686, ppc64le and s390x

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.33-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Dominik Mierzejewski <dominik@greysector.net> 1.0.33-1
- update to 1.0.33 (#2203483)
- drop obsolete patch
- disable failing tests on aarch64 and ppc64le (reported upstream)
- fix running tests on i686
- disable failing wasm2c tests on s390x (big endian not supported upstream)
- fix deprecated patchN macro usage

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Dominik Mierzejewski <dominik@greysector.net> 1.0.32-1
- update to 1.0.32 (#2156897)
- skip one new failing test on aarch64, ppc64le and s390x for now

* Fri Dec 09 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.31-1
- update to 1.0.31 (#2143772)
- fix build on 32-bit
- fix build --without check

* Sat Oct 15 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.30-1
- update to 1.0.30 (#2132095)
- increase timeout to fix tests on ARM
- skip some new failing tests on i686 and s390x for now

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.29-1
- update to 1.0.29

* Fri Apr 01 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.28-1
- update to 1.0.28 (#2065997)
- run fixed tests on 32-bit again
- work around test failures due to new gcc-12 warnings

* Tue Mar 15 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.27-1
- update to 1.0.27 (#2055947)
- drop armv7hl

* Mon Feb 07 2022 Dominik Mierzejewski <rpm@greysector.net> 1.0.25-1
- update to 1.0.25 (#2047107)
- skip some new failing tests on 32-bit
- skip two more failing tests on i686

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Dominik Mierzejewski <rpm@greysector.net> 1.0.24-1
- update to 1.0.24 (#1993479)
- enable skipped tests on s390x (fixed upstream)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 14 2021 Dominik Mierzejewski <rpm@greysector.net> 1.0.23-1
- update to 1.0.23 (#1934466)
- drop obsolete patch
- skip some failing tests on s390x and ppc64le (reported upstream)

* Tue Feb 02 2021 Dominik Mierzejewski <rpm@greysector.net> 1.0.20-3.20210130git09ac53e
- update to 09ac53e git snapshot
- enable building on big-endian (fixed upstream)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.20-1
- update to 1.0.20 (#1896654)

* Mon Aug 17 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.19-1
- update to 1.0.19 (#1838384)
- drop obsolete patches
- adapt to https://www.fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> 1.0.17-2
- Use __cmake_in_source_build

* Tue Jul 14 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.17-1
- update to 1.0.17 (#1838384)
- backport a fix for 32-bit arches
- stop pretending it works on big-endian
- use names and macros portable across Fedora and EPEL

* Wed May 06 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.15-1
- update to 1.0.15 (#1832317)
- pathfix.py no longer required, upstream moved to python3-only
- skip new failing tests in i686 and ppc64le (reported upstream)

* Fri Mar 20 2020 Dominik Mierzejewski <rpm@greysector.net> 1.0.13-1
- update to 1.0.13 (#1792557)
- drop obsolete patch and work-arounds
- bundle wasm-c-api (only wasm.h used for build)
- double test timeout again to prevent failures on armv7hl

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.12-1
- update to 1.0.12 (#1755644)
- drop obsolete patch
- disable regress/regress-30.txt until fixed for python3
- fix running test/wasm2c/spec tests under python3

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.11-1
- update to 1.0.11
- drop obsolete patches

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.10-2
- backport some fixes for test failures from upstream git
- run tests in parallel and double timeout to prevent failures on armv7hl

* Thu Mar 14 2019 Dominik Mierzejewski <rpm@greysector.net> 1.0.10-1
- initial build
