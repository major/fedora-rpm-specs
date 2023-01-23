# Conditional for release and snapshot builds. Uncomment for release-builds.
#global rel_build 1

# Place rpm-macros into proper location.
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Settings used for build from snapshots.
%{!?rel_build:%global commit		4b85bd7faa0b2bbcbbc4458655e6f35f438f1e91}
%{!?rel_build:%global commit_date	20171030}
%{!?rel_build:%global shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global gitrel		.git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global gittar		%{name}-%{version}-%{gitver}.tar.gz}

# This is needed, because we are building just the data-pkg from it's tarball.
# The main-prg is shipped in a different tarball.  This pkg is need for as a
# BuildRequires for the main-prg, mostly.
%global mainprg shogun

Name:			%{mainprg}-data
Version:		0.12
Release:		0.16%{?gitrel}%{?dist}
Summary:		Data-files for the SHOGUN machine learning toolbox
%{?el5:Group:		Documentation}

License:		GPLv3
URL:			http://%{mainprg}-toolbox.org
# Sources for release-builds.
%{?rel_build:Source0:	ftp://%{mainprg}-toolbox.org/%{mainprg}/data/%{name}-%{version}.tar.bz2}
# Sources for snapshot-builds.
%{!?rel_build:Source0:	https://github.com/%{mainprg}-toolbox/%{name}/archive/%{commit}.tar.gz#/%{gittar}}

BuildArch:		noarch
%{?el5:BuildRoot:	%(/bin/mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}

%description
This package contains data-files needed for running the test-suite
and examples of the SHOGUN machine learning toolbox.


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

# Move some documentation to toplevel.
%{__mv} easysvm/README README.easysvm
%{__mv} faces/README LICENSE

# Make sure all files are mode 0644.
%{_bindir}/find . -type f -print0 | %{_bindir}/xargs -0 %{__chmod} -c 0644


%build
# noop


%install
%if 0%{?rhel} && 0%{?rhel} <= 5
%{__rm} -rf %{buildroot}
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5

%{__mkdir} -p %{buildroot}/%{_datadir}/%{mainprg}/data	\
		%{buildroot}/%{macrosdir}
%{__cp} -a */ %{buildroot}/%{_datadir}/%{mainprg}/data

# Create a macro for use in other spec-files.
%{__cat} << EOF > %{buildroot}/%{macrosdir}/macros.%{name}
%_%{mainprg}_data_dir %{_datadir}/%{mainprg}/data
%_%{mainprg}_data_version %{version}-%{release}
EOF

%files
%if 0%{?rhel} && 0%{?rhel} <= 5
%doc LICENSE
%else  # 0%%{?rhel} && 0%%{?rhel} <= 5
%license LICENSE
%endif # 0%%{?rhel} && 0%%{?rhel} <= 5
%doc README.*
%{_datadir}/%{mainprg}
%{macrosdir}/macros.%{name}


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.16.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.15.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.14.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.13.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.12.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.11.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.10.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.9.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.8.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.7.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.6.git20171030.4b85bd7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Björn Esser <besser82@fedoraproject.org> - 0.12-0.5.git20171030.4b85bd7
- Update to new snapshot

* Tue Aug 01 2017 Björn Esser <besser82@fedoraproject.org> - 0.12-0.4.git20170705.ed8779c
- Update to new snapshot

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.3.git20170322.c877521
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Björn Esser <besser82@fedoraproject.org> - 0.12-0.2.git20170322.c877521
- Update to new snapshot

* Sat Mar 11 2017 Björn Esser <besser82@fedoraproject.org> - 0.12-0.1.git20170227.7854e3b
- Update to new snapshot

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Björn Esser <fedora@besser82.io> - 0.11-1
- new upstream release
- change source-url for releases to ftp-scheme

* Sun Aug 14 2016 Björn Esser <fedora@besser82.io> - 0.10.1-0.3.git20160811.87bcaa2
- updated to new snapshot git20160811.87bcaa259720873f3d4bbb1540ff945dd84cd35c

* Tue Aug 02 2016 Björn Esser <fedora@besser82.io> - 0.10.1-0.2.git20160727.6b54e1f
- updated to new snapshot git20160727.6b54e1fcaf24b2925e47be381d84c4cfe72be990

* Sat Apr 02 2016 Björn Esser <fedora@besser82.io> - 0.10.1-0.1.git20160330.c964e86
- updated to new snapshot git20160330.c964e86dbcc984d4d87ae94378ccf81eaa2cbb37

* Wed Feb 10 2016 Björn Esser <fedora@besser82.io> - 0.10-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.6.git20150619.7e6bd50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9.1-0.5.git20150619.7e6bd50
- updated to new snapshot git20150619.7e6bd506fc21662b0b59a0710acda01d2f7729b7

* Thu Jun 18 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9.1-0.4.git20150618.890191a
- updated to new snapshot git20150618.890191a2251d76668009b0cc77019f91405b6311

* Thu Jun 18 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9.1-0.3.git20150617.69d64ec
- updated to new snapshot git20150617.69d64ec44ebf305835a8f3b5acef480c234c9573

* Tue Apr 28 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9.1-0.2.git20150428.ae6cea5
- updated to new snapshot git20150428.ae6cea52bf47f18930ca89f5f6df9c909cfcb01f

* Fri Apr 24 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9.1-0.1.git20150421.b405c1d
- updated to new snapshot git20150421.b405c1ded32b34e3855853bfb7da6f2ded2bf50a
- use rpm-defined macros for tool invocation

* Tue Jan 27 2015 Björn Esser <bjoern.esser@gmail.com> - 0.9-1
- new upstream release

* Wed Dec 24 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.24.git20141224.6b305d3
- updated to new snapshot git20141224.6b305d33b9af2111dacaefa6e84fe70f6cea932f

* Wed Dec 24 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.23.git20141217.ab44087
- make sure all files are mode 0644

* Mon Dec 22 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.22.git20141217.ab44087
- updated to new snapshot git20141217.ab44087e1a3c5ec05c1c64ebd691fdc5f56b2e81

* Wed Dec 10 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.21.git20141208.9a2f2be
- updated to new snapshot git20141208.9a2f2bee48755c632a959244d7522654efc2e58c

* Mon Dec 08 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.20.git20141204.6b9f893
- updated to new snapshot git20141204.6b9f893fa5044eab38e19803838a42132269185d

* Mon Sep 01 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.19.git20140818.24b8341
- updated to new snapshot git20140818.24b8341a99fc2d3e2ad40f372578ea91bdbedaf6

* Mon Aug 04 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.18.git20140804.48a1abb
- updated to new snapshot git20140804.48a1abbbe8643754c4f20b9c8369015c13eac135

* Mon Aug 04 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.17.git20140728.a5eba81
- updated to new snapshot git20140728.a5eba8154251dff39f627dc35dcb1ddb1341e35d

* Sun Jul 20 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.16.git20140718.3f54017
- updated to new snapshot git20140718.3f54017300fa80b4df9ea9908523a6f9d3c1c44d

* Thu Jul 17 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.15.git20140717.390b350
- updated to new snapshot git20140717.390b350bab6337e2be894b1d71dc9682e1bab0b5

* Mon Jul 07 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.14.git20140706.527e601
- updated to new snapshot git20140706.527e6018d99652cacfd07cc05e0ad93ef08943dc

* Mon Jun 23 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.13.git20140623.a10320f
- updated to new snapshot git20140623.a10320f2494706f071d9c3cfe4967092dd59bfef

* Tue Jun 17 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.12.git20140617.d3a75a6
- updated to new snapshot git20140617.d3a75a6ff44b83e173384acc21f5e3cc8e629c52

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-0.11.git20140519.19230ef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.10.git20140519.19230ef
- updated to new snapshot git20140519.19230ef56933c7c34d5e31bb28d977d081616707

* Sat May 17 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.9.git20140428.328f363
- updated to new snapshot git20140428.328f363ad358813b2e600d2f56b20d349b239db0

* Thu Apr 24 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.8.git20140420.8652c9c
- updated to new snapshot git20140420.8652c9c8f81742a80ee9b999ea182fd9624dd4f2

* Mon Apr 14 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.7.git20140414.9a8b634
- updated to new snapshot git20140414.9a8b634ebdbc013ae020191bf1f5fe9846168087

* Mon Apr 14 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.6.git20140408.1e5eb17
- updated to new snapshot git20140408.1e5eb17040965b5ffe7f6c13ab3d7eae41fd7a25
- removed %%config from macro-files

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.5.git20140317.082eeb5
- updated to new snapshot git20140317.082eeb56ea20fc55085950e6114ef4e7849d438d

* Thu Mar 13 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.4.git20140303.6615cf0
- place rpm-macros into proper location

* Fri Mar 07 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.3.git20140303.6615cf0
- the %%{?dist}-tag must preserved in exported macros

* Wed Mar 05 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.2.git20140303.6615cf0
- added a macro for use in other spec-files

* Tue Mar 04 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8.1-0.1.git20140303.6615cf0
- updated to new snapshot git20140303.6615cf007634595d459853bf4dc6f1a227d2450c

* Sun Feb 23 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-1
- new upstream release: v0.8

* Mon Jan 06 2014 Björn Esser <bjoern.esser@gmail.com> - 0.7-1
- Initial rpm release (#1048730)
