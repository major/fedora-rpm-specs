Name:           ikiwiki
Version:        3.20200202.4
Release:        5%{?dist}
Summary:        A wiki compiler

# ikiwiki is licensed under GPLv2+, the Python code in plugins/ under
# BSD (2-clause)
# SPDX
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            http://ikiwiki.info/
Source0:        http://ftp.debian.org/debian/pool/main/i/%{name}/%{name}_%{version}.orig.tar.xz
Patch0:         ikiwiki-libexecdir.patch
# Correct t/git.t test
Patch1:         ikiwiki-fakehome.patch
Patch2:         ikiwiki-proxy_py.patch
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  gettext
BuildRequires:  findutils
BuildRequires:  make
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  perl
%else
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
# ikiwiki.in loads IkiWiki, IkiWiki::CGI, IkiWiki::Render, IkiWiki::Setup,
# and IkiWiki::Wrapper.
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(CGI::FormBuilder) >= 3.02.02
BuildRequires:  perl(CGI::Session)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::MimeInfo)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ReadBackwards)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Locale::Po4a::Chooser)
BuildRequires:  perl(Locale::Po4a::Po)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(Memoize)
# Monotone not used at tests
# Net::Amazon::S3 not used at tests
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RPC::XML)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Term::ReadLine)
# Text::MultiMarkdown || Text::Markdown::Discount || Text::Markdown || Markdown
# || /usr/bin/markdown
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
%if ! 0%{?rhel}
BuildRequires:  perl(XML::Feed)
%endif
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS)
# Optional run-time:
# Locale::gettext not used at tests
%if ! 0%{?rhel}
BuildRequires:  perl(Net::OpenID::VerifiedIdentity)
%endif
# UUID::Tiny not used at tests
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  bzr
BuildRequires:  cvs
BuildRequires:  cvsps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(XML::Twig)
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  subversion

Requires:       perl(CGI::FormBuilder) >= 3.02.02
Requires:       perl(CGI::Session)
Requires:       perl(Digest::SHA)
Requires:       perl(HTML::Scrubber)
Requires:       perl(Image::Magick)
Requires:       perl(Mail::Sendmail)
Requires:       perl(Sys::Syslog)
Requires:       perl(Text::Markdown)
%if ! 0%{?rhel}
Requires:       perl(XML::Feed)
%endif
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS)

%if "%{?python3_version}" != ""
Requires:       python(abi) = %{python3_version}
%endif
Requires:       python%{python3_pkgversion}-docutils

# IkiWiki package spreads over more files. Provide the file names as modules
# because they are loaded in that way.
Provides:       perl(IkiWiki::Render)
Provides:       perl(IkiWiki::UserInfo)

%global cgi_bin %{_libexecdir}/w3m/cgi-bin

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IkiWiki\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(IkiWiki\\)$

%description
Ikiwiki is a wiki compiler. It converts wiki pages into HTML pages
suitable for publishing on a website. Ikiwiki stores pages and history
in a revision control system such as Subversion or Git. There are many
other features, including support for blogging, as well as a large
array of plugins.


%prep
%setup -q -n ikiwiki-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# goes into the -w3m subpackage
cat << \EOF > README.fedora
See http://ikiwiki.info/w3mmode/ for more information.
EOF

# Drop Monotone plugin
# Monotone depends on botan v1, which has been EOL for a long time
rm -v IkiWiki/Plugin/monotone.pm


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
# parallel builds currently don't work
make


%check
make test || :


%install
make pure_install DESTDIR=%{buildroot} W3M_CGI_BIN=%{cgi_bin}
%find_lang %{name}

