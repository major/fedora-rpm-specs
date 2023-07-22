Name:           lmfit
Version:        8.2.2
%global         sover 8
Release:        11%{?dist}
Summary:        Levenberg-Marquardt least-squares minimization and curve fitting
# software is BSD, documentation is CC-BY
License:        BSD and CC-BY
URL:            https://jugit.fz-juelich.de/mlz/lmfit
Source0:        https://jugit.fz-juelich.de/mlz/lmfit/-/archive/v%{version}/lmfit-v%{version}.tar.bz2
Patch0:         8828e7071ed30dbded893228b1043b040b5cd26e.patch
Patch1:         version.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  %{_bindir}/pod2html

%description
C/C++ library for Levenberg-Marquardt least-squares minimization and curve
fitting

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
cp -ra demo _demo

# install to libdir
sed -i 's@${destination}/lib@${destination}/%{_lib}@' lib/CMakeLists.txt CMakeLists.txt

# install to mandir
sed -i 's@${CMAKE_INSTALL_PREFIX}/man@%{_mandir}@' man/CMakeLists.txt


%build
%{cmake}
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_mandir}/html %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/*.la
rm -rf demo
mv -f _demo demo

%check
%ctest

%files
%doc COPYING CHANGELOG
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc demo
%doc %{_datadir}/doc/lmfit/
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 8.2.2-5
- Fix out-of-source build on F33 (bug #1864079)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Christoph Junghans <junghans@votca.org> - 8.2.2-1
- Version bump to 8.2.2 (bug #1673313)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Miro Hrončok <mhroncok@redhat.com> - 8.2-1
- New release 8.2

* Thu Jan 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0-1
- New release 7.0 (#1509735)
- No more autotools, but cmake
- Remove ldconfig scripts

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Christoph Junghans <junghans@votca.org> - 6.4-1
- New release 6.4 (#1509735)

* Wed Nov 01 2017 Miro Hrončok <mhroncok@redhat.com> - 6.2-1
- New release 6.2 (#1508193)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Miro Hrončok <mhroncok@redhat.com> - 6.1-1
- New release 6.1 (#1289968)

* Fri Nov 27 2015 Miro Hrončok <mhroncok@redhat.com> - 6.0-1
- New release 6.0 (#1285385)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 5.1-1
- New version 5.1
- Download location has changed

* Tue Aug 27 2013 Miro Hrončok <mhroncok@redhat.com> - 5.0-1
- New upstream version
- Website has moved
- Add all HTML docs to %%doc
- Moved manpages and their HTML variants and demo to devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 04 2013 Miro Hrončok <mhroncok@redhat.com> - 3.5-2
- Do not package demo binaries to %%doc
- Added --disable-static to configure

* Sun Feb 03 2013 Miro Hrončok <mhroncok@redhat.com> - 3.5-1
- Initial package
