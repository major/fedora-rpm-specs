%define _lto_cflags %{nil}

Name:       libfaketime
Version:    0.9.12
Release:    1%{?dist}
Summary:    Manipulate system time per process for testing purposes
# most of the code is GPL-2.0-or-later AND GPL-3.0-only
# part of src/libfaketime.c is GPLv3
License:    GPL-2.0-or-later AND GPL-3.0-only
URL:        https://github.com/wolfcw/libfaketime
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Provides:   faketime = %{version}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-Time-HiRes

%description
libfaketime intercepts various system calls that programs use to retrieve the
current date and time. It then reports modified (faked) dates and times (as
specified by you, the user) to these programs. This means you can modify the
system time a program sees without having to change the time system-wide.

%prep
%autosetup -p1

%build
%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif

%set_build_flags
%make_build all

%check
%ifarch ppc64le
  export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif

make -C test

%install
%make_install PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}

# Pick up docs in the files section
rm -fr %{buildroot}/%{_docdir}/faketime

%files
%license COPYING
%doc README NEWS README.developers
%{_bindir}/faketime
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}MT.so.1
%{_mandir}/man1/faketime.1*

%changelog
* Mon Jul 14 2025 Simone Caronni <negativo17@gmail.com> - 0.9.12-1
- Update to 0.9.12.
- Revamp completely SPEC file and build.

* Mon Jul 14 2025 Simone Caronni <negativo17@gmail.com> - 0.9.10-12
- Trim changelog.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Paul Wouters <paul.wouters@aiven.io> - 0.9.10-7
- Fix for building for riscv64

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Pablo Greco <pgreco@centosproject.org> - 0.9.10-5
- Fix tests in ELN builds (yselkowitz)

* Tue Feb 21 2023 Pablo Greco <pgreco@centosproject.org> - 0.9.10-4
- Also disable i686 in rhel>=10 (ELN failures)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Pablo Greco <pgreco@centosproject.org> - 0.9.10-1
- Update to 0.9.10
- Disable i686 and armhfp in fedora >=36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
