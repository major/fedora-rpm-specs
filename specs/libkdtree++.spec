Name:           libkdtree++
Version:        0.7.5
Release:        2%{?dist}
Summary:        C++ template container implementation of kd-tree sorting
URL:            https://github.com/nvmd/libkdtree
License:        Artistic-2.0

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  swig

Source0:        https://github.com/nvmd/libkdtree/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix python module build
Patch0:         libkdtree_cmake.patch
# Fix python test
Patch1:         libkdtree_pythontest.patch

%description
%{summary}.


%package devel
Summary:        C++ template container implementation of kd-tree sorting
BuildArch:      noarch

%description devel
%{summary}.


%package -n python3-libkdtree++
Summary:        Python3 language bindings for libkdtree++

%description -n python3-libkdtree++
%{summary}.


%prep
%autosetup -p1 -n libkdtree-%{version}

# convert files from ISO-8859-1 to UTF-8 encoding
for f in README.md
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done


%build
pushd python-bindings
%{__python3} gen-swig-hpp.py
popd
%cmake -DBUILD_PYTHON_BINDINGS=ON
%cmake_build


%install
%cmake_install

# Fix python module permission
chmod 0755 %{buildroot}%{python3_sitearch}/_kdtree.so

sed \
  -e 's|@prefix@|%{_prefix}|' \
  -e 's|@libdir@|%{_libdir}|' \
  -e 's|@includedir@|%{_includedir}/kdtree++|' \
  -e 's|@VERSION@|%{version}|' \
  pkgconfig/libkdtree++.pc.in > pkgconfig/libkdtree++.pc
install -Dpm 0644 pkgconfig/libkdtree++.pc %{buildroot}%{_datadir}/pkgconfig/libkdtree++.pc




%check
pushd %{_vpath_builddir}/examples
./test_find_within_range
./test_hayne
./test_kdtree
popd
pushd python-bindings
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} py-kdtree_test.py
popd


%files devel
%doc README.md
%license COPYING
%{_includedir}/kdtree++/
%{_datadir}/pkgconfig/libkdtree++.pc

%files -n python3-libkdtree++
%doc README.md
%license COPYING
%{python3_sitearch}/_kdtree.so
%{python3_sitearch}/kdtree.py
%{python3_sitearch}/__pycache__/*


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Oct 13 2025 Sandro Mani <manisandro@gmail.com> - 0.7.5-1
- Update to 0.7.5

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.7.4-3
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.14.0rc2 bytecode

* Sun Aug 03 2025 Sandro Mani <manisandro@gmail.com> - 0.7.4-1
- Update to 0.7.4
- Modernize spec

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.7.0-43
- Rebuilt for Python 3.14

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.0-40
- Rebuilt for Python 3.13

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-39
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.0-35
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-32
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0-29
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-26
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-24
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-23
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-21
- Added Debian's patch for GCC 5 and newer.
- Add Python 3 bindings and drop Python 2 bindings

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-17
- Python 2 binary package renamed to python2-libkdtree++
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-14
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-4
- Updated based on package review.

* Sat Sep 29 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-3
- Updated based on package review.

* Fri Jun 22 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-2
- Updated based on package review.

* Sat Dec 03 2011 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-1
- Initial version
