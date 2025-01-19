Name:     mod_mono
Version:  3.13
Release:  17%{?dist}
Summary:  A module to deploy an ASP.NET application on Apache with Mono

License:  MIT
URL:      http://www.mono-project.com/docs/web/mod_mono/
Source0:  http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Source1:  %{name}-tmpfiles.conf
Patch0:   mod_mono-varrun.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: httpd-devel
BuildRequires: mono-devel
BuildRequires: xsp-devel
BuildRequires: pkgconfig
BuildRequires: apr-devel
# For the _tmpfilesdir macro.
BuildRequires: systemd

Requires: httpd >= 2.2
Requires: mono-core
Requires: xsp

ExclusiveArch: %mono_arches

%description
mod_mono allows Apache to serve ASP.NET pages by proxying the requests
to a slightly modified version of the XSP server, called mod-mono-server,
that is installed along with XSP

%prep
%setup -q
%patch -P0 -p1 -b .varrun

# fixup character set
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && \
touch -r ChangeLog ChangeLog.conv && \
mv -f ChangeLog.conv ChangeLog

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install APXS_SYSCONFDIR="%{_sysconfdir}/httpd/conf.d/"
find %{buildroot} -type f -name "*.la" -delete

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/httpd/modules/mod_mono.so*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_mono.conf
%dir %attr(-,apache,apache) /run/%{name}/
%{_tmpfilesdir}/%{name}.conf
%doc %{_mandir}/man8/mod_mono.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.13-12
- BuildRequires systemd for the _tmpfilesdir macro.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.13-1
- Update to 3.13

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-6
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.12-4
- Use /run/ insted /var/run/
- Correct ownership of /run/mod_mono

* Fri Dec 11 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.12-3
- Fix tmpfile config file and spec
- Remove ldconfig from spec

* Thu Dec 10 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.12-2
- Spec file fixes and clenup

* Fri Oct 30 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.12-1
- Update to 3.12
- Use mono_arches macro

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Paul Whalen <paul.whalen@senecac.on.ca> - 2.10-2
- Added arm macro to ExclusiveArch

* Wed Mar 30 2011 Christian Krause <chkr@fedoraproject.org> - 2.10-1
- Update to 2.10
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Christian Krause <chkr@fedoraproject.org> - 2.8-2
- Rebuild again to create correct requires/provides capabilities

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.8-1
- Bump to 2.8
- Update socket patch

* Sat Aug 14 2010 Christian Krause <chkr@fedoraproject.org> - 2.6.3-3
- Place the default socket for mod_mono_server into /var/run/mod_mono/ 
  so that it can be created by user apache when mod_mono_server is
  started via httpd (by updating mod_mono-2.6-varrun.patch, BZ 607718)

* Wed Jun 23 2010 Christian Krause <chkr@fedoraproject.org> - 2.6.3-2
- Fix encoding of ChangeLog

* Fri Mar 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6.3-1
- Bump to 2.6.3 release version
- Fix URL and SRC URL

* Tue Dec 22 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6-2
- Bump to 2.6 release

* Sat Oct 03 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.6-1
- Bump to 2.6 preview 1

* Tue Jun 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4.2-1
- Bump to 2.4.2 preview
- Reenable ppc
- Add in ppc64 support

* Mon Apr 06 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-4.1
- Remove ppc support

* Thu Mar 26 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-4
- Full 2.4 release

* Wed Mar 18 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-3.RC3
- Bump to RC3

* Tue Mar 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-3.RC2
- Bump to RC2

* Fri Feb 27 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-2.RC1
- Bump to RC1

* Wed Jan 28 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-1.pre1.20090124svn124159
- Update to 2.4
- altered BRs to use mono-2.4
- retagged as pre-1

* Fri Jan 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-4.RC2.20090901svn122806
- Bump to RC2
- Big update from svn

* Wed Dec 17 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-3.pre3.20081217svn117989
- Bump to preview 3
- Move to svn for bug fixes

* Sat Dec 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2.pre2
- Bump to preview 2

* Tue Nov 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1.pre1
- Bump to 2.2 preview 1
- incorporate fix to the var-run patch (thanks to Dario Lesca)

* Sat Oct 11 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-6
- use var run instead of tmp
- added additional Requires

* Fri Oct 10 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-5
- fix URLs

* Fri Oct 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-4
- bump to RC4

* Mon Sep 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-3
- bump to RC3

* Tue Sep 09 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-2
- bump to 2.0 RC 1

* Sun Aug 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-1
- bump to 2.0 preview 1
- licence changed and other spec file alterations

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.6-2.1
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-1.1
- remove arch ppc64

* Thu Nov 22 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.6-1
- bump 
- url fix

* Sun Nov 18 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.5-1
- bump

* Sun Apr 22 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.4-1
- bump

* Sat Nov 25 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2.1-1
- bump

* Fri Nov 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.2-1
- bump

* Sat Oct 14 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.18-1
- bump

* Fri Sep 08 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.17-3
- Spec file fixes
- Modified SOURCE0 and URL tags

* Thu Aug 31 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.17-1
- bump to new version
- Altered BR xsp to BR xsp-devel

* Sun Apr 23 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.14-3
- removed static libdir
- included archs mono is currently on

* Tue Apr 18 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.14-2
- libdir now usr-lib irrespective of the architecture built on
- minor change to spec file

* Mon Apr 17 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.1.14-1
- Initial import for FE
- Spec file based on the Novell version (though quite hacked)

