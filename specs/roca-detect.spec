# Fedora review: https://bugzilla.redhat.com/show_bug.cgi?id=1503915

%if 0%{?rhel} == 7
%global __python %{__python2}
%global python python
%else
%global __python %{__python3}
%global python python3
%endif

%if 0%{?fedora} >= 30 || 0%{?rhel} > 7
%global bundle_pgpdump 1
%else
%global bundle_pgpdump 0
%endif

# Use symlinks instead of the EASY entry scripts
%bcond_with symlinks

Summary:	Key fingerprinting tools for CVE-2017-15361
Name:		roca-detect
Version:	1.2.12
Release:	29%{?dist}
License:	MIT
Url:		https://crocs.fi.muni.cz/public/papers/rsa_ccs17
Source0:	https://github.com/crocs-muni/roca/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://files.pythonhosted.org/packages/4d/ad/11339cf197a6b128a9b06725681a349f61a5dc778e1fe3b69e816a2d175b/pgpdump3-1.5.2.tar.gz

# Remove coloredlogs dependency as it is not in Fedora as of f28
# Also remove python3-future dependency for f41
Patch0:		roca-detect-color.patch
Patch1:		roca-detect-pkcs7.patch

BuildRequires:	%{python}-cryptography >= 3.2.1
%if !0%{bundle_pgpdump}
BuildRequires:	%{python}-pgpdump
%endif
BuildRequires:	%{python}-setuptools %{python}-devel
# Manual dependencies - in case auto dependency doesn't work
%if 0%{?rhel} == 7
Requires:	%{python}-cryptography %{python}-pgpdump
Requires:	%{python}-six
# el7 conflicts with python2-dateutil and doesn't work with python3
Requires:	python-dateutil
#Requires:	%%{python}-dateutil
%endif

BuildArch:	noarch

%{?python_enable_dependency_generator}

%description
This tool is related to the ACM CCS 2017 conference paper #124 Return of the
Coppersmith’s Attack: Practical Factorization of Widely Used RSA
Moduli.

https://crocs.fi.muni.cz/public/papers/rsa_ccs17

Install this to test public RSA keys for the presence of the vulnerability
described by CVE-2017-15361.

%if 0%{bundle_pgpdump}
%package -n python3-pgpdump
Summary: PGP packet parser library in Python 3.x
BuildArch: noarch

%description -n python3-pgpdump
python-pgpdump is a Python 3 library for parsing PGP packets. The intent here
is not on completeness, as we don't currently decode every packet type, but
on being able to do what people actually have to 95% of the time.

Currently supported things include:

* Signature packets
* Public key packets
* Secret key packets
* Trust, user ID, and user attribute packets
* ASCII-armor decoding and CRC check
%endif

%prep
%setup -q -n roca-%{version}
%patch 0 -p0 -b .color
%patch 1 -p0 -b .pkcs7
%if 0%{bundle_pgpdump}
tar xvfz %{SOURCE1}
%endif

# remove leftover version control from upstream
find . -name .gitignore -delete

# fix env shbang in CLI scripts
%py_shebang_fix roca

# fix pgpdump requires
sed -i -e"s/'pgpdump'/'pgpdump3'/" setup.py

%build
%py_build
%if 0%{bundle_pgpdump}
cd pgpdump3-1.5.2
%py_build
%endif

%install
%py_install
%if 0%{bundle_pgpdump}
cd pgpdump3-1.5.2
%py_install
%endif

# make all CLI scripts executable to keep rpmlint happy, even though
# we are using EASY introducers instead.
chmod a+x `find %{buildroot}%{python_sitelib}/roca -name "*.py" | \
	xargs grep -l '^#!.*python'`

# Replace complex "EASY" universal wrapper with symlinks to cli scripts.
%if %{with symlinks}
ln -sf %{python_sitelib}/roca/detect.py %{buildroot}%{_bindir}/roca-detect
ln -sf %{python_sitelib}/roca/detect_tls.py %{buildroot}%{_bindir}/roca-detect-tls
%endif

%check
export PYTHONPATH=pgpdump3-1.5.2
%{__python} -m unittest discover

%files
%doc README.md docs
%license LICENSE
%{_bindir}/roca-detect*
%{python_sitelib}/roca
%{python_sitelib}/roca_detect-%{version}*

%if 0%{bundle_pgpdump}
%files -n python3-pgpdump
%doc pgpdump3-1.5.2/README.md
%license pgpdump3-1.5.2/COPYRIGHT
%{python_sitelib}/pgpdump*
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Stuart D. Gathman <stuart@gathman.org> - 1.2.12-27
- Remove python3-future dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.2.12-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.12-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.12-17
- Rebuilt for Python 3.10

* Fri Mar 12 2021 Stuart D. Gathman <stuart@gathman.org> - 1.2.12-16
- Fix for new python3-cryptography release which dropped old PKCS7 API

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.12-13
- Rebuilt for Python 3.9

* Mon May 11 2020 Stuart D. Gathman <stuart@gathman.org> - 1.2.12-12
- Fix broken dependency in setup.py

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.12-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.12-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Stuart D. Gathman <stuart@gathman.org> - 1.2.12-7
- Make python3-pgpdump a sub-package

* Sat Apr 27 2019 Stuart D. Gathman <stuart@gathman.org> - 1.2.12-6
- Bundle pgpdump3-1.5.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.12-4
- Mark manual dependencies as needed for el7

* Tue Sep 11 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.12-3
- Use pathfix.py to fix shebangs
- Use python dependency generator

* Mon Sep 10 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.12-2
- Fix broken rhel condition typo
- Fix unused (except in devel) env python shebangs to keep rpmlint happy

* Mon Sep 10 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.12-1
- Use latest upstream unreleased tag for 1.2.12

* Mon Sep 10 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-7
- Make global option to use symlinks instead of EASY introducer 

* Sat Sep  8 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-6
- Patch cli scripts and symlink to them directly.
- Add additional help to roca-detect-tls

* Fri Sep  7 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-5
- Format SPEC with tabs and double space between sections
- Split wrapper import into 2 lines 

* Tue Sep  4 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-4
- More changes from package review:
- Keep upstream introducer name and symlink to it
- Specify an additional directory level after sitelib in files

* Mon Sep  3 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-3
- More suggestions from package review

* Mon Sep  3 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-2
- Change more nits from Fedora package review

* Mon Sep  3 2018 Stuart D. Gathman <stuart@gathman.org> 1.2.1-1
- py3 support
- New upstream release

* Thu Oct 19 2017 Stuart D. Gathman <stuart@gathman.org> 1.0.7-3
- SPEC file nits from Fedora package review

* Wed Oct 18 2017 Stuart D. Gathman <stuart@gathman.org> 1.0.7-2
- Ditch the "EASY" introducer that requires setuptools >= 1.0

* Wed Oct 18 2017 Stuart D. Gathman <stuart@gathman.org> 1.0.7-1
- Initial rpm
