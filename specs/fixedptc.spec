Name:                  fixedptc
Version:               0

%global forgeurl       https://sourceforge.net/projects/%{name}/
%global date           20200303
%global commit         57887bd8c046c0c0394c22adc806d67bd5a71eaa
%global scm            hg
%global archiveext     zip
%global archivename    %{name}-code
%global forgesource    https://sourceforge.net/code-snapshots/%{scm}/f/fi/%{name}/code/%{archivename}-%{commit}.zip
%global forgesetupargs -n %{name}-code-%{commit}

%forgemeta

Release:               19%{?dist}
Summary:               Fixed point math header only library for C
# Automatically converted from old format: BSD - review is highly recommended.
License:               LicenseRef-Callaway-BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}
BuildArch:             noarch
BuildRequires:         gcc
BuildRequires: make

%description


%package  devel
Summary:  Fixed point math header only library for C
Requires: pkgconfig


%description devel
Development package for fixed point math header only library for C.

Features:
 - 32-bit and 64-bit precision support
   (for compilers with __int128_t extensions like gcc)
 - Arbitrary precision point (e.g. 24.8 or 32.32)
 - Pure header-only
 - Pure integer-only (suitable for kernels, embedded CPUs, etc)


%prep
%forgesetup

%build
%set_build_flags
export CFLAGS="${CFLAGS} -fPIE"
%{make_build} test verify_32
# This test requires 64-bit platform, so make it optional
%{make_build} test verify_64 || true

%install
install -p -m 0644 -D %{name}.h %{buildroot}%{_includedir}/%{name}/%{name}.h


%check
./test
./verify_32
# This test requires 64-bit platform, so make it optional
./verify_64 || true


%files devel
%license LICENSE
%doc README.txt
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-14
- Update to latest version
- Add -fPIE, fixes linking in F39

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-6.20200228hgb8acfec
- Remove detection of 64-bit platforms as it does not work on noarch packages, see:
  https://github.com/rpm-software-management/rpm/issues/1133#issuecomment-603138796

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-5.20200228hgb8acfec
- Fix bad %if condition:

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-4.20200228hgb8acfec
- Correct version string in the changelog history
- Remove -v option from forgemeta

* Wed Mar 18 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-3.20200228hgb8acfec
- Add generated license text

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-2.20200228hgb8acfec
- Use %%set_build_flags

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20200228hgb8acfec
- Remove patches upstream merged

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20150308hg80b0448
- Initial RPM release.
