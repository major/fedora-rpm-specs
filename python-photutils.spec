%bcond_without check

%global srcname photutils

Name: python-%{srcname}
Version: 1.5.0
Release: 1%{?dist}
Summary: Astropy affiliated package for image photometry tasks
License: BSD

URL: http://photutils.readthedocs.org/en/latest/index.html
Source0: %{pypi_source}
Patch0: photutils-fixtest-angle.patch

BuildRequires: gcc

%global _description %{expand:
Photutils contains functions for:
 * estimating the background and background rms in astronomical images
 * detecting sources in astronomical images
 * estimating morphological parameters of those sources (e.g., 
    centroid and shape parameters)
 * performing aperture and PSF photometry}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: python3-devel

Recommends: %{py3_dist scipy}
Recommends: %{py3_dist scikit-image} >= 0.14.2
Recommends: %{py3_dist scikit-learn}
Recommends: %{py3_dist matplotlib} >= 2.2

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1
sed -i 's/oldest-supported-numpy/numpy/g' pyproject.toml
# No py311 yet
sed -i 's/38,39,310/38,39,310,311/g' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t -e %{toxenv}-test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files photutils

%if %{with check}
%check
%{tox} 
%endif 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Thu Sep 01 2022 Sergio Pascual <sergiopr@fedoraproject.com> - 1.5.0-1
- New upstream source (1.5.0)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-5
- Rebuild for python3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Sun Jun 06 2021 Sergio Pascual <sergiopr@fedoraproject.com> - 1.1.0-1
- New upstream source (1.1.0)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.10

* Mon Feb 15 2021 Sergio Pascual <sergiopr@fedoraproject.com> - 1.0.2-1
- New upstream source (1.0.2)
- Use bcond to potentially disable testing

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 1.0.1-1
- New upstream source (1.0.1)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 0.7.2-1
- New upstream source (0.7.2)
- Patch astropy version in setup.cfg (bz#1758141)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.7.1-1
- new version
- skip tests on s390x for now (endianess issue in numpy...)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 0.6-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.5-1
- new version
- drop old patches
- re-enable tests

* Mon Oct 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-8
- Remove python2 subpackage (#1632572)

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.4-7
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 0.4-5
- Fix FTBFS with Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.4-3
- Added numpy 1.14 fix https://github.com/astropy/photutils/pull/639

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.4-1
- New upstream (0.4)

* Tue Oct 10 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.2-4
- Fixed tests

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.3.2-1
- New upstream (0.3.2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.com> - 0.3-1
- New upstream (0.3)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuild for Python 3.6

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-2
- rebuilt for matplotlib-2.0.0

* Wed Jul 27 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.2.2-1
- New upstream (0.2.2)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.2-1
- New upstream (0.2)

* Thu Nov 26 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-6
- Using new macros
- Disable tests until 0.2 is released

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-3
- Use license macro

* Mon Jan 26 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-2
- Disable test due to a bug (reported upstream)

* Thu Jan 08 2015 Sergio Pascual <sergiopr@fedoraproject.com> - 0.1-1
- First upstream release

* Wed Feb 26 2014 Sergio Pascual <sergiopr@fedoraproject.com> - 0.0-0.1.20140226git37a77fe
- Initial spec file

