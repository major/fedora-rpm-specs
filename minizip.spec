Name:           minizip
Version:        3.0.2
Release:        7%{?dist}
Summary:        Minizip contrib in zlib with the latest bug fixes and advanced features

License:        zlib
URL:            https://github.com/nmoinvaz/%{name}
Source0:        https://github.com/nmoinvaz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# pkgconfig file must have full paths specified.
Patch0:         minizip-ng-3.0.2-fix_pkgconfig.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbsd-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libzstd-devel
BuildRequires: xz-devel
BuildRequires: openssl-devel


%description
Minizip zlib contribution that includes:
* AES encryption
* I/O buffering
* PKWARE disk splitting
It also has the latest bug fixes that having been found all over the internet.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   zlib-devel

%description devel
Development files for %{name} library.


%prep
%autosetup -p 1 -n %{name}-ng-%{version}


%build
%cmake \
  -DMZ_BUILD_TEST:BOOL=ON \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DINSTALL_INC_DIR=%{_includedir}/%{name} \
  -DZSTD_FORCE_FETCH=OFF

%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.3.0
%{_libdir}/lib%{name}.so.3.0.2


%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}/mz*.h
%{_includedir}/%{name}/unzip.h
%{_includedir}/%{name}/zip.h


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.0.2-5
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 3.0.2-4
- Add patch to fix pkgconfig file

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- drop ldconfig scriptlets (https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets)
- drop explicit BR: make (already pulled in via cmake)
- %%build: one cmake option per line
- %%check: drop 'make test', does nothing
- -devel: drop explicit cmake dep (autodeps should add cmake-filesystem already)

* Wed Jun 09 2021 Patrik Novotný <panovotn@redhat.com> - 3.0.2-1
- Rebase to upstream release 3.0.2

* Wed Apr 14 2021 Patrik Novotný <panovotn@redhat.com> - 3.0.1-1
- Rebase to upstream release 3.0.1

* Tue Feb 09 2021 Patrik Novotný <panovotn@redhat.com> - 3.0.0-1
- Rebase to upstream release 3.0.0
- Use OpenSSL instead of BRG libraries

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Patrik Novotný <panovotn@redhat.com> - 2.10.6-1
- Rebase to upstream release 2.10.6

* Mon Oct 26 2020 Patrik Novotný <panovotn@redhat.com> - 2.10.2-1
- Rebase to upstream release 2.10.2

* Tue Oct 13 2020 Patrik Novotný <panovotn@redhat.com> - 2.10.1
- Rebase to upstream release 2.10.1

* Tue Aug 11 2020 Honza Horak <hhorak@redhat.com> - 2.10.0-4
- Fix FTBFS caused by cmake changes
  Resolves: #1864153

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Patrik Novotný <panovotn@redhat.com> - 2.10.0-1
- Rebase to upstream release 2.10.0

* Tue May 26 2020 Patrik Novotný <panovotn@redhat.com> - 2.9.3-1
- Rebase to upstream release 2.9.3

* Tue May 05 2020 Patrik Novotný <panovotn@redhat.com> - 2.9.2-1
- Rebase to upstream release 2.9.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Patrik Novotný <panovotn@redhat.com> - 2.9.1-1
- New upstream release: 2.9.1

* Tue Sep 24 2019 Patrik Novotný <panovotn@redhat.com> - 2.9.0-1
- New upstream release: 2.9.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Patrik Novotný <panovotn@redhat.com> - 2.8.9-1
- New upstream release: 2.8.9

* Mon Jun 17 2019 Patrik Novotný <panovotn@redhat.com> - 2.8.8-2
- Move header files to minizip subdirectory (fix implicit conflict)

* Wed Jun 12 2019 Patrik Novotný <panovotn@redhat.com> - 2.8.8-1
- New upstream release: 2.8.8

* Tue Apr 09 2019 Patrik Novotný <panovotn@redhat.com> - 2.8.6-1
- Rebase to upstream version 2.8.6

* Thu Mar 21 2019 Patrik Novotný <panovotn@redhat.com> 2.8.5-1
- Rebase to upstream version 2.8.5

* Wed Feb 13 2019 Patrik Novotný <panovotn@redhat.com> 2.8.3-4
- Fix shared library prefix

* Tue Feb 12 2019 Patrik Novotný <panovotn@redhat.com> 2.8.3-3
- Fix ldconfig execution during build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Patrik Novotný <panovotn@redhat.com> 2.8.3-1
- Update to upstream version 2.8.3

* Thu Dec 06 2018 Patrik Novotný <panovotn@redhat.com> 2.8.1-1
- Update to upstream version 2.8.1

* Wed Nov 28 2018 Patrik Novotný <panovotn@redhat.com> 2.8.0-2
- Use absolute paths for install directories

* Wed Nov 28 2018 Patrik Novotný <panovotn@redhat.com> 2.8.0-1
- Update to upstream version 2.8.0

* Sun Oct  7 2018 Orion Poplawski <orion@nwra.com> 2.5.4-1
- Update to 2.5.4

* Thu Aug 30 2018 Patrik Novotný <panovotn@redhat.com> 2.5.0-2
- Provide bundled AES and SHA1 libraries

* Thu Aug 16 2018 Patrik Novotný <panovotn@redhat.com> 2.5.0-1
- Version update. Build againts system bzip2.

* Thu Aug  9 2018 Patrik Novotný <panovotn@redhat.com> 2.3.9-1
- Initial build
