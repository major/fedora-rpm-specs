Name:          abrt-java-connector
Version:       1.3.2
Release:       2%{?dist}
Summary:       JNI Agent library converting Java exceptions to ABRT problems

Group:         System Environment/Libraries
License:       GPLv2+
URL:           https://github.com/abrt/abrt-java-connector
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
%if 0%{?fedora} >= 37
ExcludeArch:   %{ix86}
%endif

BuildRequires: pkgconfig(abrt) >= 2.14.1
BuildRequires: check-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
# Tests have been redone to work under Java 11, but they are not backwards-compatible.
BuildRequires: java-11-devel
BuildRequires: make
BuildRequires: pkgconfig(libreport) >= 2.14.0
BuildRequires: rpm-devel
BuildRequires: satyr-devel
BuildRequires: systemd-devel

Requires:      abrt

%description
JNI library providing an agent capable to process both caught and uncaught
exceptions and transform them to ABRT problems.

%package container
Summary: JNI Agent library converting Java exceptions to ABRT problems (minimal version)
Requires: container-exception-logger
conflicts: %{name}

%description container
JNI library providing an agent capable to process both caught and uncaught
exceptions and transform them to ABRT problems

This package contains only minimal set of files needed for container exception
logging.

%prep
%autosetup -n %{name}-%{version}


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%check
cd "%{__cmake_builddir}"
# Force serial execution of tests to prevent process interleaving which seems to
# upset abrt-java-connector.
%{__ctest} --output-on-failure -j1
cd -


%files
%doc README AUTHORS
%license LICENSE
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_java.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup_java.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/java_event.conf
%config(noreplace) %{_sysconfdir}/abrt/plugins/java.conf
%{_bindir}/abrt-action-analyze-java
%{_mandir}/man1/abrt-action-analyze-java.1*
%{_mandir}/man5/java_event.conf.5*
%{_mandir}/man5/bugzilla_format_java.conf.5*
%{_mandir}/man5/bugzilla_formatdup_java.conf.5*
%{_datadir}/abrt/conf.d/plugins/java.conf

# Applications may use a single subdirectory under/usr/lib.
# http://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE22
#
# Java does not support multilib.
# https://fedorahosted.org/fesco/ticket/961
%{_prefix}/lib/abrt-java-connector

%files container
%doc README AUTHORS
%license LICENSE
# Applications may use a single subdirectory under/usr/lib.
# http://www.pathname.com/fhs/pub/fhs-2.3.html#PURPOSE22
#
# Java does not support multilib.
# https://fedorahosted.org/fesco/ticket/961
%{_prefix}/lib/abrt-java-connector


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Packit <hello@packit.dev> - 1.3.2-1
- New version 1.3.2 (Michal Srb)
- Skip i686 build on Fedora 37+ (Michal Srb)
- Fix FTBFS in Fedora Rawhide (Michal Srb)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.3.1-2
- Rebuild for testing

* Wed Jan 19 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.3.1-1
- New upstream release

* Tue Jan 18 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.3.0-2
- Fix failing tests

* Mon Jan 17 2022 Matěj Grabovský <mgrabovs@redhat.com> 1.3.0-1
- Bump libreport dependency to 2.14.0
- Add make to build-time dependencies

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-5
- Bump for upgrade path from F-33

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 rebase-helper <rebase-helper@localhost.local> - 1.2.0-1
- new upstream release: 1.2.0

* Tue Aug 25 2020 - Ernestas Kulik <ekulik@redhat.com> - 1.1.5-9
- Rebuild against new libreport

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 - Ernestas Kulik <ekulik@redhat.com> - 1.1.5-6
- Fix non-srcdir CMake build

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.5-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 17 2020 Ernestas Kulik <ekulik@redhat.com> - 1.1.5-4
- Add more patches for Java 11 compatibility

* Wed Jun 10 2020 Ernestas Kulik <ekulik@redhat.com> - 1.1.5-3
- Add patch for Java 11 compatibility

* Wed May 13 2020 Michal Fabik <mfabik@redhat.com> - 1.1.5-1
- new upstream release: 1.1.5

