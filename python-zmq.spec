%global common_description %{expand:
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.}

Name:           python-zmq
Version:        24.0.1
Release:        3%{?dist}
Summary:        Software library for fast, message-based applications

License:        LGPLv3+ and ASL 2.0 and BSD
URL:            https://zeromq.org/languages/python/
Source0:        %{pypi_source pyzmq}

BuildRequires:  gcc

BuildRequires:  zeromq-devel

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-tornado
BuildRequires:  python%{python3_pkgversion}-gevent
BuildRequires:  python%{python3_pkgversion}-numpy

%description %{common_description}


%package -n python%{python3_pkgversion}-zmq
Summary:        %{summary}
License:        LGPLv3+
%py_provides    python%{python3_pkgversion}-pyzmq

%description -n python%{python3_pkgversion}-zmq %{common_description}

This package contains the python bindings.


%package -n python%{python3_pkgversion}-zmq-tests
Summary:        %{summary}, testsuite
License:        LGPLv3+
Requires:       python%{python3_pkgversion}-zmq = %{version}-%{release}
%py_provides    python%{python3_pkgversion}-pyzmq-tests

%description -n python%{python3_pkgversion}-zmq-tests %{common_description}

This package contains the testsuite for the python bindings.


%prep
%setup -q -n pyzmq-%{version}

# remove bundled libraries
rm -rf bundled

# remove the Cython .c files in order to regenerate them:
find zmq -name "*.c" -delete

# remove shebangs
grep -lr "^#\!/usr/bin/env python" | xargs sed -i "1d"

# remove excecutable bits
find . -type f -executable | xargs chmod -x

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zmq

%check
# to avoid partially initialized zmq module from cwd
cd %{_topdir}
# test_cython does not seem to work with --pyargs / not from cwd
%pytest --pyargs zmq -k "not test_cython and not test_on_recv_basic"


%files -n python%{python3_pkgversion}-zmq -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitearch}/zmq/tests

%files -n python%{python3_pkgversion}-zmq-tests
%{python3_sitearch}/zmq/tests


%changelog
* Thu Jun 22 2023 Python Maint <python-maint@redhat.com> - 24.0.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 24.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Kevin Fenzi <kevin@scrye.com> - 24.0.1-1
- Update to 24.0.1. Fixes rhbz#2128693

* Sun Sep 18 2022 Kevin Fenzi <kevin@scrye.com> - 24.0.0-1
- Update to 24.0.0. Fixes rhbz#2127189

* Tue Aug 02 2022 Charalampos Stratakis <cstratak@redhat.com> - 23.2.0-1
- Update to 23.2.0
Resolves: rhbz#2092836

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 22.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 22.3.0-1
- Update to 22.3.0. Fixes rhbz#2004837

* Sun Aug 08 2021 Kevin Fenzi <kevin@scrye.com> - 22.2.1-1
- Update to 22.2.1. Fixes rhbz#1989975

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 22.0.3-2
- Rebuilt for Python 3.10

* Fri Feb 12 2021 Kevin Fenzi <kevin@scrye.com> - 22.0.3-1
- Update to 22.0.3. Fixes rhbz#1928104

* Wed Feb 03 2021 Kevin Fenzi <kevin@scrye.com> - 22.0.2-1
- Update to 22.0.2. Fixes rhbz#1922110

* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 21.0.2-1
- Update to 21.0.2. Fixes rhbz#1920351

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 21.0.0-1
- Update to 21.0.0. Fixes rhbz#1916136

* Thu Dec 31 2020 Kevin Fenzi <kevin@scrye.com> - 20.0.0-1
- Update to 20.0.0. Fixes rhbz#1832893

* Tue Nov 24 2020 Joel Capitao <jcapitao@redhat.com> - 19.0.2-1
- Update to 19.0.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 19.0.0-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Carl George <carl@george.computer> - 19.0.0-1
- Latest upstream rhbz#1772343

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Jochen Breuer <jbreuer@suse.de> - 18.1.0-3
- Providing python-pyzmq, since some packages are still relying on that.
  See: https://bugzilla.redhat.com/show_bug.cgi?id=1789889

