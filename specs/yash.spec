# Upstream SCM
# Upstream is currently using SVN
# SVN path: http://svn.sourceforge.jp/svnroot/yash/yash/trunk

%global		mainver		2.58.1
%global		docver		%{mainver}

%global		yashdocdir		%{_datadir}/doc/%{name}-doc

%global		baserelease	1
%undefine		minorver
%undefine       _changelog_trimtime

Name:		yash
Version:	%{mainver}
Release:	%{?minorver:0.}%{baserelease}%{?minorver:.%{minorver}}%{?dist}
Summary:	Yet Another SHell

# License header in .c files are GPL-2.0-or-later
# However, doc/intro.txt says this is under GPL-2.0-only
# SPDX confirmed
License:	GPL-2.0-only
URL:		https://github.com/magicant/yash/
Source0:	https://github.com/magicant/yash/archive/%{version}/%{name}-%{version}%{?minorver}.tar.gz

# Patches

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	ncurses-devel
BuildRequires:	ed
BuildRequires:	/usr/bin/a2x
BuildRequires:	/usr/bin/asciidoc
BuildRequires:	/usr/bin/xgettext
BuildRequires:	/usr/bin/ps
Provides:		/bin/yash
# Write needed Requires for scriptlets explicitly
Requires(post):	grep
Requires(post):	coreutils
Requires(postun):	sed


%description
Yash is a command line shell that conforms to the POSIX.1 (IEEE Std
1003.1, 2008 Edition) standard for the most part.

Yash also has its own features beyond POSIX, such as:
  * global aliases
  * random numbers
  * socket redirections and other special redirections
  * right prompt
  * command completion


%package	doc
Summary:	Documentation for %{name}
Version:	%{docver}
License:	CC-BY-SA-2.1-JP
BuildArch:	noarch
Requires:	%{name} = %{mainver}-%{release}
#Requires:	%{name} >= %{version}

%description	doc
This package contains document files for %{name}.

%prep
%setup -q

%build
# This package use configure not based on autotools...
# won't accept --libdir=
./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--datarootdir=%{_datarootdir} \
	--docdir=%{yashdocdir}/ \

%make_build -k

%install
make install install-html \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	CPPROG="cp -p"

%find_lang %{name}

%check
teststatus=0
make test || teststatus=1

cat tests/summary.log
sleep 3
exit $teststatus


%post
if [ -f %{_sysconfdir}/shells ]
then
	grep -q '^/bin/yash$' %{_sysconfdir}/shells || echo '/bin/yash' >> %{_sysconfdir}/shells
else
	echo '/bin/yash' > %{_sysconfdir}/shells
fi
exit 0

%postun
[ "$1" = 0 ] || exit 0
[ -f %{_sysconfdir}/shells ] || exit 0
sed -i -e '\@/bin/yash$@d' %{_sysconfdir}/shells
exit 0

%files -f %name.lang
%license	COPYING
%doc	NEWS
%doc	README.md
%lang(ja)	%doc	NEWS.ja
%lang(ja)	%doc	README.ja.md

%{_bindir}/%{name}

%dir	%{_datadir}/%{name}
%{_datadir}/%{name}/completion/
%{_datadir}/%{name}/config
%{_datadir}/%{name}/initialization/

%{_mandir}/man1/yash.1*
%lang(ja)	%{_mandir}/ja/man1/yash.1*

%files	doc
%dir	%{yashdocdir}/
%{yashdocdir}/*.html
%{yashdocdir}/*.css
%lang(ja)	%{yashdocdir}/ja/

%changelog
* Tue Feb 04 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.58.1-1
- 2.58.1

* Mon Feb 03 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.58-2
- 2.58

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.57-1
- 2.57

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.56.1-1
- 2.56.1

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.55-1
- 2.55

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.54-1
- 2.54

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.53-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.53-1
- 2.53

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.52-1
- 2.52

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.51-1
- 2.51

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.50-1
- 2.50

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.49-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.49-1
- 2.49

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.48-1
- 2.48

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.47-1
- 2.47

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.46-1
- 2.46

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.45-1
- 2.45

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.44-1
- 2.44

* Mon Sep 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.43-1
- 2.43

* Mon Mar 21 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.41-1
- 2.41

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.40-2
- Remove bash %%_bindir/hash etc workaround (ref: bug 1297166)

* Sun Jan 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.40-1
- 2.40

* Sat Aug 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.39-1
- 2.39

* Mon Jun 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.38-1
- 2.38

* Wed Jun 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.37-2
- Fix broken deps

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.37-1
- 2.37

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.36-2
- Fix broken dependency

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.35-2
- Fix broken deps

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.35-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.35-1
- 2.35

* Mon Feb 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.34-1
- 2.34

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>
- bump release and fix broken deps

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.33.1-1
- 2.33.1

* Sun Oct 28 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.33-1
- 2.33

* Thu Sep 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.32.2-3
- Fix Patch0

* Thu Sep 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.32.2-2
- Make help built-in command work also on ja_JP locale

* Wed Sep 26 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.32.1-1
- 2.32.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.31-1
- 2.31

* Mon Feb  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.30-1
- 2.30

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.29-2
- F-17: rebuild against gcc47

* Sun Oct 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.29-1
- 2.29

* Sun Aug 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.28-1
- 2.28

* Wed May 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.27-1
- 2.27

* Fri Feb 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.26.1-1
- 2.26.1

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.25-3
- Patch from the upstream to check the status of /dev/tty for job.y test

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.25-2
- Ignore test failure on job.y for now

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.25-1
- 2.25

* Tue Oct  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.24-1
- 2.24

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.23-1
- 2.23

* Sun Jul 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.22-1
- 2.22

* Tue Jul 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.22-0.4.b0
- Fix scriplet error

* Mon Jul  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.22-0.3.b0
- Fix license tag for -doc subpackage

* Sun Jul  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.22-0.2.b0
- Handle %%_sysconfdir/shells
- Move binary to /bin

* Sun Jul  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.22-0.1.b0
- Update to the released 2.22 b0

* Sat Jul  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.21-3.svn2087_trunk
- Try latest trunk for
  * test failure on koji
  * test hang on mockbuild

* Sat Jun 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.21-2
- Initial creation

