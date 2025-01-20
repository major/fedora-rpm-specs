Name:		rteval
Version:	3.8
Release:	4%{?dist}
Summary:	Utility to evaluate system suitability for RT Linux

Group:		Development/Tools
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:	https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python3-devel
BuildRequires:  python3-setuptools
Requires:	python3-lxml
Requires:	python3-libxml2
Requires:	realtime-tests
Requires:	rteval-loads >= 1.6-5
Requires:	sysstat
Requires:	xz bzip2 tar gzip m4 gawk
Requires:	kernel-headers
Requires:	sos
Requires:	numactl
Requires:	gcc binutils gcc-c++ flex bison bc make
Requires:	elfutils elfutils-libelf-devel
Requires:	openssl
Requires:	openssl-devel
Requires:	stress-ng
Requires:	perl-interpreter, perl-devel, perl-generators
Requires:	libmpc, libmpc-devel
Requires:	dwarves
# not available on all arches
Recommends:     dmidecode
BuildArch:	noarch

%description
The rteval script is a utility for measuring various aspects of
realtime behavior on a system under load. The script unpacks the
kernel source, and then goes into a loop, running hackbench and
compiling a kernel tree. During that loop the cyclictest program
is run to measure event response time. After the run time completes,
a statistical analysis of the event response times is done and printed
to the screen.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*.egg-info
%doc README doc/rteval.txt
%license COPYING
%dir %{_datadir}/%{name}
%{python3_sitelib}/rteval
%{_mandir}/man8/rteval.8.gz
%config(noreplace) %{_sysconfdir}/rteval.conf
%{_datadir}/%{name}/rteval_*.xsl
%{_bindir}/rteval

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.8-2
- Rebuilt for Python 3.13

* Mon May 13 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.8-1
- Update to 3.8

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 John Kacur <jkacur@redhat.com> - 3.7-1
- Update to the latest rteval upstream
- Include a patch to use the latest rteval-loads with a newer kernel to
  compile that works with newer tool chains for example with arm

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.6-3
- Rebuilt for Python 3.12

* Fri Feb 17 2023 John Kacur <jkacur@redhat.com> - 3.6-2
- Update the BuildRequires for correct version of rteval-loads
- Remove python3-ethtool as a Requires
- Update the Requires

* Fri Feb 17 2023 John Kacur <jkacur@redhat.com> - 3.6-1
- Rebuild latest upstream release which removes use of distutils

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 John Kacur <jkacur@redhat.com> - 3.5-1
- Rebuild latest upstream release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 John Kacur <jkacur@redhat.com> - 3.2-1
- Build v3.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1-5
- Rebuilt for Python 3.10

* Thu Jan 28 2021 John Kacur <jkacur@redhat.com> - 3.1-4
- Made some changes to simplify the %%files section considerably
- Added some Requires for building the kernel that were in rteval-loads

* Wed Jan 27 2021 John Kacur <jkacur@redhat.com> - 3.1-3
- Remove the requirement to install python-schedutils
- add %%pycached to python files to properly handle __pycache__
- remove unncessary %%clean section
- Change requires rt-tests to realtime-tests
- Add a requires for stress-ng
- Use the %%license macro on the COPYING file
 
* Wed Jan 13 2021 John Kacur <jkacur@redhat.com> - 3.1-2
- Fix an incorrect import in rteval/sysinfo/__init__.py

* Mon Jan 11 2021 John Kacur <jkacur@redhat.com> - 3.1-1
- Upgrade to rteval-3.1
- Don't create a separate rteval-common package anymore
Resolves: rhbz#1890555

* Thu Aug 27 2020 John Kacur <jkacur@redhat.com> - 3.0-13
- Parse cpuinfo correctly when the model name has a colon in it.
Resolves: rhbz#1873120

* Thu Jul 23 2020 John Kacur <jkacur@redhat.com> - 3.0-12
- Use linux-5.7 in kcompile
Resolves: rhbz#1859762

