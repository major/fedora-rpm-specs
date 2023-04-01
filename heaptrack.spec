
Name:    heaptrack
Version: 1.4.0
Release: 1%{?dist}
Summary: A heap memory profiler for Linux

License: GPLv2+
URL:     https://cgit.kde.org/heaptrack.git/

Source0: http://download.kde.org/stable/heaptrack/%{version}/src/%{name}-%{version}.tar.xz

Patch0:  heaptrack-gcc13.patch

BuildRequires:  desktop-file-utils

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kitemmodels-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kiconthemes-devel

BuildRequires:  kdiagram-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel

BuildRequires:  boost-devel
BuildRequires:  libunwind-devel
BuildRequires:  libdwarf-devel
BuildRequires:  elfutils-devel
BuildRequires:  libzstd-devel
BuildRequires:  sparsehash-devel
BuildRequires:  zlib-devel

# no libunwind on s390(x)
ExcludeArch:    s390 s390x

%description
Heaptrack traces all memory allocations and annotates these events with stack
traces.Dedicated analysis tools then allow you to interpret the heap memory
profile to:
- find hotspots that need to be optimized to reduce the memory footprint of your
  application
- find memory leaks, i.e. locations that allocate memory which is never
  deallocated
- find allocation hotspots, i.e. code locations that trigger a lot of memory
  allocation calls
- find temporary allocations, which are allocations that are directly followed
  by their deallocation


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf5 \
%if "%{?_lib}" == "lib64"
  %{?_cmake_lib_suffix64}
%endif

%cmake_build


%install
%cmake_install

%find_lang heaptrack --with-qt --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.heaptrack.desktop


%files -f heaptrack.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_bindir}/heaptrack
%{_bindir}/heaptrack_gui
%{_bindir}/heaptrack_print
%{_datadir}/applications/org.kde.heaptrack.desktop
%{_includedir}/heaptrack_api.h
%{_datadir}/metainfo/org.kde.heaptrack.appdata.xml
%dir %{_libdir}/heaptrack/
%{_libdir}/heaptrack/libheaptrack_inject.so
%{_libdir}/heaptrack/libheaptrack_preload.so
%{_libdir}/heaptrack/libexec/heaptrack_interpret
%{_libdir}/heaptrack/libexec/heaptrack_env
%{_datadir}/icons/hicolor/*/apps/heaptrack*


%changelog
* Thu Mar 30 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.0-1
- 1.4.0

* Mon Mar 06 2023 Jan Grulich <jgrulich@redhat.com> - 1.2.0-13
- Fix build failure against GCC13

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-12
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-9
- Add missing BR: elfutils-devel

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.0-8
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-6
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-2
- Rebuilt for Boost 1.75

* Tue Sep 01 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Tue Sep 01 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-10
- adapt to new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-7
- Rebuilt for Boost 1.73

* Thu Feb 27 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.0-6
- BR: libzstd-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-2
- Rebuilt for Boost 1.69

* Wed Jan 02 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-1
- 1.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 1.0.0-8
- Fix build against glibc >= 2.26 (rawhide/f27)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-5
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 23 2017 Jan Grulich <jgrulich@redhat.com> - 1.0.0-3
- Add BR: qt5-qtsvg-devel

* Sat Mar 11 2017 Dan Horák <dan[at]danny.cz> - 1.0.0-2
- exclude s390(x), because libunwind is not there

* Fri Mar 10 2017 Jan Grulich <jgrulich@redhat.com> - 1.0.0-1
- Initial version
