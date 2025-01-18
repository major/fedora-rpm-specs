%global srcname fedfind

Name:           fedfind
Version:        6.0.4
Release:        2%{?dist}
Summary:        Fedora compose and image finder

License:        GPL-3.0-or-later
URL:            https://pagure.io/fedora-qa/fedfind
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python%{python3_pkgversion}-fedfind

%description
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind package provides a simple CLI for showing
image URLs.

%package -n python%{python3_pkgversion}-fedfind
Summary:        Fedora Finder finds Fedora (using Python 3)
%{?python_provide:%python_provide python%{python3_pkgversion}-fedfind}

%description -n python%{python3_pkgversion}-fedfind
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind library provides a handy interface for
interacting with Fedora composes and discovering various properties of
them, along with some miscellaneous helper functions. This is the
Python 3 library package.


%prep
%autosetup -n %{srcname}-%{version} -p1
# setuptools-scm is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/fedfind

%files -n python%{python3_pkgversion}-fedfind
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/%{srcname}*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Adam Williamson <awilliam@redhat.com> - 6.0.4-1
- New release 6.0.4: add several new subvariants to const

* Wed Sep 18 2024 Adam Williamson <awilliam@redhat.com> - 6.0.3-1
- New release 6.0.3: extend EPEL compose filtering

* Fri Sep 13 2024 Adam Williamson <awilliam@redhat.com> - 6.0.2-1
- New release 6.0.2: fix paths and respin handling for ELN

* Wed Sep 04 2024 Adam Williamson <awilliam@redhat.com> - 6.0.1-1
- New release 6.0.1: change ELN release to "eln" from "ELN"

* Fri Aug 30 2024 Adam Williamson <awilliam@redhat.com> - 6.0.0-1
- New release 6.0.0: handle PDC retirement, support new ELN composes

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 5.3.0-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.3.0-2
- Rebuilt for Python 3.13

* Thu May 30 2024 Adam Williamson <awilliam@redhat.com> - 5.3.0-1
- New release 5.3.0: FEDFIND_NO_CACHE env var to disable disk cache

* Thu May 16 2024 Adam Williamson <awilliam@redhat.com> - 5.2.0-1
- New release 5.2.0: updates composes are back, added eol and relnum

* Mon Apr 29 2024 Adam Williamson <awilliam@redhat.com> - 5.1.4-1
- New release 5.1.4: handle a few new subvariants

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Adam Williamson <awilliam@redhat.com> - 5.1.3-1
- New release 5.1.3: adjust for a Python 3.12 deprecation

* Thu Aug 31 2023 Adam Williamson <awilliam@redhat.com> - 5.1.2-1
- New release 5.1.2: handle composes with no images.json

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Adam Williamson <awilliam@redhat.com> - 5.1.1-2
- Rebuilt for Python 3.12

* Tue Jun 20 2023 Adam Williamson <awilliam@redhat.com> - 5.1.1-1
- New release 5.1.1: don't find ELN by compose ID

* Mon Jun 19 2023 Adam Williamson <awilliam@redhat.com> - 5.1.0-1
- New release 5.1.0: support ELN composes

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Adam Williamson <awilliam@redhat.com> - 5.0.1-1
- New release 5.0.1: fix bogus respin release images

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Adam Williamson <awilliam@redhat.com> 5.0.0-1
- New release 5.0.0: remove old classes, fix https_url_generic

* Thu Dec 09 2021 Adam Williamson <awilliam@redhat.com> 4.4.5-1
- New release 4.4.5: minor fixes, updated known subvariants

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.4-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 24 2020 Adam Williamson <awilliam@redhat.com> - 4.4.4-1
- New release 4.4.4: use bespoke release metadata instead of Bodhi

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Adam Williamson <awilliam@redhat.com> - 4.4.3-1
- New release 4.4.3: don't delete _pdccid property, just unset it

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Adam Williamson <awilliam@redhat.com> - 4.4.2-1
- New release 4.4.2: Fix get_current_release for new 'ELN' release

