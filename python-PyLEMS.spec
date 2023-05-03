# Require network, so run locally on mock with --enable-network
%bcond_with tests

%global _description \
A LEMS (http://lems.github.io/LEMS) simulator written in Python which can be \
used to run NeuroML2 (http://neuroml.org/neuroml2.php) models.


Name:           python-PyLEMS
Version:        0.6.0
Release:        %autorelease
Summary:        LEMS interpreter implemented in Python

License:        LGPL-3.0-only

# Use github source. Pypi source does not include license and examples.
URL:            https://github.com/LEMS/pylems/
Source0:        %{url}/archive/v%{version}/pylems-%{version}.tar.gz
# Generate man page for pylems
# help2man -n "LEMS interpreter implemented in Python" --version-string="0.5.9" -N pylems -S "https://lems.github.io" -o pylems.1
# Sent upstream: https://github.com/LEMS/pylems/pull/64

BuildArch:      noarch

%description
%{_description}

%package -n python3-PyLEMS
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-PyLEMS
%{_description}

%package doc
Summary: %{summary}

%description doc
%{_description}


%prep
%autosetup -n pylems-%{version}

# correct man-page path
sed -i 's|\[("man/man1"|\[("share/man/man1"|' setup.py

# remove shebang
sed -i '1d' lems/dlems/exportdlems.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -r}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lems


%check
%if %{with tests}
# A lot of the tests use files from other software repositories, so we can't use them.
%{pytest}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest2.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/loadtest.py
%endif

%files -n python3-PyLEMS -f %{pyproject_files}
%{_bindir}/pylems
%{_mandir}/man1/pylems.1*

%files doc
%license LICENSE.lesser
%doc README.md examples

%changelog
%autochangelog

* Sat Aug 07 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.4-1
- Update to latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.10

* Thu Feb 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Update to 0.5.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to new release
- remove py2 bits

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.9.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.9.1-1
- Initial build
