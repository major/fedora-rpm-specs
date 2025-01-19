Name:           lv2-ir-plugins
Version:        1.3.4
Release:        20%{?dist}
Summary:        LV2 Plugin: low-latency, real-time, high performance signal convolver

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tomszilagyi.github.io/plugins/ir.lv2/
Source0:        https://github.com/tomszilagyi/ir.lv2/archive/%{version}.tar.gz#/ir.lv2-%{version}.tar.gz

# This patch modifies the realtime priority as reported in the source
# Priority should match -P parameter passed to jackd, which defaults to 20
Patch0:         %{name}-realtime-priority.patch
# Fix FTBFS with recent LV2
# Patch sent upstream https://github.com/tomszilagyi/ir.lv2/pull/24
Patch1:         %{name}-lv2.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  zita-convolver-devel >= 3.1
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  gtk2-devel >= 2.20
BuildRequires:  fftw-devel

Requires:       lv2 >= 1.8.1

%description
IR is a low-latency, real time, high performance signal
convolver especially for creating reverb effects. Supports impulse
responses with 1, 2 or 4 channels, in any sound file format supported
by libsndfile.

%prep
%autosetup -p 1 -n ir.lv2-%{version}

# Delete old LV2 include file just to be safe
rm lv2_ui.h

%build
export CPPFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build INSTDIR="%{_libdir}/lv2"

%install
%make_install INSTDIR="%{buildroot}%{_libdir}/lv2"

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/ir.lv2/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.4-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.4-9
- Fix FTBFS with recent LV2
- Add BR make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.4-5
- Rebuilt for zita-convolver upgrade

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.4-3
- Fix wrong installation directory (#1607088)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.4-1
- Version 1.3.4
- Spec cleanup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.3-1
- Version 1.3.3
- Use hardened LDFLAGS

* Thu Dec 01 2016 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.2-3
- Corrected FSF address

* Fri Nov 11 2016 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.2-2
- Modified real time priority to match Jack's default value

* Thu Sep 08 2016 Guido Aulisi <guido.aulisi@gmail.com> - 1.3.2-1
- Version 1.3.2