* Thu Jun 25 2020 John Kacur <jkacur@redhat.com> - 3.0-11
- Make sure "make" is available for the kcompile module
Resolves: rhbz#1850924

* Wed Jun 24 2020 John Kacur <jkacur@redhat.com> - 3.0-10
- Ensure that a recent rteval-loads with stress-ng is required
Resolves: rhbz#1847233

* Wed Jun 24 2020 John Kacur <jkacur@redhat.com> - 3.0-9
- Ensure the stressng command line is displayed in the final report
Resolves: rhbz#1850151

* Mon Jun 15 2020 John Kacur <jkacur@redhat.com> - 3.0-8
- Add the stress-ng load module
Resolves: rhbz#1816360

* Mon May 04 2020 John Kacur <jkacur@redhat.com> - 3.0-7
- Make sure openssl is available so that rteval can compile the kernel
Resolves: rhbz#1831272

* Tue Dec 10 2019 John Kacur <jkacur@redhat.com> - 3.0-6
- Iterate over nodes and not sysTop
- Explictly add a few more software requires for compiling the kernel
Resolves: rhbz#1755603

* Tue Dec 03 2019 John Kacur <jkacur@redhat.com> - 3.0-5
- Explicitly add some software requires for compiling the kernel
Resolves: rhbz#1766879

* Mon Dec 02 2019 John Kacur <jkacur@redhat.com> - 3.0-4
- In hackbench.py node in args to Popen must be a string
Resolves: rhbz#1777048

* Tue Nov 19 2019 John Kacur <jkacur@redhat.com> - 3.0-3
- Don't assume cpu0 cannot be offlined, test for it
- Drop patches that are no longer in the spec file
Resolves: rhbz#1773792

* Mon Nov 18 2019 John Kacur <jkacur@redhat.com> - 3.0-2
- Check whether a cpu is online before adding to a list
- Change hackbench to use the systopology interface for online cpus
Resolves: rhbz#1715081

* Fri Nov 15 2019 John Kacur <jkacur@redhat.com> - 3.0-1
- Sync rt-tests and rteval-loads versions in the specfile
- Upgrade to upstream rteval-3.0
Resolves: rhbz#1748955

* Fri Nov 08 2019 John Kacur <jkacur@redhat.com> - 2.14-27
- Update kcompile sources to linux-5.1
Resolves: rhbz#1770215

* Fri Nov 08 2019 John Kacur <jkacur@redhat.com> - 2.14-26
- Fix number of hackbench jobs wrt number of CPUs
- Don't run on nodes with no CPUs available
Resolves: rhbz#1770211

* Tue Apr 02 2019 Clark Williams <williams@redhat.com> - 2.14.25
- fix incorrect test logic in gating tests
Resolves: rhbz#1682426

* Tue Apr 02 2019 Clark Williams <williams@redhat.com> - 2.14.24
- add rteval-loads dependency to gating
- added second test (short_run) to gating
Resolves: rhbz#1682426

* Mon Apr 01 2019 Clark Williams <williams@redhat.com> - 2.14.23
-  add missing gating.yaml
Resolves: rhbz#1682426

* Mon Apr 01 2019 Clark Williams <williams@redhat.com> - 2.14.22
- checkin OSCI gating framework
Resolves: rhbz#1682426

* Mon Dec 17 2018 John Kacur <jkacur@redhat.com> - 2.14-21
- Fix typo in debug output
Resolves: rhbz#1659974

* Tue Oct 16 2018 John Kacur <jkacur@redhat.com> - 2.14-20
- Disable options for the remote xmlrpc server, not currently supported
Resolves: rhbz#1628322

* Sat Oct 13 2018 John Kacur <jkacur@redhat.com> - 2.14-19
- Fix Requires for python3
Resolves: rhbz#1638135

* Fri Oct 12 2018 John Kacur <jkacur@redhat.com> - 2.14-18
- Fix time format in report
Resolves: rhbz#1630733

