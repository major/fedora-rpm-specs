# For deep debugging we need to build binaries with extra debug info
%bcond_with     debug



Name:           mariadb-connector-odbc
Version:        3.2.6
Release:        3%{?with_debug:.debug}%{?dist}
Summary:        The MariaDB Native Client library (ODBC driver)
License:        LGPL-2.1-or-later
Source:         https://archive.mariadb.org/connector-odbc-%{version}/%{name}-%{version}-src.tar.gz
Url:            https://mariadb.org/en/
# Online documentation can be found at: https://mariadb.com/kb/en/library/mariadb-connector-odbc/

Patch1: gcc-15.patch
Patch2: upstream_125389a471ba12a244029801786cc459cf930e65.patch

BuildRequires:  cmake unixODBC-devel gcc-c++
BuildRequires:  mariadb-connector-c-devel >= 3.4.5

%description
MariaDB Connector/ODBC is a standardized, LGPL licensed database driver using
the industry standard Open Database Connectivity (ODBC) API. It supports ODBC
Standard 3.5, can be used as a drop-in replacement for MySQL Connector/ODBC,
and it supports both Unicode and ANSI modes.

%package        devel
Summary:        Development files for the %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for %{name} that make developing projects with
this connector easier.


%prep
%setup -q -n %{name}-%{version}-src
%patch -P1 -p1
%patch -P2 -p1

sed -i -e "s|/usr/include/mariadb|$(pkg-config --variable=includedir libmariadb)|" CMakeLists.txt


%build

%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DMARIADB_LINK_DYNAMIC="$(pkg-config --variable=libdir libmariadb)/libmariadb.so" \
\
       -DINSTALL_LAYOUT=%{!?flatpak:RPM}%{?flatpak:DEFAULT} \
       -DINSTALL_LIBDIR="%{_lib}" \
       -DINSTALL_LIB_SUFFIX="%{_lib}" \
       -DINSTALL_DOCDIR="%{_defaultdocdir}/%{name}" \
       -DINSTALL_LICENSEDIR="%{_defaultlicensedir}/%{name}" \

# Override all optimization flags when making a debug build
%if %{with debug}
CFLAGS="$CFLAGS     -O0 -g"; export CFLAGS
CXXFLAGS="$CXXFLAGS -O0 -g"; export CXXFLAGS
FFLAGS="$FFLAGS     -O0 -g"; export FFLAGS
FCFLAGS="$FCFLAGS   -O0 -g"; export FCFLAGS
%endif

#cmake -B %_vpath_builddir -LAH

%cmake_build



%install
%cmake_install



%files
%license COPYING
%doc     README

# This is unixODBC plugin. It resides directly in %%{_libdir} to be consistent with the rest of unixODBC plugins. Since it is plugin, it doesn´t need to be versioned.
%{_libdir}/libmaodbc.so

# Example configuration file for UnixODBC
%{_pkgdocdir}/maodbc.ini

%files    devel
%dir %{_includedir}/mariadb/
%{_includedir}/mariadb/sqlmariadb.h

# Pkgconfig
%{_libdir}/pkgconfig/libmaodbc.pc

%changelog
* Thu Jul 31 2025 Michal Schorm <mschorm@redhat.com> - 3.2.6-3
- Bump release for package rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 3 2025 Pavol Sloboda <psloboda@redhat.com> - 3.2.6-1
- Rebase to 3.2.6

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Michal Schorm <mschorm@redhat.com> - 3.2.4-1
- Rebase to 3.2.4

* Thu Nov 14 2024 Michal Schorm <mschorm@redhat.com> - 3.2.3-1
- Rebase to 3.2.3

* Thu Aug 22 2024 Michal Schorm <mschorm@redhat.com> - 3.2.2-1
- Rebase to 3.2.2 GA

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.rc.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.rc.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-1.rc.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Michal Schorm <mschorm@redhat.com> - 3.2.1-1.rc
- Rebase to 3.2.1 RC

* Sun Jan 07 2024 Michal Schorm <mschorm@redhat.com> - 3.1.20-2
- Fix minimal required version of mariadb-connector-c as per:
  https://mariadb.com/kb/en/mariadb-connector-odbc-3-1-20-release-notes/

* Sun Jan 07 2024 Michal Schorm <mschorm@redhat.com> - 3.1.20-1
- Rebase to 3.1.20

