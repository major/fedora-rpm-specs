# Run the tests on gcc?
%bcond_without check_gcc
# Run the tests on clang?
%bcond_without check_clang

%global commit_simde 9609eb2cf687984277185813fdfe81b8b200377b
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
%global commit_munit da8f73412998e4f1adf1100dc187533a51af77fd
# Disable debuginfo package for the header only package.
%global debug_package %{nil}

# Disable the auto_set_build_flags. Because it sets clang flags for gcc in
# the %check section.
%undefine _auto_set_build_flags

%global simde_version 0.7.4
%global rc_version 1

Name: simde
Version: %{simde_version}%{?rc_version:~rc%{rc_version}}
# Align the release format with the packages setting Source0 by commit hash
# such as podman.spec and moby-engine.spec.
Release: 1.git%{short_commit_simde}%{?dist}
Summary: SIMD Everywhere
# find simde/ -type f | xargs licensecheck
#   simde: MIT
#   simde/check.h: CC0
#   simde/debug-trap.h: CC0
#   simde/simde-arch.h: CC0
# removed in %%prep (unbundled):
#   simde/hedley.h: CC0
License: MIT and CC0
URL: https://github.com/simd-everywhere/simde
Source0: https://github.com/simd-everywhere/%{name}/archive/%{commit_simde}.tar.gz
# munit used in the unit test.
Source1: https://github.com/nemequ/munit/archive/%{commit_munit}.tar.gz
# gcc and clang are used in the unit tests.
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
# Header-only library dependency
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires: hedley-devel
BuildRequires: hedley-static
BuildRequires: %{_bindir}/time
# Do not set noarch for header only package.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries

%description
%{summary}
The SIMDe header-only library provides fast, portable implementations of SIMD
intrinsics on hardware which doesn't natively support them, such as calling
SSE functions on ARM. There is no performance penalty if the hardware supports
the native implementation (e.g., SSE/AVX runs at full speed on x86,
NEON on ARM, etc.).

%package devel
Summary: Header files for SIMDe development
Provides: %{name}-static = %{version}-%{release}
# The API includes the hedley header-only library.
Requires: hedley-devel%{?_isa}
Requires: hedley-static

%description devel
The simde-devel package contains the header files needed
to develop programs that use the SIMDe.

%prep
%autosetup -n %{name}-%{commit_simde} -p1
ln -svf %{_includedir}/hedley.h %{name}/

%build
# The %%build section is not used.

%install
mkdir -p %{buildroot}%{_includedir}
cp -a simde %{buildroot}%{_includedir}
ln -svf ../hedley.h %{buildroot}%{_includedir}/%{name}/

%check
# Check version.
version_major=$(grep '^#define SIMDE_VERSION_MAJOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_minor=$(grep '^#define SIMDE_VERSION_MINOR ' simde/simde-common.h | cut -d ' ' -f 3)
version_micro=$(grep '^#define SIMDE_VERSION_MICRO ' simde/simde-common.h | cut -d ' ' -f 3)
test "%{simde_version}" = "${version_major}.${version_minor}.${version_micro}"

# Check if all the shipped file is a valid header file.
# Suppress the command logging during the check by running on bash.
bash - <<\EOF
for file in $(find simde/ -type f); do
  if ! [[ "${file}" =~ \.h$ ]]; then
    echo "${file} is not a header file."
    false
  elif [ -x "${file}" ]; then
    echo "${file} has executable bit."
    false
  fi
done
EOF

# Set munit.
rm -rf test/munit
tar xzvf %{SOURCE1}
mv munit-%{commit_munit} test/munit

# Define functions.
JOB_NUM="$(nproc)"

function _time {
  %{_bindir}/time -f '=> [%E]' ${@}
}

function _setup {
  meson setup "${BUILD_DIR}" || (
    cat "${BUILD_DIR}/meson-logs/meson-log.txt"
    false
  )
}

function _build {
  rm -f build.log
  _time ninja -C "${BUILD_DIR}" -v -j "${JOB_NUM}" >& build.log || (
    cat build.log
    false
  )
  head -4 build.log
  tail -3 build.log
}

function _test {
  _time meson test -C "${BUILD_DIR}" -q --no-rebuild --print-errorlogs
}

BACKUP_FILES="
  meson.build
  test/x86/meson.build
  test/wasm/simd128/meson.build
"

function _backup {
  for file in ${BACKUP_FILES}; do
    cp -p ${file}{,.orig}
  done
}

function _reset {
  for file in ${BACKUP_FILES}; do
    cp -p ${file}{.orig,}
  done
}

_backup

# Run the unit tests.
# gcc
%if %{with check_gcc}
%global toolchain gcc
bash - <<\EOF
echo "== 1. tests on gcc =="
EOF
gcc --version
g++ --version

bash - <<\EOF
echo "=== 1.1. tests on gcc without flags ==="
EOF
# gcc 11.1.1 without flags + i686 x86/avx512/dbsad failures
# https://github.com/simd-everywhere/simde/issues/867
%ifarch i686
sed -i "/^simde_avx512_families/,/\]/ s/'dbsad',/#\0/" meson.build
%endif
# gcc 13.0.1 without flags + ppc64le test failures and errors.
# https://github.com/simd-everywhere/simde/issues/986
%ifarch ppc64le
sed -i -E "/^simde_avx512_families/,/\]/ s/'(range|range_round)',/#\0/" meson.build
sed -i '/^test_simde_x_mm_copysign_ps *(/,/^}$/ s|simde_test_x86_assert_equal_f32x4|//\0|' \
  test/x86/sse.c
sed -i '/^test_simde_x_mm_copysign_pd *(/,/^}$/ s|simde_test_x86_assert_equal_f64x2|//\0|' \
  test/x86/sse2.c
sed -i '/^test_simde_wasm_i16x8_mul *(/,/^}$/ s|simde_test_wasm_i16x8_assert_equal|//\0|' \
  test/wasm/simd128/mul.c
sed -i '/^test_simde_wasm_u16x8_shr *(/,/^}$/ s|simde_test_wasm_u16x8_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
sed -i '/^test_simde_wasm_u32x4_shr *(/,/^}$/ s|simde_test_wasm_u32x4_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
sed -i '/^test_simde_wasm_u64x2_shr *(/,/^}$/ s|simde_test_wasm_u64x2_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
%endif
# gcc 13.0.1 without flags + s390x test qdmulh* failures and errors
# https://github.com/simd-everywhere/simde/issues/987
%ifarch s390x
sed -i -E "/^simde_neon_families/,/\]/ s/'(qdmulh|qdmulh_lane|qdmulh_n)',/#\0/" meson.build
%endif
BUILD_DIR="build/gcc"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
  _setup
_build
_test

bash - <<\EOF
echo "=== 1.2. tests on gcc with O2 flag ==="
EOF
# _reset
# gcc 13.0.1 with O2 + i686 test dpbf16 failures and x86/avx512/dpbf16 errors
# https://github.com/simd-everywhere/simde/issues/988
%ifarch i686
sed -i "/^simde_avx512_families/,/\]/ s/'dpbf16',/#\0/" meson.build
%endif
# gcc 11.1.1 with -O2 + s390x arm/neon/{mlal_lane,mlsl_lane} failures
# https://github.com/simd-everywhere/simde/issues/874
%ifarch s390x
sed -i -E "/^simde_neon_families/,/\]/ s/'(mlal_lane|mlsl_lane)',/#\0/" meson.build
%endif
BUILD_DIR="build/gcc-O2"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
CFLAGS="-O2" CXXFLAGS="-O2" \
  _setup
# gcc 13.0.1 with -O2 + -fno-strict-aliasing + aarch64 (arm64) build stucking.
# https://github.com/simd-everywhere/simde/issues/992
%ifnarch aarch64
_build
_test
%endif

bash - <<\EOF
echo "=== 1.3. tests on gcc with flags macro ==="
EOF
# gcc 11 with flags + i686 x86/{sse,sse2} test_simde_mm_cvt* failures
# https://github.com/simd-everywhere/simde/issues/719
%ifarch i686
sed -i '/^test_simde_mm_cvt_ps2pi *(/,/^}$/ s|simde_test_x86_assert_equal_i32x2|//\0|' \
  test/x86/sse.c
sed -i '/^test_simde_mm_cvtps_pi16 *(/,/^}$/ s|simde_test_x86_assert_equal_i16x4|//\0|' \
  test/x86/sse.c
sed -i '/^test_simde_mm_cvtsi64_ss *(/,/^}$/ s|simde_test_x86_assert_equal_f32x4|//\0|' \
  test/x86/sse.c
sed -i '/^test_simde_mm_cvtsd_si64 *(/,/^}$/ s|simde_assert_equal_i64|//\0|' \
  test/x86/sse2.c
sed -i '/^test_simde_mm_cvtsi64_sd *(/,/^}$/ s|simde_assert_m128d_close|//\0|' \
  test/x86/sse2.c
sed -i '/^test_simde_mm_cvttsd_si64 *(/,/^}$/ s|simde_assert_equal_i64|//\0|' \
  test/x86/sse2.c
%endif
# gcc 11.1.1 with flags + ppc64le arm/neon failures
# https://github.com/simd-everywhere/simde/issues/865
%ifarch ppc64le
sed -i -E "/^simde_neon_families/,/\]/ s/'\w+',/#\0/" meson.build
%endif
BUILD_DIR="build/gcc-flags-macro"
CC="gcc -fno-strict-aliasing" CXX="g++ -fno-strict-aliasing" \
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" \
  _setup
# gcc 13.0.1 with -O2 + -fno-strict-aliasing + aarch64 (arm64) build stucking.
# https://github.com/simd-everywhere/simde/issues/992
%ifnarch aarch64
_build
_test
%endif

# with check_gcc
%endif

# clang
%if %{with check_clang}
%global toolchain clang
bash - <<\EOF
echo "== 2. tests on clang =="
EOF
clang --version
clang++ --version

bash - <<\EOF
echo "=== 2.1. tests on clang without flags ==="
EOF
_reset
# clang 12 + i686 {x86/sse,x86/sse2,arm/neon} failures
# https://github.com/simd-everywhere/simde/issues/721
%ifarch i686
sed -i -E "/^simde_test_x86_tests/,/\]/ s/'(sse|sse2)',/#\0/" test/x86/meson.build
sed -i -E "/^simde_neon_families/,/\]/ s/'(abd|max|min|mla|mls|mls_n|mul|mul_n|pmax|pmin|rev64|sub|zip|zip1|zip2)',/#\0/" meson.build
%endif
%ifarch ppc64le
# clang 15.0.7 without flags + ppc64le test arm/neon/ld1q_x{2,3,4} failures and errors
# https://github.com/simd-everywhere/simde/issues/989
sed -i -E "/^simde_neon_families/,/\]/ s/'(ld1q_x2|ld1q_x3|ld1q_x4)',/#\0/" meson.build
# clang 15.0.7 without flags + ppc64le test wasm/simd128/{mul,shr} failures
# https://github.com/simd-everywhere/simde/issues/991
sed -i '/^test_simde_wasm_i16x8_mul *(/,/^}$/ s|simde_test_wasm_i16x8_assert_equal|//\0|' \
  test/wasm/simd128/mul.c
sed -i '/^test_simde_wasm_u16x8_shr *(/,/^}$/ s|simde_test_wasm_u16x8_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
sed -i '/^test_simde_wasm_u32x4_shr *(/,/^}$/ s|simde_test_wasm_u32x4_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
sed -i '/^test_simde_wasm_u64x2_shr *(/,/^}$/ s|simde_test_wasm_u64x2_assert_equal|//\0|' \
  test/wasm/simd128/shr.c
%endif
# clang 12.0.1 without flags + s390x x86/avx512/shldv, arm/neon/qdmulh* failures
# https://github.com/simd-everywhere/simde/issues/869
%ifarch s390x
sed -i -E "/^simde_neon_families/,/\]/ s/'(qdmulh|qdmulh_lane|qdmulh_n)',/#\0/" meson.build
sed -i "/^simde_avx512_families/,/\]/ s/'shldv',/#\0/" meson.build
%endif
BUILD_DIR="build/clang"
CC=clang CXX=clang++ \
  _setup
_build
_test

bash - <<\EOF
echo "=== 2.2. tests on clang with O2 flag ==="
EOF
_reset

# clang 15.0.7 with -O2 + x86_64 arm/qabs/vqabsq_s32
# https://github.com/simd-everywhere/simde/issues/901
sed -i -E "/^simde_neon_families/,/\]/ s/'qabs',/#\0/" meson.build
# clang 12 with -O2 + i686 x86/sse2 test_simde_mm_cvtsi64_sd failures
# https://github.com/simd-everywhere/simde/issues/740
%ifarch i686
sed -i '/^test_simde_mm_cvtsi64_sd *(/,/^}$/ s|simde_assert_m128d_close|//\0|' \
  test/x86/sse2.c
%endif
# clang 12.0.1 with -O2 + armv7hl wasm_simd128/trunc_sat failures
# https://github.com/simd-everywhere/simde/issues/880
%ifarch %{arm}
sed -i "/^simde_test_wasm_simd128_tests/,/\]/ s/'trunc_sat',/#\0/" test/wasm/simd128/meson.build
%endif
# clang 12.0.1 with -O2 + ppc64le x86/avx512/ror failures
# https://github.com/simd-everywhere/simde/issues/875
%ifarch ppc64le
sed -i "/^simde_avx512_families/,/\]/ s/'ror',/#\0/" meson.build
%endif
%ifarch s390x
sed -i -E "/^simde_neon_families/,/\]/ s/'(qdmulh|qdmulh_lane|qdmulh_n)',/#\0/" meson.build
%endif
BUILD_DIR="build/clang-O2"
CC="clang" CXX="clang++" \
CFLAGS="-O2" CXXFLAGS="-O2" \
  _setup
_build
_test

bash - <<\EOF
echo "=== 2.3. tests on clang with flags macro ==="
EOF
BUILD_DIR="build/clang-flags-macro"
# clang is broken armv7hl.
# https://bugzilla.redhat.com/show_bug.cgi?id=1918924
# A temporary workaround to avoid the segmentation fault on armv7hl.
%ifarch %{arm}
%global _lto_cflags %{nil}
%endif
CC="clang" CXX="clang++" \
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" \
  _setup
_build
_test

# with check_clang
%endif

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}

