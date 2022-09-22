Summary:    Sticky notes is a free and open source paste-bin application
Name:       sticky-notes
Version:    0.4
Release:    20%{?dist}
License:    BSD
URL:        https://github.com/sayakb/sticky-notes

# Use the following commands to generate the tarball
# wget https://github.com/sayakb/sticky-notes/releases/tag/VERSION
Source0:    sticky-notes-%{version}.tar.gz
Source1:    sticky-notes.conf
Patch0:     sticky-notes-unbundle-php-libs.patch
Patch1:     sticky-notes-use-free-url-shortener.patch
Patch2:     sticky-notes-0.4-dont-use-eval-for-login.patch
Patch3:     sticky-notes-0.4-fix-error-when-retrieving-last-insered-id.patch
BuildArch:  noarch
Requires:   httpd
Requires:   php, php-geshi, php-pdo, php-swiftmailer

%description
Sticky notes is a free and open source paste-bin application.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/%{name}
install -m 0644 -D -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/sticky-notes.conf

# Remove exec perms on files
find . -type f -exec chmod -x {} \;

# Remove bundled php-geshi
rm -rf addons/geshi
rm -rf addons/swiftmailer

# Remove non-required dirs
rm -f lighttpd.conf
rm -rf cache testing
cp -pr * ${RPM_BUILD_ROOT}%{_datadir}/%{name}
mkdir ${RPM_BUILD_ROOT}%{_sysconfdir}/sticky-notes
cp config.sample.php ${RPM_BUILD_ROOT}%{_sysconfdir}/sticky-notes/config.php
ln -s ../../../etc/sticky-notes/config.php ${RPM_BUILD_ROOT}%{_datadir}/%{name}/config.php
mv install.php ${RPM_BUILD_ROOT}%{_sysconfdir}/sticky-notes/
ln -sf ../../../etc/sticky-notes/install.php ${RPM_BUILD_ROOT}%{_datadir}/%{name}/install.php

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/sticky-notes.conf
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%config(noreplace) %{_sysconfdir}/%{name}/install.php
%dir %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%doc LICENSE
%doc README*
%doc VERSION

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 01 2016 Athmane Madjoudj <athmane@fedoraproject.org> 0.4-8
- Fix php-swiftmailer dep

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Athmane Madjoudj <athmane@fedoraproject.org> 0.4-4
- Depend on pdo instead of mysql
- Add a patch to fix a login issue
- Add a patch to fix a error when retrieving last insered id
- Misc specfile cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Athmane Madjoudj <athmane@fedoraproject.org> 0.4-2
- Patch to use free URL shortener ur1.ca instead of Google's goo.gl.

* Sat Jul 13 2013 Athmane Madjoudj <athmane@fedoraproject.org> 0.4-1
- Update to 0.4
- Drop upstreamed patches
- Unbundle new libs
- Simplify the specfile.

* Sun Apr 14 2013 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.13112012.2-1
- Drop upstreamed patches
- Update spec (url change / download method)
- Add support for url shortening

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.09062012.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-10
- Fix some XSS issues. 

* Tue Oct 30 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-9
- Make sticky-notes.conf compatible with both httpd 2.4.x and 2.2.x.

* Fri Oct 12 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-8
- Fix hostname issue in rss URLs when reverse proxy is used.

* Fri Jul 20 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-7
- Remove exec perms on files

* Fri Jul 20 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-6
- Remove defattr to avoid bug #481363.
- Remove clean section

* Tue Jun 19 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-5
- Add a patch to fix XSS issue in username parameter at login page.

* Thu Jun 14 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.09062012.4-4
- Fix version number

* Wed Jun 13 2012 Athmane Madjoudj <athmane@fedoraproject.org> 20120507git-3
- Move install to config since it requires modification

* Thu Jun 07 2012 Athmane Madjoudj <athmane@fedoraproject.org> 20120507git-2
- Remove mysql-server dep
- Update to latest upstream version which includes security patch from #810928
- Unbundle php-geshi
- Add a config file to make sticky-notes installable
- Add php-mysql as requirement

* Sat Apr 07 2012 david <david.r@ultracar.co.uk> - 20120407git-1
- First packaged

