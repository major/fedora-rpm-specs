Name:           beets
Version:        2.0.0
Release:        2%{?dist}
Summary:        Music library manager and MusicBrainz tagger
License:        MIT and ISC
URL:            http://beets.io
Source0:        https://github.com/beetbox/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pydata-sphinx-theme
BuildRequires:  python3-PyYAML
BuildRequires:  python3-mediafile
BuildRequires:  python3-musicbrainzngs >= 0.4
BuildRequires:  python3-jellyfish
BuildRequires:  python3-munkres
BuildRequires:  python3-mutagen >= 1.23
BuildRequires:  python3-unidecode
BuildRequires:  python3-rarfile
# Tests
BuildRequires:  python3-jellyfish
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  make
BuildArch:      noarch

Requires:       python3 >= 3.8
Requires:       python3-confuse
Requires:       python3-jellyfish
Requires:       python3-mediafile >= 0.12.0
Requires:       python3-munkres >= 1.0.0
Requires:       python3-musicbrainzngs >= 0.4
Requires:       python3-mutagen >= 1.23
Requires:       python3-unidecode
Requires:       python3-rarfile
Requires:       python3-PyYAML

%description
The purpose of beets is to get your music collection right once and for all. It
catalogs your collection, automatically improving its meta-data as it goes using
the MusicBrainz database. Then it provides a bouquet of tools for manipulating
and accessing your music.
Because beets is designed as a library, it can do almost anything you can
imagine for your music collection. Via plugins, beets becomes a panacea:
- Fetch or calculate all the meta-data you could possibly need: album art,
  lyrics, genres, tempos, ReplayGain levels, or acoustic fingerprints.
- Get meta-data from MusicBrainz, Discogs, or Beatport. Or guess meta-data using
  songs' file names or their acoustic fingerprints.
- Transcode audio to any format you like.
- Check your library for duplicate tracks and albums or for albums that are
  missing tracks.
- Browse your music library graphically through a Web browser and play it in
  any browser that supports HTML5 Audio.

%package plugins
Summary:        Plugins for beets
Requires:       beets == %{version}-%{release}
# bpd/
Requires:       python3-gstreamer1
# chroma
Requires:       python3-acoustid
# fetchart, beatport, lastimport, spotify
Requires:       python3-requests
# lastgenre/
Requires:       python3-pylast
# autotag, mbcollection
Requires:       python3-musicbrainzngs >= 0.4
# mpdstats
Requires:       python3-mpd
# replaygain (GStreamer backend)
Requires:       python3-gobject >= 3.0
Requires:       gstreamer1

Requires:	    js-jquery
Requires:	    js-backbone
Requires:	    js-underscore
Requires:	    python3-flask

%description plugins
Contains a number of plugins to improve meta-data, format paths,
inter-operability aids and so on.

%package doc
Summary:        Documentation for beets

%description doc
The beets-doc package provides useful information on the
beets Music Library Manager. Documentation is shipped in
both text and html formats.

%prep
# Tarball has wrong basedir https://github.com/beetbox/beets/issues/5284
%autosetup -p1 -n beets-1.6.1

%build
%{__python3} setup.py build
pushd docs
# Not using {smp_flags} as sphinx fails with it from time to time
make SPHINXBUILD=sphinx-build-3 man html text
popd

%check
# Currently disabled as it is forcing the download of pypi modules
# even when they are installed. Will require python-rarfile and discocg if
# enabled
# skip tests that broken
#mv test/test_replaygain.py test/broken_replaygain.py
# https://github.com/beetbox/beets/issues/2400
#mv test/test_ui.py test/broken_ui.py
#%{__python3} setup.py test

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man5
%{__install} -p -m 0644 docs/_build/man/beet.1 $RPM_BUILD_ROOT%{_mandir}/man1
%{__install} -p -m 0644 docs/_build/man/beetsconfig.5 $RPM_BUILD_ROOT%{_mandir}/man5
# Remove extra copy of text docs
rm -rf docs/_build/html/_sources
rm -f docs/_build/html/{.buildinfo,objects.inv}

