Name:           python-aiostream
Version:        0.7.0
Release:        3%{?dist}
Summary:        Generator-based operators for asynchronous iteration

License:        GPL-3.0-only
URL:            https://github.com/vxgmichel/aiostream
Source:         %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

Patch0:         require-lower-setuptools-version.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
aiostream provides a collection of stream operators that can be combined to
create asynchronous pipelines of operations.

It can be seen as an asynchronous version of itertools, although some aspects
are slightly different. Essentially, all the provided operators return a
unified interface called a stream.}

%description %_description

%package -n python3-aiostream
Summary:        %{summary}

%description -n python3-aiostream %_description


%prep
%autosetup -p1 -n aiostream-%{version}

# Don't run coverage as part of tests
sed -r \
    -e 's/ --cov aiostream//' \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files aiostream


%check
# Use --import-mode to solve file mismatch error
%pytest -v --import-mode importlib


%files -n python3-aiostream -f %{pyproject_files}
%doc README.*


%changelog
* Thu Jan 29 2026 Michel Lind <salimma@fedoraproject.org> - 0.7.0-3
- Lower setuptools requirement further to accomodate EPEL 10

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 26 2025 David Kaufmann <astra@ionic.at> - 0.7.0-1
- Version bump

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.6.1-8
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.6.1-7
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.6.1-5
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Sandro <devel@penguinpee.nl> - 0.6.1-2
- Fix running tests (properly)

* Thu Jun 20 2024 David Kaufmann <astra@ionic.at> - 0.6.1-1
- Version bump

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.13

* Fri Mar 01 2024 David Kaufmann <astra@ionic.at> - 0.5.2-1
- Unretired package and updated version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-2
- Add missing BR
- Add LICENSE file (rhbz#1809927)

* Wed Mar 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora
