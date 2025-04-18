# Python sitearch
%{!?python3_sitearch: %define python3_sitearch %(%{__python3} -c "from sysconfig import get_path; print(get_path('platlib'))")}

Name:           gfal2-util
Version:        1.9.0
Release:        2%{?dist}
Summary:        GFAL2 utility tools
Group:          Applications/Internet
License:        Apache-2.0
URL:            http://dmc.web.cern.ch/
# git clone --depth=1 --branch=v1.9.0 https://gitlab.cern.ch/dmc/gfal2-util.git gfal2-util-1.9.0
# tar czf gfal2-util-1.9.0.tar.gz --exclude-vcs gfal2-util-1.9.0
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch

BuildRequires:  gfal2-core
BuildRequires:  gfal2-plugin-file

%global _description \
gfal2-util is a set of basic utility tools for file \
interactions and file copy based on the GFAL 2.0 toolkit. \
gfal2-util supports the protocols of GFAL 2.0 : WebDav(s), \
gridFTP, http(s), SRM, xrootd, etc...

%description %_description

%prep
%setup -q

%build
# Validate the version
gfal2_util_ver=`sed -n "s/VERSION = '\(.*\)'/\1/p" src/gfal2_util/base.py`
gfal2_util_spec_ver=`expr "%{version}" : '\([0-9]*\\.[0-9]*\\.[0-9]*\)'`
if [ "$gfal2_util_ver" != "$gfal2_util_spec_ver" ]; then
    echo "The version in the spec file does not match the base.py version!"
    echo "%{version} != $gfal2_util_ver"
    exit 1
fi

python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

#-------------------------------------------------------------------------------
# Gfal2-util-scripts package
#-------------------------------------------------------------------------------
%package scripts
Summary:        gfal2 command line scripts
Requires:       python3-gfal2-util

%description scripts
Provides a set of command line scripts to call gfal2-util python functions.

%files scripts
%defattr (-,root,root)
%{_bindir}/gfal-*
%{_mandir}/man1/*

#-------------------------------------------------------------------------------
# Gfal2-util package for Python3
#-------------------------------------------------------------------------------
%package -n python3-gfal2-util
Summary:        gfal2 clients for python3

BuildRequires:  python3-gfal2 >= 1.13.0
BuildRequires:  python3
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-gfal2 >= 1.13.0
Requires:       gfal2-util-scripts = %{version}-%{release}
Requires:       gfal2-plugin-file
Requires:       python3

%description -n python3-gfal2-util %_description

%files -n python3-gfal2-util
%defattr (-,root,root)
%{python3_sitelib}/gfal2_util*
%doc RELEASE-NOTES VERSION LICENSE readme.html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 1.9.0-1
- Upstream release 1.9.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.1-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Mihai Patrascoiu <mipatras@cern.ch> - 1.8.1-1
- Upgrade to upstream release 1.8.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Mihai Patrascoiu <mipatras@cern.ch> - 1.8.0-1
- Upgrade to upstream release 1.8.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 07 2022 Mihai Patrascoiu <mipatras@cern.ch> - 1.7.1-1
- Upgrade to upstream release 1.7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Michal Simon <michal.simon@cern.ch> - 1.6.0-7
- Add provides/obsoletes for the python3 package.

* Thu Nov 19 2020 Petr Vokac <petr.vokac at cern.ch> - 1.6.0-1
- New upstream release
- Provide distinct packages for Python2 and Python3

* Mon Sep 14 2020 Mihai Patrascoiu <mipatras at cern.ch> - 1.5.4-1
- New upstream release

* Fri Mar 29 2019 Andrea Manzi <amanzi at cern.ch> - 1.5.3-1
- New upstream release

* Mon Feb 20 2017 Alejandro Alvarez <aalvarez at cern.ch> - 1.5.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016  Alejandro Alvarez <aalvarez at cern.ch> - 1.4.0-1
- New upstream release
- python-argparse is part of python's stdlib

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Alejandro Alvarez <aalvarez at cern.ch> - 1.3.2-1
- Update for new upstream 1.3.2 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.3.1-1
- Update for new upstream 1.3.1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Alejandro Alvarez <aalvarez at cern.ch> - 1.2.1-1
- Update for new upstream 1.2.1 release

* Fri Nov 07 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.1.0-1
- Update for new upstream 1.1.0 release

* Wed Jul 02 2014 Alejandro Alvarez <aalvarez at cern.ch> - 1.0.0-1
- Update for new upstream 1.0.0 release
- Installation done with distutils
- Run tests on check stage 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 04 2013 Adrien Devresse <adevress at cern.ch> - 0.2.1-1
- Initial EPEL compatible version
