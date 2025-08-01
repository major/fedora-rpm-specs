# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6} || 0%{?el7}
ase-3.16 requires numpy 1.9 or newer
%quit
%endif

%if 0%{?el8} || 0%{?el9}
ase-3.23 requires pyproject.toml setuptools support
%quit
%endif

%global upstream_name ase

Name:			python-ase
Version:		3.24.0
Release:		4%{?dist}
Summary:		Atomic Simulation Environment


# The entire source code is LGPLv2+ except:
# ase/io/fortranfile.py which is MIT
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT

URL:			https://wiki.fysik.dtu.dk/ase/
Source0:		https://gitlab.com/%{upstream_name}/%{upstream_name}/-/archive/%{version}/%{upstream_name}-%{version}.tar.gz


BuildArch:		noarch

BuildRequires:		gettext
BuildRequires:		desktop-file-utils

BuildRequires:		python3-devel
BuildRequires:		python3-matplotlib
BuildRequires:		python3-numpy
BuildRequires:		python3-pytest
BuildRequires:		python3-pytest-mock
BuildRequires:		python3-scipy
BuildRequires:		python3-setuptools
BuildRequires:		python3-tkinter

Requires:		python3-matplotlib
Requires:		python3-netcdf4
Requires:		python3-numpy
# Missing on fedora
#Requires:		python3-pycodcif
Requires:		python3-scipy
Requires:		python3-spglib
Requires:		python3-tkinter

%global _description\
The Atomic Simulation Environment (ASE) is the common part of the simulation\
tools developed at CAMd. ASE provides Python modules for manipulating atoms,\
analyzing simulations, visualization etc.

%description %_description

%package -n python3-ase
Summary:		Atomic Simulation Environment for Python 3
Obsoletes:		python2-ase < 3.16.2-7
%{?python_provide:%python_provide python3-ase}

%description -n python3-ase
The Atomic Simulation Environment (ASE) is the common part of the simulation
tools developed at CAMd. ASE provides Python 3 modules for manipulating atoms,
analyzing simulations, etc.

%prep
%setup -qn %{upstream_name}-%{version}

# https://gitlab.com/ase/ase/-/issues/1461
rm -f ase/test/fio/test_espresso.py
# https://gitlab.com/ase/ase/-/issues/1614
rm -f ase/test/db/test_o2b2o.py

# copy required sources and remove doc directory
cp -p doc/static/%{upstream_name}256.png %{upstream_name}.png
cp -p doc/%{upstream_name}-gui.desktop %{upstream_name}-gui.desktop
rm -rf doc

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%{__python3} setup.py build


%install

%{__python3} setup.py install --skip-build --prefix=%{_prefix} \
	   --optimize=1 --root $RPM_BUILD_ROOT

# doc would go under $RPM_BUILD_ROOT%%{_datadir}/%%{name}
# if only we get rid of povray dependency one could build doc with:
# cd $RPM_BUILD_ROOT%%{_datadir}/%%{name}/doc&& sphinx-build . _build

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
--dir $RPM_BUILD_ROOT%{_datadir}/applications \
%if (0%{?fedora} && 0%{?fedora} < 20) || (0%{?rhel} && 0%{?rhel} < 7)
--vendor "%{upstream_name}" \
%endif
%{upstream_name}-gui.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{upstream_name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

# we store translations in ase/gui/po/*/*/ag.mo
# but /usr/lib/rpm/find-lang.sh wants locale (Fedora) or share/locale (el6)
mkdir $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share
cp -rp $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/po $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share/locale
%find_lang ag
rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name}/gui/share
sed -i "s|share/locale|po|g" ag.lang

# create list of all installed dirs/files(exclude *.mo) and concat with ag.lang
find $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name} -type d | xargs -I _file echo "%dir _file" > d3.list
find $RPM_BUILD_ROOT%{python3_sitelib}/%{upstream_name} -type f ! -name "*.mo" > f3.list
cat ag.lang d3.list f3.list > files3.list
# trim the $RPM_BUILD_ROOT
sed -i "s|$RPM_BUILD_ROOT||g" files3.list


%check
export PYTHONPATH=`pwd`/build/lib
export PATH=`pwd`/bin:${PATH}  # the tests assume Python 3 scripts are named the same as Python 2 scripts
# the cli tests assume there is /usr/bin/env python
ln -s `which python3` `pwd`/bin/python
# Ignore pytest deprecation warnings treated as errors https://gitlab.com/ase/ase/-/issues/909
LC_ALL=C.UTF-8 ase test --verbose --pytest -W ignore -W 'once::DeprecationWarning'
cd -