* Fri Nov 29 2019 Miro Hrončok <mhroncok@redhat.com> - 18.1.0-2
- Subpackages python2-zmq, python2-zmq-test have been removed
  See https://fedoraproject.org/wiki/Changes/RetirePython2

* Sun Oct 06 2019 Kevin Fenzi <kevin@scrye.com> - 18.1.0-1
- Update to 18.1.0. Fixes bug #1742606

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.0.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 18.0.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 18.0.2-1
- Update to 18.0.2. Fixes bug #1724706

* Mon Apr 29 2019 Kevin Fenzi <kevin@scrye.com> - 18.0.1-1
- Update to 18.0.1. Fixes bug #1601128

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 17.0.0-2
- Rebuilt for Python 3.7

* Sat May 12 2018 Miro Hrončok <mhroncok@redhat.com> - 17.0.0-1
- Update to 17.0.0 (#1538381)
- Fix shebangs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 16.0.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 16.0.2-2
- Rebuild for Python 3.6

* Wed Nov 23 2016 Kevin Fenzi <kevin@scrye.com> - 16.0.2-1
- Update to 16.0.2. Fixes bug #1397615

* Sun Nov 13 2016 Thomas Spura <tomspur@fedoraproject.org> - 16.0.1-1
- update to 16.0.1
- build twice (for installing and testing in-place)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 15.3.0-1
- Update to 15.3.0

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 14.7.0-7
- Use modern provides filtering

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Thomas Spura <tomspur@fedoraproject.org> - 14.7.0-5
- Use setupegg.py for building/installing to have an unzip'ed egg

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 16 2015 Thomas Spura <tomspur@fedoraproject.org> - 14.7.0-3
- rebuilt to pick up new obsoletes/provides

* Wed Oct 14 2015 Thomas Spura <tomspur@fedoraproject.org> - 14.7.0-2
- Use python_provide and py_build macros
- Cleanup spec

* Mon Jun 29 2015 Ralph Bean <rbean@redhat.com> - 14.7.0-2
- Support python34 on EPEL7.

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 14.7.0-1
- update to 14.7.0
- temporarily disable python3 testsuite as it hangs on koji

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 14.4.1-1
- update to 14.4.1
- build against zeromq-4

* Wed Aug 27 2014 Thomas Spura <tomspur@fedoraproject.org> - 14.3.1-1
- update to 14.3.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 13.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 13.0.2-1
- update to new version (fixes FTBFS)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Thomas Spura <tomspur@fedoraproject.org> - 13.0.0-1
- update to 13.0.0
- add BSD to license list

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0.1-1
- update to 2.2.0.1
- move to BR zeromq3
- not all *.c files may be deleted, when receneration of .c files by Cython
- remove bundled folder explicitely

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.0-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.0-4
- force regeneration of .c files by Cython (needed for python 3.3 support)

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.0-3
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Wed Mar  7 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.1.11-1
- update to new version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.9-3
- tests package requires main package
- filter python3 libs

* Thu Dec  8 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.9-2
- use proper buildroot macro
- don't include tests twice

* Wed Sep 21 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.9-1
- update to new version
- run testsuite on python3

* Sun Jul 31 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.4-2
- don't delete the tests, needed by ipython-tests on runtime
- don't use _sourcedir macro

* Wed Apr  6 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.4-1
- update to new version (#690199)

* Wed Mar 23 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-1
- update to new version (#682201)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.10.1-1
- update to new version (fixes memory leak)
- no need to run 2to3 on python3 subpackage

* Thu Jan 13 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.10-1
- update to new version
- remove patch (is upstream)
- run tests differently

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.8-2
- rebuild for newer python3

* Thu Sep 23 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.8-1
- update to new version to be comply with zeromp

* Sun Aug 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.20100725git18f5d06-4
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Thu Aug  5 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.20100725git18f5d06-3
- add missing BR for 2to3

* Tue Aug  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.20100725git18f5d06-2
- build python3 subpackage
- rename to from pyzmq to python-zmq
- change license

* Sun Jul 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.20100725git18f5d06-1
- renew git snapshot
- start from version 0.1 like upstream (not the version from zeromq)
- remove buildroot / %%clean

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org - 2.0.7-1
- initial package (based on upstreams example one)