* Fri Sep 28 2018 John Kacur <jkacur@redhat.com> - 2.14-17
- Change python3 to platform-python
Resolves: rhbz#1633619

* Fri Aug 10 2018 John Kacur <jkacur@redhat.com> - 2.14-16
- remove unnecssary encode that is causing problems
Resolves: rhbz#1614384

* Tue Aug 07 2018 John Kacur <jkacur@redhat.com> - 2.14-15
- tar is required in kcompile.py. Make it a Require in the specfile
Resolves: rhbz#1612992

* Fri Aug 03 2018 John Kacur <jkacur@redhat.com> - 2.14-14
- fix python3 division of integers
Resolves: rhbz#1611813

* Fri Aug 03 2018 John Kacur <jkacur@redhat.com> - 2.14-13
-fix rtevalclient import
Resolves: rhbz#1608464

* Sat Jun 23 2018 John Kacur <jkacur@redhat.com> - 2.14-12
- More python3 changes
- Changes for the new version of rt-tests that automates --numa
Resolves: rhbz#1594287

* Tue Jun 12 2018 John Kacur jkacur@redhat.com> - 2.14-11
- More specfile changes for python3 build
Resolves: rhbz#1518699

* Wed May 30 2018 John Kacur <jkacur@redhat.com> - 2.14-10
- Chnages for a python3 build
Resolves: rhbz#1518699

* Fri Oct 27 2017 John Kacur <jkacur@redhat.com> - 2.14-9
- Remove redundant files for clarity.
Resolves: rhbz1504162

* Fri Oct 27 2017 John Kacur <jkacur@redhat.com> - 2.14-8
- Don't fail if we don't know the init system
Resolves: rhbz1504168

* Fri Oct 20 2017 John Kacur <jkacur@redhat.com> - 2.14-7
- Remove underscore from sysread function in systopology.py
Resolves: rhbz1504164

* Fri Oct 20 2017 John Kacur <jkacur@redhat.com> - 2.14-6
- Improve error handling if cyclictest fails to run
Resolves: rhbz1504159

* Fri Oct 20 2017 John Kacur <jkacur@redhat.com> - 2.14-5
- Remove trace-cmd from Requires, since it is not needed to run rteval
Resolves: rhbz1504173

* Mon Oct 16 2017 John Kacur <jkacur@redhat.com> - 2.14-4
- Don't sleep if hackbench fails to launch due to out-of-memory
- Instead, exit gracefully
Resolves: rhbz1380144

* Wed Oct 11 2017 John Kacur <jkacur@redhat.com> - 2.14-3
- Add sos as a requires since this package is needed to run sosreport
Resolves: rhbz1500722

* Wed Oct 11 2017 John Kacur <jkacur@redhat.com> - 2.14-2
- Add the contents of the kernel boot command line to the summary report
Resolves: rhbz1452788

* Thu Mar 16 2017 Clark Williams <williams@redhat.com> - 2.14-1
- removed leftover import of systopology from sysinfo

* Wed Mar 15 2017 Clark Williams <williams@redhat.com> - 2.13-2
- Updated specfile to correct version and bz [1382155]

* Tue Sep 20 2016 Clark Williams <williams@rehdat.com> - 2.12-1
- handle empty environment variables SUDO_USER and USER [1312057]

* Tue Aug 30 2016 Clark Williams <williams@rehdat.com> - 2.11-1
- make sure we return non-zero for early exit from tests

* Wed Aug  3 2016 Clark Williams <williams@rehdat.com> - 2.10-1
- bumped version for RHEL 7.3 release

* Mon May  9 2016 Clark Williams <williams@redhat.com> - 2.9.1
- default cpulist for modules if only one specified [1333831]

* Tue Apr 26 2016 Clark Williams <williams@redhat.com> - 2.8.1
- add the --version option to print the rteval version
- made the --cyclictest-breaktrace option work properly [1209986]

* Fri Apr  1 2016 Clark Williams <williams@redhat.com> - 2.7.1
- treat SIGINT and SIGTERM as valid end-of-run events [1278757]
- added cpulist options to man page

