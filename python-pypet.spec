# Multiple tests currently failing.
# Temporarily disabling tests
# https://github.com/SmokinCaterpillar/pypet/issues/63
%bcond_with tests

%global pypi_name pypet

%global _description %{expand:
The new python parameter exploration toolkit: pypet manages exploration of the
parameter space of any numerical simulation in python, thereby storing your
data into HDF5 files for you. Moreover, pypet offers a new data container which
lets you access all your parameters and results from a single source. Data I/O
of your simulations and analyses becomes a piece of cake!}

Name:           python-%{pypi_name}
Version:        0.5.2
Release:        7%{?dist}
Summary:        Parameter exploration toolbox

License:        BSD
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        https://github.com/SmokinCaterpillar/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  google-benchmark-devel
# For tests
%if %{with tests}
BuildRequires:  %{py3_dist brian2}
BuildRequires:  %{py3_dist deap}
BuildRequires:  hdf5
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist tables}
%endif

# For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(amsthm.sty)
BuildRequires:  /usr/bin/dvipng

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Remove gitignore files
rm -fv  examples/{,example_17_wrapping_an_existing_project,example_24_large_scale_brian2_simulation}/.gitignore

%build
%py3_build

make -C doc SPHINXBUILD=sphinx-build-3 html
rm -rf doc/build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

%check
# https://github.com/SmokinCaterpillar/pypet/blob/develop/ciscripts/travis/runtests.sh
# Scoop is unmaintained. I've asked upstream to drop support for it:
# https://github.com/SmokinCaterpillar/pypet/issues/56
%if %{with tests}
export HDF5_DISABLE_VERSION_CHECK=1
# Memory issues on s390x: OverflowError: Python int too large to convert to C int
%if "%{_host_cpu}" == "s390x"
echo "Skip tests on s390x"
%else
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} pypet/tests/all_single_core_tests.py
%endif
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%files doc
%license LICENSE CHANGES.txt
%doc doc/build/html examples/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Update to latest release
- disable tests on s390x
- temporarily disable tests

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.10

* Sat May 22 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-3
- Correctly detect host builder cpu

* Sat May 22 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-2
- Use correct macro for build arch

* Fri May 21 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-2
- Disable tests for s390x where it runs into memory issues

* Fri May 21 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Update to latest release
- Include patch to for py3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-2
- Explicitly BR setuptools

* Tue Jun 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to 0.5.0
- Enable tests

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-1
- Add missing BRs for docs

* Fri May 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-1
- Initial spec
