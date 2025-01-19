%global sover 1.6

Name:           liquid-dsp
Version:        1.6.0
Release:        3%{?dist}
Summary:        Digital Signal Processing Library for Software-Defined Radios

License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch configure.ac for ppc64
Patch1:         ppc64-configureac.patch
# fixes ppc64 altivec, other 64-bit problems. Patch by Dan Horák.
# https://github.com/jgaeddert/liquid-dsp/pull/136
Patch3:         ppc64.patch

ExcludeArch:    i686

BuildRequires:  gcc
BuildRequires:  fftw-devel fftw-libs-single
BuildRequires:  autoconf automake libtool
BuildRequires:  make

%description
Digital signal processing library for software-defined radios

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Digital signal processing library for software-defined radios


%prep
%autosetup -p1 -n %{name}-%{version}
autoreconf -f -i


%build
%configure --exec_prefix=/ --enable-simdoverride
%make_build


%check
make check


%install
%make_install
pushd ${RPM_BUILD_ROOT}/%{_libdir} > /dev/null 2>&1
rm libliquid.a
chmod a+x libliquid.so.%{sover}
popd > /dev/null 2>&1

%ldconfig_scriptlets


%files
%license LICENSE
%{_libdir}/libliquid.so.1
%{_libdir}/libliquid.so.%{sover}

%files -n %{name}-devel
%{_includedir}/liquid/
%{_libdir}/libliquid.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-1
- Update to 1.6.0.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb  7 2022 Matt Domsch <matt@domsch.com> 1.4.0-2
- Use full version number for soname

* Sat Feb  5 2022 Matt Domsch <matt@domsch.com> 1.4.0-1
- Upstream 1.4.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6.20201010git7ad2496
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5.20201010git7ad2496
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4.20201010git7ad2496
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Matt Domsch <matt@domsch.com> 1.3.2-3.20201010git7ad2496
- Upstream removed the exit() calls https://github.com/jgaeddert/liquid-dsp/issues/134
- invoke autoreconf at build time, as upstream doesn't package what we need
- Add BR: fftw-devel
- Remove BR: gcovr and --enable-coverage. It was keeping the exit call in the library,
  and we aren't looking at the coverage results anyhow.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr  7 2020 Matt Domsch <matt@domsch.com> 1.3.2-1
- upstream 1.3.2
- upstream constantly changes the ABI in backwards-incompatible ways without versioning
  with sonames themselves. Add a fedora_soname.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  15 2018 Matt Domsch <matt@domsch.com> 1.3.1-3.20180806git9658d81
- apply patch fixing ppc64, armv7hl build failures

* Tue Aug  14 2018 Matt Domsch <matt@domsch.com> 1.3.1-2.20180806git9658d81
- remove -faltivec from ppc64le build gcc args

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 1.3.1-1.20180806git9658d81
- Initial Fedora packaging