* Thu Feb 11 2016 Clark Williams <williams@redhat.com> - 2.6.1
- update to make --loads-cpulist and --measurement-cpulist work [1306437]

* Thu Dec 10 2015 Clark Williams <williams@refhat.com> - 2.5-1
- stop using old numactl --cpubind argument

* Wed Dec  9 2015 Clark Williams <williams@refhat.com> - 2.4.2
- added Require of package numactl

* Tue Nov 17 2015 Clark Williams <williams@refhat.com> - 2.4.1
- rework hackbench load to not generate cross-node traffic [1282826]

* Wed Aug 12 2015 Clark Williams <williams@redhat.com> - 2.3-1
- comment out HWLatDetect module from default config [1245699]

* Wed Jun 10 2015 Clark Williams <williams@redhat.com> - 2.2-1
- add --loads-cpulist and --measurement-cpulist to allow cpu placement [1230401]

* Thu Apr 23 2015 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 2.1-8
- load default configs when no config file is specified (Jiri kastner) [1212452]

* Wed Jan 14 2015 Clark Williams <williams@redhat.com> - 2.1-7
- added requires of bzip2 to specfile [1151567]

* Thu Jan  8 2015 Clark Williams <williams@redhat.com> - 2.1-6
- cleaned up product documentation [1173315]

* Mon Nov 10 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 2.1-5
- rebuild for RHEL-7.1 (1151567)

* Thu Mar 27 2014 Clark Williams <williams@redhat.com> - 2.1-4
- cherry-picked old commit to deal with installdir problem

* Wed Mar 26 2014 Clark Williams <williams@redhat.com> - 2.1-3
- added sysstat requires to specfile

* Tue Mar 12 2013 David Sommerseth <davids@redhat.com> - 2.1-2
- Migrated from libxslt-python to python-lxml

* Fri Jan 18 2013 David Sommerseth <davids@redhat.com> - 2.1-1
- Made some log lines clearer
- cyclictest: Added --cyclictest-breaktrace feature
- cyclictest: Removed --cyclictest-distance option
- cyclictest: Use a tempfile buffer for cyclictest's stdout data
- cyclictest: Report if breaktrace was triggered
- cyclictest: Make the unit test work again
- cyclictest: Only log and show statistic data when samples are collected
- Copyright updates

* Thu Jan 17 2013 David Sommerseth <davids@redhat.com> - 2.0.1-1
- Fix up type casting in the core module code
- hwlatdetect: Add some more useful debug info
- Reworked the run logic for modules - allow them to flag they won't run
- Fixed a few log messages in load modules
- Add a 30 seconds sleep before unleashing the measurement threads

* Thu Jan 10 2013 David Sommerseth <davids@redhat.com> - 2.0-3
- Separate out RTEVAL_VERSION into rteval.version, to avoid
  massive BuildRequirements

* Fri Dec 21 2012 David Sommerseth <davids@redhat.com> - 2.0-2
- Split out common files into rteval-common

* Fri Dec 21 2012 David Sommerseth <davids@redhat.com> - 2.0-1
- Updated to rteval v2.0 and reworked spec file to use setup.py directly

* Tue Oct 23 2012 Clark Williams <williams@redhat.com> - 1.36-1
- deal with system not having dmidecode python module
- make sure to cast priority parameter to int
- from Raphaël Beamonte <raphael.beamonte@gmail.com>:
  - Rewrite of the get_kthreads method to make it cross-distribution
  - Adds getcmdpath method to use which to locate the used commands
  - Rewrite of the get_services method to make it cross-distribution

* Mon Apr  2 2012 Clark Williams <williams@redhat.com> - 1.35-1
- fix thinko where SIGINT and SIGTERM handlers were commented out

* Thu Jan 12 2012 Clark Williams <williams@redhat.com> - 1.34-1
- fix missing config merge in rteval.py to pass parameters
  down to cyclictest
