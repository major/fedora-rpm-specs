%global summary A set of tools for managing snapshots

Name:		snapm
Version:	0.5.2
Release:	%autorelease
Summary:	%{summary}

License:	Apache-2.0
URL:		https://github.com/snapshotmanager/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		0001-schedule-fix-TIMELINE-policy-retention-indexing-when.patch
Patch2:		0002-container_tests-add-GcPolicyParamsTimeline-progressi.patch

BuildArch:	noarch

BuildRequires:	boom-boot
BuildRequires:	lvm2
BuildRequires:	make
BuildRequires:	stratis-cli
BuildRequires:	stratisd
BuildRequires:	systemd-rpm-macros
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
%if 0%{?fedora}
BuildRequires: libfaketime
%endif

Requires: python3-snapm = %{version}-%{release}
Recommends: boom-boot

%package -n python3-snapm
Summary: %{summary}

%package -n python3-snapm-doc
Summary: %{summary}

%description
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

%description -n python3-snapm
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module.

%description -n python3-snapm-doc
Snapshot manager (snapm) is a tool for managing sets of snapshots on Linux
systems.  The snapm tool allows snapshots of multiple volumes to be captured at
the same time, representing the system state at the time the set was created.

This package provides the python3 snapm module documentation in HTML format.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%{make_build} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -rf doc/html/_sources doc/_build
rm -f doc/*.rst doc/Makefile doc/conf.py

%install
%pyproject_install

mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/schedule.d
%{__install} -p -m 644 etc/%{name}/snapm.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}
%{__install} -p -m 644 etc/%{name}/plugins.d/lvm2-cow.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
%{__install} -p -m 644 etc/%{name}/plugins.d/lvm2-thin.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d
%{__install} -p -m 644 etc/%{name}/plugins.d/stratis.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}/plugins.d

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man8/snapm.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
%{__install} -p -m 644 man/man5/snapm.conf.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man5/snapm-plugins.d.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
%{__install} -p -m 644 man/man5/snapm-schedule.d.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5

mkdir -p ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-create@.service ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-create@.timer ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-gc@.service ${RPM_BUILD_ROOT}/%{_unitdir}
%{__install} -p -m 644 systemd/snapm-gc@.timer ${RPM_BUILD_ROOT}/%{_unitdir}

mkdir -p ${RPM_BUILD_ROOT}/%{_tmpfilesdir}
%{__install} -p -m 644 systemd/tmpfiles.d/%{name}.conf ${RPM_BUILD_ROOT}/%{_tmpfilesdir}/

%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}
%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}/mounts
%{__install} -d -m 0700 ${RPM_BUILD_ROOT}/%{_rundir}/%{name}/lock

%check
%pytest --log-level=debug -v tests/

%files
# Main license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%{_bindir}/snapm
%doc %{_mandir}/man*/snapm*
%attr(644, -, -) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/snapm.conf
%attr(644, -, -) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins.d/*
%dir %attr(755, -, -) %{_sysconfdir}/%{name}/schedule.d
%attr(644, -, -) %{_unitdir}/snapm-create@.service
%attr(644, -, -) %{_unitdir}/snapm-create@.timer
%attr(644, -, -) %{_unitdir}/snapm-gc@.service
%attr(644, -, -) %{_unitdir}/snapm-gc@.timer
%attr(644, -, -) %{_tmpfilesdir}/%{name}.conf
%dir %{_rundir}/%{name}/
%dir %{_rundir}/%{name}/mounts
%dir %{_rundir}/%{name}/lock

%files -n python3-snapm
# license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info/

%files -n python3-snapm-doc
# license for snapm (Apache-2.0)
%license LICENSE
%doc README.md
%doc doc

%changelog
%autochangelog
