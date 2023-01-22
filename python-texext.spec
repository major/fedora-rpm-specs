Name:           python-texext
Version:        0.6.7
Release:        4%{?dist}
Summary:        Sphinx extensions for working with LaTeX math

License:        BSD-2-Clause
URL:            https://github.com/matthew-brett/texext
Source0:        %pypi_source texext

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinxtesters}
BuildRequires:  %{py3_dist sympy}
BuildRequires:  %{py3_dist wheel}

%description
This package contains Sphinx extensions for working with LaTeX math.

%package -n     python3-texext
Summary:        Sphinx extensions for working with LaTeX math

%description -n python3-texext
This package contains Sphinx extensions for working with LaTeX math.

%prep
%autosetup -n texext-%{version} -p0

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files texext

%check
%pytest

%files -n python3-texext -f %{pyproject_files}
%doc README.html

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.6.7-3
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.6.7-2
- Rebuilt for Python 3.11

* Thu Jun  2 2022 Jerry James <loganjerry@gmail.com> - 0.6.7-1
- Version 0.6.7
- All patches have been upstreamed

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Jerry James <loganjerry@gmail.com> - 0.6.6-7
- Add upstream patch for Sphinx 4 support

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.6-6
- Rebuilt for Python 3.10

* Fri Feb 19 2021 Jerry James <loganjerry@gmail.com> - 0.6.6-5
- Add -sphinx3.5 patch to fix FTBFS with Sphinx 3.5 (bz 1930797)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Jerry James <loganjerry@gmail.com> - 0.6.6-3
- Add -docutils patch to fix build

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.9

* Sun Apr 12 2020 Jerry James <loganjerry@gmail.com> - 0.6.6-1
- Version 0.6.6

* Fri Mar  6 2020 Jerry James <loganjerry@gmail.com> - 0.6.5-1
- Version 0.6.5
- All patches have been upstreamed; drop them all

* Fri Jan 31 2020 Jerry James <loganjerry@gmail.com> - 0.6.1-8
- Add -still-more-sphinx2 patch to fix FTBFS in Rawhide

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Jerry James <loganjerry@gmail.com> - 0.6.1-7
- Add -more-sphinx2 patch
- Ship README in html form instead of rst

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-5
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.6.1-4
- Add -sphinx2 patch to fix FTBFS (bz 1736543)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 0.6.1-2
- Drop python2 subpackage (bz 1651177)
- Add -escape patch

* Mon Sep  3 2018 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- Initial RPM
