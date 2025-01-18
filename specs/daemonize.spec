Name: daemonize
Version: 1.7.8
Release: 11%{?dist}
Summary: Run a command as a Unix daemon

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.clapper.org/software/daemonize/
# $UPSTREAM no longer supplies hand made .tar.gz-Files for releases 
# so a github tarball it is:
# https://github.com/bmc/daemonize/tarball/release-1.7.8
Source: daemonize-1.7.8.tar.gz

BuildRequires:  gcc
BuildRequires: make
%description
daemonize runs a command as a Unix daemon. As defined in W. Richard Stevens' 
1990 book, Unix Network Programming (Addison-Wesley, 1990), a daemon is "a 
process that executes 'in the background' (i.e., without an associated 
terminal or login shell) either waiting for some event to occur, or waiting 
to perform some specified task on a periodic basis." Upon startup, a typical 
daemon program will:

- Close all open file descriptors (especially standard input, standard output 
  and standard error)
- Change its working directory to the root filesystem, to ensure that it 
  doesn’t tie up another filesystem and prevent it from being unmounted
- Reset its umask value
- Run in the background (i.e., fork)
- Disassociate from its process group (usually a shell), to insulate itself 
  from signals (such as HUP) sent to the process group
- Ignore all terminal I/O signals
- Disassociate from the control terminal (and take steps not to reacquire one)
- Handle any SIGCLD signals

Most programs that are designed to be run as daemons do that work for 
themselves. However, you’ll occasionally run across one that does not. 
When you must run a daemon program that does not properly make itself into a 
true Unix daemon, you can use daemonize to force it to run as a true daemon.

%prep
%setup -q -n bmc-%{name}-18869a7

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

%files
%doc CHANGELOG.md LICENSE.md README.md
%{_sbindir}/daemonize
%{_mandir}/man1/daemonize.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.8-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Sven Lankes <sven@lank.es> - 1.7.8-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 13 2015 Sven Lankes <sven@lank.es> - 1.7.7-1
- update to latest upstream release
- clean up spec-file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Sven Lankes <sven@lank.es> - 1.7.3-1
- update to latest upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Gary T. Giesen <giesen@snickers.org> 1.5.6-1
- New upstream version, incorporates previous Makefile patch

* Sun Jul 05 2009 Gary T. Giesen <giesen@snickers.org> 1.5.4-5
- Changed spec file to preserve timestamp on files for make install

* Sun Jul 05 2009 Gary T. Giesen <giesen@snickers.org> 1.5.4-4
- Fixed missed line in patch for compiler flags

* Sun Jul 05 2009 Gary T. Giesen <giesen@snickers.org> 1.5.4-3
- Further spec file cleanup
- New Makefile patch to make build respect compiler flags and
  install man pages

* Sun Jul 05 2009 Gary T. Giesen <giesen@snickers.org> 1.5.4-2
- Spec file cleanup for consistency with Fedora Packaging Guidelines
- Added install for man pages (it's not installed by 'make install')

* Sat Jul 04 2009 Gary T. Giesen <giesen@snickers.org> 1.5.4-1
- Initial Spec file creation for Fedora
