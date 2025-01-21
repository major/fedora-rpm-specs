%global commit_simde fefc7857ff3e785b988a61a8f5f3c5bd5eb24342
%global short_commit_simde %(c=%{commit_simde}; echo ${c:0:7})
# Disable debuginfo package for the header only package.
%global debug_package %{nil}

# Disable the auto_set_build_flags. Because it sets clang flags for gcc in
# the %%check section.
%undefine _auto_set_build_flags

%global simde_version 0.8.2
# %%global rc_version 1

Name: simde
Version: %{simde_version}%{?rc_version:~rc%{rc_version}}
# Align the release format with the packages setting Source0 by commit hash
# such as podman.spec and moby-engine.spec.
Release: 3%{?dist}
Summary: Implementations of SIMD instruction sets for non-native systems
# find simde/ -type f | xargs licensecheck
#   simde: MIT
#   simde/check.h: CC0-1.0
#   simde/debug-trap.h: CC0-1.0
#   simde/simde-align.h: CC0-1.0
#   simde/simde-arch.h: CC0-1.0
#   simde/simde-detect-clang.h: CC0-1.0
# removed in %%prep (unbundled):
#   simde/hedley.h: CC0
# Consider relicensing CC0 code to another license (MIT?)
# https://github.com/simd-everywhere/simde/issues/999
License: MIT AND CC0-1.0
URL: https://github.com/simd-everywhere/simde
Source0: https://github.com/simd-everywhere/simde/archive/v%{version}/simde-%{version}.tar.gz
# fix for https://github.com/simd-everywhere/simde/issues/1200
Patch: https://github.com/simd-everywhere/simde/pull/1220/commits/a891834ff66c80bb9e0491d6be92c7ab7ed6362f.patch#/simde-issue-1200.patch
# avoid warnings when "__ARM_NEON_FP" is not defined
Patch: https://github.com/simd-everywhere/simde/commit/f046ab773733f09edaadec30345b592dfe85368e.patch
# Partial fix for https://github.com/simd-everywhere/simde/issues/1203
Patch: https://github.com/simd-everywhere/simde/commit/a1ce45cf5dc2253a1f9c0590fe111ebd8d1613c0.patch
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
Requires: hedley-devel
Requires: hedley-static
# subpackage can be noarch, it's identical across all arches
# the main package is archful, so tests run on all arches
BuildArch: noarch
Obsoletes: simde-devel < 0.8.2-2%{?dist}

%description devel
The simde-devel package contains the header files needed
to develop programs that use the SIMDe.

%prep
%autosetup -n %{name}-%{version} -p1
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
    exit 1
  elif [ -x "${file}" ]; then
    echo "${file} has executable bit."
    exit 1
  fi
done
EOF

# Only test the GCC and Clang cases with RPM build flags.
# If you find test failures on the cases, reproduce it in the upstream CI.
# in the O2 or RPM build flags cases, and report it.
# See <https://github.com/simd-everywhere/simde/blob/master/.packit/>.

# Copy to use the modified script.
cp -p .packit/ci.sh ci.sh
# Suppress the system info.
sed -i -e '/^cat \/proc\/cpuinfo/ s/^/#/' ci.sh
sed -i -e '/^cat \/proc\/meminfo/ s/^/#/' ci.sh
# Use the meson RPM package instead of the PyPI package.
sed -i -e '/^pip3 install meson/ s/^/#/' ci.sh
# Comment out the default configuration.
sed -i -e '/^IGNORE_EXIT_STATUS=/ s/^/#/' ci.sh
sed -i -e '/^MATRIX_.*=/ s/^/#/' ci.sh
# Prepare the configuration.
cat > config.txt <<EOF
IGNORE_EXIT_STATUS=
MATRIX_DEFAULT_GCC_DEFAULT="exclude"
MATRIX_DEFAULT_GCC_O2="exclude"
MATRIX_DEFAULT_GCC_RPM="include"
MATRIX_DEFAULT_CLANG_DEFAULT="exclude"
MATRIX_DEFAULT_CLANG_O2="exclude"
MATRIX_DEFAULT_CLANG_RPM="include"
# https://github.com/simd-everywhere/simde/issues/1201
MATRIX_i686_GCC_RPM="exclude"
# https://github.com/simd-everywhere/simde/issues/1202
MATRIX_i686_CLANG_RPM="exclude"
# internal compiler error
MATRIX_ppc64le_CLANG_RPM="exclude"
# https://github.com/simd-everywhere/simde/issues/1203
MATRIX_s390x_CLANG_RPM="exclude"
EOF
# Insert the configuration.
sed -i -e '/^# Configuration$/r config.txt' ci.sh
# Print the difference on the debugging purpose.
if diff -u .packit/ci.sh ci.sh; then
  exit 1
elif "${?}" != 1; then
  exit 2
fi

# Set environment variables to test with RPM build flags.
# See <https://github.com/simd-everywhere/simde/blob/master/.packit/simde.spec>.
# Append the `-fno-strict-aliasing` for a compatibility from the past commit
# below, though it's not related to the shipping simde RPM package.
# https://src.fedoraproject.org/rpms/simde/c/3371c3a422f2512562fd4641b956d0c4b848c7ec
%global toolchain clang
export CI_CLANG_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_CLANG_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_CLANG_RPM_LDFLAGS="%{build_ldflags}"
%global toolchain gcc
export CI_GCC_RPM_CFLAGS="%{build_cflags} -fno-strict-aliasing"
export CI_GCC_RPM_CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing"
export CI_GCC_RPM_LDFLAGS="%{build_ldflags}"

# Run tests.
/bin/time -f '=> [%E]' ./ci.sh

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 13 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.8.2-2
- use upstream PR to fix tests with clang on aarch64
- switch to noarch for the devel subpackage (tests still run on all arches)

* Fri Jul 26 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.8.2-1
- Upgrade to SIMDe 0.8.2
  Resolves: rhbz#2251016
- Use upstream ci.sh
- Fix build on aarch64 and backport some upstream fixes

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5.gitfefc785
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Pavel Solovev <daron439@gmail.com> - 0.7.6-4.gitfefc785
- fix -devel deps

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3.gitfefc785
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2.gitfefc785
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Jun Aruga <jaruga@redhat.com> - 0.7.6-1.gitfefc785
- Upgrade to SIMDe 0.7.6.
  Resolves: rhbz#2192076

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
