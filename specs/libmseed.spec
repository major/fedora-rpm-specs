Name:		libmseed
Version:	2.19.5
Release:	20%{?dist}
License:	LGPL-3.0-or-later
Summary:	A C library framework for manipulating and managing SEED data records
Url:		https://www.iris.edu/ds/nodes/dmc/software/downloads/libmseed
Source0:	https://github.com/iris-edu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream doesn't want this, but we want to fail the build for failing tests.
Patch0001:	0001-Fail-tests-early.patch

BuildRequires:	binutils
BuildRequires:	diffutils
BuildRequires:	gcc
BuildRequires:	make

%package devel
Summary:	%{summary}
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description
The Mini-SEED library provides a framework for manipulation of SEED data
records including the unpacking and packing of data records. Functionality is
also included for managing waveform data as continuous traces. All structures
of SEED 2.4 data records are supported with the following exceptions:
Blockette 2000 opaque data which has an unknown data structure by definition
and Blockette 405 which depends on full SEED (SEED including full ASCII
headers) for a full data description.

%description devel
Development files for %{name} library.


%prep
%autosetup -p1


# This code is not strict-aliasing safe.  See the various swap routines
%build
CC=gcc CFLAGS="%{optflags} -fno-strict-aliasing" %make_build shared

pushd example
CC=gcc CFLAGS="%{optflags} -fno-strict-aliasing" %make_build all
popd


%install
%make_install \
	PREFIX=%{_prefix} \
	EXEC_PREFIX=%{_exec_prefix} \
	LIBDIR=%{_libdir} \
	INCLUDEDIR=%{_includedir} \
	DATAROOTDIR=%{_datarootdir} \
	DOCDIR=%{_docdir}/%{name} \
	MANDIR=%{_mandir} \
	install

mkdir -p %{buildroot}%{_bindir}
cp -pd example/msrepack example/msview %{buildroot}%{_bindir}/

# We don't use this.
rm -rf %{buildroot}%{_docdir}/%{name}


%check
pushd test
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" make test
popd


%files
%doc README.md README.byteorder ChangeLog
%license LICENSE.txt
%{_bindir}/msrepack
%{_bindir}/msview
%{_libdir}/libmseed.so.*

%files devel
%doc doc/libmseed-UsersGuide example/test.mseed
%license LICENSE.txt
%{_includedir}/libmseed.h
%{_libdir}/libmseed.so
%{_libdir}/pkgconfig/mseed.pc
%{_mandir}/man3/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.19.5-18
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Jeff Law <law@redhat.com> - 2.19.5-9
- Disable strict-aliasing as this code is not strict-aliasing safe

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.19.5-3
- Remove unnecessary ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.19.5-1
- New upstream release

* Sun Aug 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.19.4-4
- Add more explicit BRs.

* Sun Aug 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.19.4-3
- Fix license to LGPLv3+.
- Use more macros.

* Fri Aug 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.19.4-2
- Minor tweaks to spec.

* Thu Jun 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.19.4-1
- New upstream release

* Sat Mar 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.19.2-3
- New upstream release

* Thu Mar 16 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.19.2-2
- Fix global variable symbol export

* Fri Mar 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.19.2-1
- New upstream release

* Sat Oct 15 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18-1
- New upstream release

* Thu Feb 18 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.17-2
- Rebuild for Rawhide

* Mon Aug 3 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.17-1
- New upstream release

* Thu May 14 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16m-1
- New upstream release

* Fri May 08 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.16-1
- New upstream release

* Thu Mar 12 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.15-1
- New upstream release
- Remove patch that was applied upstream

* Wed Mar 11 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.14-1
- New upstream release

* Tue Oct 21 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.13-3
- Add patch for infinite loop on corrupt files

* Wed Aug 27 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.13-2
- Add example programs to package

* Tue Aug 26 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.13-1
- New upstream release

* Thu Aug 21 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.12-4
- Add parallel build patch

* Wed Aug 20 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.12-3
- Add missing include file

* Wed Aug 20 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.12-2
- Include patches from ObsPy

* Wed Aug 20 2014 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.12-1
- Initial package release
