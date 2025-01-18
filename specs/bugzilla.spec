%define bzinstallprefix %{_datadir}
%define bzdatadir %{_sharedstatedir}/bugzilla

Summary: Bug tracking system
URL: https://www.bugzilla.org/
Name: bugzilla
Version: 5.0.6
Release: 24%{?dist}
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License: LicenseRef-Callaway-MPLv1.1
Source0: https://github.com/bugzilla/bugzilla/archive/release-%{version}.tar.gz
Source1: bugzilla-httpd-conf
Source2: README.fedora.bugzilla
Source3: bugzilla.cron-daily
Patch0: bugzilla-rw-paths.patch
Patch1: bugzilla-dnf.patch
Patch2: bugzilla-1438957-concatenate-assets.patch
# https://bug1657496.bmoattachments.org/attachment.cgi?id=9169528
Patch3: bugzilla-1855962-non-html-mail.patch
Patch4: bugzilla-2180465-sphinx-build.patch

BuildArch: noarch
Requires: patchutils
Requires: perl(CGI) >= 3.51
Requires: perl(Digest::SHA)
Requires: perl(Date::Format) >= 2.23
Requires: perl(DateTime) >= 0.75
Requires: perl(DateTime::TimeZone) >= 1.64
Requires: perl(DBI) >= 1.614
Requires: perl(ExtUtils::MM)
Requires: perl(Template) >= 2.24
Requires: perl(Email::Sender) >= 1.300011
Requires: perl(Email::MIME) >= 1.904
Requires: perl(URI) >= 1.55
Requires: perl(List::MoreUtils) >= 0.32
Requires: perl(Math::Random::ISAAC) >= 1.0.1
Requires: perl(File::Slurp) >= 9999.13
Requires: perl(JSON::XS) >= 2.01
Requires: perl(Locale::Language)
Requires: webserver
Requires: which

# for building docs
BuildRequires: latexmk
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Which)
BuildRequires: perl(lib)
BuildRequires: perl(Memoize)
BuildRequires: perl(parent)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: python3-sphinx
BuildRequires: texlive-collection-latexrecommended
BuildRequires: texlive-collection-basic
BuildRequires: tex(fncychap.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(tgtermes.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(wrapfig.sty)
BuildRequires: tex(capt-of.sty)
BuildRequires: tex(eqparbox.sty)
BuildRequires: tex(needspace.sty)
BuildRequires: tex(tabulary.sty)
BuildRequires: tex(upquote.sty)

%package doc
Summary: Bugzilla documentation

%package doc-build
Summary: Tools to generate the Bugzilla documentation

%package contrib
Summary: Bugzilla contributed scripts
BuildRequires: python3-devel

%{?perl_default_filter}

# Remove private modules from the requires stream
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(sanitycheck.cgi\\)$

# Remove all optional modules from the requires stream
# mod_perl modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Apache2::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(ModPerl::
# installation of optional modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Config\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN\\)$
# authentification modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::Radius\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::LDAP
# database modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Oracle\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::Pg\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::db\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::st\\)$
# graphical reports and charts
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Chart::Lines\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(GD::Graph\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Template::Plugin::GD::Image\\)$
# inbound email modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::MIME::Attachment::Stripper\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Email::Reply\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::FormatText::WithLinks\\)$
# automatic charset detection for text attachments
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Encode
# sniff MIME type of attachments
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::MimeInfo::Magic\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::Scalar\\)$
# mail queueing
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TheSchwartz\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Daemon::Generic\\)$
# smtp security
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Authen::SASL\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Net::SMTP::SSL\\)$
# bug moving modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(MIME::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Twig\\)$
# update notifications
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(LWP::UserAgent\\)$
# use html in product and group descriptions
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTML::Scrubber\\)$
# memcached support
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Cache::Memcached\\)$
# documentation
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Copy::Recursive\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Which\\)$
# xml-rpc and json-rpc modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XMLRPC::
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Message\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Taint\\)$
# extension modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)$

# and remove the extensions from the provides stream
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::BmpConvert\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Auth::Login\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Auth::Verify\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::Config\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Example::WebService\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::OldBugMove\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::OldBugMove::Params\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Bugzilla::Extension::Voting\\)$