- modify hackbench to use helper function to start process

* Sat May 14 2011 Clark Williams <williams@redhat.com> - 1.33-1
- modify hackbench cutoff to be 0.75GB/core

* Mon Aug 23 2010 Clark Williams <williams@redhat.com> - 1.32-1
- update docs
- refactor some RTEval methods to utility functions
- modify hackbench.py not to run under low memory conditions
- clean up XML generation to deal with new hackbench code
- clean up XSL code to deal with new XML 'run' attribute
- from David Sommerseth <davids@redhat.com>:
  - improve CPU socket counting logic
  - delay log directory creation until actually needed
- from Gowrishankar <gowrishankar.m@in.ibm.com>:
  - check if the core id really exists (multithreading fix)

* Mon Jul 26 2010 Clark Williams <williams@redhat.com> - 1.31-1
- from David Sommerseth <davids@redhat.com>:
  - Updated hackbench implementation to avoid overusing resources
  - Don't show NUMA node information if it's missing in the summary.xml
  - Show CPU cores properly

* Wed Jul 21 2010 Clark Williams <williams@redhat.com> - 1.30-1
- added code to hackbench to try to detect and ease memory pressure

* Fri Jul 16 2010 Clark Williams <williams@redhat.com> - 1.29-1
- fixed incorrect type value in kcompile.py

* Fri Jul 16 2010 Clark Williams <williams@redhat.com> - 1.28-1
- added logic to loads to adjust number of jobs based on ratio
  of memory per core

* Wed Jul 14 2010 Clark Williams <williams@redhat.com> - 1.27-1
- modified hackbench to go back to using threads rather than
  processes for units of work
- added memory size, number of numa nodes and run duration to the
  parameter dictionary passed to all loads and cyclictest

* Tue Jul 13 2010 Clark Williams <williams@redhat.com> - 1.26-1
- modified hackbench parameters to reduce memory consumption

* Mon Jul 12 2010 Clark Williams <williams@redhat.com> - 1.25-1
- fixed cyclictest bug that caused everything to be uniprocessor
- updated source copyrights to 2010

* Fri Jul  9 2010 Clark Williams <williams@redhat.com> - 1.24-1
- modified hackbench arguments and added new parameters for
  hackbench in rteval.conf

* Thu Jul  8 2010 Clark Williams <williams@redhat.com> - 1.23-1
- version bump to deal with out-of-sync cvs issue

* Thu Jul  8 2010 Clark Williams <williams@redhat.com> - 1.22-1
- merged David Sommerseth <davids@redhat.com> changes to use
  hackbench from rt-tests packages rather than carry local copy
- converted all loads and cyclictest to pass __init__ parameters
  in a dictionary rather than as discrete parameters
- added logging for load output

 * Tue Apr 13 2010 Clark Williams <williams@redhat.com> - 1.21-1
- from Luis Claudio Goncalves <lgoncalv@redhat.com>:
  - remove unecessary wait() call in cyclictest.py
  - close /dev/null after using it
  - call subprocess.wait() when needed
  - remove delayloop code in hackbench.py
- from David Sommerseth <davids@redhat.com>:
  - add SIGINT handler
  - handle non-root user case
  - process DMI warnings before command line arguments
  - added --annotate feature to rteval
  - updates to xmlrpc code

  * Tue Apr  6 2010 Clark Williams <williams@redhat.com> - 1.20-1
- code fixes from Luis Claudio Goncalves <lgoncalv@redhat.com>
- from David Sommerseth <davids@redhat.com>:
  - xmlrpc server updates
  - cputopology.py for recording topology in xml
  - added NUMA node recording for run data
  - rpmlint fixes
- added start of rteval whitepaper in docs dir

* Tue Mar 16 2010 Clark Williams <williams@redhat.com> - 1.19-1
- add ability for --summarize to read tarfiles
- from David Sommerseth <davids@redhat.com>
  - gather info about loaded kernel modules for XML file
  - added child tracking to hackbench to prevent zombies

