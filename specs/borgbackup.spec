%global srcname borgbackup

Name:           %{srcname}
Version:        1.4.0
Release:        3%{?dist}
Summary:        A deduplicating backup program with compression and authenticated encryption
# zlib:         src/borg/algorithms/{crc32_clmul.c, crc32_slice_by_8.c}
# Apache-2.0:   src/borg/cache_sync/{sysdep.h, unpack.h, unpack_template.h, unpack_define.h}
# PSF-2.0:      src/borg/shellpattern.py
License:        BSD-3-clause AND zlib AND Apache-2.0 AND PSF-2.0

URL:            https://borgbackup.readthedocs.org
Source0:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz
Source1:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz.asc
# upstream publishes only key ids:
#    https://borgbackup.readthedocs.io/en/stable/support.html#verifying-signed-releases
# gpg2 --export --export-options export-minimal "6D5B EF9A DD20 7580 5747 B70F 9F88 FB52 FAF7 B393" > gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg
Source2:        gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg

# we don't need the guzzley_sphinx theme for only man page generation
Patch1:         0002-disable-sphinx-man-page-build.patch

BuildRequires:  gnupg2
# build
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pkgconfig

# test
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

# doc
BuildRequires:  python3-sphinx

# no python deps
BuildRequires:  gcc
BuildRequires:  openssl-devel >= 1.0.2
BuildRequires:  fuse-devel
BuildRequires:  make
BuildRequires:  libacl-devel
# versions required in "setup_checksums.py"
BuildRequires:  lz4-devel >= 1.7.0
BuildRequires:  libzstd-devel >= 1.3.0
BuildRequires:  xxhash-devel >= 0.7.3

# msgpack dependency is detected automatically
Requires:       python3-llfuse >= 1.3.8
Requires:       fuse

%description
BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm -rf %{srcname}.egg-info

# remove copies of bundled libraries to ensure these don't end up in our
# binaries
rm -rf src/borg/algorithms/{lz4,xxh64,zstd}
# remove precompiled Cython code to ensure we always built "from source"
find src/ -name '*.pyx' | sed -e 's/.pyx/.c/g' | xargs rm -f

# https://bugzilla.redhat.com/show_bug.cgi?id=1630992
sed -i 's/msgpack-python/msgpack/' setup.py

%generate_buildrequires
%pyproject_buildrequires -x fuse


%build
%pyproject_wheel

# MANPAGE GENERATION
# workaround to dump sphinx_rtd_theme dependency - not needed for manpages
export READTHEDOCS=True

# workaround to include borg module for usage generation
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

make -C docs SPHINXBUILD=sphinx-build-%python3_version man


%install
find . -name *.so -type f -exec chmod 0755 {} \;

%pyproject_install
install -D -m 0644 docs/_build/man/borg*.1* %{buildroot}%{_mandir}/man1/borg.1

# add shell completions
#%define bash_compdir %(pkg-config --variable=completionsdir bash-completion)
%define bash_compdir %{_prefix}/share/bash-completion/completions
%define zsh_compdir %{_prefix}/share/zsh/site-functions
%define fish_compdir %{_prefix}/share/fish/completions

install -d  %{buildroot}%{bash_compdir}
install -d  %{buildroot}%{zsh_compdir}
install -d  %{buildroot}%{fish_compdir}

