%global pypi_name zipp

Name:           python-%{pypi_name}
Version:        3.9.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Not using test dependencies because the list
# is full of linters and static code checkers
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(jaraco-functools)

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%prep
%autosetup -n %{pypi_name}-%{version}
# jaraco.itertools and func_timeout are not available in Fedora yet
sed -i "/import jaraco.itertools/d" test_zipp.py
# this sed removes two lines - one import and one decorator
sed -i "/func_timeout/d" test_zipp.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Skipped test needs jaraco.itertools
%pytest -k "not test_joinpath_constant_time"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Sun Oct 09 2022 Lumír Balhar <lbalhar@redhat.com> - 3.9.0-1
- Update to 3.9.0
Resolves: rhbz#2133213

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Lumír Balhar <lbalhar@redhat.com> - 3.8.1-1
- Update to 3.8.1
Resolves: rhbz#2106391

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.8.0-2
- Rebuilt for Python 3.11

* Mon Apr 04 2022 Lumír Balhar <lbalhar@redhat.com> - 3.8.0-1
- Update to 3.8.0
Resolves: rhbz#2071401

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Lumír Balhar <lbalhar@redhat.com> - 3.7.0-1
- Update to 3.7.0
Resolves: rhbz#2036287

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 3.6.0-1
- Update to 3.6.0
Resolves: rhbz#2008627

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Lumír Balhar <lbalhar@redhat.com> - 3.5.0-1
- Update to 3.5.0
Resolves: rhbz#1978839

* Wed Jun 30 2021 Lumír Balhar <lbalhar@redhat.com> - 3.4.1-1
- Unretired package with new upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-1
- Initial package