%files
%doc LICENSE MANIFEST.in README.rst
%{_bindir}/beet
%{python3_sitelib}/beets/
%{python3_sitelib}/beets*egg-info/
%{_mandir}/*/*
%{python3_sitelib}/beetsplug/__init__.py*

%files plugins
# beetsplug/mbcollection.py is the plugin that has ISC license
%{python3_sitelib}/beetsplug/[a-zA-Z0-9]*
%{python3_sitelib}/beetsplug/__pycache__

%files doc
%doc docs/_build/html docs/_build/text

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 03 2024 Michele Baldessari <michele@acksyn.org> - 2.0.0-1
- New upstream

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.6.0-8
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Michele Baldessari <michele@acksyn.org> - 1.6.0-3
- Fix doc build with sphinx > 6.0.0 (rhbz#2180464)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Michele Baldessari <michele@acksyn.org> - 1.6.0-1
- New upstream
- Add python-mediafile as a new dependency

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.9-13
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.9-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Michele Baldessari <michele@acksyn.org> - 1.4.9-8
- Fix rhbz#1862737

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Michele Baldessari <michele@acksyn.org> - 1.4.9-1
- New upstream

* Fri May 17 2019 Michele Baldessari <michele@acksyn.org> - 1.4.8-1
- New upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Michele Baldessari <michele@acksyn.org> - 1.4.7-4
- Fix python3.7 incompatibility (rhbz#1653869)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.7-2
- Rebuilt for Python 3.7

* Wed May 30 2018 Michele Baldessari <michele@acksyn.org> - 1.4.7-1
- New upstream release

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.6-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 Michele Baldessari <michele@acksyn.org> - 1.4.6-2
- Fix up wrong changelog dates

* Fri Dec 22 2017 Michele Baldessari <michele@acksyn.org> - 1.4.6-1
- New upstream release

* Tue Oct 10 2017 Michele Baldessari <michele@acksyn.org> - 1.4.5-1
- New upstream release

* Mon Sep 11 2017 Michele Baldessari <michele@acksyn.org> - 1.4.4-1
- New upstream release

* Sun Aug 13 2017 Michele Baldessari <michele@acksyn.org> - 1.4.3-4
- Move to python3 by default

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Michele Baldessari <michele@acksyn.org> - 1.4.3-1
- New upstream release

* Sun Jan 01 2017 Michele Baldessari <michele@acksyn.org> - 1.4.2-2
- Enable all plugins (discogs, convert and echonest*) and let the user install
  any dependencies by hand or via other non official repos. RHBZ: #1409374

* Mon Dec 19 2016 Michele Baldessari <michele@acksyn.org> - 1.4.2-1
- New upstream release

* Wed Nov 30 2016 Michele Baldessari <michele@acksyn.org> - 1.4.1-1
- New upstream release

* Fri Aug 19 2016 Andrea Perotti <fedora@goodfellow.it> - 1.3.19-3
- Add web plugin as all js dependencies are in Fedora

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.19-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Michele Baldessari <michele@acksyn.org> - 1.3.19-1
- New upstream release

* Wed Jun 01 2016 Michele Baldessari <michele@acksyn.org> - 1.3.18-1
- New upstream release

* Mon Mar 14 2016 Michele Baldessari <michele@acksyn.org> - 1.3.17-4
- Bump release as bodhi is seeing an old build

* Mon Mar 14 2016 Michele Baldessari <michele@acksyn.org> - 1.3.17-3
- Fix up requires

* Mon Mar 14 2016 Michele Baldessari <michele@acksyn.org> - 1.3.17-2
- Add replaygain as it does support a gstreamer backend (BZ#1317212)

* Tue Feb 09 2016 Michele Baldessari <michele@acksyn.org> - 1.3.17-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Michele Baldessari <michele@acksyn.org> - 1.3.16-1
- New upstream release

* Thu Nov 26 2015 Michele Baldessari <michele@acksyn.org> - 1.3.15-1
- New upstream release

* Sun Aug 09 2015 Michele Baldessari <michele@acksyn.org> - 1.3.14-1
- New upstream release

* Sun Aug 09 2015 Michele Baldessari <michele@acksyn.org> - 1.3.13-4
- Move beetplugs/__init__.py to main packages (BZ#1246799)

* Thu Jul 02 2015 Michele Baldessari <michele@acksyn.org> - 1.3.13-3
- Add brainzngs req as the main program checks for its presence BZ#1236315

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Michele Baldessari <michele@acksyn.org> - 1.3.13-1
- New upstream release (needs additional python-jellyfish dep)

* Wed Apr 08 2015 Michele Baldessari <michele@acksyn.org> - 1.3.11-1
- New upstream release (makes python 2.7 a requirement)
- python-enum34 >= 1.0.4 is now a Requires (RHBZ 1210053)

* Mon Mar 23 2015 Michele Baldessari <michele@acksyn.org> - 1.3.10-4
- Add python-munkres dep (needs RHBZ 1202146 fixed)

* Thu Mar 19 2015 Michele Baldessari <michele@acksyn.org> - 1.3.10-3
- Use python2 macros in preparation of the python3 migration
- Add ISC license for beetsplugs/mbcollection.py
- Add owner for dirs beets-*.egg-info, beetsplug, beets

* Tue Jan 27 2015 Michele Baldessari <michele@acksyn.org> - 1.3.10-2
- Add html and text documentation in a separate -doc package
- Add a comment why we do not use %%{?_smp_mflags}

* Tue Jan 27 2015 Michele Baldessari <michele@acksyn.org> - 1.3.10-1
- New upstream

* Thu Dec 25 2014 Michele Baldessari <michele@acksyn.org> - 1.3.9-2
- Split off plugins into a separate package with additional Requires: added
- Disable a few plugins due to missing deps in Fedora

* Mon Dec 15 2014 Michele Baldessari <michele@acksyn.org> - 1.3.9-1
- Initial release
