Name:           cgreen
Version:        1.6.2
Release:        5%{?dist}
Summary:        Modern unit test and mocking framework for C and C++
License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=2068898
ExcludeArch: s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  asciidoctor

%description
A modern, portable, cross-language unit testing and mocking framework for C
and C++.


%package devel
Summary:        Libraries and headers for developing programs with Cgreen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with Cgreen.


%package runner
Summary:        A runner for the Cgreen unit testing and mocking framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description runner
A runner for the Cgreen unit testing and mocking framework.


%prep
%autosetup -p1

%build
%cmake -DCGREEN_WITH_HTML_DOCS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libcgreen.so.1*


%files devel
%doc doc/cgreen-guide-en-docinfo.html
%{_libdir}/libcgreen.so
%{_includedir}/cgreen
%{_libdir}/cmake/cgreen


%files runner
%{_bindir}/cgreen-debug
%{_bindir}/cgreen-runner
%{_mandir}/man1/cgreen-runner.1*
%{_mandir}/man1/cgreen-debug.1*
%{_mandir}/man5/cgreen.5*
%{_datadir}/bash-completion/completions/cgreen-debug
%{_datadir}/bash-completion/completions/cgreen-runner


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 06 2023 Egor Artemov <egor.artemov@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 27 2022 Egor Artemov <egor.artemov@gmail.com> - 1.5.1-1
- Bump to 1.5.1 version

* Sun Jan 23 2022 Egor Artemov <egor.artemov@gmail.com> - 1.4.1-1
- Bump to 1.4.1 version

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Egor Artemov egor.Artemov@gmail.com - 1.3.0-1
- Upstream fixed bugs that do not allow to run tests on s390x and pple64
  architectures. Backporting patches from master and enabling tests on s390x
  and pple64.

* Fri Jul 17 2020 Egor Artemov <egor.artemov@gmail.com> - 1.3.0-1
- Bump to 1.3.0 version

* Thu May 7 2020 Egor Artemov <egor.artemov@gmail.com> - 1.2.0-1
- Build of 1.2.0 release
