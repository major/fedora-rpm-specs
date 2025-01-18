Name:           entr
Version:        5.6
Release:        3%{?dist}
Summary:        Run arbitrary commands when files change

# The entire source code is ISC except missing/sys/event.h which is BSD-2-Clause
License:        ISC AND BSD-2-Clause
URL:            http://eradman.com/entrproject/
Source0:        %{url}/code/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A utility for running arbitrary commands when files change. Uses inotify to
avoid polling. It was written to make rapid feedback and automated testing
natural and completely ordinary.

%prep
%autosetup
ln -s Makefile{.linux,}

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build

%install
export PREFIX=%{_prefix}
%make_install


%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Lubomír Sedlář <lsedlar@redhat.com> - 5.6-1
- New upstream release 5.6

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 Lubomír Sedlář <lsedlar@redhat.com> - 5.4-1
- New upstream release 5.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Lubomír Sedlář <lsedlar@redhat.com> - 5.3-1
- New upstream release 5.3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 09 2022 Lubomír Sedlář <lsedlar@redhat.com> - 5.2-1
- New upstream release 5.2
- Updated upstream URL

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Lubomír Sedlář <lsedlar@redhat.com> - 5.1-1
- New upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Lubomír Sedlář <lsedlar@redhat.com> - 5.0-1
- New upstream release 5.0

* Tue May 04 2021 Lubomír Sedlář <lsedlar@redhat.com> - 4.9-1
- New upstream release 4.9

* Mon Mar 01 2021 Lubomír Sedlář <lsedlar@redhat.com> - 4.8-1
- New upstream release 4.8

* Mon Feb 01 2021 Lubomír Sedlář <lsedlar@redhat.com> - 4.7-1
- New upstream release 4.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Lubomír Sedlář <lsedlar@redhat.com> - 4.6-1
- New upstream release 4.6

* Tue Apr 21 2020 Lubomír Sedlář <lsedlar@redhat.com> - 4.5-1
- New upstream release 4.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Lubomír Sedlář <lsedlar@redhat.com> - 4.4-2
- Fix building with GCC 10

* Mon Jan 06 2020 Lubomír Sedlář <lsedlar@redhat.com> - 4.4-1
- Update to 4.4 (#1758145)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Lubomír Sedlář <lsedlar@redhat.com> - 4.2-2
- Work with undefined ldflags

* Thu May 30 2019 Lubomír Sedlář <lsedlar@redhat.com> - 4.2-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Lubomír Sedlář <lsedlar@redhat.com> - 4.1-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Lubomír Sedlář <lsedlar@redhat.com> - 4.0-1
- New upstream release 4.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Lubomír Sedlář <lsedlar@redhat.com> - 3.9-1
- New upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Lubomír Sedlář <lsedlar@redhat.com> - 3.7-2
- Bump to rebuild with correct dist tag

* Wed Mar 01 2017 Lubomír Sedlář <lsedlar@redhat.com> - 3.7-1
- New upstream version with bugfixes

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-7
- Add build dependency on gcc

* Mon Aug 29 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-6
- Fixes to spec file by Igor Gnatenko

* Tue Aug 09 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-5
- Update licensing information in spec

* Wed Aug 03 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-4
- Add optflags

* Tue Jul 19 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-3
- Install license and news files

* Tue Jul 19 2016 Lubomír Sedlář <lsedlar@redhat.com> - 3.6-2
- New upstream release

* Thu Apr 14 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 3.5-1
- New upstream release
- Removed contrib/*
- Detect new subdirectories on Linux
- Direct users to http://entrproject.org/limits.html if inotify hits a kernel limit
