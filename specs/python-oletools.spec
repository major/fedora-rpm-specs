Name:           python-oletools
Version:        0.56.2
Release:        20%{?dist}
Summary:        Tools to analyze Microsoft OLE2 files

# oletools/*.py: BSD
# oletools/olevba*.py: BSD and MIT
# oletools/thirdparty/xxxswf/*.py: No license specified
# oletools/thirdparty/xglob/*.py: BSD
# oletools/thirdparty/tablestream/*.py: BSD
# oletools/thirdparty/zipfile27/*.py: Python
# oletools/thirdparty/msoffcrypto/*.py: MIT
# Automatically converted from old format: BSD and MIT and Python - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Python
URL:            https://www.decalage.info/python/oletools
VCS:            https://github.com/decalage2/oletools/
#               https://github.com/decalage2/oletools/releases
#               https://github.com/nolze/msoffcrypto-tool/releases

%global         srcname oletools


# Bootstrap may be needed to break circular dependencies between
# python-oletools and python-pcodedmp
%bcond_with     bootstrap

# Build with python3 package by default
%bcond_without  python3

# Bundles taken from oletools-0.54.2b/oletools/thirdparty
%global         _provides \
Provides:       bundled(oledump) = 0.0.49 \
Provides:       bundled(tablestream) = 0.09 \
Provides:       bundled(xglob) = 0.07 \
Provides:       bundled(xxxswf) = 0.1


%global         _description %{expand:
The python-oletools is a package of python tools from Philippe Lagadec
to analyze Microsoft OLE2 files (also called Structured Storage,
Compound File Binary Format or Compound Document File Format),
such as Microsoft Office documents or Outlook messages, mainly for
malware analysis, forensics and debugging.
It is based on the olefile parser.
See http://www.decalage.info/python/oletools for more info.
}

Source0:        https://github.com/decalage2/oletools/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Remove the bundled libraries from the build. Use the system libraries instead
Patch0:         %{name}-01-thirdparty.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-colorclass
BuildRequires:  python%{python3_pkgversion}-easygui
BuildRequires:  python%{python3_pkgversion}-olefile
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pymilter
BuildRequires:  python%{python3_pkgversion}-prettytable
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-msoffcrypto
%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-pcodedmp
%endif

%description    %{_description}



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%{_provides}

Requires:       python%{python3_pkgversion}-pymilter
Requires:       python%{python3_pkgversion}-pyparsing
Requires:       python%{python3_pkgversion}-colorclass
Requires:       python%{python3_pkgversion}-easygui
Requires:       python%{python3_pkgversion}-olefile
Requires:       python%{python3_pkgversion}-prettytable
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-msoffcrypto
%if %{without bootstrap}
Requires:       python%{python3_pkgversion}-pcodedmp
%endif

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python3 version.


%package -n python-%{srcname}-doc
Summary:        Documentation files for %{name}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-doc}

%description -n python-%{srcname}-doc %{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}

# Use globally installed python modules instead of bundled ones
for i in colorclass easygui olefile prettytable pyparsing; do
  rm -rf "oletools/thirdparty/${i}"
done

sed -i -e '
  s|from oletools.thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.olefile import olefile|from olefile import olefile|;
  s|from oletools.thirdparty.prettytable import prettytable|import prettytable|;
  s|from oletools.thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from thirdparty.pyparsing.pyparsing import|from pyparsing import|;
  s|from .thirdparty import olefile|import olefile|;
  s|from oletools.thirdparty.easygui import easygui|import easygui|;
' */*.py

sed -i -e 's|pyparsing>=2\.1\.0,<3|pyparsing|' requirements.txt setup.py

%if %{with bootstrap}
sed -i -e '/pcodedmp/d' requirements.txt setup.py
%endif


%build
%py3_build


%install
# Install python3 files
%py3_install

# Move executables to python3 versioned names
pushd %{buildroot}%{_bindir}
  main=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}'.format(sys.version_info))")  # e.g. 3
  full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4

  # mraptor3 and olevba3 are deprecated, mraptor or olevba should be used instead
  rm -f mraptor3 olevba3

  for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    mv -f "${i}" "${i}-${full}"
    ln -s "${i}-${full}" "${i}-${main}"
  done
popd

# Remove '\r' line ending and shebang from non-executable python libraries
for file in %{buildroot}%{python3_sitelib}/%{srcname}/{.,*,*/*}/*.py; do
  sed -e '1{\@^#![[:space:]]*/usr/bin/env python@d}' -e 's|\r$||' "${file}" > "${file}.new"
  touch -c -r "${file}" "${file}.new"
  mv -f "${file}.new" "${file}"
done

# Remove files that should either go to %%doc or to %%license
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/{doc,LICENSE.txt,README.*}
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/msoffcrypto/LICENSE.txt
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xglob/LICENSE.txt
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/thirdparty/xxxswf/LICENSE.txt

