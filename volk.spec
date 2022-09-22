Name:          volk
Version:       2.5.2
Release:       1%{?dist}
Summary:       The Vector Optimized Library of Kernels
License:       GPLv3+
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


%description devel
%{summary}.


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

# drop list_cpu_features, not needed, just some demo binary,
# unavailable on s390x, for details see:
# https://github.com/gnuradio/volk/issues/442#issuecomment-772059840
rm -f %{buildroot}%{_bindir}/list_cpu_features

# drop static objects
rm -f %{buildroot}%{_libdir}/libcpu_features.a

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
%ifnarch s390x
%{_includedir}/cpu_features
%{_libdir}/cmake/CpuFeatures
%endif
%{_libdir}/libvolk.so
%{_libdir}/cmake/volk
%{_libdir}/pkgconfig/*.pc


%files doc
%doc %{_docdir}/%{name}/html


%changelog
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