* Wed May 13 2020 Ernestas Kulik <ekulik@redhat.com> - 1.1.5-1
- new upstream release: 1.1.5

* Tue May 12 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 1.1.5-1
- new upstream release: 1.1.5

* Fri Feb 07 2020 Ernestas Kulik <ekulik@redhat.com> - 1.1.4-1
- Fix build failure with GCC 10

* Fri Feb 07 2020 Ernestas Kulik <ekulik@redhat.com> - 1.1.3-1
- Fix stack traces not being logged in journald

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.2-4
- Rebuild for satyr 0.30

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Martin Kutlak <mkutlak@redhat.com> - 1.1.2-1
- Fix gcc string truncation warning for strncpy
- Replace legacy backticked with $() notation

* Mon Jun 10 22:13:17 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-5
- Rebuild for RPM 4.15

* Mon Jun 10 15:41:59 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-4
- Rebuild for RPM 4.15

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Matej Habrnal <mhabrnal@redhat.com> - 1.1.1-1
- Add possibility report reports problems to CEL
- Upate test results
- Change log() to log_warning()
- Correct includes for ABRT
- Make the dependency on systemd optional

* Wed Oct 29 2014 Jakub Filak <jfilak@redhat.com> - 1.1.0-1
- Support java-1.8-openjdk
- Install the library to /usr/lib/abrt-java-connector on all arches

* Fri Apr 4 2014 Jakub Filak <jfilak@redhat.com> - 1.0.10-1
- Temporarily ignore failures of reporter-ureport until ABRT start using FAF2
- Prevent users from reporting low quality stack traces

* Tue Mar 18 2014 Jakub Filak <jfilak@redhat.com> - 1.0.9-1
- Make the agent configurable via a configuration file
- Include custom debug info in bug reports
- Make the detection of 'executable' working with JAR files

* Wed Jan 22 2014 Jakub Filak <jfilak@redhat.com> - 1.0.8-1
- Do not report exceptions caught in a native method
- Mark stack traces with 3rd party classes as not-reportable
- Calculate 'duphash' & 'uuid' in satyr
- Use the main class URL for 'executable'
- Do not ship own reporting workflow definitions
- Code optimizations

* Fri Jan 10 2014 Jakub Filak <jfilak@redhat.com> - 1.0.7-1
- Use the last frame class path for executable
- Gracefully handle JVMTI errors
- Add an abstract to README
- Add support for journald and syslog
- Make log output disabled by default
- Add support for changing log directory
- Fix a race condition causing a crash of JVM

* Tue Oct 01 2013 Jakub Filak <jfilak@redhat.com> - 1.0.6-1
- Fix a deadlock in GC start callback
- Disable experimental features in production releases

* Tue Jul 30 2013 Jakub Filak <jfilak@redhat.com> - 1.0.5-1
- Provide a proper configuration for libreport

* Thu Jul 18 2013 Jakub Filak <jfilak@redhat.com> - 1.0.4-1
- Stop creating an empty log file

* Tue Jul 16 2013 Jakub Filak <jfilak@redhat.com> - 1.0.3-1
- Fix tests on arm

* Tue Jul 09 2013 Jakub Filak <jfilak@redhat.com> - 1.0.2-1
- Do not crash on empty command line options

* Mon Jul 08 2013 Jakub Filak <jfilak@redhat.com> - 1.0.1-1
- Fix tests on ppc and s390 on both 32 and 64 bit

* Thu Jun 27 2013 Jakub Filak <jfilak@redhat.com> - 1.0.0-1
- Publicly releasable version

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.2-1
- Start versioning library
- Drop build dependency on abrt-devel

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.1-2
- Provide ABRT configuration

* Mon Jun 03 2013 Jakub Filak <jfilak@redhat.com> - 0.1.1-1
- New release

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-3
- Build with the library name same as the package name

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-2
- Build with ABRT enabled

* Fri May 31 2013 Jakub Filak <jfilak@redhat.com> - 0.1.0-1
- Initial version
