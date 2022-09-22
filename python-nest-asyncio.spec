%global pypi_name nest_asyncio

Name:           python-nest-asyncio
Version:        1.5.5
Release:        3%{?dist}
Summary:        Patch asyncio to allow nested event loops

License:        BSD
URL:            https://github.com/erdewit/nest_asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%description
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.


%package -n     python3-nest-asyncio
Summary:        %{summary}

# This package used to be called python3-nest_asyncio
Obsoletes:      python3-nest_asyncio < 1.4.3-100
%py_provides    python3-nest_asyncio

%description -n python3-nest-asyncio
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 tests/nest_test.py

%files -n python3-nest-asyncio -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.5-2
- Rebuilt for Python 3.11

* Mon Apr 04 2022 Lumír Balhar <lbalhar@redhat.com> - 1.5.5-1
- Update to 1.5.5
Resolves: rhbz#2071300

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Lumír Balhar <lbalhar@redhat.com> - 1.5.4-1
- Update to 1.5.4
Resolves: rhbz#2028135

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 1.5.1-2
- Obsolete and provide nest_asyncio package
Resolves: rhbz#2007799

* Tue Aug 31 2021 Lumír Balhar <lbalhar@redhat.com> - 1.5.1-1
- Initial package