* Fri Feb 21 2020 Adam Williamson <awilliam@redhat.com> - 4.4.1-1
- New release 4.4.1: drop Python 2.6 support, update tests, use Bodhi not pkgdb
- Simplify spec by dropping EL 6 support (can't build on EL 6 now anyway)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Adam Williamson <awilliam@redhat.com> - 4.3.0-1
- New release 4.3.0: enhance metadata for composes without it
  + Retrieve metadata from PDC for older nightly and candidates
  + Retrieve image sizes from imagelist files for stable releases

* Tue Oct 01 2019 Adam Williamson <awilliam@redhat.com> - 4.2.8-1
- New release 4.2.8: expire collections cache after a day

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.7-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Adam Williamson <awilliam@redhat.com> - 4.2.7-1
- New release 4.2.7: fix 'version' for update composes

* Tue Jul 09 2019 Adam Williamson <awilliam@redhat.com> - 4.2.6-1
- New release 4.2.6: update the respin image regex, again

* Tue Jun 25 2019 Adam Williamson <awilliam@redhat.com> - 4.2.5-1
- New release 4.2.5:
  * Fix expected images for F30+ Branched / Rawhide nightlies too
  * Resurrect old previous_release due to PDC import bug

* Mon Jun 24 2019 Adam Williamson <awilliam@redhat.com> - 4.2.3-1
- New release 4.2.3: fix expected images for F30+ update composes

* Fri Mar 08 2019 Adam Williamson <awilliam@redhat.com> - 4.2.2-1
- New release 4.2.2: work correctly with productmd 1.20

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Adam Williamson <awilliam@redhat.com> - 4.2.1-1
- New release 4.2.1: make test suite work without Python 2
- Disable Python 2 build on F30+, EL8+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Adam Williamson <awilliam@redhat.com> - 4.2.0-1
- New release 4.2.0: support several new compose types

* Mon May 28 2018 Adam Williamson <awilliam@redhat.com> - 4.1.3-1
- New release 4.1.3: handle unexpected nightly compose move

* Mon May 21 2018 Adam Williamson <awilliam@redhat.com> - 4.1.2-1
- New release 4.1.2: fixes for live-respins releases

* Tue Mar 06 2018 Adam Williamson <awilliam@redhat.com> - 4.1.1-1
- New release 4.1.1: adjustments for Atomic compose variant renames

* Tue Feb 20 2018 Adam Williamson <awilliam@redhat.com> - 4.1.0-1
- New release 4.1.0: add `get_package_nevras_pdc`
- Update all Python 2 dependencies to 'python2-foo' format

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Adam Williamson <awilliam@redhat.com> - 4.0.0-1
- New release 4.0.0: multiple changes, see CHANGELOG

* Tue Nov 21 2017 Adam Williamson <awilliam@redhat.com> - 3.8.3-1
- New release 3.8.3: fix modular get_package_nvras harder

* Wed Nov 15 2017 Adam Williamson <awilliam@redhat.com> - 3.8.2-1
- New release 3.8.2: fix modular get_package_nvras and https_generic_url

* Tue Nov 14 2017 Adam Williamson <awilliam@redhat.com> - 3.8.1-1
- New release 3.8.1: get release info from pkgdb collections again

* Tue Nov 07 2017 Adam Williamson <awilliam@redhat.com> - 3.8.0-1
- New release 3.8.0: handle modular candidate composes

* Fri Oct 27 2017 Adam Williamson <awilliam@redhat.com> - 3.7.1-1
- New release 3.7.1: handle missing 'updates-testing' release type

* Fri Oct 27 2017 Adam Williamson <awilliam@redhat.com> - 3.7.0-1
- New release 3.7.0: new CID parser, update supported compose types

* Mon Oct 16 2017 Adam Williamson <awilliam@redhat.com> - 3.6.4-1
- New release 3.6.4: update CHANGELOG for 3.6.3 and 3.6.4

* Fri Oct 13 2017 Adam Williamson <awilliam@redhat.com> - 3.6.3-1
- New release 3.6.3: fix expected images for modular composes

* Mon Sep 11 2017 Adam Williamson <awilliam@redhat.com> - 3.6.2-1
- New release 3.6.2: fix PDC queries and update subvariant list

* Fri Aug 18 2017 Adam Williamson <awilliam@redhat.com> - 3.6.1-1
- New release 3.6.1: hard code 'current release' info for now

* Wed Aug 16 2017 Adam Williamson <awilliam@redhat.com> - 3.6.0-1
- New release 3.6.0: modular compose support

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 3.5.4-2
- Bump release as 3.5.4-1 for EPEL 7 got trashcanned

* Tue Apr 18 2017 Adam Williamson <awilliam@redhat.com> - 3.5.4-1
- New release 3.5.4: handle cache directory vanishing

* Thu Apr 06 2017 Adam Williamson <awilliam@redhat.com> - 3.5.3-1
- New release 3.5.3: Allow 'FACD' as a compose short name

* Sun Mar 26 2017 Adam Williamson <awilliam@redhat.com> - 3.5.2-1
- New release 3.5.2: add other secondary arch URLs to whitelist

* Sun Mar 26 2017 Adam Williamson <awilliam@redhat.com> - 3.5.1-1
- New release 3.5.1: add PPC compose URL to URL whitelist (RHBZ #1435953)

* Fri Feb 17 2017 Adam Williamson <awilliam@redhat.com> - 3.5.0-1
- New release 3.5.0: support for Cloud nightlies, PyPI as upstream

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 3.4.3-1
- New release 3.4.3: include `disc_number` in synthesized image dicts

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 3.4.1-2
- Enable Python 3 build for EPEL 7
- Split CLI and library packages
- Use Python 3 executable on distros where Python 3 build is enabled
- Drop the old fedfind3 provides/obsoletes, it's been long enough

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 3.4.1-1
- New release 3.4.1:
- * Include `composeinfo` dict in synthesized metadata
- * Don't return Pungi4Release for unknown URLs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Adam Williamson <awilliam@redhat.com> - 3.4.0-1
- new release 3.4.0: fix `RespinRelease` by URL, remove `release_number`

* Wed Jan 18 2017 Adam Williamson <awilliam@redhat.com> - 3.3.0-1
- new release 3.3.0:
- * Add `helpers.get_current_stables()` for finding current stable releases
- * Add `Release.release_number` for getting Rawhide compose release numbers
- * Add `url` and `direct_url` URL entries to image dicts

* Fri Jan 13 2017 Adam Williamson <awilliam@redhat.com> - 3.2.5-1
- new release 3.2.5: support Docker stable nightly composes

* Tue Jan 10 2017 Adam Williamson <awilliam@redhat.com> - 3.2.3-3
- Conditionalize argparse dependency since it disappeared from Rawhide

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 3.2.3-2
- rebuild for Python 3.6

* Wed Dec 14 2016 Adam Williamson <awilliam@redhat.com> - 3.2.3-1
- new release 3.2.3: support live-respins post-release live respin composes

* Mon Dec 05 2016 Adam Williamson <awilliam@redhat.com> - 3.1.3-2
- don't include python-argparse in Python 3 package requirements

* Wed Nov 30 2016 Adam Williamson <awilliam@redhat.com> - 3.1.3-1
- new release 3.1.3: fix some release number check problems (inc. a crash)

* Wed Nov 30 2016 Adam Williamson <awilliam@redhat.com> - 3.1.2-1
- new release 3.1.2: improve caching to handle non-writable home

* Tue Nov 29 2016 Adam Williamson <awilliam@redhat.com> - 3.1.1-1
- new release 3.1.1: original metadata for split composes, cache PDC queries

* Wed Nov 23 2016 Adam Williamson <awilliam@redhat.com> - 3.0.4-1
- new release 3.0.4: use `imagelist` files not rsync scraping

* Sun Nov 20 2016 Adam Williamson <awilliam@redhat.com> - 2.7.2-1
- new release 2.7.2: optionally provide distro in `parse_cid`

* Wed Nov 09 2016 Adam Williamson <awilliam@redhat.com> - 2.7.1-1
- new release 2.7.1: handle 'RC' composes correctly

* Mon Oct 10 2016 Adam Williamson <awilliam@redhat.com> - 2.7.0-1
- new release 2.7.0: more ostree stuff, handle 'alt' split

* Mon Oct 10 2016 Adam Williamson <awilliam@redhat.com> - 2.6.3-1
- new release 2.6.3: handle -ostree- as well as -dvd- in ostree filenames

* Thu Oct 06 2016 Adam Williamson <awilliam@redhat.com> - 2.6.2-1
- new release 2.6.2: use dvd-ostree type when synthesizing metadata

* Thu Oct 06 2016 Adam Williamson <awilliam@redhat.com> - 2.6.0-1
- new release 2.6.0: drop PostRelease class, tweak expected images

* Wed Oct 05 2016 Adam Williamson <awilliam@redhat.com> - 2.5.0-1
- new release 2.5.0: workaround a pungi metadata issue, add image identifier

* Fri Aug 26 2016 Adam Williamson <awilliam@redhat.com> - 2.4.11-1
- new release 2.4.11: cli exits cleanly if no complete compose found

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Adam Williamson <awilliam@redhat.com> - 2.4.10-1
- new release 2.4.10: support for Pungi 4 2 Week Atomic composes

* Mon May 30 2016 Adam Williamson <awilliam@redhat.com> - 2.4.9-1
- new release 2.4.9: helpers.parse_cid raises ValueError if cid is invalid

* Mon May 30 2016 Adam Williamson <awilliam@redhat.com> - 2.4.8-1
- new release 2.4.8: ensure Releases always have a `label`

* Wed May 04 2016 Adam Williamson <awilliam@redhat.com> - 2.4.7-1
- new release 2.4.7 (remove a stray debug print)

* Thu Apr 28 2016 Adam Williamson <awilliam@redhat.com> - 2.4.6-1
- new release 2.4.6 (handle 2-week Atomic CIDs in get_release)

* Thu Apr 14 2016 Adam Williamson <awilliam@redhat.com> - 2.4.5-1
- new release 2.4.5 (allow ignoring arch for helpers.get_weight)

* Sun Apr 10 2016 Adam Williamson <awilliam@redhat.com> - 2.4.4-1
- new release 2.4.4 (couple of fixes/improvements for fedora_nightlies)

* Wed Mar 30 2016 Adam Williamson <awilliam@redhat.com> - 2.4.3-1
- new release 2.4.3 (re-add milestone release support)

* Wed Mar 30 2016 Adam Williamson <awilliam@redhat.com> - 2.4.2-1
- new release 2.4.2 (temp get_package_nvras workaround for PDC problem)

* Mon Mar 21 2016 Adam Williamson <awilliam@redhat.com> - 2.4.1-1
- new release 2.4.1 (CLI search by cid / label, get_package_nvras)
- enable tests

* Thu Mar 17 2016 Adam Williamson <awilliam@redhat.com> - 2.3.0-1
- new release 2.3.0 (drop 'payload', support candidates synced to alt)

* Thu Mar 17 2016 Adam Williamson <awilliam@redhat.com> - 2.2.3-1
- new release 2.2.3 (fix a get_release bug which broke check-compose)

* Wed Mar 16 2016 Adam Williamson <awilliam@redhat.com> - 2.2.2-1
- new release 2.2.2 (fix get_size for Python 3)
    
* Wed Mar 16 2016 Adam Williamson <awilliam@redhat.com> - 2.2.1-1
- new release 2.2.1 (quite big changes to Pungi 4 compose handling)

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 2.1.1-1
- new release 2.1.1 (fix check_expected)

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 2.1.0-2
- version the python2-fedfind and python-fedfind provides

* Wed Mar 02 2016 Adam Williamson <awilliam@redhat.com> - 2.1.0-1
- new release 2.1.0 (various bugfixes)
- twiddle description a bit

* Mon Feb 29 2016 Adam Williamson <awilliam@redhat.com> - 2.0.0-1
- new release 2.0.0 (major rewrite for Pungi 4)
- add productmd requirement

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 02 2015 Adam Williamson <awilliam@redhat.com> - 1.6.2-1
- new release 1.6.2: adjust for new Postrelease nightly location

* Tue Sep 29 2015 Adam Williamson <awilliam@redhat.com> - 1.6.1-1
- new release 1.6.1: behind the scenes stuff, docs changes

* Sat Sep 19 2015 Adam Williamson <awilliam@redhat.com> - 1.6-1
- new release 1.6: image tweaks, post-release daily handling

* Thu Sep 03 2015 Adam Williamson <awilliam@redhat.com> - 1.5.1-1
- new release 1.5.1: image 'size' property, more image parsing tweaks

* Thu Aug 27 2015 Adam Williamson <awilliam@redhat.com> - 1.5-1
- new release 1.5: rsync retries, release wait, tests, expected image changes

* Fri Aug 21 2015 Adam Williamson <awilliam@redhat.com> - 1.4.2-1
- new release 1.4.2: py3 fix

* Fri Aug 21 2015 Adam Williamson <awilliam@redhat.com> - 1.4.1-1
- new release 1.4.1: branched guessing, rsync cleanups, bugfixes

* Thu Aug 20 2015 Adam Williamson <awilliam@redhat.com> - 1.4-1
- new release 1.4: use multicall instead of multiprocess, improve caching

* Thu Aug 20 2015 Adam Williamson <awilliam@redhat.com> - 1.3-1
- new release 1.3: check compose status, image parsing improvements, speedups

* Thu Jul 23 2015 Adam Williamson <awilliam@redhat.com> - 1.2-1
- new release 1.2: proper logging, some small fixes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Adam Williamson <awilliam@redhat.com> - 1.1.5-1
- new release: add a 'generic URL' output, allow --milestone Branched/Rawhide

* Thu Apr 23 2015 Adam Williamson <awilliam@redhat.com> - 1.1.4-1
- new release: drop shebangs from non-exec files, fix them in exec files
- rename 'fedfind3' to 'python3-fedfind'
- drop the executables from the python3 package (not really needed)

* Thu Apr 16 2015 Adam Williamson <awilliam@redhat.com> - 1.1.3-1
- new release: drop bundled cached_property

* Tue Mar 10 2015 Adam Williamson <awilliam@redhat.com> - 1.1.2-1
- new release: fix path for milestone releases

* Thu Feb 26 2015 Adam Williamson <awilliam@redhat.com> - 1.1.1-1
- 1.1.1: handle a python3 argparse bug causing a crash when no subcmd given

* Thu Feb 26 2015 Adam Williamson <awilliam@redhat.com> - 1.1.0-1
- new release 1.1.0: cleaner URL pref implementation, Python 3 support
- add a fedfind3 package for Python 3

* Wed Feb 25 2015 Adam Williamson <awilliam@redhat.com> - 1.0.8-1
- 1.0.8: use dl.fp.o not download.fp.o URLs for TC/RC images

* Wed Feb 25 2015 Adam Williamson <awilliam@redhat.com> - 1.0.7-1
- 1.0.7: fix a bug in finding nightly images by type

* Wed Feb 18 2015 Adam Williamson <awilliam@redhat.com> - 1.0.6-1
- consolidate image versioning with python-wikitcms/relval, bugfixes

* Thu Feb 12 2015 Adam Williamson <awilliam@redhat.com> - 1.0.5-1
- new release 1.0.5: image detection bugfixes, no koji dep, cleanups

* Mon Feb 09 2015 Adam Williamson <awilliam@redhat.com> - 1.0.4-1
- new release 1.0.4: fix EL 6 compat

* Mon Feb 09 2015 Adam Williamson <awilliam@redhat.com> - 1.0.3-1
- new release 1.0.3: bugfixes, Python 2.6 / RHEL 6 compatibility

* Fri Feb 06 2015 Adam Williamson <awilliam@redhat.com> - 1.0.2-1
- new release 1.0.2: misc. bugfixes and CLI reorg

* Fri Feb 06 2015 Adam Williamson <awilliam@redhat.com> - 1.0.1-1
- add ppc to arches

* Thu Feb 05 2015 Adam Williamson <awilliam@redhat.com> - 1.0-1
- first package build of fedfind
