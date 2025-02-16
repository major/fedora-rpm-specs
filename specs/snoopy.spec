# compat was already shipped on Fedora < 42 and EL9,  even though
# they never had snoopy <= 2.4.x,
# so we need to keep it for the duration of the lifecycle, but we can drop this
# in Fedora >= 42 and RHEL >= 10
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 10)
%bcond_without compat
%else
%bcond_with compat
%endif

Name:           snoopy
Version:        2.5.2
Release:        1%{?dist}
Summary:        A preload library to send shell commands to syslog
License:        GPL-2.0-or-later
URL:            https://github.com/a2o/snoopy
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        snoopy-disable
Source2:        snoopy-enable

# Upstream patches (0001~0500)

# Proposed upstream patches (0501~1000)

# Fedora-only patches (1001+)
# arch-specific (1101+)
Patch1101:      %{name}-disable-utmp-tests.diff

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
# For tests
BuildRequires:  %{_bindir}/hostname
BuildRequires:  %{_bindir}/socat
BuildRequires:  %{_bindir}/ps

%if %{with compat}
%if 0%{?el8}
Recommends:     %{name}-compat = %{version}-%{release}
%endif
%else
# drop in Fedora 44 (upgrading from 41 no longer supported)
# and EPEL 11
%if (0%{?fedora} && 0%{?fedora} < 44) || (0%{?rhel} && 0%{?rhel} < 11)
Obsoletes:      %{name}-compat < 2.5.1-6%{?dist}
%endif
%endif

%global _description %{expand:
Snoopy is designed to aid a sysadmin by providing a log of commands executed.
Snoopy is completely transparent to the user and applications.
It is linked into programs to provide a wrapper around calls to execve().
Logging is done via syslog.}

%description %{_description}

%if %{with compat}
%package        compat
Summary:        Compatibility scripts for %{name}

BuildArch:      noarch

# this is only needed for the lifetime of Fedora and EPEL releases that
# originally shipped snoopy <= 2.4.x (which has snoopy-disable and
# snoopy-enable instead of snoopyctl)
#
# per policy we can't mark a package as deprecated on a released
# Fedora branch
Provides:       deprecated()
Requires:       %{name} = %{version}-%{release}

%description compat %{_description}

This package contains compatibility scripts for Snoopy.
%endif


%prep
%autosetup -N
%ifarch aarch64 s390x
%autopatch -p1
%else
%autopatch -p1 -M 1100
%endif
%if %{with compat}
# compat scripts
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
%endif


%build
%configure
%make_build


%install
%make_install
%if %{with compat}
for cmd in disable enable; do
  install -p snoopy-${cmd} %{buildroot}%{_sbindir}/
done
%endif

# Get rid of libtool archive file
rm %{buildroot}%{_libdir}/libsnoopy.la


%check
%make_build check


%files
%license COPYING
%doc README.md ChangeLog doc/FAQ.md doc/FILTER_exclude_spawns_of.md
# Note, the plain .so file needs to be here since it's a preload library
%{_libdir}/libsnoopy.so*
%{_sbindir}/snoopyctl
%config(noreplace) %{_sysconfdir}/snoopy.ini

%if %{with compat}
%files compat
%{_sbindir}/snoopy-disable
%{_sbindir}/snoopy-enable
%endif


%changelog
* Thu Feb 13 2025 Packit <hello@packit.dev> - 2.5.2-1
- Update to version 2.5.2
- Resolves: rhbz#2321673

* Thu Feb 13 2025 Michel Lind <salimma@fedoraproject.org> - 2.5.1-6
- Remove compat subpackage on Fedora >= 42 and EPEL >= 10
- Create Packit configuration to automate future updates

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 03 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1
- Convert to SPDX license identifier
- Add compat subpackage for snoopy-disable and snoopy-enable

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Neal Gompa <ngompa@fedoraproject.org> - 2.4.14-1
- Rebase to 2.4.14
- Modernize packaging to current packaging guidelines
- Drop unsupported devel content
- Run test suite

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Mosaab Alzoubi <moceap@hotmail.com> - 2.2.6-1
- Update to 2.2.6
- Clean spec up
- Add -devel package
- Use Github source guidline
- Remove old guideline tags
- Remove la lib
- Remove old %%clean way
- Remove README.Fedora due to its included in tools
- Add %%license macro
- Fix BRs
- Support new automake building
- Use %%make_install
- Right way for ldconfig
- Right way for lib macro
- Fix lines length of %%descriotion
- Use snoopy.ini

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Steve Traylen <steve.traylen@cern.ch> 1.9.0-1A
- New upstream version, also upstream moved to github.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Steve Traylen <steve.traylen@cern.ch> - 1.8.0-3
- Correct previous wrong date in changelog.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 2 2011 Steve Traylen <steve.traylen@cern.ch> - 1.8.0-1
- New upstream 1.8.0
- Use make install 
- Clarify README.Fedora to use $LIB for configuration. rhbz#701241.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Steve Traylen <steve.traylen@cern.ch> - 1.7.10-1
- New upstream 1.7.10

* Mon Jan 10 2011 Steve Traylen <steve.traylen@cern.ch> - 1.7.9-1
- New upstream 1.7.9

* Mon Nov 1 2010 Steve Traylen <steve.traylen@cern.ch> - 1.7.6-1
- New upstream 1.7.6

* Fri Aug 6 2010 Steve Traylen <steve.traylen@cern.ch> - 1.7.1-2
- Move lib from /usr/lib64 to /lib64 since a preload over glibc.

* Fri Aug 6 2010 Steve Traylen <steve.traylen@cern.ch> - 1.7.1-1
- New upstream 1.7.1-1

* Wed Aug 4 2010 Steve Traylen <steve.traylen@cern.ch> - 1.6.1-3
- Don't edit /etc/ld.so.preload, instead provide README.Fedora

* Tue Aug 3 2010 Steve Traylen <steve.traylen@cern.ch> - 1.6.1-2
- Call ldconfig in post and preun

* Tue Aug 3 2010 Steve Traylen <steve.traylen@cern.ch> - 1.6.1-1
- Initial packaging.