install -D -m 0644 scripts/shell_completions/bash/* %{buildroot}%{bash_compdir}
install -D -m 0644 scripts/shell_completions/zsh/* %{buildroot}%{zsh_compdir}
install -D -m 0644 scripts/shell_completions/fish/* %{buildroot}%{fish_compdir}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}

cd $PYTHONPATH
# exclude test_fuse: there is no modprobe in mock for fuse
# test_readonly_mount: needs fuse mount
# exclude benchmark: not relevant for package build
TEST_SELECTOR="not test_fuse and not test_readonly_mount and not benchmark"
%pytest -n auto -x -vk "$TEST_SELECTOR" borg/testsuite/*.py


%files
%license LICENSE
%doc README.rst AUTHORS
%doc docs/changes.rst
%{_mandir}/man1/*

%{python3_sitearch}/borg
%{python3_sitearch}/borgbackup-%{version}.dist-info
# - files in %%{python3_sitearch}/borg/algorithms/msgpack are licensed under the ASL
# - %%{python3_sitearch}/borg/algorithms/checksums.*.so contains code licensed
#   under the zlib license
%{_bindir}/borg
%{_bindir}/borgfs
%{_prefix}/share/bash-completion/completions/*
%{_prefix}/share/zsh/site-functions/*
%{_prefix}/share/fish/completions/*
# left-overs from testing
%exclude %{python3_sitearch}/.pytest_cache


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.8-2
- Rebuilt for Python 3.13

* Mon Apr 01 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.8-1
- update to 1.2.8

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 10 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.7-1
- update to 1.2.7

* Sun Nov 05 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.6-3
- add unistd.h explicitely for compatibility with Python 3.13

* Sun Oct 01 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.6-2
- also accept msgpack 1.0.7

* Tue Sep 05 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.6-1
- update to 1.2.6 to fix CVE-2023-36811

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.4-4
- add patch for Python 3.12 compatibility

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.4-3
- Rebuilt for Python 3.12

* Sun May 14 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.4-2
- SPDX migration
- rely on auto-generated version requirement for msgpack

* Fri Mar 24 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Sun Aug 21 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Mon Feb 21 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.17-2
- Rebuilt with OpenSSL 3.0.0

* Sun Jul 25 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.17-1
- update to 1.1.17

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.16-3
- add patch for Sphinx 4 compatibility

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.16-2
- Rebuilt for Python 3.10

* Tue Mar 23 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.16-1
- update to 1.1.16

* Wed Feb 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.15-3
- fix building with Python 3.10 (#1927146)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.15-1
- update to 1.1.15

* Thu Oct 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.14-1
- update to 1.1.14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.13-1
- update to 1.1.13

* Thu Jun 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.11-3
- add patch to prevent sporadic test failures (see F31 rebuild attempts)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.11-2
- Rebuilt for Python 3.9

* Sun Mar 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.11-1
- update to 1.1.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-6
- enable GPG source file verification

* Mon Sep 23 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-5
- Rebuilt for libb2 0.98.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.10-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-2
- declare bundled xxhash correctly and adapt license tag accordingly
- bundle python3-msgpack only when necessary (Fedora 30+)
- fine-grained test exclusion to run as many tests as possible

* Thu May 16 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-1
- Upstream Release 1.1.10

* Thu May 09 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.9-3
- bundle msgpack 0.5.6 (rhbz 1669083)

* Sun Mar 10 2019 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.9-2
- drop python2-sphinx dependency

* Sat Mar 09 2019 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.9-1
- Upstream Release 1.1.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.8-1
- Upstream Release 1.1.8

* Sun Sep 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-2
- Fix entrypoint broken by the msgpack rename (#1630992)

* Mon Sep 03 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.7-1
- Upstream Release 1.1.7
- Rawhide compliant

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-3
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.5-2
- require python-msgpack >= 0.5.6 (see GH#3753)

* Tue Apr 10 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.5-1
- upstream version 1.1.5 (see upstream changelog)
- require python-msgpack < 0.5.0
- patch0 not needed anymore - fixed upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 1 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.4-2
- add testsuite, needed for selftest

* Mon Jan 1 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.4-1
- upstream version 1.1.4 (see upstream changelog)
- added zstd compression
- removed patch for borg check --repair malfunction
- remove testsuite from package

* Sun Dec 17 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.3-2
- fix borg check --repair malfunction (upstream pull #3444)

* Tue Nov 28 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.3-1
- upstream version 1.1.3
- fixes CVE-2017-15914 (BZ#1517664)

* Tue Nov 07 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.2-1
- upstream version 1.1.2
- added shell completions

* Wed Nov 01 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.1-1
- upstream version 1.1.1

* Mon Oct 09 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.0-1
- upstream version 1.1.0 (BZ#1499512)
- added missing fuse dependency (BZ#1493434)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.11-3
- removed sphinx_rtd_theme dependency

* Sat Jul 29 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.11-1
- upstream version 1.0.11 (BZ#1473897)
- removed setup.py build_api

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.10-1
- upstream version 1.0.10 (BZ#1421660)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.9-1
- upstream version 1.0.9 (BZ#1406277)
- fix manifest spoofing vulnerability - see docs for info

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-3
- Rebuild for Python 3.6

* Mon Oct 31 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.8-2
- upstream version 1.0.8 (BZ#1389986)

* Sun Aug 21 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.7-1
- security fix with borg serve and restrict-to-path (BZ#1354371)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.6-1
- upstream version 1.0.6 (BZ#1354371)
- update source url (now pointing to files.pythonhosted.org)
- testsuite on XFS is patched upstream

* Fri Jul 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.3-2
- Fix testsuite on XFS (#1331820)

* Sun May 22 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.3-1
- Added requires for setuptools (BZ#1335325)
- upstream version 1.0.3

* Thu Apr 28 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-2
- rebuilt

* Thu Apr 28 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-2
- Missing dependency python-setuptools

* Sun Apr 17 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-1
- added epel7 specific parts
- make manpage generation work with epel7
- upstream version 1.0.2

* Sat Apr 16 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.1-2
- simplified specfile
- removed unneeded dependencies: python3-mock, python3-pytest-cov

* Sun Apr 10 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.1-1
- Upstream version 1.0.1. see changelog

* Thu Apr 07 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.0-2
- Added requires for python3-llfuse (#1324685)
- Added minversion for openssl

* Mon Apr 04 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.0-1
- Upstream version 1.0.0
- Rewrote build requirements for EPEL7

* Thu Dec 17 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-3
- Specified correct project URL
- Added Buildrequires python3-sphinx_rtd_theme for f23

* Thu Dec 17 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-2
- Cleanup Spec
- Rename package to borgbackup
 
* Mon Dec 14 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-1
- New Upstream Version
- Added manpage from Upstream
- Testsuite now functional without benchmark

* Sat Dec 05 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-6
- Added correct testsuite to check
- Removed unnessesary statements

* Fri Dec 04 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-5
- Renamed Specfile to python3 only and remove pre-built egg-info

* Wed Dec 02 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-4
- Removed double package statement and sum macro

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-3
- Added dependency python3-msgpack to buildrequires

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-2
- Added dependency python3-msgpack

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-1
- Initial Packaging for the BorgBackup Project