# Create trivial name symlinks to the default executables of preferred python version
# For example in FC31 exists python3 package, but puthon2 is the preferred one
pushd %{buildroot}%{_bindir}
for i in ezhexviewer msodde mraptor olebrowse oledir olefile oleid olemap olemeta oleobj oletimes olevba pyxswf rtfobj; do
    full=$(%{__python3} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")  # e.g. 3.4
    ln -s "${i}-${full}" "${i}"
done
popd


# Prepare licenses from bundled code for later %%license usage
mv -f %{srcname}/thirdparty/xglob/LICENSE.txt xglob-LICENSE.txt
mv -f %{srcname}/thirdparty/xxxswf/LICENSE.txt xxxswf-LICENSE.txt


%check
%{__python3} -m unittest

# Simple self-test: If it fails, package won't work after installation
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/olevba-3 --code cheatsheet/oletools_cheatsheet.docx
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/mraptor-3 cheatsheet/oletools_cheatsheet.docx


%files -n python%{python3_pkgversion}-%{srcname}
%license %{srcname}/LICENSE.txt xglob-LICENSE.txt xxxswf-LICENSE.txt
%doc README.md
%{python3_sitelib}/*
%{_bindir}/ezhexviewer-3*
%{_bindir}/msodde-3*
%{_bindir}/olebrowse-3*
%{_bindir}/oledir-3*
%{_bindir}/oleid-3*
%{_bindir}/olefile-3*
%{_bindir}/olemap-3*
%{_bindir}/olemeta-3*
%{_bindir}/oleobj-3*
%{_bindir}/oletimes-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/olevba-3*
# ModuleNotFoundError: No module named 'cStringIO'
%{_bindir}/mraptor-3*
%{_bindir}/pyxswf-3*
%{_bindir}/rtfobj-3*
%{_bindir}/ezhexviewer
%{_bindir}/mraptor
%{_bindir}/msodde
%{_bindir}/olebrowse
%{_bindir}/oledir
%{_bindir}/oleid
%{_bindir}/olefile
%{_bindir}/olemap
%{_bindir}/olemeta
%{_bindir}/oleobj
%{_bindir}/oletimes
%{_bindir}/olevba
%{_bindir}/pyxswf
%{_bindir}/rtfobj


%files -n python-%{srcname}-doc
%doc %{srcname}/doc/*
%doc cheatsheet


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Robert Scheck <robert@fedoraproject.org> - 0.56.2-19
- Switch to '%%{python3} -m unittest' due to setuptools 74+ (#2319684)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.56.2-18
- convert license to SPDX

* Tue Aug 13 2024 Python Maint <python-maint@redhat.com> - 0.56.2-17
- Rebuilt for Python 3.13

* Tue Aug 13 2024 Python Maint <python-maint@redhat.com> - 0.56.2-16
- Bootstrap for Python 3.13

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 0.56.2-11
- Rebuilt for Python 3.12

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 0.56.2-10
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.56.2-7
- Rebuilt for pyparsing-3.0.9

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.56.2-6
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.56.2-5
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.56.2-2
- Rebuilt for Python 3.10

* Sun May 09 2021 Robert Scheck <robert@fedoraproject.org> - 0.56.2-1
- Upgrade to 0.56.2 (#1958528)

* Sat Apr 03 2021 Robert Scheck <robert@fedoraproject.org> - 0.56.1-1
- Upgrade to 0.56.1 (#1945976)

* Tue Feb 02 2021 Robert Scheck <robert@fedoraproject.org> - 0.56-3
- Weak Python 2.7 pyparsing requirement for EPEL 7 correctly
- Add simple self-test mechanism to detect future weaking mistakes

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Robert Scheck <robert@fedoraproject.org> - 0.56-1
- Upgrade to 0.56 (#1885099)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Robert Scheck <robert@fedoraproject.org> 0.55-4
- Require python-setuptools during build-time explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.55-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.55-1
- bump to bugfix release 0.55

* Sun Nov 10 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.54.2-2
- use the msoffcrypto bundling only for python2 subpackage
- use python3-msoffcrypto for python3 package

* Fri Nov 08 2019 Michal Ambroz <rebus AT_ seznam.cz> - 0.54.2-1
- bump to release 0.54.2
- stop building the python2 for fc32+ epel8+
- add missing msoffcrypto python module
- fix python36 dependencies for EPEL7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.51-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.51-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.51-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Robert Scheck <robert@fedoraproject.org> 0.51-3
- Correct line endings and remove shebang from non-executable
  python libraries (#1505374 #c5)
- Clarify python3 related scripts in %%description (#1505374 #c4)
- Correct summary of -doc subpackage (#1505374 #c2)

* Thu Oct 05 2017 Robert Scheck <robert@fedoraproject.org> 0.51-2
- Various spec file enhancements (#1471561)
- Added spec file conditionals to build for EPEL 7

* Thu Jun 22 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-1
- bump to 0.51 release

* Thu Jun 22 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-0.3.dev11.b4b52d22
- gaps in python3 detected, using python2 as default

* Thu Jun 15 2017 Michal Ambroz <rebus at, seznam.cz> 0.51-0.2.dev11.b4b52d22
- initial version
