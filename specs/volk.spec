Name:          volk
Version:       3.1.2
Release:       5%{?dist}
Summary:       The Vector Optimized Library of Kernels
License:       GPL-3.0-or-later
URL:           https://github.com/gnuradio/%{name}
Source0:       https://github.com/gnuradio/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/gnuradio/volk/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:       https://github.com/gnuradio/volk/releases/download/v2.4.1/gpg_volk_release_key.asc

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-mako
BuildRequires: orc-devel
BuildRequires: sed
%ifnarch s390x
BuildRequires: google-cpu_features-devel
%endif
Conflicts:     python3-gnuradio < 3.9.0.0
Conflicts:     gnuradio-devel < 3.9.0.0

%description
VOLK is the Vector-Optimized Library of Kernels. It is a library that contains
kernels of hand-written SIMD code for different mathematical operations.
Since each SIMD architecture can be very different and no compiler has yet
come along to handle vectorization properly or highly efficiently, VOLK
approaches the problem differently. VOLK is a sub-project of GNU Radio.


%package devel
Summary:       Development files for VOLK
Requires:      %{name}%{?_isa} = %{version}-%{release}
Conflicts:     vulkan-volk-devel


%description devel
%{summary}.
%ifarch s390x
Conflicts:     google-cpu_features-devel
%endif


%package doc
Summary:       Documentation files for VOLK
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch


%description doc
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# fix shebangs
pushd python/volk_modtool
sed -i '1 {/#!\s*\/usr\/bin\/env\s\+python/ d}' __init__.py cfg.py
popd

%build
# workaround, the code is not yet compatible with the strict-aliasing
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%cmake
%cmake_build

# Use make_build for EL8 compat
%make_build -C %{__cmake_builddir} volk_doc


# temporally disabled the testsuite due to https://github.com/gnuradio/volk/issues/442
# gnuradio (and all volk consumers) could coredump on s390x and ppc64le under some
# circumstances, see https://bugzilla.redhat.com/show_bug.cgi?id=1917625#c6
#%%check
#cd %{__cmake_builddir}
#make test


%install
%cmake_install

# docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a %{__cmake_builddir}/html %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc README.md docs/CHANGELOG.md
%{_bindir}/volk-config-info
%{_bindir}/volk_modtool
%{_bindir}/volk_profile
%{_libdir}/libvolk*.so.*
%{python3_sitearch}/volk_modtool


%files devel
%{_includedir}/volk
%{_libdir}/libvolk.so
%{_libdir}/cmake/volk
%{_libdir}/pkgconfig/*.pc


%files doc
%doc %{_docdir}/%{name}/html


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.2-3
- Rebuilt for Python 3.13

* Fri Mar 29 2024 Zhengyu He <hezhy472013@gmail.com> - 3.1.2-2
- Enable google-cpu_features for riscv64

* Mon Feb 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.1.2-1
- New version
  Resolves: rhbz#2266046
- Converted license tag to SPDX

* Thu Feb  1 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.1.1-1
- New version
  Resolves: rhbz#2262148

* Wed Jan 31 2024 José Expósito <jexposit@redhat.com> - 3.1.0-3
- Add conflict with vulkan-volk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 3.1.0-1
- New version
  Resolves: rhbz#2253664

* Thu Oct 19 2023 Marcus Müller <marcus_fedora@baseband.digital> - 3.0.0-4
- Depend on system google-cpu_features-devel instead of using the vendored
- Fixes rhbz#2245047

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 3.0.0-1
- New version
  Resolves: rhbz#2161009

* Mon Sep  5 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.2-1
- New version
  Resolves: rhbz#2124323

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.1-1
- New version
  Resolves: rhbz#2053851

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.0-1
- New version
  Resolves: rhbz#1968142

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.1-6
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.1-5
- Updated patch for python detection

* Mon Feb 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.1-4
- Fixed python detection
  Resolves: rhbz#1928144

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.1-2
- Fixed according to the review
  Related: rhbz#1917625

* Mon Jan 18 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 2.4.1-1
- Initial release
  Related: rhbz#1917167