%files -n python3-ase -f files3.list
%doc COPYING* LICENSE README*
%{_bindir}/ase*
%{_datadir}/applications/%{upstream_name}-gui.desktop
%{_datadir}/pixmaps/%{upstream_name}.png
%{python3_sitelib}/*.egg-info


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 3.24.0-3
- Rebuilt for Python 3.14

* Tue Jan 28 2025 Marcin Dulak <marcindulak@fedoraproject.org> - 3.24.0-2
- Remove test/db/test_o2b2o.py failing with Python 3.14

* Sat Jan 25 2025 Marcin Dulak <marcindulak@fedoraproject.org> - 3.24.0-1
- New upstream release

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.23.0-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.23.0-2
- Rebuilt for Python 3.13

* Mon Jun 03 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 3.23.0-1
- New upstream release

* Fri Apr 05 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.1-12
- Remove tests failing with pytest-8 bug #2273562

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.1-9
- Remove tests failing on python-3.13

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.1-7
- Workaround for Python 3.12 removed 'importlib.find_loader' https://gitlab.com/ase/ase/-/issues/1256

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.22.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.1-3
- Remove ase/test/test_units.py for scipy 1.8.0 https://gitlab.com/ase/ase/-/issues/1038

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.22.1-2
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.1-1
- New upstream release
- Ignore pytest warnings https://gitlab.com/ase/ase/-/issues/909

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.22.0-1
- New upstream release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.21.1-5
- Rebuilt for Python 3.10

* Mon May 10 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.21.1-4
- Remove more distutils

* Mon May 10 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.21.1-3
- Patch to remove distutils

* Fri May 07 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.21.1-2
- Remove flaky ase/test/constraints/test_fixinternals.py test

* Fri May 07 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.21.1-1
- New upstream release
- Add br
- Add suggested requires
- Change changelog email

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 3.19.1-5
- Remove test/preconsmallcell.py https://gitlab.com/ase/ase/-/issues/828

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 3.19.1-3
- Add explicit python3-setuptools br

* Mon May 11 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 3.19.1-2
- Restore patch for Python 3.9 (#1792937)

* Thu May 07 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 3.19.1-1
- New upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 3.18.0-4
- Patch for Python 3.9 (#1792937)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.0-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 3.18.0-1
- new upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 3.17.0-1
- new upstream release

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 3.16.2-8
- add obsoletes
- drop manual requires

* Sat Apr 27 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 3.16.2-7
- don't use 3 affix in python scripts
- adjust Exec in ase-gui.desktop

* Sat Apr 27 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 3.16.2-6
- enable ase-gui3
- switch to python3
- add flask requires and scipy requires/buildrequires

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 3.16.2-4
- the cli tests assume there is /usr/bin/env python

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.16.2-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 3.16.2-1
- new upstream release
- no more git commit in tar directory name

* Sat Apr 07 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 3.16.0-1
- new upstream release
- clean rhel5 leftovers
- drop rhel6 support: Python 2.7 is required
- drop rhel7 support: Numpy 1.9 is required
- link Python 2 scripts as defaults

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.13.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.13.0-3
- Python 2 binary package renamed to python2-ase
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 3.13.0-1
- new, upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-23
- Rebuild for Python 3.6

* Tue Nov 08 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 3.12.0-22
- new way of running tests

* Sat Nov 05 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 3.12.0-21
- new upstream release

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.11.0-21
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0-20
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jun 18 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 3.11.0-19
- upstream moved to gitlab

* Wed Feb 17 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 3.10.0-18
- upstream 3.10.1, no more upstream_svn
- LC_ALL=C.UTF-8 needed by the tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1.4567-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1.4567-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 22 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 3.9.1.4567-15
- upstream 3.9.1.4567
- files-attr

* Fri May 29 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 3.9.0.4465-14
- python3, build log files removed
- upstream 3.9.0.4465

* Fri Oct 31 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 3.8.1.3440-13
- larger icon - https://bugzilla.redhat.com/show_bug.cgi?id=1157516

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1.3440-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Björn Esser <bjoern.esser@gmail.com> - 3.8.1.3440-11
- failsafe backport of Python2-macros for RHEL <= 6

* Fri Jan 17 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 3.8.1.3440-10
- https://bugzilla.redhat.com/show_bug.cgi?id=1044199
- https://bugzilla.redhat.com/show_bug.cgi?id=1044200

* Tue Dec 10 2013 Marcin Dulak <marcindulak@fedoraproject.org> - 3.8.1.3440-9
- upstream patch for launching ase-gui without terminal (gtk-launch ase-gui)
- desktop file in svn

* Sat Nov 30 2013 Marcin Dulak <marcindulak@fedoraproject.org> - 3.8.1.3440-8
- fix Exec in ase-gui.desktop
- remove MANIFEST.in from %%doc 
- PATH modified for tests to include scripts dir

* Fri Nov 22 2013 Marcin Dulak <marcindulak@fedoraproject.org> - 3.8.1.3440-7
- new upstream version, old patches removed

* Thu Sep 19 2013 Björn Esser <bjoern.esser@gmail.com> - 3.7.1.3184-6
- Devendorized!

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1.3184-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Marcin Dulak <marcindulak@fedoraproject.org> 3.7.1.3184-4
- fix bug #976886 c#9

* Sun Jun 23 2013 Marcin Dulak <marcindulak@fedoraproject.org> 3.7.1.3184-3
- builds on el5
- remove doc
- %%{upstream_name}.png goes to %%{_datadir}/pixmaps
- fix bug #976886 c#4

* Sat Jun 22 2013 Marcin Dulak <marcindulak@fedoraproject.org> 3.7.1.3184-2
- include desktop file
- partly fix bug#976886#c1 and #c2

* Fri Jun 21 2013 Marcin Dulak <marcindulak@fedoraproject.org> 3.7.1.3184-1
- trimmed for Fedora/RHEL

* Mon May 6 2013 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk> 3.6.1-2
- include docs

* Mon Jun 11 2012 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk> 3.6.0-1
- restructured for build.opensuse.org and Fedora based on campos-ase3.spec

* Tue Apr 27 2010 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk>
- common Requires for EL, Fedora, openSUSE
- perform testase.py when building
- removed dependecy in python-lxml

* Wed Jun 18 2008 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk>
- FC 9: set -- ${variable} converts dashes of $1 into underlines so use $2

* Mon Jun 16 2008 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk>
- initial version