%description
Bugzilla is a popular bug tracking system used by multiple open source projects
It requires a database engine installed - either MySQL, PostgreSQL or Oracle.
Without one of these database engines (local or remote), Bugzilla will not work
- see the Release Notes for details.

%description doc
Documentation distributed with the Bugzilla bug tracking system

%description doc-build
Tools to generate the documentation distributed with Bugzilla

%description contrib
Contributed scripts and functions for Bugzilla

%prep
%setup -q -n %{name}-release-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

# Deal with changing /usr/local paths here instead of via patches
/usr/bin/perl -pi -e 's|/usr/local/bin/python\b|%{__python3}|' contrib/*.py
/usr/bin/rm -rf contrib/bugzilla-submit

grep -rl '/usr/lib/sendmail\b' contrib docs \
| xargs /usr/bin/perl -pi -e 's|/usr/lib/sendmail\b|%{_sbindir}/sendmail|'

%build
# Build docs
docs/makedocs.pl --with-pdf
# Remove the execute bit from files that don't start with #!
for file in `find -type f -perm /111`; do
  if head -1 $file | grep -E -v '^\#!' &>/dev/null; then
    chmod a-x $file
  fi
done
# Ensure shebang shell scripts have executable bit set
for file in `find -type f -perm /664`; do
  if head -1 $file | grep -E '^\#!' &>/dev/null; then
    chmod a+x $file
  fi
done

%install
mkdir -p %{buildroot}%{bzinstallprefix}/bugzilla
# these files are only used for testing Bugzilla code
# see https://bugzilla.mozilla.org/show_bug.cgi?id=995209
rm Build.PL MANIFEST.SKIP
cp -pr * %{buildroot}%{bzinstallprefix}/bugzilla
echo "0-59/15 * * * * apache cd %{bzinstallprefix}/bugzilla && env LANG=C %{bzinstallprefix}/bugzilla/whine.pl" > %{buildroot}%{bzinstallprefix}/bugzilla/cron.whine
rm -f %{buildroot}%{bzinstallprefix}/bugzilla/README \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/TODO \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/en/Makefile \
    %{buildroot}%{bzinstallprefix}/bugzilla/docs/en/make.bat
cp %{SOURCE2} ./README.fedora
mkdir -p %{buildroot}%{bzdatadir}/assets
mkdir -p %{buildroot}%{_sysconfdir}/bugzilla
install -m 0644 -D -p %{SOURCE1}  %{buildroot}%{_sysconfdir}/httpd/conf.d/bugzilla.conf
install -m 0755 -D -p %{SOURCE3}  %{buildroot}%{bzinstallprefix}/bugzilla/cron.daily
ln -s ../../..%{bzdatadir}/assets %{buildroot}%{bzinstallprefix}/bugzilla/assets

%post
(pushd %{bzinstallprefix}/bugzilla > /dev/null
[ -f /etc/bugzilla/localconfig ] || ./checksetup.pl > /dev/null
popd > /dev/null)

%files
%defattr(-,root,apache,-)
%dir %{bzinstallprefix}/bugzilla
%{bzinstallprefix}/bugzilla/LICENSE
%{bzinstallprefix}/bugzilla/*.cgi
%{bzinstallprefix}/bugzilla/*.json
%{bzinstallprefix}/bugzilla/*.pl
%{bzinstallprefix}/bugzilla/Bugzilla.pm
%{bzinstallprefix}/bugzilla/robots.txt
%{bzinstallprefix}/bugzilla/Bugzilla
%{bzinstallprefix}/bugzilla/extensions
%{bzinstallprefix}/bugzilla/images
%{bzinstallprefix}/bugzilla/js
%{bzinstallprefix}/bugzilla/lib
%{bzinstallprefix}/bugzilla/skins
%{bzinstallprefix}/bugzilla/t
%{bzinstallprefix}/bugzilla/xt
%{bzinstallprefix}/bugzilla/template
%{bzinstallprefix}/bugzilla/cron.daily
%{bzinstallprefix}/bugzilla/cron.whine
%{bzinstallprefix}/bugzilla/contrib/README
%{bzinstallprefix}/bugzilla/assets
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bugzilla.conf
%attr(770,root,apache) %dir %{bzdatadir}
%attr(770,root,apache) %dir %{bzdatadir}/assets
%attr(750,root,apache) %dir %{_sysconfdir}/bugzilla
%defattr(-,root,root,-)
%doc README
%doc README.fedora

%files doc
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/docs/en/html
%{bzinstallprefix}/bugzilla/docs/en/images
%{bzinstallprefix}/bugzilla/docs/en/pdf
%{bzinstallprefix}/bugzilla/docs/en/txt
%{bzinstallprefix}/bugzilla/docs/en/rst
%{bzinstallprefix}/bugzilla/docs/style.css


%files doc-build
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/docs/makedocs.pl
%{bzinstallprefix}/bugzilla/docs/lib

%files contrib
%defattr(-,root,apache,-)
%{bzinstallprefix}/bugzilla/contrib/bugzilla-queue.rhel
%{bzinstallprefix}/bugzilla/contrib/bugzilla-queue.suse
%{bzinstallprefix}/bugzilla/contrib/bzdbcopy.pl
%{bzinstallprefix}/bugzilla/contrib/bz_webservice_demo.pl
%{bzinstallprefix}/bugzilla/contrib/cmdline
%{bzinstallprefix}/bugzilla/contrib/console.pl
%{bzinstallprefix}/bugzilla/contrib/convert-workflow.pl
%{bzinstallprefix}/bugzilla/contrib/extension-convert.pl
%{bzinstallprefix}/bugzilla/contrib/fixperms.pl
%{bzinstallprefix}/bugzilla/contrib/jb2bz.py*
%{bzinstallprefix}/bugzilla/contrib/merge-users.pl
%{bzinstallprefix}/bugzilla/contrib/mysqld-watcher.pl
%{bzinstallprefix}/bugzilla/contrib/new-yui.sh
%{bzinstallprefix}/bugzilla/contrib/perl-fmt
%{bzinstallprefix}/bugzilla/contrib/recode.pl
%{bzinstallprefix}/bugzilla/contrib/sendbugmail.pl
%{bzinstallprefix}/bugzilla/contrib/sendunsentbugmail.pl
%{bzinstallprefix}/bugzilla/contrib/syncLDAP.pl
%{bzinstallprefix}/bugzilla/contrib/Bugzilla.pm

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.6-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 07 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-18
- Patch to build against Sphinx 6.1.3 (#2180465)
- Use new patch syntax

* Sun Feb 12 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-17
- Add missing buildrequirement on tgtermes.sty (#2160038)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-12
- Add make to BuildRequires

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-10
- Replace calls to %%{__perl} with /usr/bin/perl
- Remove contrib/bugzilla-submit (no longers works) (#1835451)

* Tue Sep 29 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-9
- Remove automagic Python bytecompilation macro
- Include upstream patch for text mails (#1855962)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Tue Mar 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.6-6
- Add all perl dependencies needed for build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-4
- Drop unused build dependency on Python 2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-2
- Use %%{__python3} instead of %%{__python2}
- Depend on python3-sphinx instead of python2-sphinx

* Thu Feb 14 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-1
- Update to 5.0.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.4-1
- Update to 5.0.4
- Remove backported File::Slurp patch, no longer needed
- use %%{__python2} instead of %%{__python}
- Disable the concatenation of assets (#1438957)

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.0.3-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-8
- Tighten macro expansion (thanks to ppisar)
- Drop Group tag
- Use tex(..) BuildRequires where possible

* Mon Aug 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-7
- Add doc-building requirement to fix FTBS
- Add perl(ExtUtils::MM) to the list of required modules

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-5
- Include more dependencies to fix FTBFS (#1423283)
- Allow AuthConfig directives in Bugzilla's directory (#1403588)
- Backport patch to use internal functions rather than File::Slurp (#1425077)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 27 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-3
- Check for perl(JSON::RPC::Legacy::Server::CGI) instead of perl(JSON::RPC)

* Sun Jul 17 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-2
- Add build requirements for texlive sub-packages
- Filter out more optional dependencies

* Mon May 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-1
- Update to 5.0.3, dropping backported patch

* Sun May 01 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.2-3
- backport patch to prevent email address encoding

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.2-1
- Update to 5.0.2, with thanks to Tuomo Soini (#1275609)
- Use dnf instead of yum when advising to install perl modules
- Change documentation URL to bugzilla.readthedocs.org

* Mon Sep 28 2015 Tuomo Soini <tis@foobar.fi> - 5.0.1-3
- fix data directory permissions and config dir permissions

* Mon Sep 28 2015 Tuomo Soini <tis@foobar.fi> - 5.0.1-2
- Fix file owners to be mostly correct
- rewrite patching of paths in Constants.pm

* Fri Sep 11 2015 Tuomo Soini <tis@foobar.fi> - 5.0.1-1
- Update to 5.0.1 new stable series
- update dependencies for 5.0.1
- build documentation
- add documentation build dependencies

* Thu Sep 10 2015 Tuomo Soini <tis@foobar.fi> - 4.4.10-1
- Update to 4.4.10 to fix CVE-2015-4499

* Wed Jun 17 2015 Tuomo Soini <tis@foobar.fi> - 4.4.9-1
- Update to 4.4.9 for several important bug fixes

* Tue Jun 16 2015 Tuomo Soini <tis@foobar.fi> - 4.4.8-1
- Import from rawhide (F23)

* Sat Jan 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4.8-1
- Update to 4.4.8 (fixes regressions in 4.4.7 which itself
  fixed security flaws) (CVE-2014-1571, CVE-2014-8630)

* Sun Jan 04 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4.6-2
- Remove bundled binary files (#1000245)
- Add webdot directory perms to apache configuration

* Wed Oct 08 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4.6-1
- Update to 4.4.6

* Fri Jul 25 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4.5-1
- Update to 4.4.5

* Mon Jul 07 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4.4-1
- Update to 4.4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.9-1
- Update to 4.2.9 (regression fix for 4.2.8 which was a security update)
- Drop backported patches

* Tue Jan 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.7-3
- Fix the comparison of module versions (#1044854)
- Really honor the PROJECT environment variable (#911943)

* Thu Nov 14 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.7-2
- Add patch to cache bz_locations() (bmo #843457)
- Fix constants patch to honor the PROJECT environment variable (#911943)

* Thu Oct 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.7-1
- Update to 4.2.7 (security updates)
- Patch bugzilla to write compiled templates under /var (#949130)

* Thu Aug 15 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.6-5
- Stop creating /usr/share/doc/bugzilla-<version> (#993688)
- Fix incorrect date in changelog

* Sun Aug 04 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.6-4
- Change apache conf to enable access to all machines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.2.6-2
- Perl 5.18 rebuild

* Sun May 26 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.6-1
- Update to 4.2.6

* Wed Feb 20 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.5-1
- Update to 4.2.5 (fixes CVE-2013-0785)

* Tue Feb 05 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.4-2
- Update httpd configuration file for Apache 2.4
- Update httpd configuration file for the upcoming bugzilla 4.4

* Wed Nov 14 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.4-1
- Update to 4.2.4
- Remove the defattr and clean macros (no longer used)

* Sun Sep 02 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 4.2.3-1
- Update to 4.2.3

* Mon Jul 30 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.2.2-1
- Update to 4.2.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.2.1-1
- Update to 4.2.1 (CVE-2012-0465, CVE-2012-0466)

* Sun Feb 26 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.2-1
- Update to 4.2 (#797225)
- Include contrib/README instead of contrib/recode.pl in the main package

* Sun Feb 26 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.5-2
- Leave perl(Bugzilla::Extension::Example::Util) in the provides stream

* Thu Feb 23 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.5-1
- Update to 4.0.5 to fix security issues
- Block all ModPerl::* and Apache2::* from requires
- Remove rpm4.8 filters

* Wed Feb  1 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.4-1
- Update to 4.0.4 to fix security flaws (#786550)
- Remove JSON:RPC patch, upstreamed (bmo #706753)
- Correct upstream URL in README.fedora.bugzilla, thanks to Ken Dreyer (#783014)

* Tue Jan 10 2012 Tom Callaway <spot@fedoraproject.org> - 4.0.3-2
- patch bz to use JSON::RPC::Legacy::Server::CGI

* Fri Dec 30 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.3-1
- Update to 4.0.3
- Add perl(Locale::Language) to the Requires
- Put the xml docs source in the doc-build subpackage
- Add index.html to the DirectoryIndex
- Fix typo in README.fedora.bugzilla

* Fri Aug 05 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.2-1
- Update to 4.0.2
- Add RPM-4.9-style filtering
- Put graphs in /var/lib/bugzilla/graphs.

* Sun May 01 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0.1-1
- Update to 4.0.1
- Patch the installation procedure to recommend yum

* Sun Mar 27 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 4.0-1
- Update to 4.0

* Sun Mar 06 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-7
- Put contrib/recode.pl in the main package so that it no longer depends on
  python and ruby
- Remove the contents of the lib/ directory, not the directory itself.

* Tue Feb 15 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-6
- More filtering

* Mon Feb 14 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-5
- Fix broken dependencies
- Remove unused patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-3
- Remove no-longer-needed files

* Sat Jan 29 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-2
- Move to the current filtering system for provides and requires

* Tue Jan 25 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.4-1
- Update to 3.6.4
- Add RPM-4.9-style filtering
- 

* Wed Nov 03 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.3-1
- Update to 3.6.3 (#649406)
- Fix webdot alias in /etc/httpd/conf.d/bugzilla (#630255)
- Do not apply graphs patch (upstreamed)

* Wed Aug 18 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.2-1
- Update to 3.6.2 (#623426)
- Only run checksetup if /etc/bugzilla/localconfig does not exist (#610210)
- Add bugzilla-contrib to Requires (#610198)

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 3.6.1-2
- recompiling .py files against Python 2.7 (rhbz#623281)

* Fri Jun 25 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6.1-1
- Update to 3.6.1

* Sun Jun  6 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6-3
- Remove mod_perl from the requirements (#600924)

* Sun Jun  6 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6-2
- Fix missing provides (#600922)

* Tue Apr 13 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.6-1
- Update to 3.6 (#598377)
- Patch to put graphs in /var/lib/bugzilla/ (brc #564450, bmo #313739)

* Mon Feb 01 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4.5-1
- Update to 3.4.5 (CVE-2009-3989, CVE-2009-3387)
- Remove bugzilla-EL5-perl-versions.patch which is EPEL-specific

* Thu Nov 19 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4.4-1
- Update to 3.4.4 (CVE-2009-3386)

* Wed Nov 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4.3-1
- Update to 3.4.3 (fixes memory leak issues)
- Add perl(Digest::SHA) in the Requires
- Specify Perl module versions in the Requires (fixes #524309)
- Add an alias to make $webdotdir a working path (fixes #458848)

* Fri Sep 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4.2-1
- Update to 3.4.2 (CVE-2009-3125, CVE-2009-3165 and CVE-2009-3166)

* Tue Aug 04 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.4.1-2
- fix EL-5 perl dependencies bz#515158

* Sun Aug 02 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4.1-1
- Update to 3.4.1, fixing a security leak

* Wed Jul 29 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.4-1
- Update to 3.4 (fixes #514315)
- move makedocs.pl to its own package (fixes #509041)
- move the extensions dir to /usr/share/ (fixes #450636)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.2.4-1
- fix https://bugzilla.mozilla.org/show_bug.cgi?id=495257

* Mon Apr 06 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.2.3-1
- fix CVE-2009-1213

* Thu Mar 05 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.2.2-2
- fix from BZ #474250 Comment #16, from Chris Eveleigh -->
- add python BR for contrib subpackage
- fix description
- change Requires perl-SOAP-Lite to perl(SOAP::Lite) according guidelines

* Sun Mar 01 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.2.2-1
- thanks to Chris Eveleigh <chris dot eveleigh at planningportal dot gov dot uk>
- for contributing with patches :-)
- Upgrade to upstream 3.2.2 to fix multiple security vulns
- Removed old perl_requires exclusions, added new ones for RADIUS, Oracle and sanitycheck.cgi
- Added Oracle to supported DBs in description (and moved line breaks)
- Include a patch to fix max_allowed_packet warnin when using with mysql

* Sat Feb 28 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.0.8-1
- Upgrade to 3.0.8, fix #466077 #438080
- fix macro in changelog rpmlint warning
- fix files-attr-not-set rpmlint warning for doc and contrib sub-packages

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Stepan Kasal <skasal@redhat.com> - 3.0.4-3
- do not require perl-Email-Simple, it is (no longer) in use
- remove several explicit perl-* requires; the automatic dependencies
  do handle them

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.4-2
- fix license tag

* Fri May  9 2008 John Berninger <john at ncphotography dot com> - 3.0.4-1
- Update to upstream 3.0.4 to fix multiple security vulns
- Change perms on /etc/bugzilla for bz 427981

* Sun May  4 2008 John Berninger <john at ncphotography dot com> - 3.0.3-0
- Update to upstream 3.0.3 - bz 444669

* Fri Dec 28 2007 John Berninger <john at ncphotography dot com> - 3.0.2-6
- Add cron.daily, cron.whine to payload list

* Fri Dec 28 2007 John Berninger <john at ncphotography dot com> - 3.0.2-5
- Typo in spec file, rebuild

* Fri Dec 28 2007 John Berninger <john at ncphotography dot com> - 3.0.2-3
- bz 426465 - don't enable cron jobs so cron doesn't complain about
  an unconfigured installation

* Fri Oct 26 2007 John Berninger <john at ncphotography dot com> - 3.0.2-2
- fix issue with AlowOverride Options

* Mon Oct 22 2007 John Berninger <john at ncphotography dot com> - 3.0.2-1
- updates to requires and httpd conf for BZ's 279961, 295861, 339531

* Mon Sep 24 2007 John Berninger <john at ncphotography dot com> - 3.0.2-0
- update to 3.0.2 - bz 299981

* Mon Aug 27 2007 John Berninger <john at ncphotography dot com> - 3.0.1-0
- update to 3.0.1 - bz 256021

* Fri May 18 2007 John Berninger <jwb at redhat dot com> - 3.0-2
- update Requires for bz's 241037, 241206

* Fri May 18 2007 John Berninger <jwb at redhat dot com> - 3.0-1
- update to upstream version 3.0
- add new dependencies on mod_perl, perl-SOAP-Lite
- refactor patch(es) to change paths for read-only /usr

* Tue Feb 20 2007 John Berninger <jwb at redhat dot com> - 2.22.2-1
- update to 2.22.2 - bz 229163

* Wed Feb 14 2007 John Berninger <jwb at redhat dot com> - 2.22-12
- More cron job fixes

* Wed Jan 31 2007 John Berninger <jwb at redhat dot com> - 2.22-11
- Fix cron job perms

* Sat Jan 27 2007 John Berninger <jwb at redhat dot com> - 2.22-10
- Fix collectstats cron job, bx 224550

* Mon Jan 22 2007 John Berninger <jwb at redhat dot com> - 2.22-9
- Fix linebreak issues in specfile

* Mon Jan 22 2007 John Berninger <jwb at redhat dot com> - 2.22-8
- Put daily and hourly cronjobs in place per bz 223747

* Wed Nov  8 2006 John Berninger <johnw at berningeronline dot net> - 2.22-7
- Fixes for bz # 212355

* Tue Jun 27 2006 John Berninger <johnw at berningeronline dot net> - 2.22-6
- Clean up BugzillaEmail requires (filter it out)

* Mon Jun 26 2006 John Berninger <johnw at berningeronline dot net> - 2.22-5
- License is MPL, not GPL
- Clean up %%doc specs

* Sun Jun 25 2006 John Benringer <johnw at berningeronline dot net> - 2.22-4
- Remove localconfig file per upstream
- Patch to have localconfig appear in /etc/bugzilla when checksetup.pl is run

* Tue Jun 20 2006 John Berninger <johnw at berningeronline dot net> - 2.22-3
- Add README.fedora file
- Add additional requires per comments from upstream

* Mon Jun 19 2006 John Berninger <johnw at berningeronline dot net> - 2.22-2
- Code to /usr/share, data to /var/lib/bugzilla per FE packaging req's

* Tue Jun 13 2006 John Berninger <johnw at berningeronline dot net> - 2.22-1
- Shift to /var/lib/bugzilla install dir per discussion in review request
- Minor change in filtering requires

* Tue May 23 2006 John Berninger <johnw at berningeronline dot net> - 2.22-0
- Update to upstream 2.22 release
- Split off -contrib package, but keep it where it usually gets installed

* Wed Apr 26 2006 John Berninger <johnw at berningeronline dot net> - 2.20.1-4
- rpmlint cleanups

* Mon Apr 24 2006 John Berninger <johnw at berningeronline dot net> - 2.20.1-3
- Cleanup of prov/req filters
- Split docs into -doc package

* Thu Apr 20 2006 John Berninger <johnw at berningeronline dot net> - 2.20.1-2
- No need for CVS tarball - I was thinking things too far through.  Change
  to 2.20.1 release.

* Fri Apr  7 2006 John Berninger <johnw at berningeronline dot net> - 2.20-0.1cvs20060407
- Initial spec creation/build for Fedora Extras packaging.

