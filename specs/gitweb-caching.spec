# Pass --without docs to rpmbuild if you don't want the documentation


%global SHA1         b1ab8b5d1748b0174fb7014651f0f91de3b4c05a
%global SHA1SHORT    b1ab8b5

Name:           gitweb-caching
Version:        1.6.5.2
Release:        36.%{SHA1SHORT}%{?dist}
Summary:        Simple web interface to git repositories w/ caching support
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://git.kernel.org/?p=git/warthog9/gitweb.git;a=summary
# Tarball is generated from a snapshot of the SHA1 sum above.
# http://git.kernel.org/?p=git/warthog9/gitweb.git;a=snapshot;h=%{SHA1};sf=tgz
#
# NOTE: When downloading a snapshot in this manor (or really anytime git archive
#       is used) the sha1sum of this and any subsequent run is going to be
#       minutely different (the timestamp in the tarball will be current time)
#       because each time it is requested gitweb (and gitweb-caching) is going
#       to completely regenerate the file for download, and thus things like
#       the md5um / sha1sum of the tarball that's present in the RPM here and
#       what could be downloaded to "verify" that things match - won't.
#
#       With that said git already gives us a point of cryptographic integrity
#       internally, and the SHA1 is included here in full so if one cared
#       the individual files would be verified in the tarball vs. what is 
#       present in the repository.  Also to help make verification faster / 
#       easier I, John 'Warthog9' Hawley, am going to GPG sign the tarballs 
#       present so that the chain of trust becomes me claiming the tarball
#       was created by snagging the snapshot from the URL below and if 
#       additional verification is needed please confirm the files via a git
#       checkout of the sha1 above and doing a file by file comparison of the
#       two.
#
# NOTE: When using something like wget or curl to download the snapshot URL
#       this will likely end up in an unexpected state.  The caching, currently,
#       assumes that the client attempting to make use of it will actually
#       interpret the html passed back to it.  During cache generation an interim
#       page is displayed containing "Generating..." as a wait page.  At the end
#       of the page load a meta tag forces an immediate refresh of the page and
#       the actual intended data is shown.  However if your using the
#       aforementioned clients, they do not interpret the data downloaded and thus
#       do not 'refresh' to get the actual data intended.  In those cases the easiest
#       thing to do is to run wget until the data intended does download, or 
#       use an actual webbrowser on the same link.
Source0:        gitweb-%{SHA1}.tar.gz
Source1:        gitweb-%{SHA1}.tar.gz.asc
Source2:        gitweb-caching.conf.httpd
Patch0:         gitweb-caching-1.6-gitweb-home-link.patch
Patch1:         gitweb-caching-fix-base-bin-path.patch
Patch2:         gitweb-caching-default-cache-dir.patch
Patch3:         gitweb-caching-disable-version-matching.patch

BuildArch:      noarch
BuildRequires:      perl-generators
BuildRequires: make
Requires:       git

%description
Simple web interface to track changes in git repositories
w/ caching from John 'Warthog9' Hawley from kernel.org

%prep
%setup -n gitweb-%{SHA1SHORT} -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
make %{_smp_mflags} V=1 NO_CURL=1 gitweb/gitweb.cgi gitweb/gitweb_defaults.pl

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_var}/www/gitweb-caching
install -pm 644 gitweb/*.png gitweb/*.css gitweb/gitweb_defaults.pl gitweb/cache.pm $RPM_BUILD_ROOT%{_var}/www/%{name}
install -pm 755 gitweb/gitweb.cgi $RPM_BUILD_ROOT%{_var}/www/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -pm 0755 --directory $RPM_BUILD_ROOT%{_var}/cache/gitweb-caching
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

%files
%doc gitweb/README COPYING
%{_var}/www/%{name}/
%config(noreplace)%{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0755, apache, apache) %{_var}/cache/gitweb-caching

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-36.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.5.2-35.b1ab8b5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-34.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-33.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-32.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-31.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-30.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-29.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-28.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-27.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-26.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-25.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-24.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-23.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-22.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-21.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-20.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-19.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-18.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5.2-17.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-16.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-15.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-14.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.6.5.2-13.b1ab8b5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-12.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-11.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-10.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5.2-9.b1ab8b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-8.b1ab8b5
- New snapshot from upstream
- Flock fixes for binary files (snapshots mainly)
- Ability to disable forking in the code
- Other fixes from upstream
* Thu Jun 1 2010 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-7.9eb8a78
- New snapshot from upstream
- Fix for older File::Path not having make_path
  (Enterprise Linux 5 and older related)
* Thu Feb 4 2010 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-6.cda981c9
- Really fixing apache configuration now
* Thu Feb 4 2010 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-5.cda981c9
- Fixing apache configuration so that it points to the right location
- Added missing cache.pm file
- Fixed git binary path
- Created and pointed caching directory to /var/cache/gitweb-caching (default)
- Disable git version matching
* Wed Jan 6 2010 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-4.cda981c9
- Added COPYING
* Sun Dec 7 2009 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-3.cda981c9
- Added documentation about wget + gitweb-caching will likely result in unexpected
  results
- Signed tarball with GPG
- Added documentation about why git snapshots do not match md5sum or sha1sums
  naturally.

* Sun Dec 6 2009 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-2.cda981c9
- Fixing URL
- Adding version to changelog
- Sha1 sum added to release
- Setting to always build noarch

* Sun Dec 6 2009 John 'Warthog9' Hawley <warthog9@kernel.org> 1.6.5.2-1.cda981c9
- initial gitweb-caching spec file
