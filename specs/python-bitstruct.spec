# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global pypi_name bitstruct
%global global_desc \
This module performs conversions between Python values and C bit \
field structs represented as Python byte strings.  It is intended to \
have a similar interface as the python struct module, but working on \
bits instead of primitive data types (char, int, …).


Name:           python-%{pypi_name}
Version:        8.17.0
Release:        10%{?dist}
Summary:        Interpret strings as packed binary data

# the c module won't compile
ExcludeArch:    s390x

License:        MIT
URL:            https://github.com/eerimoq/bitstruct
Source0:        %{url}/archive/%{version}/bitstruct-%{version}.tar.gz

%description
%{global_desc}


%package        doc
Summary:        Documentation-files for %{name}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

%description    doc
Documentation-files for %{name}.


%package        -n python3-%{pypi_name}
Summary:        %{summary}

%description    -n python3-%{pypi_name}
%{global_desc}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%py3_build
%make_build
%{_bindir}/find docs/_build -name '.*' -print0 | %{_bindir}/xargs -0 %{__rm} -frv


%install
%py3_install
%{__mkdir} -p %{buildroot}/%{_pkgdocdir}


%files doc
%license LICENSE
%doc %{_pkgdocdir}


%files -n python3-%{pypi_name}
%license LICENSE
%doc %dir %{_pkgdocdir}
%doc README.rst
%{python3_sitearch}/%{pypi_name}*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 8.17.0-9
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.17.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 8.17.0-2
- Rebuilt for Python 3.12

* Sat Mar 25 2023 Jonathan Wright <jonathan@almalinux.org> - 8.17.0-1
- Update to 8.17.0 rhbz#2170634

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 8.15.1-1
- Update to 8.15.1 rhbz#1742096
- Fix FTBFS rhbz#2046684 rhbz#2098850

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.12.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Björn Esser <besser82@fedoraproject.org> - 8.12.1-1
- New upstream release
  Fixes rhbz#1742096

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.1.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Björn Esser <besser82@fedoraproject.org> - 7.1.0-1
- New upstream release (rhbz#1574056)
- Explicitly BR: python3-sphinx_rtd_theme (rhbz#1716451)
- Do not remove inventory files generated by sphinx

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-5
- Subpackage python2-bitstruct has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Björn Esser <besser82@fedoraproject.org> - 3.7.0-1
- New upstream release (rhbz#11504327)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-1
- New upstream release (rhbz#1450026)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuild for Python 3.6

* Mon Oct 24 2016 Björn Esser <fedora@besser82.io> - 3.3.1-1
- Initial import (rhbz 1387836)

* Sat Oct 22 2016 Björn Esser <fedora@besser82.io> - 3.3.1-0.1
- Initial package (rhbz 1387836)
