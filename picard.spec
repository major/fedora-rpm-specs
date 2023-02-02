%global forgeurl    https://github.com/musicbrainz/picard/
%global commit      4c1bd2f5e986cf166aaf0a8c4658b9f92fe08d3b

Name:           picard
Version:        2.8.5
Summary:        MusicBrainz-based audio tagger
License:        GPL-2.0-or-later
Release:        3%{?dist}

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        picard.rpmlintrc
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       hicolor-icon-theme
Requires:       python3-qt5
Requires:       python3-qt5-webkit
Requires:       python3-dateutil
Requires:       python3-libdiscid
Requires:       python3-mutagen >= 1.37
Requires:       python3-markdown
Requires:       qt5-qtmultimedia

%if 0%{?rhel}
ExcludeArch:    ppc64
%endif

%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%forgesetup
%autosetup -n %{archivename}

%build
%{__python3} setup.py config
%py3_build

%install
%py3_install

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%{buildroot}%{_datadir}/applications      \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name}
%find_lang %{name}-attributes
%find_lang %{name}-countries

%check

%files -f %{name}.lang -f %{name}-attributes.lang -f %{name}-countries.lang
%doc AUTHORS.txt
%license COPYING.txt
%{_bindir}/picard
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python3_sitearch}/*egg-info
%{python3_sitearch}/picard/

%changelog
* Tue Jan 31 2023 Gerald Cox <gbcox@member.fsf.org> - 2.8.5-3
- Update for SPDX

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.5-1
- Upstream release - rhbz#2151167

* Tue Nov 22 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.4-1
- Upstream release - rhbz#2144889

* Wed Aug 17 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.3-1
- Upstream release - rhbz#2119178

* Thu Jul 07 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.2-1
- Upstream release - rhbz#2104856

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.1-2
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.1-1
- Upstream release - rhbz#2094299

* Tue May 24 2022 Gerald Cox <gbcox@member.fsf.org> - 2.8.0-1
- Upstream release - rhbz#2081460

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Gerald Cox <gbcox@member.fsf.org> - 2.7.2-1
- Upstream release - rhbz#2039384

* Tue Dec 21 2021 Gerald Cox <gbcox@member.fsf.org> - 2.7.1-1
- Upstream release - rhbz#2034620

* Fri Dec 17 2021 Gerald Cox <gbcox@member.fsf.org> - 2.7.0-3
- F36 needs pyyaml => 6 - rhbz#2033701

* Fri Dec 17 2021 Gerald Cox <gbcox@member.fsf.org> - 2.7.0-2
- F36 needs pyyaml => 6 - rhbz#2033701

* Thu Dec 16 2021 Gerald Cox <gbcox@member.fsf.org> - 2.7.0-1
- Upstream release - rhbz#2033412

* Thu Sep 30 2021 Gerald Cox <gbcox@member.fsf.org> - 2.6.4-1
- Python 3.10 - rhbz#2001976

* Thu Sep 30 2021 Gerald Cox <gbcox@member.fsf.org> - 2.6.3-4
- Python 3.10 - rhbz#2001976

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 2.6.3-2
- Rebuilt for Python 3.10

* Mon Jun 07 2021 Gerald Cox <gbcox@member.fsf.org> - 2.6.3-1
- Upstream release rhbz#1968403

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.2-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Gerald Cox <gbcox@member.fsf.org> - 2.6.2-1
- Upstream release rhbz#1954013

* Thu Apr 15 2021 Gerald Cox <gbcox@member.fsf.org> - 2.6.1-1
- Upstream release rhbz#1949946

* Tue Mar 30 2021 Gerald Cox <gbcox@fedoraproject.org> - 2.6.0-1
- Upstream release rhbz#1944898

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Gerald Cox <gbcox@fedoraproject.org> - 2.5.6-2
- Update dependencies rhbz#1915526

* Tue Jan 05 2021 Gerald Cox <gbcox@fedoraproject.org> - 2.5.6-1
- Upstream release rhbz#1912918

* Thu Dec 17 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.5.5-1.git7e4c106
- Upstream release rhbz#1907943

* Tue Dec 15 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.5.4-1.gitcdb5808
- Upstream release rhbz#1907943

* Sun Nov 15 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.5.2-1.gitb8fc83b
- Upstream release rhbz#1897951

* Wed Oct 28 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.5.1-1.git6cab6ad
- Upstream release rhbz#1892486

* Thu Oct 22 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.5.0-1.git869dbd5
- Upstream release rhbz#1890694

* Mon Oct 05 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.4.4-2.git559126e
- BuildRequire python3-setuptools explicitly

* Fri Sep 04 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.4.4-1.git559126e
- Upstream release rhbz#1875866

* Tue Aug 18 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.4.2-1.git6d76533
- Upstream release rhbz#1869555

* Tue Aug 11 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.4.1-1.git9abd145
- Upstream release rhbz#1867989

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.9

* Wed May 06 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.3.2-1.git3881261
- Upstream release rhbz#1832338

* Fri Feb 28 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.3.1-1.gitdd5be66
- Upstream release rhbz#1808127

* Tue Feb 18 2020 Gerald Cox <gbcox@fedoraproject.org> - 2.3.0-1.git3de8ee4
- Upstream release rhbz#1803981

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.3-1
- Upstream release rhbz#1769394

* Tue Oct 08 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.2-1
- Upstream release rhbz#1759614

* Wed Oct 02 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.1-3.gita4fff06
- Plugin causes crash rhbz#1756626

* Wed Oct 02 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.1-2.gita4fff06
- Upstream release rhbz#1753956

* Fri Sep 20 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.1-1
- Upstream release rhbz#1753956

* Sun Sep 15 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.2.0-1
- Upstream release rhbz#1752247

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.3-1
- Upstream release rhbz#1685280

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.2-1
- Upstream release rhbz#1670378

* Tue Jan 29 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.1-1
- Upstream release rhbz#1670378

* Sun Jan 20 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.0-1
- Upstream release rhbz#1662328
- Incorporate Justin W. Flory <jflory7@fedoraproject.org>
- modifications

* Thu Oct 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-2
- Require python3-qt5 instead of python2-qt5

* Tue Oct 16 2018 Gerald Cox <gbcox@fedoraproject.org> - 2.0.4-1
- Upstream release rhbz#1603193

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.4.2-5
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Oliver Haessler <oliver@redhat.com> - 1.4.2-3
- Exclude arch ppc64 in EPEL, as we are missing the python-mutagen rpm for ppc64

* Tue Jul 03 2018 Oliver Haessler <oliver@redhat.com> - 1.4.2-2
- corrected Source url to ftp:// as otherwise we get a 404 error

* Mon Jul 02 2018 Tim Jackson <rpm@timj.co.uk> - 1.4.2-1
- Update to 1.4.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-5
- Requires: PyQt4-webkit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 1.3.2-2
- Require python-libdiscid instead of libdiscid

* Tue Feb 03 2015 Christopher Meng <rpm@cicku.me> - 1.3.2-1
- Update to 1.3.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr  7 2013 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2-1
- Update to latest upstream (1.2)
- Remove cover art plugin, now in core package

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-3
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.1-1
- Update to upstream 1.1 (#854142)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun  4 2012  Alex Lancaster <alexlan[AT]fedoraproject org> - 1.0-1
- Update to latest upstream 1.0 (#827880)
- Use versions of plugins now distributed in contrib/plugins
- Update BR for PyQt >= 4.6 (#757398)
- Drop obsolete conditional in %%files (#757234)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.16-1
- Update to 0.16
- Update plugins, add titlesort, titleversion plugins.

* Sun Aug 21 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.15.1-1
- Update to 0.15.1
- Add more plugins

* Mon May 30 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.15-0.1.beta1
- Update to 0.15beta1 (#683055)
- Convert plugin files to files in git, easier to manage
- Only use plugins certified to be API compatible with 0.15 from
  http://users.musicbrainz.org/~luks/picard-plugins/

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Nov  3 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.12.1-1
- Update to upstream 0.12.1 (brown bag fix release)

* Tue Oct 27 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.12-1
- Update to 0.12 (#531224)
- Icons now in icons/hicolor directory

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.11-2
- Fixed sources.

* Tue Dec  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.11-1
- Update to latest upstream (0.11)
- Drop upstreamed patch
- Remove sed-ing of .desktop file

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10-3
- Rebuild for Python 2.6

* Tue Sep  2 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.10-2
- Update plugin versions to 0.10 where possible.  
- Temporarily disable the search plugins until they are ported to new API.

* Sun Aug 31 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.10-1
- Update to latest upstream (0.10).
- Add patch to work around broken setup.py.
- Fixed some spec file errors: duplicate sources.

* Sat Feb  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.9.0-6
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Wed Dec 19 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-5
- Add support for python eggs for F9+

* Wed Dec 19 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-4
- Update to proper release: 0.9.0
- Drop plugins directory patch, applied upstream

* Tue Dec 04 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.6.beta1
- strip out png extension from .desktop file

* Tue Dec 04 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.5.beta1
- Add plugins from http://musicbrainz.org/doc/PicardQt/Plugins
- Patch to find proper plugins directory (filed upstream:
  http://bugs.musicbrainz.org/ticket/3430)
- Does not depend on python-musicbrainz2 any longer, uses libdiscid directly 

* Wed Nov 14 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.4.beta1
- Various minor spec file cleanups to make sure timestamps stay correct

* Wed Nov 14 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.3.beta1
- Create pixmaps directory

* Wed Nov 14 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.2.beta1
- Missing BR: python-devel
- Use sitearch to make sure x86_64 builds work
- Install icons share/pixmaps/, rather than share/icons/

* Wed Nov 14 2007 Alex Lancaster <alexlan@fedoraproject.org> 0.9.0-0.1.beta1
- Initial packaging
