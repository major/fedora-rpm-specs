# git ls-remote git://github.com/dl1ksv/gr-funcube.git
%global git_commit cbda6c6cd5de9731734985aa6f67ea85a2b0e193
%global git_date 20240726

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          gr-funcube
URL:           https://github.com/dl1ksv/gr-funcube
Version:       3.10.0~rc3^%{git_suffix}
Release:       4%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: hidapi-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: pybind11-devel
BuildRequires: libunwind-devel
BuildRequires: alsa-lib-devel
BuildRequires: libusbx-devel
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: gmp-devel
BuildRequires: libsndfile-devel
# for _udevrulesdir macro
BuildRequires: systemd-rpm-macros
Obsoletes:     gr-fcdproplus < 3.8.0-5.20200807git06069c2e
Summary:       GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+
Source0:       %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:       10-funcube.rules

%description
GNURadio support for FUNcube Dongle Pro and FUNcube Dongle Pro+.

%package devel
Summary:       Development files for gr-funcube
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-funcube.

%package doc
Summary:       Documentation files for gr-funcube
Requires:      %{name} = %{version}-%{release}
# Workaround for rhbz#1814356
#BuildArch:    noarch

%description doc
Documentation files for gr-funcube.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%check
# Temporary disabled until resolved ppc64le problems
#cd %{_vpath_builddir}
#make test

%install
%cmake_install

# udev rule
install -Dpm 0644 %{S:1} %{buildroot}%{_udevrulesdir}/10-funcube.rules

%ldconfig_scriptlets

%pre
# sharing group with the rtl-sdr package not to introduce new group
# todo: consolidate also with the uhd package (usrp group) to have one generic
# group e.g. 'sdr' for this class of devices
getent group rtlsdr >/dev/null || \
  %{_sbindir}/groupadd -r rtlsdr >/dev/null 2>&1
exit 0

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license COPYING
%doc README.md
%{_libdir}/*.so.*
%{python3_sitearch}/funcube
%{_datadir}/gnuradio/grc/blocks/*
%{_udevrulesdir}/10-funcube.rules

%files devel
%{_includedir}/funcube
%{_libdir}/*.so
%{_libdir}/cmake/funcube

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0~rc3^20240726gitcbda6c6c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.10.0~rc3^20240726gitcbda6c6c-3
- Rebuilt for new spdlog
  Resolves: rhbz#2329123

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 3.10.0~rc3^20240726gitcbda6c6c-2
- Rebuilt for spdlog 1.15.0

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.10.0~rc3^20240726gitcbda6c6c-1
- New snapshot

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-34.20220130gitbf71b979
- Rebuilt for new gnuradio

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-33.20220130gitbf71b979
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Python Maint <python-maint@redhat.com> - 1.0.0-31.20220130gitbf71b979
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 1.0.0-30.20220130gitbf71b979
- Rebuilt for spdlog 1.14.1

* Thu Apr 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-29.20220130gitbf71b979
- Rebuilt for new gnuradio

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-26.20220130gitbf71b979
- Rebuilt for new gnuradio

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-24.20220130gitbf71b979
- Rebuilt for new python
  Resolves: rhbz#2220006

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-23.20220130gitbf71b979
- Rebuilt due to spdlog 1.12 update.

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-22.20220130gitbf71b979
- Rebuilt due to fmt 10 update.

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-21.20220130gitbf71b979
- Rebuilt for new gnuradio

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-20.20220130gitbf71b979
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-18.20220130gitbf71b979
- Rebuilt due to spdlog update.

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-17.20220130gitbf71b979
- Rebuilt for new gnuradio
  Resolves: rhbz#2129779

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16.20220130gitbf71b979
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-15.20220130gitbf71b979
- Rebuild for fmt.

* Thu Jun 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-14.20220130gitbf71b979
- Rebuilt for new gnuradio

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 1.0.0-13.20220130gitbf71b979
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-12.20220130gitbf71b979
- Rebuilt for new gnuradio

* Tue Mar 29 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-11.20220130gitbf71b979
- Bumped release a bit to fix upgrade path

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-4.20220130gitbf71b979
- Rebuilt for new gnuradio

* Tue Feb 15 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-3
- Use double for ppm

* Mon Jan 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-2.20220130gitbf71b979
- Rebuilt for new gnuradio

* Sun Jan 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-1.20220130gitbf71b979
- New version

* Thu Jan 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-10
- Rebuilt for new gnuradio

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-8
- Rebuilt for new gnuradio

* Thu Nov  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-7
- Rebuild for new gnuradio
  Resolves: rhbz#2020176

* Thu Oct  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-6
- Rebuilt for new gnuradio
  Resolves: rhbz#2011279

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-5
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-3
- Rebuilt for new gnuradio
  Resolves: rhbz#1971251

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.10

* Wed Feb 17 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-1
- Initial version
  Related: rhbz#1924712