* Tue Feb 16 2010 Clark Williams <williams@redhat.com> - 1.18-1
- fix usage of python 2.6 features on RHEL5 (python 2.4)

* Tue Feb 16 2010 Clark Williams <williams@redhat.com> - 1.17-1
- added logic to filter non-printables from service status output
  so that we have legal XML output
- added logic to hackbench.py to cleanup properly at the end
  of the test

* Thu Feb 11 2010 Clark Williams <williams@redhat.com> - 1.16-1
- fix errors in show_remaining_time() introduced because
  time values are floats rather than ints

* Thu Feb 11 2010 Clark Williams <williams@redhat.com> - 1.15-1
- added logic to use --numa and --smp options of new cyclictest
- added countdown report for time remaining in a run

* Tue Feb  9 2010 Clark Williams <williams@redhat.com> - 1.14-1
- David Sommerseth <davids@redhat.com>:
  merged  XMLReport() changes for hwcert suite

* Tue Dec 22 2009 Clark Williams <williams@redhat.com> - 1.13-1
- added cyclictest default initializers
- added sanity checks to statistics reduction code
- updated release checklist to include origin push
- updated Makefile clean and help targets
- davids updates (mainly for v7 integration):
  - Add explicit sys.path directory to the python sitelib+
    '/rteval'
  - Send program arguments via RtEval() constructor
  - Added more DMI data into the summary.xml report
  - Fixed issue with not including all devices in the
    OnBoardDeviceInfo tag

* Thu Dec  3 2009 David Sommerseth <davids@redhat.com> - 1.12-2
- fixed Makefile and specfile to include and install the
  rteval/rteval_histogram_raw.py source file for gaining
  raw access to histogram data
- Removed xmlrpc package during merge against master_ipv4 branch

* Wed Nov 25 2009 Clark Williams <williams@redhat.com> - 1.12-1
- fix incorrect reporting of measurement thread priorities

* Mon Nov 16 2009 Clark Williams <williams@redhat.com> - 1.11-5
- ensure that no double-slashes ("//") appear in the symlink
  path for /usr/bin/rteval (problem with rpmdiff)

* Tue Nov 10 2009 Clark Williams <williams@redhat.com> - 1.11-4
- changed symlink back to install and tracked by %%files

* Mon Nov  9 2009 Clark Williams <williams@redhat.com> - 1.11-3
- changed symlink generation from %%post to %%posttrans

* Mon Nov  9 2009 Clark Williams <williams@redhat.com> - 1.11-2
- fixed incorrect dependency for libxslt

* Fri Nov  6 2009 Clark Williams <williams@redhat.com> - 1.11-1
- added base OS info to XML file and XSL report
- created new package rteval-loads for the load source code

* Wed Nov  4 2009 Clark Williams <williams@redhat.com> - 1.10-1
- added config file section for cyclictest and two settable
  parameters, buckets and interval

* Thu Oct 29 2009 Clark Williams <williams@redhat.com> - 1.9-1
- merged davids updates:
	-H option (raw histogram data)
	cleaned up xsl files
	fixed cpu sorting

* Mon Oct 26 2009 David Sommerseth <davids@redhat.com> - 1.8-3
- Fixed rpmlint complaints

* Mon Oct 26 2009 David Sommerseth <davids@redhat.com> - 1.8-2
- Added xmlrpc package, containing the XML-RPC mod_python modules

* Tue Oct 20 2009 Clark Williams <williams@redhat.com> - 1.8-1
- split kcompile and hackbench into sub-packages
- reworked Makefile (and specfile) install/uninstall logic
- fixed sysreport incorrect plugin option
- catch failure when running on root-squashed NFS

* Tue Oct 13 2009 Clark Williams <williams@redhat.com> - 1.7-1
- added kthread status to xml file
- merged davids changes for option processing and additions
  to xml summary

