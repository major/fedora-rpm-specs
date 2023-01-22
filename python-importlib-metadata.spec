Name:           python-importlib-metadata
Version:        6.0.0
Release:        2%{?dist}
Summary:        Library to access the metadata for a Python package

License:        ASL 2.0
URL:            https://importlib-metadata.readthedocs.io/
Source0:        %{pypi_source importlib_metadata}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Test dependencies
# Not loaded via %%pyproject_buildrequires -x testing because upstream
# uses a lot unnecessary packages and some of them are not in Fedora.
BuildRequires:  python3-test
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyfakefs)

%description
Library to access the metadata for a Python package.
This package supplies third-party access to the functionality
of importlib.metadata including improvements added to subsequent
Python versions.


%package -n     python3-importlib-metadata
Summary:        %{summary}

%description -n python3-importlib-metadata
Library to access the metadata for a Python package.
This package supplies third-party access to the functionality
of importlib.metadata including improvements added to subsequent
Python versions.


%prep
%autosetup -n importlib_metadata-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files importlib_metadata

%check
# Ignored file uses pytest_perf not available in Fedora
# test_find_local tries to install setuptools from PyPI
%pytest --ignore exercises.py -k "not test_find_local"

%files -n python3-importlib-metadata -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Lumír Balhar <lbalhar@redhat.com> - 6.0.0-1
- Update to 6.0.0 (rhbz#2157297)

* Wed Dec 21 2022 Lumír Balhar <lbalhar@redhat.com> - 5.2.0-1
- Update to 5.2.0 (rhbz#2154722)

* Sun Nov 27 2022 Lumír Balhar <lbalhar@redhat.com> - 5.1.0-1
- Update to 5.1.0 (rhbz#2148187)

* Mon Oct 03 2022 Lumír Balhar <lbalhar@redhat.com> - 4.13.0-1
- Update to 4.13.0
Resolves: rhbz#2131478

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Lumír Balhar <lbalhar@redhat.com> - 4.12.0-1
- Update to 4.12.0
Resolves: rhbz#2101112

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.11.4-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Lumír Balhar <lbalhar@redhat.com> - 4.11.4-1
- Update to 4.11.4
Resolves: rhbz#2088922

* Mon Mar 14 2022 Lumír Balhar <lbalhar@redhat.com> - 4.11.3-1
- Update to 4.11.3
Resolves: rhbz#2063566

* Mon Feb 28 2022 Lumír Balhar <lbalhar@redhat.com> - 4.11.2-1
- Update to 4.11.2
Resolves: rhbz#2059016

* Tue Feb 15 2022 Lumír Balhar <lbalhar@redhat.com> - 4.11.1-1
- Update to 4.11.1
Resolves: rhbz#2054478

* Fri Feb 11 2022 Lumír Balhar <lbalhar@redhat.com> - 4.11.0-1
- Update to 4.11.0
Resolves: rhbz#2053332

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Lumír Balhar <lbalhar@redhat.com> - 4.10.1-1
- Update to 4.10.1
Resolves: rhbz#2041301

* Mon Jan 03 2022 Lumír Balhar <lbalhar@redhat.com> - 4.10.0-1
- Update to 4.10.0
Resolves: rhbz#2034072

* Sat Dec 18 2021 Lumír Balhar <lbalhar@redhat.com> - 4.8.3-1
- Update to 4.8.3
Resolves: rhbz#2033335

* Tue Nov 09 2021 Lumír Balhar <lbalhar@redhat.com> - 4.8.2-1
- Update to 4.8.2
Resolves: rhbz#2021375

* Mon Aug 30 2021 Lumír Balhar <lbalhar@redhat.com> - 4.8.1-1
- Update to 4.8.1
Resolves: rhbz#1997891

* Mon Aug 16 2021 Lumír Balhar <lbalhar@redhat.com> - 4.6.4-1
- Update to 4.6.4
Resolves: rhbz#1993538

* Mon Aug 02 2021 Lumír Balhar <lbalhar@redhat.com> - 4.6.3-1
- Update to 4.6.3
Resolves: rhbz#1988649

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Lumír Balhar <lbalhar@redhat.com> - 4.6.1-1
- Update to 4.6.1
Resolves: rhbz#1979098

* Wed Jun 30 2021 Lumír Balhar <lbalhar@redhat.com> - 4.6.0-1
- Unretired and updated package

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-1
- Initial package
