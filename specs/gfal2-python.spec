%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

# Use static linking against boost
%bcond_with static_boost_python

# Python sitearch
%{!?python3_sitearch: %define python3_sitearch %(%{__python3} -c "from sysconfig import get_path; print(get_path('platlib'))")}

# Python modules filtering
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:               gfal2-python
Version:            1.13.0
Release:            2%{?dist}
Summary:            Python bindings for gfal 2
License:            Apache-2.0
URL:                http://dmc.web.cern.ch/
# git clone --depth=1 --branch=v1.13.0 https://gitlab.cern.ch/dmc/gfal2-bindings.git gfal2-python-1.13.0
# tar czf gfal2-python-1.13.0.tar.gz --exclude-vcs gfal2-python-1.13.0
Source0:            %{name}-%{version}.tar.gz

BuildRequires:      gcc-c++
BuildRequires:      cmake3
BuildRequires:      python3
BuildRequires:      gfal2-devel >= 2.23.0
BuildRequires:      boost-devel
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      boost-python%{python3_pkgversion}-devel

%global _description \
Python3 bindings for Gfal2. \
Gfal2 offers a single, simple and portable API \
for file operations in the Grid and Cloud environments.

%description %_description

%package -n python3-gfal2
Summary:            gfal2 python bindings for Python 3
Requires:           gfal2-core >= 2.23.0
Requires:           python3
# Remove before F30
Provides:           gfal2-python3 = %{version}-%{release}
Provides:           gfal2-python3%{?_isa} = %{version}-%{release}
Obsoletes:          gfal2-python3 < %{version}-%{release}

%description -n python3-gfal2 %_description

%clean
%cmake3_build --target clean

%prep
%setup -q

%build
# Make sure the version in the spec file and the version used
# for building matches
gfal2_python_cmake_ver=`sed -n 's/^set *(VERSION_\(MAJOR\|MINOR\|PATCH\) *\([0-9]\+\).*/\2/p' CMakeLists.txt | paste -sd '.'`
gfal2_python_spec_ver=`expr "%{version}" : '\([0-9]*\\.[0-9]*\\.[0-9]*\)'`
if [ "$gfal2_python_cmake_ver=" != "$gfal2_python_spec_ver=" ]; then
    echo "The version in the spec file does not match the CMakeLists.txt version!"
    echo "$gfal2_python_cmake_ver!= %{version}"
    exit 1
fi

%cmake3 \
     -DDOC_INSTALL_DIR=%{_pkgdocdir} \
%if 0%{?with_static_boost_python}
     -DBoost_USE_STATIC_LIBS=ON \
%endif
     -DUNIT_TESTS=TRUE

%cmake3_build

%install
%cmake3_install

%files -n python3-gfal2
%{python3_sitearch}/gfal2.so
%doc LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.13.0-1
- Upstream release 1.13.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.2-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.12.2-5
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.12.2-2
- Rebuilt for Boost 1.83

* Wed Dec 13 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.12.2-1
- Upgrade to upstream release 1.12.2

* Tue Nov 21 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.12.1-2
- Patch for the Python 3.13 rebuild (close RHBZ#2250873)

* Tue Sep 05 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.12.1-1
- Upgrade to upstream release 1.12.1
- Closes bugzilla#2154855, bugzilla#2220000, bugzilla#2225821

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.12.0-4
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.12.0-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.12.0-1
- Upgrade to upstream release 1.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.11.1-4
- Patch for the Python 3.11 rebuild (close RHBZ#2098706)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.11.1-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.11.1-2
- Rebuilt for Boost 1.78

* Mon Mar 07 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.11.1-1
- Upgrade to upstream release 1.11.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.9.5-15
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.5-13
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.9.5-11
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.9.5-8
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Andrea Manzi <amanzi@cern.ch> - 1.9.5-5
- rename python3 package
- remove python2 package from f32 on
- remove el5 compilation

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 1.9.5-3
- Rebuilt to change main python from 3.4 to 3.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Andrea Manzi <amanzi@cern.ch> - 1.9.5-2
- Update for release 1.9.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.3-5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.3-4
- Python 2 binary package renamed to python2-gfal2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.3-1
- Update for release 1.9.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 1.9.2-3
- Rebuilt for Boost 1.64

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.9.2-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Apr 03 2017 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.2-1
- Update for release 1.9.2

* Mon Feb 20 2017 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.1-1
- Update for release 1.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.8.5-2
- Rebuilt for Boost 1.63

* Wed Jan 18 2017 Alejandro Alvarez <aalvarez@cern.ch> - 1.8.5-1
- Update to upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Alejandro Alvarez <aalvarez@cern.ch> - 1.8.4-4
- Add patch to work with newer versions of Boost

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.8.4-2
- Rebuilt for Boost 1.60

* Mon Nov 09 2015 Alejandro Alvarez <aalvarez@cern.ch> - 1.8.4-1
- Update for release 1.8.4

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.8.3-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.8.3-2
- rebuild for Boost 1.58

* Fri Jul 03 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.8.3-1
- Update for release 1.8.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.8.1-1
- Update for release 1.8.1

* Thu Apr 02 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.7.1-1
- Update for release 1.7.1

* Fri Feb 06 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.7.0-1
- Update for release 1.7.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.6.0-2
- Rebuild for boost 1.57.0

* Fri Nov 07 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.6.0-1
- Update for release 1.6.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.0-1
- Update for release 1.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4.1-2
- Rebuild for boost 1.55.0

* Fri Feb 28 2014 Adrien Devresse <adevress at cern.ch> - 1.4.1-1
- Release 1.4.1 of gfal2 python bindings, see RELEASE-NOTES for details

* Sat Nov 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.3.0-2
- Install docs to %%{_pkgdocdir} where available (#993774).
- Own doc dirs.

* Fri Nov 01 2013 Adrien Devresse <adevress at cern.ch> - 1.3.0-1  
- Release 1.3.0 of gfal2 python bindings, see RELEASE-NOTES for details

* Wed May 08 2013 Adrien Devresse <adevress at cern.ch> - 1.2.1-1 
- First release compatible for EPEL
