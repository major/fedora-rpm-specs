Name:           python-stack-data
Version:        0.6.3
Release:        3%{?dist}
Summary:        Extract data from python stack frames and tracebacks for informative displays

License:        MIT
URL:            http://github.com/alexmojaki/stack_data
Source0:        %{pypi_source stack_data}
# don't run type checks, see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          no-typeguard.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-zombie-imp
# Extra test dependency
# Tests use Cython and try to compile some extensions
BuildRequires:  gcc

%global _description %{expand:
This is a library that extracts data from stack frames and tracebacks,
particularly to display more useful tracebacks than the default.}


%description %_description

%package -n     python3-stack-data
Summary:        %{summary}

%description -n python3-stack-data %_description


%prep
%autosetup -p1 -n stack_data-%{version}


%generate_buildrequires
%pyproject_buildrequires -r -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files stack_data


%check
%if v"%{python3_version}" >= v"3.11"
# https://github.com/alexmojaki/stack_data/issues/25
%tox -- -- -k "not _example"
%else
%tox
%endif


%files -n python3-stack-data -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Lumír Balhar <lbalhar@redhat.com> - 0.6.3-1
- Update to 0.6.3 (rhbz#2241507)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 0.6.2-4
- Rebuilt for Python 3.12

* Mon May 29 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.2-3
- Skip running type checks via typeguard, per packaging guidelines

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.2-1
- Update to 0.6.2 (rhbz#2148769)

* Tue Nov 01 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-1
- Update to 0.6.1
Resolves: rhbz#2138555

* Mon Sep 26 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.1-1
- Update to 0.5.1
Resolves: rhbz#2129634

* Sat Aug 27 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.0-1
- Update to 0.5.0
Resolves: rhbz#2121934

* Sat Aug 13 2022 Lumír Balhar <lbalhar@redhat.com> - 0.4.0-1
- Update to 0.4.0
Resolves: rhbz#2118041

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Lumír Balhar <lbalhar@redhat.com> - 0.3.0-1
- Update to 0.3.0
Resolves: rhbz#2097361

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.11

* Wed May 11 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.2.0-2
- Fix tests with pygments 2.12.0
Resolves: rhbz#2081905

* Tue Feb 15 2022 Lumír Balhar <lbalhar@redhat.com> - 0.2.0-1
- Update to 0.2.0
Resolves: rhbz#2054370

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Lumír Balhar <lbalhar@redhat.com> - 0.1.4-1
- Update to 0.1.4
Resolves: rhbz#2041029

* Tue Jan 04 2022 Lumír Balhar <lbalhar@redhat.com> - 0.1.3-1
- Package generated with pyp2spec
