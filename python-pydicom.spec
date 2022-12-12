# Enable test with --with=pytest, because they download data from the net and they don't
# work in koji
%bcond_with pytest

%global modname pydicom


%global _description %{expand:
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Documentation is available at https://pydicom.github.io/pydicom}

Name:           python-%{modname}
Version:        2.3.1
Release:        1%{?dist}
Summary:        Read, modify and write DICOM files with python code

# There are generated data (private dict) in special format from GDCM
License:        MIT and BSD
URL:            https://github.com/darcymason/%{modname}
Source0:        https://github.com/darcymason/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%py_provides python3-%{modname} 

BuildRequires:  python3-devel python3-setuptools python3-six

%if %{with pytest}
# Test deps
BuildRequires:  python3-numpy python3-dateutil python3-pytest
%endif

Requires:       python3-dateutil
Recommends:     python3-numpy
Recommends:     python3-matplotlib
Recommends:     python3-tkinter
Recommends:     python3-pillow

%description -n python3-%{modname} %_description

%prep
%autosetup -n %{modname}-%{version} -p 1

%build
%py3_build

%install
%py3_install

%if %{with pytest}
%check
# Disable TestPillowHandler_JPEG.test_color_3d because koji is unable to
# allocate enough RAM during build. Works ok building locally
# Disable test_handler_util, it fails to build with numpy 1.19
# reported upstream https://github.com/pydicom/pydicom/issues/1119
%if 0%{?fedora} > 32
  %{__python3} -m pytest -k "not test_color_3d and not test_handler_util"
%else
  %{__python3} -m pytest -k "not test_color_3d"
%endif
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}*
%{_bindir}/pydicom

%changelog
* Thu Nov 17 2022 Alessio <alciregi@fedoraproject.org> - 2.3.1-1
- 2.3.1 release

* Sat Aug 06 2022 Alessio <alciregi@fedoraproject.org> - 2.3.0-1
- 2.3.0 release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Alessio <alciregi@fedoraproject.org> - 2.2.2-1
- 2.2.2 release

* Fri Aug 06 2021 Alessio <alciregi@fedoraproject.org> - 2.2.0-1
- 2.2.0 release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.1.2-1
- 2.1.2 release

* Wed Dec 02 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.1.1-2
- Removed sphinx-* buildrequire. Removed docs subpackage: bundles JS bits.

* Mon Nov 30 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.1.1-1
- 2.1.1 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.0.0-3
- New build

* Wed Jun 03 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.0.0-2
- Modified conditional to disable test_handler_util python test

* Wed Jun 03 2020 Alessio <alciregi AT fedoraproject DOT org> - 2.0.0-1
- 2.0.0. release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-3
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.4.2-2
- Disabled TestPillowHandler_JPEG.test_color_3d test

* Mon Feb 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.4.2-1
- Update to new release
- Splitted docs into a subpackage

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.1-1
- Update to new release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Update to 1.3.0
- Add patch to fix python 3.8 error
- Enable all tests

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.2-1
- Update to latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-1
- Update to 1.1.0 (#1544224)
- Stop building python2 docs as they have python2 syntax errors
- Skip test_PI_RGB[JPEG_RGB_RGB] for now
- Skip TestTimeZone.test_constructor on Python 3 for now

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.12.gitf6191c7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.gitf6191c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-0.10.gitf6191c7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.9.gitf6191c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.gitf6191c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.7.gitf6191c7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.6.gitf6191c7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.gitf6191c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 1.0.0-0.4.gitf6191c7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.3.gitf6191c7
- Fix provide macro for py3 (typo)
- Remove shebang from dicom_dao.py (non-executable-script)

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.2.gitf6191c7
- Include license file
- Add BSD to license list (generated data) from GDCM

* Tue Nov 03 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.1.gitf6191c7
- Simplify building docs

* Sat Oct 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.0.gitf6191c7
- Initial package