%changelog
* Thu Feb 16 2023 Jun Aruga <jaruga@redhat.com> - 0.7.4~rc1-1.git9609eb2
- Upgrade to SIMDe 0.7.4 rc1.
  Resolves: rhbz#2047012
  Resolves: rhbz#2166982

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4.git3378ab3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3.git3378ab3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2.git3378ab3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 01 2021 Jun Aruga <jaruga@redhat.com> - 0.7.3-1.git3378ab3
- Upgrade to SIMDe 0.7.3 upstream master branch commit 3378ab3.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2.git22609d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 04 2021 Jun Aruga <jaruga@redhat.com> - 0.7.2-1.git22609d4
- Upgrade to SIMDe 0.7.2.
  Resolves: rhbz#1940179

* Wed Mar 24 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.0-10.git396e05c
- Fix incorrectly-arched dependency on hedley-static

* Tue Mar 23 2021 Jun Aruga <jaruga@redhat.com> - 0.0.0-9.git396e05c
- Fix a warning by the rpmlint.

* Mon Mar 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.0-9.git396e05c
- Unbundle hedley dependency

* Mon Mar 08 2021 Jun Aruga <jaruga@redhat.com> - 0.0.0-8.git396e05c
- Fix FTBFS.
  Resolves: rhbz#1923371

* Sat Feb 13 2021 Jeff Law <law@redhat.com> - 0.0.0-7.git396e05c
- Compile with -fno-strict-aliasing as this code clearly violates ISO aliasing rules

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-6.git396e05c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-5.git396e05c
- Fix FTBFS.
  Resolves: rhbz#1865487
- Skip clang flags case for arm 32-bit due to the segmentation fault.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-4.git396e05c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-3.git396e05c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-2.git396e05c
- Update to the latest upstream commit: 396e05c.

* Fri Apr 10 2020 Jun Aruga <jaruga@redhat.com> - 0.0.0-1.git29b9110
- Initial package