# move external plugins
mkdir -p %{buildroot}%{_libexecdir}/ikiwiki/plugins
mv %{buildroot}%{_prefix}/lib/ikiwiki/plugins/* \
   %{buildroot}%{_libexecdir}/ikiwiki/plugins

# remove shebang
sed -e '1{/^#!/d}' -i \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto.setup \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto-blog.setup \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/proxy.py \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst

# fix shebang
sed -e '1i#!%{__python3}' -i \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst

# fix permissions
find %{buildroot}%{perl_vendorlib}/IkiWiki -type f \
     -exec chmod -x {} \;


%files -f %{name}.lang
%{_bindir}/ikiwiki*
%{_sbindir}/ikiwiki*
%{_mandir}/man1/ikiwiki*
%{_mandir}/man8/ikiwiki*
%{_datadir}/ikiwiki
%dir %{_sysconfdir}/ikiwiki
%config(noreplace) %{_sysconfdir}/ikiwiki/*
# contains a packlist only
%exclude %{perl_vendorarch}
%{perl_vendorlib}/IkiWiki*
%exclude %{perl_vendorlib}/IkiWiki*/Plugin/skeleton.pm.example
%if 0%{?rhel}
# disable the S3 plugin for now, as perl-Net-Amazon-S3 is not
# available on epel6 (rhbz#1125850)
%exclude %{perl_vendorlib}/IkiWiki*/Plugin/amazon_s3.pm
%endif
%{_libexecdir}/ikiwiki
%doc README debian/changelog debian/NEWS html
%doc IkiWiki/Plugin/skeleton.pm.example
%if 0%{?_licensedir:1}
# include license file a second time
%license html/GPL
%endif


%package w3m
Summary:        Ikiwiki w3m cgi meta-wrapper
Requires:       w3m
Requires:       %{name} = %{version}-%{release}

%description w3m
Enable usage of all of ikiwiki's web features (page editing, etc) in
the w3m web browser without a web server. w3m supports local CGI
scripts, and ikiwiki can be set up to run that way using the
meta-wrapper in this package.


%files w3m
%doc README.fedora
%{cgi_bin}/ikiwiki-w3m.cgi


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.20200202.4-3
- Rebuilt for Python 3.13

* Thu Apr 04 2024 Sandro <devel@penguinpee.nl> - 3.20200202.4-2
- Drop dependency on Monotone
- Migrate to SPDX license

* Fri Mar 22 2024 Jens Petersen <petersen@redhat.com> - 3.20200202.4-1
- update to 3.20200202.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Python Maint <python-maint@redhat.com> - 3.20200202.3-15
- Rebuilt for Python 3.12

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.20200202.3-11
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.20200202.3-10
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.20200202.3-7
- Rebuilt for Python 3.10

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.20200202.3-6
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20200202.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.20200202.3-3
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.20200202.3-2
- Rebuilt for Python 3.9

* Mon Feb 17 2020 Thomas Moschny <thomas.moschny@gmx.de> - 3.20200202.3-1
- Update to 3.20200202.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20190228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Thomas Moschny <thomas.moschny@gmx.de> - 3.20190228-1
- Update to 3.20190228.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.20180311-9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20180311-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.20180311-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20180311-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20180311-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 3.20180311-4
- Perl 5.28 rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.20180311-3
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.20180311-2
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.20180311-1
- Update to 2.0180311.

* Sat Mar  3 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.20180228-1
- Update to 3.20180228.
- Update BRs.
- The rst plugin now uses python3.

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.20180105-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.20180105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.20180105-1
- Update to 20180105.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20170111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.20170111-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20170111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.20170111-1
- Update to 3.20170111.

* Wed Jan 11 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.20170110-1
- Update to 3.20170110.

* Wed Jan  4 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.20161229.1-1
- Update to 3.20161229.1.
- Remove patch applied upstream.
- Don't fail build if the test suite fails.

* Tue Aug 30 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.20160509-3
- Fix failing test with git 2.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20160509-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 13 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.20160509-1
- Update to 3.20160509.

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.20160121-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.20160121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.20160121-1
- Update to 3.20160121.
- Rebase patches.