* Tue Oct 13 2009 Clark Williams <williams@redhat.com> - 1.6-1
- changed stat calculation to loop less
- added methods to grab service and kthread status

* Mon Oct 12 2009 Clark Williams <williams@redhat.com> - 1.5-1
- changed cyclictest to use less memory when doing statisics
  calculations
- updated debug output to use module name prefixes
- changed option processing to only process config file once

* Fri Oct  9 2009 Clark Williams <williams@redhat.com> - 1.4-1
- changed cyclictest to use histogram rather than sample array
- calcuated statistics directly from histogram
- changed sample interval to 100us
- added -a (affinity) argument to force cpu affinity for
  measurement threads

* Thu Sep 24 2009 David Sommerseth <davids@redhat.com> - 1.3-3
- Cleaned up the spec file and made rpmlint happy

* Wed Sep 23 2009 David Sommerseth <davids@redhat.com> - 1.3-2
- Removed version number from /usr/share/rteval path

* Tue Sep 22 2009 Clark Williams <williams@redhat.com> - 1.3-1
- changes from davids:
  * changed report code to sort by processor id
  * added report submission retry logic
  * added emailer class

* Fri Sep 18 2009 Clark Williams <williams@redhat.com> - 1.2-1
- added config file handling for modifying load behavior and
  setting defaults
- added units in report per IBM request

* Wed Aug 26 2009 Clark Williams <williams@redhat.com> - 1.1-2
- missed a version change in rteval/rteval.py

* Wed Aug 26 2009 Clark Williams <williams@redhat.com> - 1.1-1
- modified cyclictest.py to start cyclictest threads with a
  'distance' of zero, meaning they all have the same measurement
  interval

* Tue Aug 25 2009 Clark Williams <williams@redhat.com> - 1.0-1
- merged davids XMLRPC fixes
- fixed --workdir option
- verion bump to 1.0

* Thu Aug 13 2009 Clark Williams <williams@redhat.com> - 0.9-2
- fixed problem with incorrect version in rteval.py

* Tue Aug  4 2009 Clark Williams <williams@redhat.com> - 0.9-1
- merged dsommers XMLRPC and database changes
- Specify minimum python-dmidecode version, which got native XML support
- Added rteval_dmi.xsl
- Fixed permission issues in /usr/share/rteval-x.xx

* Wed Jul 22 2009 Clark Williams <williams@redhat.com> - 0.8-1
- added code to capture clocksource info
- added code to copy dmesg info to report directory
- added code to display clocksource info in report
- added --summarize option to display summary of existing report
- added helpfile target to Makefile

* Thu Mar 26 2009 Clark Williams <williams@torg> - 0.7-1
- added require for python-schedutils to specfile
- added default for cyclictest output file
- added help parameter to option parser data
- renamed xml output file to summary.xml
- added routine to create tarfile of result files

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-6
- added code to handle binary data coming from DMI tables

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-5
- fixed logic for locating XSL template (williams)
- fixed another stupid typo in specfile (williams)

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-4
- fixed specfile to install rteval_text.xsl in /usr/share directory

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-3
- added Requires for libxslt-python (williams)
- fixed race condition in xmlout constructor/destructor (williams)

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-2
- added Requires for libxslt (williams)
- fixed stupid typo in rteval/rteval.py (williams)

* Wed Mar 18 2009 Clark Williams <williams@torg> - 0.6-1
- added xml output logic (williams, dsommers)
- added xlst template for report generator (dsommers)
- added dmi/smbios output to report (williams)
- added __del__ method to hackbench to cleanup after run (williams)
- modified to always keep run data (williams)

* Fri Feb 20 2009 Clark Williams <williams@torg> - 0.5-1
- fixed tab/space mix problem
- added report path line to report

* Fri Feb 20 2009 Clark Williams <williams@torg> - 0.4-1
- reworked report output
- handle keyboard interrupt better
- removed duration mismatch between rteval and cyclictest

* Mon Feb  2 2009 Clark Williams <williams@torg> - 0.3-1
- initial checkin
