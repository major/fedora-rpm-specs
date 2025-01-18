Name:           dumb-init
Version:        1.2.5
Release:        13%{?dist}
Summary:        Entry-point for containers that proxies signals

License:        MIT
URL:            https://github.com/Yelp/dumb-init
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# pytest 7.2.0+ no longer installs the "py" library,
# which is used by dumb-init's test suite.
# Backported from upstream commit: https://github.com/Yelp/dumb-init/commit/b1a2551ad3c909384d97bca914f7c42cfdcdbf05
Patch0:         0000-update-for-pytest-7.2.0.patch

BuildRequires: gcc
BuildRequires: help2man
BuildRequires: make

BuildRequires: python3
BuildRequires: python3-pytest


%description
dumb-init is a simple process supervisor and init system designed to run as
PID 1 inside minimal container environments (such as Podman and Docker).

* It can handle orphaned zombie processes.
* It can pass signals properly for simple containers.

%prep
%autosetup -p1

%build
gcc -std=gnu99 %{optflags} -o %{name} dumb-init.c
help2man --no-discard-stderr --include debian/help2man --no-info --name '%{summary}' ./%{name} > %{name}.1

%check
PATH=.:$PATH timeout --signal=KILL 60 pytest-3 -vv tests/

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.5-7
- Remove build-time dependency on python3-mock (https://fedoraproject.org/wiki/Changes/DeprecatePythonMock)
- Remove EPEL7-specific parts of the spec

* Sat Nov 12 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.5-6
- Add a patch to make test suite work properly with pytest 7.2.0+

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.5-1
- Update to v1.2.5

* Tue Dec 08 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.4-1
- Update to v1.2.4
- Drop Patch0 (longer sleep in tests - backport from upstream)
- Drop Patch1 (missing NUL-terminator - issue fixed upstream)

* Mon Nov 30 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.2-9
- Add a patch to fix random test failures due to non-NUL-terminated strings

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Muayyad Alsadi <alsadi@gmail.com> - 1.2.2-5
- fix rpmlint about a comment

* Tue Nov 19 2019 Muayyad Alsadi <alsadi@gmail.com> - 1.2.2-4
- enable tests

* Thu Nov 14 2019 Muayyad Alsadi <alsadi@gmail.com> - 1.2.2-3
- disable tests

* Thu Nov 14 2019 Muayyad Alsadi <alsadi@gmail.com> - 1.2.2-2
- latest 1.2.2, use python3 to run test

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.3-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-10
- revert to python2

* Wed Aug 31 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-9
- support epel

* Fri Aug 26 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-8
- run tests

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-7
- let manpage automatically marked as document

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-6
- remove gzip after help2man
- add missing BuildRequire

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-4
- install 644 for manpage

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-3
- remove vim-common and use install

* Mon Aug 15 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-2
- initial packaging