* Tue Sep 15 2015 Petr Pisar <ppisar@redhat.com> - 3.20150614-2
- Specify more dependencies (bug #1258815)
- Enable tests
- Remove bogus dependency filters

* Tue Jun 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 3.20150614-1
- Update to 3.20150614.
- Mark license.
- Add BR on perl(open).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20150329-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.20150329-2
- Perl 5.22 rebuild

* Mon Apr 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 3.20150329-1
- Update to 3.20150329.
- Minor packaging changes regarding the Python plugin.

* Sun Feb 22 2015 Thomas Moschny <thomas.moschny@gmx.de> - 3.20150107-1
- Update to 3.20150107.

* Thu Dec 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20141016-1
- Update to 3.20141016.

* Thu Sep 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140916-1
- Update to 3.20140916.
- Exclude the S3 plugin on on RHEL instead of renaming it.

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.20140831-2
- Perl 5.20 mass

* Fri Sep  5 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140831-1
- Update to 3.20140831.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.20140815-2
- Perl 5.20 rebuild

* Fri Aug 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140815-1
- Update to 3.20140815.

* Fri Aug  1 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140613-2
- Disable the S3 plugin (rhbz#1125850).

* Fri Jun 27 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140613-1
- Update to 3.20140613-1.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20140227-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar  8 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140227-1
- Update to 3.20140227.

* Sat Jan 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140125-1
- Update to 3.20140125.

* Sat Jan 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 3.20140102-1
- Update to 3.20140102.
- Modernize spec file.

* Thu Sep 12 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.20130904.1-1
- Update to 3.20130904.1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20130711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.20130711-1
- Update to 3.20130711.

* Sat Jun  8 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.20130518-1
- Update to 3.20130518.

* Sat May 11 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.20130504-1
- Update to 3.20130504.

* Wed Feb 13 2013 Thomas Moschny <thomas.moschny@gmx.de> - 3.20130212-1
- Update to 3.20130212.

* Fri Dec 21 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20121212-1
- Update to 3.20121212.

* Thu Oct 18 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20121017-1
- Update to 3.20121017.

* Fri Oct  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120725-2
- Add missing runtime dependency on YAML::XS.

* Sat Sep 29 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120725-1
- Update to 3.20120725.
- Add missing BR.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20120629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120629-1
- Update to 3.20120629.

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 3.20120516-2
- Perl 5.16 rebuild

* Thu May 17 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120516-1
- Update to 3.20120516.

* Mon Apr 30 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120419-1
- Update to 3.20120419.
- Specfile cleanups.

* Mon Mar 26 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120203-1
- Update to 3.20120203.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120202-1
- Update to 3.20120202.
- Add BR on YAML::XS.

* Tue Jan 17 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120115-1
- Update to 3.20120115.

* Fri Jan 13 2012 Thomas Moschny <thomas.moschny@gmx.de> - 3.20120109-1
- Update to 3.20120109.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20111107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20111107-1
- Update to 3.20111107.

* Wed Nov  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20111106-1
- Update to 3.20111106.

* Wed Sep 14 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110905-1
- Update to 3.20110905.

* Sat Jul 23 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110715-3
- Update license tag.
- Add BR on Python to ensure the Python plugin gets byte-compiled.
- Add runtime dependency on Python.

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 3.20110715-2
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110715-1
- Update to 3.20110715.

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 3.20110707-2
- Perl mass rebuild

* Sat Jul  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110707-1
- Update to 3.20110707.

* Sun Jun 19 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110608-1
- Update to 3.20110608.

* Sat May  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110430-1
- Update to 3.20110430.
- Reset spurious x-bits.

* Sun Apr 10 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110328-1
- Update to 3.20110328.
- New BR perl(YAML).

* Fri Mar 25 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110321-1
- Update to 3.20110321.

* Wed Mar  2 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110225-1
- Update to 3.20110225.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20110124-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110124-2
- Use new filtering macros for provides and requires.

* Sun Feb  6 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110124-1
- Update to 3.20110124.

* Fri Jan  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20110105-1
- Update to 3.20110105.

* Mon Jan  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 3.20101231-1
- Update to 3.20101231.

* Sat Dec 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20101201-1
- Update to 3.20101201.

* Tue Nov 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20101129-1
- Update to 3.20101129.

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20101023-1
- Update to 3.20101023.

* Sat Oct  2 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100926-1
- Update to 3.20100926.

* Thu Sep 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100915-1
- Update to 3.20100915.

* Tue Sep  7 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100831-1
- Update to 3.20100831.

* Fri Aug 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100815-1
- Update to 3.20100815.

* Thu Aug  5 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100804-1
- Update to 3.20100804.

* Fri Jul 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100722-1
- Update to 3.20100722.

* Fri Jul  2 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100623-1
- Rebase libexecdir patch.
- Update to 3.20100623.

* Wed Jun 23 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100610-1
- Update to 3.20100610.

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.20100518.2-2
- Mass rebuild with perl-5.12.0

* Sun May 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100518.2-1
- Update to 3.20100518.2.

* Sat May  8 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100504-1
- Update to 3.20100504.

* Wed May  5 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100501-1
- Update to 3.20100501.

* Tue Apr  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100403-1
- Update to 3.20100403.

* Thu Mar 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100312-1
- Update to 3.20100312 (fixes bz 574548).

* Wed Mar  3 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100302-1
- Update to 3.20100302.

* Sun Feb 14 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100212-1
- Update to 3.20100212.

* Thu Feb  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100122-1
- Update to 3.20100122.

* Tue Jan  5 2010 Thomas Moschny <thomas.moschny@gmx.de> - 3.20100102.3-1
- Update to 3.20100102.3.
- Replace %%define with %%global.

* Tue Dec 22 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.20091218-1
- Update to 3.20091218.

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 3.20091113-2
- rebuild against perl 5.10.1

* Tue Nov 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.20091113-1
- Update to 3.20091113.

* Thu Oct  8 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.14159265-1
- Update to 3.14159265.

* Tue Sep  1 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.1415926-1
- Update to 3.1415926 (fixes CVE-2009-2944, see bz 520543).

* Wed Aug 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.141592-1
- Update to 3.141592.
- po4a is needed now.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1415-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.1415-1
- Update to 3.1415.

* Thu Jun 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.14-1
- Update to 3.14.

* Fri May 15 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.12-1
- Update to 3.12.

* Tue May  5 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.11-1
- Update to 3.11.

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.10-1
- Update to 3.10.

* Tue Apr  7 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.09-1
- Update to 3.09.

* Fri Mar 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.08-1
- Update to 3.08.

* Mon Mar  9 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.07-1
- Update to 3.07.

* Thu Mar  5 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.06-1
- Update to 3.06.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.04-1
- Update to 3.04.

* Mon Feb  9 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.03-1
- Update to 3.03.

* Sat Jan 10 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.01-1
- Update to 3.01.

* Fri Jan  2 2009 Thomas Moschny <thomas.moschny@gmx.de> - 3.00-1
- Update to 3.00.

* Fri Jan  2 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.72-1
- Update to 2.72.
- Patch for mtn plugin has been applied upstream.
- Encoding of ikiwiki.vim has been changed to utf-8 upstream.
- Use new W3M_CGI_BIN option in %%install.

* Tue Dec 16 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.70-3
- Patch for monotone plugin: Prevent broken pipe message.
- Cosmetic changes to satisfy rpmlint.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.70-2
- Rebuild for Python 2.6

* Thu Nov 20 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.70-1
- Update to 2.70.
- Install and enable the external rst plugin.
- Stop filtering perl(RPC::XML*) requires.

* Fri Oct 10 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.66-1
- Update to 2.66.

* Fri Sep 19 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.64-1
- Update to 2.64.

* Thu Sep 11 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.63-1
- Update to 2.63.

* Sat Aug 30 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.62.1-1
- Update to 2.62.1. Add /etc/ikiwiki.

* Thu Aug  7 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.56-1
- Update to 2.56.
- Stop filtering perl(Net::Amazon::S3), has been approved (bz436481).

* Thu Jul 31 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.55-1
- Update to 2.55.

* Thu Jul 24 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.54-1
- Update to 2.54.
- Move example plugin file to doc.

* Sat Jul 12 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.53-1
- Update to 2.53.

* Thu Jul 10 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.52-1
- Update to 2.52.

* Sun Jul  6 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.51-1
- Update to 2.51.
- Save iconv output to a temporary file.

* Sun Jun 15 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.50-1
- Update to 2.50.
- Move ikiwiki-w3m.cgi into a subpackage.
- Add ikiwiki's own documentation.
- Remove duplicate requirement perl(File::MimeInfo).
- Minor cleanups.

* Mon Jun  2 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.48-1
- Update to 2.48.

* Wed May 28 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.47-1
- Update to 2.47.

* Tue May 13 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.46-1
- Update to 2.46.

* Sat May 10 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.45-1
- New package.
