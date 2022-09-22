%global gitcommit 2c2a79d85508c8988b6d4ecfd4d0f55cff35ef11
%global gitdate 20150408
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           python-igor
Version:        0.3
Release:        20.%{gitdate}git%{shortcommit}%{?dist}
Summary:        Parser for Igor Binary Waves (.ibw) and Packed Experiment (.pxp) files

# igor-0.2/igor/igorpy.py is PD, the restis LGPLv3+
License:        LGPLv3+ and Public Domain

URL:            http://blog.tremily.us/posts/igor/
Source0:        https://github.com/wking/igor/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         adapt-doctests-for-Python-3.8-and-newer-Numpy.patch
Patch1:         0001-Avoid-syntax-warning-with-python3.8.patch
Patch2:         0002-Remove-use-of-deprecated-method.patch

BuildArch:      noarch
BuildRequires:  /usr/bin/rename
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-matplotlib
BuildRequires:  python3-nose

%description
Python parsers for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics’ IGOR Pro software.

Note that this package is unrelated to igor (Automated distribution
life-cycle testing).

%package -n python3-igor
Summary:        %{summary}
Requires:       python3-numpy
Requires:       python3-matplotlib
Obsoletes:      python2-igor < 0.3-9
%{?python_provide:%python_provide python3-igor}

%description -n python3-igor
Python parsers for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics’ IGOR Pro software.

Note that this package is unrelated to igor (Automated distribution
life-cycle testing).

%prep
%autosetup -p1 -n igor-%{version}

%build
%py3_build

%install
%py3_install

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/*.py
rename '.py' '' %{buildroot}%{_bindir}/*

%check
nosetests-%{python3_version} --with-doctest --doctest-tests igor test -v

%global _docdir_fmt %{name}

# make sure that we got the python version right in the header
head -n1 %{buildroot}%{_bindir}/igorbinarywave | grep %{__python3} -q
head -n1 %{buildroot}%{_bindir}/igorpackedexperiment | grep %{__python3} -q

%files -n python3-igor
%{python3_sitelib}/*
%license COPYING.LESSER
%doc README
%{_bindir}/igorbinarywave
%{_bindir}/igorpackedexperiment

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.3-19.20150408git2c2a79d
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3-16.20150408git2c2a79d
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-13.20150408git2c2a79d
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-12.20150408git2c2a79d
- Fix compatiblity with python3.9 (#1793999)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Lumír Balhar <lbalhar@redhat.com> - 0.3-10.20150408git2c2a79d
- New patch: Adapt doctests for Python 3.8 and newer Numpy

* Thu Oct 17 2019 Lumír Balhar <lbalhar@redhat.com> - 0.3-9.20150408git2c2a79d
- Remove Python 2 subpackage, move scripts to Python 3 subpackage

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-8.20150408git2c2a79d
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-7.20150408git2c2a79d
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-3.20150408git2c2a79d
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-2.20150408git2c2a79d
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Feb 24 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-1
- Update to latest version
- Drop python3-only patches to fix tests under python3, build and test everything
  with a single source, and just ignore test result under python3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8.20150408git2c2a79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-7.20150408git2c2a79d
- Rebuild for Python 3.6

* Wed Sep 28 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.2-6.20150408git2c2a79d
- rebuilt for matplotlib-2.0.0
- make sure the scripts in bindir use python2 for now

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5.20150408git2c2a79d
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-4.20150408git2c2a79d
- Update License and add link to upstream pull request

* Sun Feb 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-3.20150408git2c2a79d
- Update to latest git snapshot
- Add nose to BR, fix Provides
- Patch tests to pass under Python 3

* Fri Feb 19 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-1
- Initial packaging
