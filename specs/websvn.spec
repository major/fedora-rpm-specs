Name:           websvn
Version:        2.8.4
Release:        4%{?dist}
Summary:        Online subversion repository browser

License:        GPL-2.0-or-later
URL:            https://websvnphp.github.io
Source0:        https://github.com/websvnphp/websvn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        websvn-httpd.conf

BuildArch:      noarch

Requires(pre):  httpd
Requires:       sed
Requires:       enscript
Requires:       php >= 5.4.0
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-geshi
Requires:       php-pear(Archive_Tar)
# Text_Diff is broken with PHP 8.
# Use system diff instead where needed.
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
Requires:       diffutils
%else
Requires:       php-pear(Text_Diff)
%endif


%description
WebSVN offers a view onto your subversion repositories that's been designed to
reflect the Subversion methodology. You can view the log of any file or
directory and see a list of all the files changed, added or deleted in any
given revision. You can also view the differences between two versions of a
file so as to see exactly what was changed in a particular revision.


%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils


%description selinux
SElinux context for %{name}.


%prep
%setup -q
find -name .gitignore -delete

mv include/distconfig.php include/config.php
sed -i -e "s#^\/\/ \$config->useMultiViews();#\$config->useMultiViews();#" \
    include/config.php


%build
# Nothing to build


%install
# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a *.php include javascript languages templates \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}

# Move the conf to the proper place
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
ln -s ../../../..%{_sysconfdir}/%{name}/config.php \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php

# Apache conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
                $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Move the cache dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/cache/%{name}
ln -s ../../..%{_localstatedir}/cache/%{name} \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/cache

# Move the temp dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/tmp
ln -s ../../..%{_localstatedir}/tmp $RPM_BUILD_ROOT/%{_datadir}/%{name}/temp

# Add a compat symlink from removed wsvn.php to new browse.php
# This needs FollowSymlinks option in the httpd conf
ln -s %{_datadir}/%{name}/browse.php %{buildroot}/%{_datadir}/%{name}/wsvn.php


%post selinux
semanage fcontext -a -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_localstatedir}/cache/%{name} || :


%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
fi


%files
%doc README.md changes.txt
%license license.txt
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%{_datadir}/%{name}
%attr(-,apache,root) %{_localstatedir}/cache/%{name}


%files selinux


%changelog
* Mon Feb 03 2025 Christian Krause <chkr@fedoraproject.org> - 2.8.4-4
- Fix FailsToInstall in F42 due to orphaned package (php-erusev-parsedown)
  by removing that dependency (RHBZ#2342582)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Christian Krause <chkr@fedoraproject.org> - 2.8.4-1
- Update to 2.8.4 (RHBZ#2255355)
- Delete .gitignore files from source directory

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Xavier Bachelot <xavier@bachelot.org> - 2.8.2-1
- Update to 2.8.2 (RHBZ#2215709)

* Wed Jun 07 2023 Xavier Bachelot <xavier@bachelot.org> - 2.8.1-1
- Update to 2.8.1 (RHBZ#2134251)
- Convert License: to SPDX

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-1
- Update to 2.7.0 (RHBZ#2064103)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Xavier Bachelot <xavier@bachelot.org> - 2.6.1-3
- Use system diff rather than Text_Diff with PHP 8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Xavier Bachelot <xavier@bachelot.org> - 2.6.1-1
- Update to 2.6.1 (RHBZ#1960100)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Xavier Bachelot <xavier@bachelot.org> - 2.6.0-1
- Update to 2.6.0 (RHBZ#1893501)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Xavier Bachelot <xavier@bachelot.org> 2.5-1
- Update to 2.5

* Fri Jul 10 2020 Xavier Bachelot <xavier@bachelot.org> 2.3.3-23
- Better website URL fix

* Thu Jul 09 2020 Xavier Bachelot <xavier@bachelot.org> 2.3.3-22
- Fix website URL

* Thu May  7 2020 Tom Hughes <tom@compton.nu> - 2.3.3-21
- Add patch to fix exceptions accessing GeSHi error property

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Xavier Bachelot <xavier@bachelot.org> 2.3.3-13
- Add patch for CVE-2016-1236 (RHBZ#1333673).

* Tue Mar 01 2016 Xavier Bachelot <xavier@bachelot.org> 2.3.3-12
- Add patch for CVE-2016-2511 (RHBZ#1310758).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Xavier Bachelot <xavier@bachelot.org> 2.3.3-9
- Add missing javascript directory (RHBZ#1218590).

* Wed Jan 21 2015 Xavier Bachelot <xavier@bachelot.org> 2.3.3-8
- Add patch for CVE-2013-6892 (RHBZ#1183632).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.3.3-4
- Fix apache 2.4 configuration (bz #871495)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Xavier Bachelot <xavier@bachelot.org> 2.3.3-1
- Update to 2.3.3.

* Tue Mar 01 2011 Xavier Bachelot <xavier@bachelot.org> 2.3.2-1
- Update to 2.3.2.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Xavier Bachelot <xavier@bachelot.org> 2.3.1-2
- Add an selinux subpackage for compatibility with selinux (RHBZ#585969).

* Tue Jun 15 2010 Xavier Bachelot <xavier@bachelot.org> 2.3.1-1
- Update to 2.3.1.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.1-1
- Update to 2.2.1.
- Preserve time stamp when fixing encoding.

* Sat May 09 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.0-2
- php-pear(Text_Diff) is mandatory now.
- Add Requires(pre): httpd.

* Thu Apr 23 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.0-1
- Update to 2.2.0.
- Actually use the system provided classes.
- Add Requires: php-pear(Archive_Tar).
- Remove implicit Requires: php-common.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-3
- Turn multiview on by default.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-2
- More Requires:.
- Move temp and cache dir to a better place.
- Set a proper locwebsvnhttp in wsvn.php.

* Wed Mar 18 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-1
- Initial build.
