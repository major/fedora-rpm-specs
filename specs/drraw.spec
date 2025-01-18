Name:           drraw
Version:        2.2
Release:        0.35.b2%{?dist}
Summary:        Web based presentation front-end for RRDtool

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://web.taranis.org/drraw/
Source0:        http://web.taranis.org/drraw/dist/drraw-2.2b2.tar.gz
Source1:        drraw-httpd.conf
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RRDs)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       mod_perl 


%description
drraw is a simple web based presentation front-end for RRDtool that allows you
to interactively build graphs of your own design. A graph definition can be
turned into a template which may be applied to many Round Robin Database files.
drraw specializes in providing an easy mean of displaying data stored with
RRDtool and does not care about how the data is collected, making it a great
complement to other RRDtool front-ends.


%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils


%description selinux
SElinux context for drraw.


%prep
%setup -q -n drraw-2.2b2
# Set work dirs in conf file
sed -i -e "s|^\$saved_dir = .*|\$saved_dir = '/var/lib/drraw';|" \
       -e "s|^\$tmp_dir = .*|\$tmp_dir = '/var/tmp';|" drraw.conf
# Patch drraw.cgi for conf file location
sed -i -e 's|^my $config = .*|my $config = "/etc/drraw.conf";|' drraw.cgi
# Fix file encoding
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.conv && \
touch -r CHANGES CHANGES.conv && \
mv -f CHANGES.conv CHANGES


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 drraw.cgi $RPM_BUILD_ROOT/%{_datadir}/%{name}/drraw.cgi
install -Dp -m 0644 drraw.conf $RPM_BUILD_ROOT/%{_sysconfdir}/drraw.conf
install -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/drraw.conf
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}



%post selinux
semanage fcontext -a -t httpd_sys_script_exec_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_datadir}/%{name} %{_localstatedir}/lib/%{name} || :


%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_sys_script_exec_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_localstatedir}/lib/%{name}(/.*)?' 2>/dev/null || :
fi


%files
%license LICENSE
%doc README.EVENTS INSTALL CHANGES
%config(noreplace) %{_sysconfdir}/drraw.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drraw.conf
%{_datadir}/%{name}
%attr(755,apache,root) %{_localstatedir}/lib/%{name}


%files selinux


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.35.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2-0.34.b2
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.33.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.32.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.31.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.30.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.29.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.28.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.27.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.26.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.25.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.24.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Xavier Bachelot <xavier@bachelot.org> 2.2-0.23.b2
- Specify all perl deps
- Use %%license

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.22.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.21.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.20.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.19.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.18.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.17.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.16.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.15.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.14.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.13.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.12.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2-0.11.b2
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.10.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.9.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.8.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.7.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Xavier Bachelot <xavier@bachelot.org> 2.2-0.6.b2
- Fix -selinux %%post and %%postun.
- Remove comments trigering rpmlint warnings.
- Preserve timestamp on file encoding fix.
- Clean up files installation.
- Sed conf file rather than patch it.

* Fri Apr 03 2009 Xavier Bachelot <xavier@bachelot.org> 2.2-0.5.b2
- Add a Group: tag to the -selinux subpackage.

* Tue Mar 03 2009 Xavier Bachelot <xavier@bachelot.org> 2.2-0.4.b2
- Update to 2.2 beta 2.
- Drop the patch updating the code to svn revision 1564.

* Tue Jan 13 2009 Xavier Bachelot <xavier@bachelot.org> 2.2-0.3.b1
- A %%files section is needed to build a subpackage that doesn't contain any file...

* Mon Jan 12 2009 Xavier Bachelot <xavier@bachelot.org> 2.2-0.2.b1
- Update to latest trunk (rev. 1564) :
  - Added pnp4nagios awareness (courtesy of Jeremy Jacquier-Roux).
  - Dashboards weren't always sorted.
  - Updated logic to prevent Data Source Templates from skipping too many files.
  - It wasn't possible to add a numeric DS (reported by Jeremy Jacquier-roux).
  - Removed compatibility reporting code.
- Add an selinux subpackage for compatibility with selinux.

* Wed Nov 19 2008 Xavier Bachelot <xavier@bachelot.org> 2.2-0.1.b1
- Initial build.
