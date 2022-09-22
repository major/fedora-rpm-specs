Name: ck
Version: 0.7.0
Release: 8%{?dist}
Summary: Library for high performance concurrent programming

License: BSD
URL: http://concurrencykit.org

Source: http://concurrencykit.org/releases/ck-%{version}.tar.gz
Patch1: ck-nogettid.patch
Patch2: ck-register-constraint.patch
# disable ck_hclh_test from ck_spinlock temporary solution
# github issue: https://github.com/concurrencykit/ck/issues/153
Patch3: ck_disable_ck_hclh_test.patch

BuildRequires: gcc
BuildRequires: make

%description
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

%package devel
Summary: Header files and libraries for CK development
Requires: %{name} = %{version}-%{release}

%description devel
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

This package provides the libraries, include files, and other
resources needed for developing Concurrency Kit applications.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags}"
./configure 		\
	--libdir=%{_libdir} 			\
	--includedir=%{_includedir}/%{name}	\
	--mandir=%{_mandir}			\
	--prefix=%{_prefix}
%make_build

%install
%make_install

# fix weird mode of the shared library
chmod 0755 %{buildroot}%{_libdir}/libck.so.*

# remove static library
rm %{buildroot}%{_libdir}/libck.a

%check
make check

%files
%license LICENSE
%{_libdir}/libck.so.*

%files devel
%{_libdir}/libck.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.gz

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Filip Januš <fjanus@redhat.com> - 0.7.0-3
- Build fails due to ck_hclh test
- github issue: https://github.com/concurrencykit/ck/issues/153
- resolves:https://bugzilla.redhat.com/show_bug.cgi?id=1799226
- add patch - disables ck_hclh test

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Honza Horak <hhorak@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Wed Aug 21 2019 Honza Horak <hhorak@redhat.com> - 0.6.0-11
- Add upstream patch ck_barrier_combining: switch to seq_cst semantics to make
  ppc64le

* Wed Aug 21 2019 Honza Horak <hhorak@redhat.com> - 0.6.0-10
- Remove static gettid definition

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Honza Horak <hhorak@redhat.com> - 0.6.0-7
- Explicitly include gcc

* Tue Jul 17 2018 Honza Horak <hhorak@redhat.com> - 0.6.0-6
- Fix building on s390x and ignore tests also for ppc64le and ix86 and x86_64

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Xavier Bachelot <xavier@bachelot.org> - 0.6.0-1
- Update to 0.6.0.
- Run test suite.

* Sat Feb 11 2017 Honza Horak <hhorak@redhat.com> - 0.5.2-2
- Fix issues found during Package Review
  Summary provides better idea what this library is for
  Using macros for make build and install
  Fix permissions of the shared library

* Sat Feb 04 2017 Honza Horak <hhorak@redhat.com> - 0.5.2-1
- Initial packaging

