%global commit 55c5c285558c410bb35ebf421245d320ab9ee9fa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkoutdate 20181107
%global checkout %{checkoutdate}git%{shortcommit}

Name:       gitstats
Version:    0
Release:    0.26.%{checkout}%{?dist}
Summary:    Generates statistics based on GIT repository activity

# All code and content other than sortable.js is available under the GPLv2
# and GPLv3 licenses. The sortable.js file is available under the MIT license.
License:    GPLv2 and GPLv3 and MIT
URL:        http://%{name}.sourceforge.net
Source0:    https://github.com/hoxu/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:     %{name}-%{version}-gitstats.patch
BuildArch:  noarch

BuildRequires: /usr/bin/pod2man
BuildRequires: make
Requires:   python3
Requires:   gnuplot >= 4.0.0
Requires:   git >= 1.5.2.4

%description

GitStats is a statistics generator for git (a distributed revision control
system) repositories. It examines the repository and produces some interesting
statistics from the history of it. Currently HTML is the only output format.

%prep
%setup -qn %{name}-%{commit}
%patch0

%build
# Use pod2man directly instead of 'make man' as Makefile task expects to be
# running from a git clone (and generates the --release value based on this
# rather than the tarball.
pod2man --center "User Commands" -r "%{name}-%{version}-%{release}" doc/%{name}.pod doc/%{name}.1
gzip doc/%{name}.1

%install
make install PREFIX=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/AUTHOR %{buildroot}%{_docdir}/%{name}/AUTHOR
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/GPLv2 %{buildroot}%{_docdir}/%{name}/GPLv2
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/GPLv3 %{buildroot}%{_docdir}/%{name}/GPLv3
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/README %{buildroot}%{_docdir}/%{name}/README
install -p -m 0644 $RPM_BUILD_DIR/%{name}-%{commit}/doc/%{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%{_bindir}/%{name}
%dir %{_datarootdir}/%{name}
%{_datarootdir}/%{name}/arrow-down.gif
%{_datarootdir}/%{name}/arrow-none.gif
%{_datarootdir}/%{name}/arrow-up.gif
%{_datarootdir}/%{name}/%{name}.css
%{_datarootdir}/%{name}/sortable.js
%doc %{_docdir}/%{name}
%doc %{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 4 2019 Stephen Gordon <sgordon@redhat.com> 0-0.19.20181107git55c5c28
Remove errant python2 requirement.

* Fri Oct 4 2019 Stephen Gordon <sgordon@redhat.com> 0-0.18.20181107git55c5c28
- Patch for Python3 support https://bugzilla.redhat.com/show_bug.cgi?id=1737997

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20181107git55c5c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Stephen Gordon <sgordon@redhat.com> - 0-0.15.20181107git55c5c285
- Rebase from upstream to include change to explicitly call python2
- https://bugzilla.redhat.com/show_bug.cgi?id=1583357

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0-0.13.20141209gitc2310a8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20141209gitc2310a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Stephen Gordon <sgordon@redhat.com> - 0-0.7.20141209c2310a8
- Change manpage repository address to github.
- Fix Makefile `make man` to work w/o .git
- Correct splitting of git-ls-tree output
- Add missing alt text for img.
- Move </tr> to right place.
- Use id-based fragment identifiers.
- Generate html5, not xhtml.
- Add missing xhtml end tag.
- Added HTML header meta tag so that author names will be shown correctly also when the file is opened in a browser.
- Removed useless merge_authors configuration option. Use .mailmap instead.
- How to merge author information.
- Document start_date option on the manpage.
- implement a way to limit the statistics to commits after a start date
- properly terminate created subprocesses
- Fix indentation to be consistent.
- Go back to previous dir to no fail on relative paths
- Bump copyright year.
- Y-Axis of graphs start at zero
- fix: let "Pool" for line count data collection honor "processes" configuration setting
- Bump README python requirement to 2.6.0.
- Remove backticks from author names passed to gnuplot.
- Fix minor documentation issues
- Make number of processes configurable.
- Fix performance issue for huge repositories
- Bump copyright year.
- Refer to manual page in usage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20130723gita923085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20130723gita923085
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Stephen Gordon <sgordon@redhat.com> 0.0.4-20130723gita923085
- Added handling of -h and --help arguments (rhbz#962168).

* Mon Feb 25 2013 Stephen Gordon <sgordon@redhat.com> 0-0.4-20130224git0843039
- Added /usr/share/gitstats to files list.
- Added -p argument to install invocation to preserve timestamps.
- Use release macro in pod2man arguments instead of rebuilding the equivalent
  again using the other macros.

* Mon Feb 25 2013 Stephen Gordon <sgordon@redhat.com> 0-0.3-20130224git0843039
- Removed BuildRequires on gzip.
- Removed attribute declarations on file list.
- Updated version/release strategy to be more consistent with Fedora naming
  guidelines.

* Sun Feb 24 2013 Stephen Gordon <sgordon@redhat.com> 0-0.2-20130224git0843039
- Updated file names to match upstream:
  s/license/LICENSE/
  s/author.txt/AUTHOR/
- Added required build dependencies (gzip, pod2man) to build manual page.
- Added build and install of manual page.

* Sat Feb 23 2013 Stephen Gordon <sgordon@redhat.com> 0-0.1-20130223gitaa77a89
- Initial package submission.
