Summary: Client and protocol library for the Couchbase project
Name: libcouchbase
Version: 3.3.14
Release: 2%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
BuildRequires: gcc, gcc-c++
BuildRequires: cmake >= 3.5.1
BuildRequires: pkgconfig(libevent) >= 2
BuildRequires: pkgconfig(libuv) >= 1
BuildRequires: libev-devel >= 3
BuildRequires: openssl-devel
BuildRequires: make
URL: https://docs.couchbase.com/c-sdk/current/project-docs/sdk-release-notes.html
Source: https://packages.couchbase.com/clients/c/%{name}-%{version}.tar.gz
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Recommends: %{name}-libevent%{_isa} = %{version}-%{release}
Suggests: %{name}-libev%{_isa} = %{version}-%{release}
Suggests: %{name}-tools%{_isa} = %{version}-%{release}
%endif

Patch0: %{name}-0001-enforce-system-crypto-policies.patch

# exclude from "Provides" private IO plugins
%{?filter_provides_in: %filter_provides_in %{name}/%{name}.*\.so$}
%{?filter_setup}

%description
This package provides the core for libcouchbase. It contains an IO
implementation based on select(2). If preferred, you can install one
of the available back-ends (libcouchbase-libevent or libcouchbase-libev).
libcouchbase will automatically use the installed back-end. It is also
possible to integrate another IO back-end or write your own.

%package libevent
Summary: Couchbase client library - libevent IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libevent
This package provides libevent back-end for libcouchbase.

%package libev
Summary: Couchbase client library - libev IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libev
This package provides libev back-end for libcouchbase.

%package libuv
Summary: Couchbase client library - libuv IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libuv
This package provides libuv back-end for libcouchbase.

%package tools
Summary: Couchbase client tools
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libevent%{?_isa} = %{version}-%{release}
%description tools
This is the CLI tools Couchbase project.

%package devel
Summary: Couchbase client library - Header files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the Couchbase client Library.

%prep
%autosetup -p1
%cmake -DLCB_NO_MOCK=1 -DLCB_BUILD_DTRACE=0

%build
%cmake_build

%install
%cmake_install

%check
export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build --target alltests
%ctest

%ldconfig_scriptlets

%files
%{_libdir}/%{name}.so.*
%doc README.markdown RELEASE_NOTES.markdown
%license LICENSE
%dir %{_libdir}/%{name}

%files libevent
%{_libdir}/%{name}/%{name}_libevent.so

%files libev
%{_libdir}/%{name}/%{name}_libev.so

%files libuv
%{_libdir}/%{name}/%{name}_libuv.so

%files tools
%{_bindir}/cbc*
%{_mandir}/man1/cbc*.1*
%{_mandir}/man4/cbcrc*.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.14-1
- Update to 3.3.14

* Wed Sep 25 2024 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.13-1
- Update to 3.3.13

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.12-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.12-1
- Update to 3.3.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 23 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.9-1
- Update to 3.3.9

* Sat Aug 19 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.8-2
- Disable systemtap integration to fix the build.

* Thu Aug 17 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.8-1
- Update to 3.3.8

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.7-2
- Fix systemtap exception for ppc64le

* Thu May 11 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.7-1
- Update to 3.3.7

* Wed Apr 26 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.6-1
- Update to 3.3.6

* Thu Mar 09 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.5-1
- Update to 3.3.5

* Tue Mar 07 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.4-2
- Disable systemtap support for AArch64

* Fri Feb 10 2023 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.3.4-1
- Update to 3.3.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.4-1
- Update to 3.2.4

* Wed Oct 20 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Wed Sep 22 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.2.1-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 20 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Tue May 11 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Mon Apr 26 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Fri Apr 09 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Wed Mar 03 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.0.7-2
- Use cmake macros for build, install and test steps

* Wed Dec 16 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.0.7-1
- Update to 3.0.7

* Sun Nov 15 2020 Jeff Law <law@redhat.com> - 2.10.8-2
- Disable pointer-comparison warning in StackLowerThanAddress

* Thu Sep 24 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.8-1
- Update to 2.10.8

- Mon Sep  7 2020 Remi Collet <remi@remirepo.net> - 2.10.6-3
- fix FTBFS #1863985

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.6-1
- Update to 2.10.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.5-1
- Update to 2.10.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.4-1
- Update to 2.10.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.3-2
- Add explicit curdir on CMake invocation

* Thu Dec 20 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Fri Nov 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.2-1
- Update to 2.10.2

* Fri Nov 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Thu Oct 18 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Fri Sep 21 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.5-1
- Update to 2.9.5

* Wed Aug 29 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.4-1
- Update to 2.9.4

* Wed Jul 18 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Sat Jul 14 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-4
- Display output of failed tests

* Fri Jul 13 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-3
- Fix build with libuv-1.21.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Fri Jun 22 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu May 24 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Wed May 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.7-2
- Port patch for JSON datatype

* Wed May 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.7-1
- Update to 2.8.7

* Fri Apr 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.6-1
- Update to 2.8.6

* Fri Feb 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.5-1
- Update to 2.8.5

* Mon Feb 19 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-5
- Rebuilt with libevent-2.1.8

* Wed Feb 14 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-4
- replace ldconfig scriptlets with macro
  https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Remi Collet <remi@remirepo.net> - 2.8.4-2
- filter private plugins (not shared libraries)

* Wed Dec 20 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-1
- Update to 2.8.4

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.3-2
- Parallel tests

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.3-1
- Update to 2.8.3

* Mon Nov 13 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.2-2
- Fix loading IO plugins

* Wed Oct 18 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Tue Sep 26 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.1-1
- Initial package