* Wed Jul 26 2023 Michal Schorm <mschorm@redhat.com> - 3.1.19-1
- Rebase to 3.1.19

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Michal Schorm <mschorm@redhat.com> - 3.1.18-1
- Rebase to 3.1.18

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Michal Schorm <mschorm@redhat.com> - 3.1.15-1
- Rebase to 3.1.15

* Fri Feb 18 2022 Michal Schorm <mschorm@redhat.com> - 3.1.14-1
- Rebase to 3.1.14

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Michal Schorm <mschorm@redhat.com> - 3.1.13-1
- Rebase to 3.1.13

* Thu Apr 22 2021 Michal Schorm <mschorm@redhat.com> - 3.1.12-1
- Rebase to 3.1.12

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.11-1
- Rebase to 3.1.11
- Add updates for paths in libraries_include_path.patch

* Thu Aug 06 2020 Michal Schorm <mschorm@redhat.com> - 3.1.9-4
- Force the CMake change regarding the in-source builds also to F31 and F32
- %%cmake macro covers the %%{set_build_flags}, so they are not needed
  That also means, the debug build changes to the build flags must be done AFTER the
  %%cmake macro was used.
- %%cmake macro also covers several other options which redudndant specification I removed in this commit
- Default to %%cmake commands instead of %%make commands

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.9-1
- Rebase to 3.1.9
- Add patch add_docs_license_dir_option

* Thu Apr 09 2020 Michal Schorm <mschorm@redhat.com> - 3.1.7-1
- Rebase to 3.1.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.6-1
- Rebase to 3.1.6

* Fri Nov 15 2019 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.5-1
- Rebase to 3.1.5

* Tue Nov 12 2019 Michal Schorm <mschorm@redhat.com> - 3.1.4-2
- Rebuild on top of new mariadb-connector-c

* Mon Nov 04 2019 Michal Schorm <mschorm@redhat.com> - 3.1.4-1
- Rebase to 3.1.4

* Mon Aug 19 2019 Michal Schorm <mschorm@redhat.com> - 3.1.3-1
- Rebase to 3.1.3

* Wed Jul 31 2019 Michal Schorm <mschorm@redhat.com> - 3.1.2-1
- Rebase to 3.1.2
- Patch2 upstreamed

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Michal Schorm <mschorm@redhat.com> - 3.1.1-4
- Use macro for setting the compiler flags

* Wed Jun 05 2019 Michal Schorm <mschorm@redhat.com> - 3.1.1-3
- Added debug build switch
- Added patch2: configurable doc and license dirs paths

* Wed Jun 05 2019 Michal Schorm <mschorm@redhat.com> - 3.1.1-2
- Patch solution found

* Tue Jun 04 2019 Michal Schorm <mschorm@redhat.com> - 3.1.1-1
- Rebase to 3.1.1

* Tue Jun 04 2019 Michal Schorm <mschorm@redhat.com> - 3.0.9-1
- Rebase to 3.0.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.8-2
- Append curdir to CMake invokation. (#1668512)

* Sun Jan 06 2019 Michal Schorm <mschorm@redhat.com> - 3.0.8-1
- Rebase to 3.0.8

* Tue Nov 20 2018 Michal Schorm <mschorm@redhat.com> - 3.0.7-1
- Rebase to 3.0.7

* Fri Aug 03 2018 Michal Schorm <mschorm@redhat.com> - 3.0.6-1
- Rebase to 3.0.6
- Raise the minimal version of the connector-c required, because of a fixed bug
  which affected connector-odbc builds

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Michal Schorm <mschorm@redhat.com> - 3.0.3-1
- Rebase to 3.0.3 version
- Use more macros

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Michal Schorm <mschorm@redhat.com> - 3.0.2-1
- Rebase to 3.0.2 version
- Update ldconfig scriptlets
- Remove Group tag

* Thu Sep 07 2017 Augusto Caringi <acaringi@fedoraproject.org> - 3.0.1-2
- Update to top of 3.0 branch from GitHub 860e7f8b754f (version supporting dynamic linking)
- Source tarball composed from upstream GitHub, because the latest version solves the issues
  with dynamic linking.

* Mon Sep 04 2017 Augusto Caringi <acaringi@fedoraproject.org> - 3.0.1-1
- Update to version 3.0.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Michal Schorm <mschorm@redhat.com> - 2.0.14-1
- Update to version 2.0.14 and check, if blockers still apply. They do.
- Upstream issue created

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Michal Schorm <mschorm@redhat.com> - 2.0.12-1
- Initial version for 2.0.12
